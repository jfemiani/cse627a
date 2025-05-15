import os
import re
import json
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from canvasapi import Canvas

load_dotenv()

# ------------------ API Setup ------------------
CANVAS_ACCESS_TOKEN = os.environ.get("CANVAS_ACCESS_TOKEN")
CANVAS_BASE_URL = os.environ.get("CANVAS_BASE_URL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

canvas = Canvas(CANVAS_BASE_URL, CANVAS_ACCESS_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

# ------------------ Canvas API Helpers ------------------
def get_course_id_from_url(course_url):
    match = re.search(r"courses/(\d+)", course_url)
    return match.group(1) if match else None

def get_quizzes(course_id):
    course = canvas.get_course(course_id)
    return list(course.get_quizzes())

def get_quiz_questions(course_id, quiz_id):
    course = canvas.get_course(course_id)
    quiz = course.get_quiz(quiz_id)
    return {str(q.id): q for q in quiz.get_questions()}

def get_quiz_submissions(course_id, quiz_id):
    course = canvas.get_course(course_id)
    quiz = course.get_quiz(quiz_id)
    return list(quiz.get_submissions())

def get_student_answers(submission):
    events = submission.get_submission_events()
    answers = {}
    for event in events:
        if event.event_type == 'question_answered':
            data = event.event_data
            for entry in data:
                question_id = str(data.get('quiz_question_id'))
                answer = data.get('answer')
                if question_id and answer is not None:
                    answers[question_id] = answer
    return answers


def update_score(submission_id, question_id, score, comment):
    # canvasapi does not directly support per-question grading via submission ID
    # This part will need raw requests unless wrapped manually, so for now this remains as-is
    url = f"{CANVAS_BASE_URL}/quiz_submissions/{submission_id}/questions/{question_id}"
    payload = {"attempt": 1, "question_id": question_id, "score": score, "comment": comment}
    from requests import put
    put(url, headers={"Authorization": f"Bearer {CANVAS_ACCESS_TOKEN}", "Content-Type": "application/json"}, json=payload)

# ------------------ LLM Grading ------------------
def grade_with_llm(answer, logic):
    system_msg = "You are a grading assistant. Return JSON: {'score': 'CORRECT'|'INCORRECT', 'justification': string}."
    prompt = f"""
<answer>
{answer}
</answer>
<logic>
{logic}
</logic>
"""
    try:
        response = client.chat.completions.create(model="gpt-4",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": prompt}
        ],
        temperature=0)
        parsed = json.loads(response.choices[0].message.content)
        return parsed['score'], parsed['justification']
    except Exception as e:
        return "INCORRECT", f"LLM error: {str(e)}"

# ------------------ Streamlit UI ------------------
st.title("Canvas Quiz Grader")
course_url = st.text_input("Paste Canvas Course URL")

grading_results = {}

if course_url:
    course_id = get_course_id_from_url(course_url)
    quizzes = get_quizzes(course_id)
    quiz_map = {f"{q.title} (ID: {q.id})": q.id for q in quizzes}
    selected = st.multiselect("Select Quizzes to Grade", list(quiz_map.keys()))

    if st.button("Grade Selected Quizzes"):
        for quiz_name in selected:
            quiz_id = quiz_map[quiz_name]
            st.subheader(f"Results for {quiz_name}")

            questions = get_quiz_questions(course_id, quiz_id)
            submissions = get_quiz_submissions(course_id, quiz_id)

            for sub in submissions:
                sid = sub.id
                user = sub.user_id
                answers = get_student_answers(sub)

                for qid, ans in answers.items():
                    feedback = questions[qid].correct_comments or ""
                    if feedback.startswith("LLM_VERIFY:"):
                        logic = feedback[len("LLM_VERIFY:"):].strip()
                        score, justification = grade_with_llm(ans, logic)

                        if score == "INCORRECT":
                            key = f"quiz_{quiz_id}_sub_{sid}_q_{qid}"
                            grading_results[key] = {
                                "submission_id": sid,
                                "question_id": qid,
                                "student_id": user,
                                "answer": ans,
                                "justification": justification
                            }

        for key, res in grading_results.items():
            with st.expander(f"Student {res['student_id']} - Q{res['question_id']}"):
                st.markdown(f"**Answer:** {res['answer']}")
                st.markdown(f"**LLM Justification:** {res['justification']}")
                if st.button(f"Confirm Correct for {key}"):
                    update_score(res['submission_id'], res['question_id'], 1, res['justification'])
                    st.success("Score updated to 1")

        if st.button("Confirm All Incorrects as 0"):
            for res in grading_results.values():
                update_score(res['submission_id'], res['question_id'], 0, res['justification'])
            st.success("All incorrect scores confirmed as 0")
