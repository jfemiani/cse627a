import os
import glob
from dotenv import load_dotenv
from canvasapi import Canvas
import pypandoc
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments import highlight
import markdown
import re
import datetime

# Load API key from .env
load_dotenv()
API_URL = 'https://miamioh.instructure.com'
API_KEY = os.getenv('CANVAS_ACCESS_TOKEN')
COURSE_ID = 230947  # Replace with your actual Canvas course ID
TEMPLATE_PATH = "tools/page-template.html"

# Initialize Canvas
canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(COURSE_ID)

# NOTES_DIR = "chapter1"
# NOTES_DIR = "chapter5"
# NOTES_DIR = "chapter6"
NOTES_DIR = "chapter7"
# NOTES_DIR = "chapter8"
# NOTES_DIR = "chapter14"

NOTES_DIRS= [
    "chapter1",
    "chapter5",
    "chapter6",
    "chapter7",
    "chapter8",
    "chapter14",
]



def get_page_modified_date(page):
    """Get the Canvas page's last modified date (already in UTC)"""
    return datetime.datetime.strptime(page.updated_at, "%Y-%m-%dT%H:%M:%SZ")

def get_local_modified_date(file_path):
    """Get local file's last modified timestamp converted to UTC"""
    local_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    # Convert local time to UTC
    local_time_utc = local_time.astimezone(datetime.timezone.utc)
    return local_time_utc


def needs_update(local_file, canvas_page=None):
    """Check if local file is newer than Canvas page"""
    if not canvas_page:
        return True  # Page doesn't exist yet, so create it
    
    local_date = get_local_modified_date(local_file)
    canvas_date = get_page_modified_date(canvas_page)

    # Make canvas_date timezone-aware by assuming it's UTC
    if canvas_date.tzinfo is None:
        canvas_date = canvas_date.replace(tzinfo=datetime.timezone.utc)
    
    time_difference = (local_date - canvas_date).total_seconds()
    # Debug info to verify correct comparison
    print(f"local_date {local_date}")
    print(f"canvas_date {canvas_date}")
    print(f"Comparison result: {time_difference > -20 * 60}")
       

    return time_difference > -20 * 60

# 🆕 Extract image paths from markdown
def extract_image_paths(md_content):
    return re.findall(r'!\[.*?\]\((.*?)\)', md_content)

# 🆕 Upload or replace images in Canvas
def upload_or_replace_image(course, local_path, folder_name="notes"):
    filename = os.path.basename(local_path)
    folder = next((f for f in course.get_folders() if f.full_name.endswith(folder_name)), None)
    if not folder:
        folder = course.create_folder(folder_name)
    existing = [f for f in folder.get_files() if f.filename == filename]
    for f in existing:
        f.delete()
    with open(local_path, 'rb') as f:
        return folder.upload(f)[1]  # returns a CanvasFile object

# 🆕 Replace local image paths with Canvas URLs in HTML
def patch_image_urls(html, local_to_canvas_url):
    for local_path, canvas_url in local_to_canvas_url.items():
        html = html.replace(f'src="{local_path}"', f'src="{canvas_url}"')
    return html

def markdown_to_html(md_path, image_map):  # accepts image_map
    template_path = TEMPLATE_PATH

    html = pypandoc.convert_file(
        md_path,
        to='html',
        format='md',
        extra_args=[
            "--mathjax",
            f"--template={template_path}",
            "--no-highlight"  # 👈 disables <pre class="sourceCode ...">
        ]
    )

    # Step 2: Highlight <pre><code class="language-xxx">...</code></pre> using Pygments
    def highlight_code_block(match):
      indent = match.group(1)
      lang = match.group(2) or "text"
      code = match.group(3)

      # Decode HTML entities
      code = code.replace("&lt;", "<").replace("&gt;", ">")
      code = code.replace("&amp;", "&")
      code = code.replace("&quot;", "\"")
      code = code.replace("&nbsp;", " ")

      try:
          lexer = get_lexer_by_name(lang)
      except Exception:
          lexer = get_lexer_by_name("text")

      formatter = HtmlFormatter(nowrap=True, noclasses=True, style="default")
      highlighted = highlight(indent+code, lexer, formatter)

      return (
          f"<pre style='background:#f5f5f5; padding:1em; border-radius:4px; overflow-x:auto; "
          "font-family:monospace; font-size:0.95em;'>\n"
          f"{highlighted}</pre>"
      )

    html = re.sub(
        r'([ \t]*)<pre class="(.*?)"><code>(.*?)</code></pre>',
        highlight_code_block,
        html,
        flags=re.DOTALL
    )

    html = patch_image_urls(html, image_map)  # patch in Canvas URLs
    return html


def create_or_update_canvas_page(course, title, html_content, md_file_path):
    page_url = title.lower().replace(" ", "-")

    try:
        # Try to get existing page
        page = course.get_page(page_url)
        
        # Only update if local file is newer
        if needs_update(md_file_path, page):
            page.edit(wiki_page={"body": html_content})
            print(f"✅ Updated: {title} (local file newer than Canvas)")
        else:
            print(f"⏭️ Skipped: {title} (Canvas version is current)")
    except Exception:
        # If not found, create new page
        course.create_page(wiki_page={
            "title": title,
            "body": html_content,
            "published": True
        })
        print(f"✅ Created: {title}")




def main():
    
  for notes_dir in NOTES_DIRS:
    note_files = glob.glob(os.path.join(notes_dir, "*-notes.md"))

    for md_file in sorted(note_files):
        filename = os.path.basename(md_file)
        title = (
            filename.replace("-notes.md", "")
                    .replace("prml-", "")
                    .replace("-", " ")
                    .title()
        )

        # Check if we need to update before processing the file
        page_url = title.lower().replace(" ", "-")
        try:
            page = course.get_page(page_url)
            if not needs_update(md_file, page):
                print(f"⏭️ Skipped: {title} (Canvas version is current)")
                continue  # Skip to next file
        except Exception:
            # Page doesn't exist yet, so we'll need to create it
            pass

        # 🆕 STEP 1: Load raw Markdown and extract image paths
        with open(md_file, "r", encoding="utf-8") as f:
            md_content = f.read()
        image_paths = extract_image_paths(md_content)

        # 🆕 STEP 2: Upload images and build mapping
        image_map = {}
        for img_path in image_paths:
            full_path = os.path.join(os.path.dirname(md_file), img_path)
            if os.path.exists(full_path):
                uploaded = upload_or_replace_image(course, full_path)
                image_map[img_path] = uploaded["url"]

        # 🆕 STEP 3: Convert markdown with image map
        html = markdown_to_html(md_file, image_map)
        create_or_update_canvas_page(course, title, html, md_file)

if __name__ == "__main__":
    main()
