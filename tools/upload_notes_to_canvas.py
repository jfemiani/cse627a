import os
import glob
from dotenv import load_dotenv
from canvasapi import Canvas
import pypandoc

# Load API key from .env
load_dotenv()
API_URL = 'https://miamioh.instructure.com'
API_KEY = os.getenv('CANVAS_ACCESS_TOKEN')
COURSE_ID = 230947  # Replace with your actual Canvas course ID

# Initialize Canvas
canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(COURSE_ID)

NOTES_DIR = "chapter1"

def markdown_to_html(md_path):
    return pypandoc.convert_file(
        md_path,
        to='html',
        format='md',
        extra_args=["--mathjax"]  # enables MathJax rendering in Canvas
    )

def create_or_update_canvas_page(course, title, html_content):
    page_url = title.lower().replace(" ", "-")

    try:
        # Try to get existing page
        page = course.get_page(page_url)
        page.edit(wiki_page={"body": html_content})
        print(f"✅ Updated: {title}")
    except Exception:
        # If not found, create new page
        course.create_page(wiki_page={
            "title": title,
            "body": html_content,
            "published": True
        })
        print(f"✅ Created: {title}")

def main():
    note_files = glob.glob(os.path.join(NOTES_DIR, "*-notes.md"))

    for md_file in sorted(note_files):
        filename = os.path.basename(md_file)
        title = (
            filename.replace("-notes.md", "")
                    .replace("prml-", "")
                    .replace("=", "-")  # handle that one typo you had
                    .replace("-", " ")
                    .title()
        )

        html = markdown_to_html(md_file)
        create_or_update_canvas_page(course, title, html)

if __name__ == "__main__":
    main()
