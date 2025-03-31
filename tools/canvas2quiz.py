import os
from canvasapi import Canvas
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Canvas API URL and Access Token
API_URL = 'https://miamioh.instructure.com'
API_KEY = os.getenv('CANVAS_ACCESS_TOKEN')

# Initialize Canvas object
canvas = Canvas(API_URL, API_KEY)

# Course ID and Quiz ID
course_id = 230947
quiz_id = 700329  # Replace with your specific quiz ID

# Get the course and quiz objects
course = canvas.get_course(course_id)
quiz = course.get_quiz(quiz_id)

# Retrieve all questions in the quiz
questions = quiz.get_questions()


def format_question_to_text2qti(question):
    """
    Formats a Canvas quiz question into Text2QTI format.
    """
    qti_question = []

    # Add question title and points
    qti_question.append(f"Title: {question.question_name}")
    qti_question.append(f"Points: {question.points_possible}")

    # Add question text
    qti_question.append(f"1. {question.question_text}")

    # Process answer choices based on question type
    if question.question_type in ['multiple_choice_question', 'true_false_question']:
        for opt, answer in zip("ABCDEFGH", question.answers):
            prefix = '*' if answer['weight'] == 100 else ''
            qti_question.append(f"{prefix}{opt}) {answer['text']}")
            qti_question.append(f"... {answer.get('comments', '')}")
    else:
        # Handle other question types or provide a warning
        qti_question.append(f"... [Unsupported question type: {question.question_type}]")

    return "\n".join(qti_question)

# Generate the Text2QTI formatted quiz
text2qti_quiz = []

# Add quiz title and description
text2qti_quiz.append(f"Quiz title: {quiz.title}")
text2qti_quiz.append(f"Quiz description: {quiz.description}")

# Convert each question
for question in questions:
    text2qti_quiz.append(format_question_to_text2qti(question))

# Combine all parts into the final Text2QTI content
text2qti_content = "\n\n".join(text2qti_quiz)

# Output or save the content
print(text2qti_content)

# Save to a file
with open('quiz_export.txt', 'w', encoding='utf-8') as file:
    file.write(text2qti_content)
