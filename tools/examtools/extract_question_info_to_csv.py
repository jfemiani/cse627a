import os
import csv
import re

# Directories containing quiz files
QUIZ_DIRS = [
    # "chapter1",
    # "chapter5",
    
    # "chapter6",
    # "chapter7",
    # "chapter8",
    # "chapter14",
    
    "exams",
]

# Output CSV file
OUTPUT_CSV = 'question_info.csv'

def extract_titles_from_file(filepath):
    """
    Extracts quiz question titles from a file.
    Titles are lines that start with "Title:" and follow the pattern:
      Title: difficulty – level – edge/non-edge – description
    Returns a list of (difficulty, level, edge_flag, description) tuples.
    """
    titles = []
    title_pattern = re.compile(r'^Title:\s*(.+)$')
    for line in open(filepath, encoding='utf-8'):
        match = title_pattern.match(line)
        if match:
            # Split the remainder on en-dash
            parts = re.split(r'\s*–\s*', match.group(1))
            if len(parts) >= 4:
                difficulty = parts[0].strip()
                level = parts[1].strip()
                edge_flag = parts[2].strip()
                description = ' – '.join(parts[3:]).strip()
                titles.append((difficulty, level, edge_flag, description))
    return titles

def main():
    print("Extracting question information from quiz files...")
    print("Directories to search:", QUIZ_DIRS)
    # Color the next text red
    print("\033[91mNOTE: This will ignore the original 'points' value in the quiz files and assign 1 point to each question.\033[0m")
    
    # Prepare output CSV
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['filename', 'difficulty', 'level', 'edge_flag', 'description', 'points'])
        
        # Iterate through quiz directories
        for quiz_dir in QUIZ_DIRS:
            if not os.path.isdir(quiz_dir):
                continue
            for fname in os.listdir(quiz_dir):
                if fname.endswith('-quiz.md') or fname.endswith('-quiz.txt'):
                    filepath = os.path.join(quiz_dir, fname)
                    titles = extract_titles_from_file(filepath)
                    for difficulty, level, edge_flag, description in titles:
                        writer.writerow([filepath, difficulty, level, edge_flag, description, '1'])
    print("-"*40)
    print(f"Extracted question information to {OUTPUT_CSV}")
    
if __name__ == "__main__":
    main()

