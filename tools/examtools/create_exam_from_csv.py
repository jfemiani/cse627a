import os
import csv
import re

# Directories containing quiz files
QUIZ_DIRS = [
    "chapter1",
    "chapter5",
    "chapter6",
    "chapter7",
    "chapter8",
    "chapter14",
]

# Input CSV containing quiz filenames and descriptions of questions to include
# INPUT_CSV = 'question_info.csv'
INPUT_CSV = 'final_exam_selection.csv'

# Output file for the assembled exam
OUTPUT_FILE = 'exam.txt'

def load_included_descriptions(csv_path):
    """
    Reads the CSV and returns a dict mapping each filename to a set of descriptions
    for questions marked with '1' in the points column.
    Assumes CSV headers include: filename, difficulty, level, edge_flag, description, points
    """
    included = {}
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('final_points', '').strip() == '1':
                fname = row['filename'].strip()
                desc = row['description'].strip()
                included.setdefault(fname, set()).add(desc)
    return included

def find_quiz_file(fname):
    """
    Searches QUIZ_DIRS for the given filename and returns its full path if found.
    """
    # check current directory
    if os.path.exists(fname):
        return fname
    # search in quiz directories
    for d in QUIZ_DIRS:
        path = os.path.join(d, fname)
        if os.path.exists(path):
            return path
    return None

def split_question_blocks(content):
    """
    Splits file content into question blocks.
    Each block starts with 'Title:' and ends before the next 'Title:' or EOF.
    """
    pattern = re.compile(r'^Title:.*?(?=^Title:|\Z)', flags=re.MULTILINE | re.DOTALL)
    return pattern.findall(content)

def parse_block_description(block):
    """
    Extracts the description from a question block's title line.
    Format: Title: difficulty – level – edge_flag – description
    """
    first_line = block.splitlines()[0]
    title_body = first_line[len('Title: '):].strip()
    parts = re.split(r'\s*–\s*', title_body)
    if len(parts) >= 4:
        return ' – '.join(parts[3:]).strip()
    return None

def filter_file_questions(filepath, descriptions):
    """
    Reads a quiz file, splits into question blocks, and returns only those blocks
    whose description matches the provided set.
    """
    content = open(filepath, encoding='utf-8').read()
    blocks = split_question_blocks(content)
    return [blk.strip() for blk in blocks if parse_block_description(blk) in descriptions]

def main():
    included_map = load_included_descriptions(INPUT_CSV)
    all_blocks = []
    
    for quiz_file, descs in included_map.items():
        full_path = find_quiz_file(quiz_file)
        if not full_path:
            print(f"Warning: file not found: {quiz_file}")
            continue
        questions = filter_file_questions(full_path, descs)
        all_blocks.extend(questions)
    
    # Write all filtered questions to a single exam file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(all_blocks))
    
    print(f"Wrote {len(all_blocks)} questions to {OUTPUT_FILE}")

if __name__ == '__main__':
    main()
