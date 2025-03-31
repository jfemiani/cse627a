import os
import glob
import subprocess
import requests
from canvasapi import Canvas
from dotenv import load_dotenv

# === Canvas config ===
load_dotenv()
API_URL = "https://miamioh.instructure.com"
API_KEY = os.getenv("CANVAS_ACCESS_TOKEN")
COURSE_ID = 230947
MODULE_NAME = "Week 1 (Jan 27–Feb 2) - Introduction to Machine Learning, ML Paradigms"
TEXT2QTI = '/home/femianjc/Courses/cse627/.conda/bin/text2qti'

canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(COURSE_ID)

def run_text2qti(quiz_txt_path):
    print(f"🔧 Running text2qti on {quiz_txt_path}")
    subprocess.run([
        TEXT2QTI,
        quiz_txt_path,
        "--pandoc-mathml"
    ], check=True)
    zip_path = quiz_txt_path.replace(".txt", ".zip")
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
    module = get_or_create_module(course, MODULE_NAME)
    quiz_txt_files = sorted(glob.glob("chapter1/*-quiz.txt"))

    for quiz_txt in quiz_txt_files:
        base_name = os.path.splitext(os.path.basename(quiz_txt))[0]
        title = base_name.replace("prml-", "").replace("-", " ").title()

        zip_path = run_text2qti(quiz_txt)
        
        # import_qti_zip(course, zip_path)

        # # Wait for the import to complete
        # print("⏳ Waiting for import to complete...")
        # input("Check Canvas. Press Enter to continue...")

        # quiz = find_quiz_by_title(course, title)
        # if quiz:
        #     add_quiz_to_module(module, quiz, title)
        # else:
        #     print(f"⚠️ Could not find quiz titled '{title}' after import. You may need to wait.")

if __name__ == "__main__":
    main()
