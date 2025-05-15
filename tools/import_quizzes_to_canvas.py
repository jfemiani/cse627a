"""Prepare quizzes for Canvas from text files using text2qti.

This script converts Text2QTI quiz files into QTI zip files. 
It does NOT upload them to Canvas - that must be done separately at the moment.

It will only process quiz files that are newer than the corresponding zip file.
"""
import os
import glob
import subprocess
import requests
from canvasapi import Canvas
from dotenv import load_dotenv

# === Canvas config ===
load_dotenv()

QUIZ_DIRS = [
    "chapter1",
    "chapter5",
    "chapter6",
    "chapter7",
    "chapter8",
    "chapter14",
]

API_URL = "https://miamioh.instructure.com"
API_KEY = os.getenv("CANVAS_ACCESS_TOKEN")
COURSE_ID = 230947
MODULE_NAME = "Week 1 (Jan 27–Feb 2) - Introduction to Machine Learning, ML Paradigms"
TEXT2QTI = '/home/femianjc/Courses/cse627/.conda/bin/text2qti'

canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(COURSE_ID)


def is_source_older_than_zip(quiz_txt_path, zip_path):
    """Check if the quiz text file is older than the zip file."""
    if not os.path.exists(zip_path):
        return False
    
    txt_mtime = os.path.getmtime(quiz_txt_path)
    zip_mtime = os.path.getmtime(zip_path)
    
    return txt_mtime < zip_mtime

def run_text2qti(quiz_txt_path):
    zip_path = quiz_txt_path.replace(".txt", ".zip")
    
    if is_source_older_than_zip(quiz_txt_path, zip_path):
        print(f"🔄 Skipping text2qti for {quiz_txt_path} - source file older than zip")
        return zip_path
    
    print(f"🔧 Running text2qti on {quiz_txt_path}")
    subprocess.run([
        TEXT2QTI,
        quiz_txt_path,
        "--pandoc-mathml"
    ], check=True)
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"❌ Expected zip file not found: {zip_path}")
    return zip_path

def get_or_create_module(course, module_name):
    for module in course.get_modules():
        if module.name == module_name:
            return module
    return course.create_module(module={"name": module_name})

def find_quiz_by_title(course, title):
    for quiz in course.get_quizzes():
        if quiz.title.strip().lower() == title.strip().lower():
            return quiz
    return None

def import_qti_zip(course, zip_path):
    print(f"📤 Uploading QTI zip: {zip_path}")

    # Step 1: Upload to Canvas
    with open(zip_path, 'rb') as f:
        upload_response = course.upload(f, {
            "name": os.path.basename(zip_path),
            "content_type": "application/zip"
        })

    upload_url = upload_response[0]['upload_url']
    upload_params = upload_response[0]['upload_params']

    # Step 2: Post file to upload_url
    with open(zip_path, 'rb') as f:
        response = requests.post(
            upload_url,
            data=upload_params,
            files={"file": f}
        )

    # Step 3: Get file_id from Canvas
    file_list = course.get_files(search_term=os.path.basename(zip_path))
    file_id = next((file.id for file in file_list if file.display_name == os.path.basename(zip_path)), None)
    if not file_id:
        raise RuntimeError("❌ Could not retrieve uploaded file ID.")

    # Step 4: Create content migration
    course.create_content_migration(
        migration_type="common_cartridge_importer",
        settings={"file_id": file_id}
    )

    print("✅ Migration started (QTI zip uploaded).")

def add_quiz_to_module(module, quiz, title):
    for item in module.get_module_items():
        if item.title.strip().lower() == title.strip().lower():
            print(f"🟡 Quiz already in module: {title}")
            return
    module.create_module_item({
        "type": "Quiz",
        "content_id": quiz.id,
        "published": True
    })
    print(f"✅ Added quiz to module: {title}")

def main():
    for quiz_dir in QUIZ_DIRS:
        quiz_txt_files = sorted(glob.glob(f"{quiz_dir}/*-quiz.txt"))
        quiz_txt_files += sorted(glob.glob(f"{quiz_dir}/*-quiz.md"))

        for quiz_txt in quiz_txt_files:
            base_name = os.path.splitext(os.path.basename(quiz_txt))[0]
            title = base_name.replace("prml-", "").replace("-", " ").title()
            zip_path = run_text2qti(quiz_txt)
        

if __name__ == "__main__":
    main()
