"""Make sure that all canvas quizzes have the same settings. 
They should all have unlimited attempts, keep highest score, and hide results until the due date.
This script will add a link to the quiz description that allows students to anonymously report issues with the quiz questions.
"""

import os
import re
from dotenv import load_dotenv
from canvasapi import Canvas

# Load API key from .env file
load_dotenv()
API_URL = 'https://miamioh.instructure.com'
API_KEY = os.getenv('CANVAS_ACCESS_TOKEN')
COURSE_ID = 230947  # Replace with your actual Canvas course ID

QUIZ_ISSUE_REPORT_URL = "https://miamioh.instructure.com/courses/230947/quizzes/707070"
ISSUE_LINK_HTML = f'<p><a href="{QUIZ_ISSUE_REPORT_URL}" target="_blank">Anonymously tell the instructor about an issue with this question</a></p>'


# Initialize Canvas API
canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(COURSE_ID)

def update_quizzes(course):
    # Retrieve all quizzes for the course
    quizzes = course.get_quizzes()
    
    for quiz in quizzes:
        if quiz.quiz_type != 'assignment':
            print(f"🟡 Skipping ungraded quiz: {quiz.title}")
            continue
        
        if re.search(r'exam', quiz.title, re.IGNORECASE):
            print(f"🟡 Skipping quiz (name contains 'exam'): {quiz.title}")
            continue
            
        try:
            if QUIZ_ISSUE_REPORT_URL not in quiz.description:
                updated_description = (quiz.description or "") + ISSUE_LINK_HTML
                quiz.edit(quiz={
                    "description": updated_description,
                    "allowed_attempts": -1,
                    "scoring_policy": "keep_highest",
                    "hide_results": ""
                })
                print(f"✅ Updated quiz description and settings: {quiz.title}")
            else:
                # Just update settings
                quiz.edit(quiz={
                    "allowed_attempts": -1,
                    "scoring_policy": "keep_highest",
                    "hide_results": ""
                })
                print(f"✅ Updated quiz settings only: {quiz.title}")
        except Exception as e:
            print(f"❌ Failed to update quiz: {quiz.title}. Error: {e}")
       
       
        # questions = quiz.get_questions()

        # for question in questions:
        #     try:
        #         # Only update if the feedback isn't already present
        #         if ISSUE_LINK_HTML not in (question.neutral_comments_html or ""):
        #             new_feedback = (question.neutral_comments_html or "") + ISSUE_LINK_HTML
        #             question.edit(question={"neutral_comments_html": new_feedback})
        #             print(f"  📝 Added feedback link to: {question.question_name}")
        #         else:
        #             print(f"  ✔️ Feedback already present: {question.question_name}")
        #     except Exception as e:
        #         print(f"  ❌ Failed to update question '{question.question_name}': {e}")
        
        # print(f"✔️ Finished processing quiz: {quiz.title}")

def main():
    update_quizzes(course)

if __name__ == "__main__":
    main()
