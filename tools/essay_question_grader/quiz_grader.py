"""This script grades quiz answers in Canvas using a logic rubric and an LLM (OpenAI's GPT-4).
It is currently a work in progress and not fully functional.
It retrieves quiz questions and student submissions from Canvas, grades the answers based on the rubric,
and updates the scores in Canvas.

It uses the Feedback field of the quiz questions to determine the grading logic.
The grading logic can be a regex pattern, a minimum word count, or an LLM verification command.
The script also supports a dry run mode to simulate the grading process without updating Canvas.
It requires the following environment variables to be set:
- CANVAS_BASE_URL: The base URL of the Canvas instance (e.g., https://miamioh.instructure.com)
- CANVAS_ACCESS_TOKEN: The access token for the Canvas API
- OPENAI_API_KEY: The API key for OpenAI's GPT-4

"""

import os
import re
import requests
import csv
import argparse
from typing import Dict, List
import openai
import json

# ------------------ Configuration ------------------
CANVAS_BASE_URL = os.environ.get("CANVAS_BASE_URL")
CANVAS_ACCESS_TOKEN = os.environ.get("CANVAS_ACCESS_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {CANVAS_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

openai.api_key = OPENAI_API_KEY

# ------------------ Helpers ------------------
def get_quiz_questions(course_id: str, quiz_id: str) -> Dict[str, Dict]:
    url = f"{CANVAS_BASE_URL}/courses/{course_id}/quizzes/{quiz_id}/questions"
    questions = {}
    response = requests.get(url, headers=HEADERS)
    for q in response.json():
        questions[str(q["id"])] = {
            "question_text": q["question_text"],
            "feedback": q.get("correct_comments") or ""
        }
    return questions

def get_student_submissions(course_id: str, quiz_id: str) -> List[Dict]:
    url = f"{CANVAS_BASE_URL}/courses/{course_id}/quizzes/{quiz_id}/submissions"
    response = requests.get(url, headers=HEADERS)
    return response.json().get("quiz_submissions", [])

def get_student_answers(course_id: str, quiz_id: str, submission_id: str) -> Dict[str, str]:
    url = f"{CANVAS_BASE_URL}/quiz_submissions/{submission_id}/questions"
    response = requests.get(url, headers=HEADERS)
    return {str(ans["quiz_question_id"]): ans["answer"] for ans in response.json()}

def update_score(submission_id: str, question_id: str, score: int, comment: str, dry_run: bool = False):
    url = f"{CANVAS_BASE_URL}/quiz_submissions/{submission_id}/questions/{question_id}"
    payload = {
        "attempt": 1,
        "question_id": question_id,
        "score": score,
        "comment": comment
    }
    if dry_run:
        print(f"[Dry Run] Would update score: {payload}")
        return
    try:
        response = requests.put(url, headers=HEADERS, json=payload)
        response.raise_for_status()
    except Exception as e:
        print(f"Error updating score for {submission_id}, {question_id}: {e}")

# ------------------ LLM Verification ------------------
def grade_with_llm(answer: str, logic: str) -> (int, str):
    system_msg = "You are a grading assistant. You evaluate student answers based on a logic rubric. Always return a JSON object with two keys: 'score' and 'justification'. 'score' must be either 'CORRECT' or 'INCORRECT'."

    user_prompt = f"""
Here is the provided answer:
<answer>
{answer}
</answer>

Use the following logic to determine if the answer is correct or incorrect:
<logic>
{logic}
</logic>

Respond only with a JSON object like:
{{
  "score": "CORRECT",
  "justification": "..."
}}
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0
        )
        parsed = json.loads(response['choices'][0]['message']['content'])
        return (1 if parsed['score'].upper() == "CORRECT" else 0), parsed['justification']
    except Exception as e:
        return 0, f"LLM error: {str(e)}"

# ------------------ Grading Logic ------------------
def grade_answer(answer: str, feedback: str, min_words_default: int = 5) -> (int, str):
    answer = (answer or "").strip()
    if not answer:
        return 0, "Empty response"

    if feedback.startswith("LLM_VERIFY:"):
        logic = feedback[len("LLM_VERIFY:"):].strip()
        return grade_with_llm(answer, logic)

    regex_match = re.search(r"REGEX:(.*?)($|MIN_WORDS=|\n)", feedback, re.IGNORECASE)
    min_words_match = re.search(r"MIN_WORDS=(\d+)", feedback)

    if regex_match:
        pattern = regex_match.group(1).strip()
        if not re.search(pattern, answer, re.IGNORECASE):
            return 0, f"Failed REGEX match: {pattern}"

    min_words = int(min_words_match.group(1)) if min_words_match else min_words_default
    if len(answer.split()) < min_words:
        return 0, f"Too short (min {min_words} words)"

    return 1, "Passed"

# ------------------ Main ------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--course", required=True, help="Canvas course ID")
    parser.add_argument("--quiz", required=True, help="Canvas quiz ID")
    parser.add_argument("--output", default=None, help="Optional output CSV file")
    parser.add_argument("--dry-run", action="store_true", help="Do not update Canvas, just simulate")
    args = parser.parse_args()

    questions = get_quiz_questions(args.course, args.quiz)
    submissions = get_student_submissions(args.course, args.quiz)

    if args.output:
        csvfile = open(args.output, "w", newline="")
        fieldnames = ["student", "question_id", "score", "comment"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    else:
        writer = None

    for sub in submissions:
        sid = sub["id"]
        student = sub["user_id"]
        answers = get_student_answers(args.course, args.quiz, sid)

        for qid, answer in answers.items():
            feedback = questions[qid].get("feedback", "")
            score, comment = grade_answer(answer, feedback)

            if writer:
                writer.writerow({
                    "student": student,
                    "question_id": qid,
                    "score": score,
                    "comment": comment
                })

            update_score(sid, qid, score, comment, dry_run=args.dry_run)

    if args.output:
        csvfile.close()

if __name__ == "__main__":
    main()
