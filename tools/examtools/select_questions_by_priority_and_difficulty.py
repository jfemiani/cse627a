import pandas as pd

df = pd.read_csv("question_info.csv")


# Extract unique filenames to determine which questions came from Exam 1 and which from Exam 2
df['source_exam'] = df['filename'].apply(lambda x: 'exam1' if 'exam1' in x.lower() else 'exam2')

# Calculate how many points we can take from each exam
total_points = 100
exam1_weight = 0.20
exam2_weight = 0.80
points_exam1 = round(total_points * exam1_weight)
points_exam2 = total_points - points_exam1

# Separate the data
df_exam1 = df[df['source_exam'] == 'exam1']
df_exam2 = df[df['source_exam'] == 'exam2']

# Sort by 'edge_flag' and 'difficulty' for priority ranking
priority_order = {'edge': 1, 'non-edge': 0} # Prefer non-edge questions 
difficulty_order = {'concept-check': 0, 'easy': 1, 'medium': 2, 'hard': 3} # Prefer easy questions
df_exam1_sorted = df_exam1.copy()
df_exam1_sorted['priority'] = df_exam1['edge_flag'].map(priority_order)
df_exam1_sorted['difficulty_rank'] = df_exam1['difficulty'].map(difficulty_order)
df_exam1_sorted = df_exam1_sorted.sort_values(by=['priority', 'difficulty_rank'])

df_exam2_sorted = df_exam2.copy()
df_exam2_sorted['priority'] = df_exam2['edge_flag'].map(priority_order)
df_exam2_sorted['difficulty_rank'] = df_exam2['difficulty'].map(difficulty_order)
df_exam2_sorted = df_exam2_sorted.sort_values(by=['priority', 'difficulty_rank'])

# Select questions from each exam up to their respective point budgets
selected_exam1 = []
selected_exam2 = []
running_total_exam1 = 0
running_total_exam2 = 0

for _, row in df_exam1_sorted.iterrows():
    if running_total_exam1 + row['points'] <= points_exam1:
        selected_exam1.append(row.name)
        running_total_exam1 += row['points']

for _, row in df_exam2_sorted.iterrows():
    if running_total_exam2 + row['points'] <= points_exam2:
        selected_exam2.append(row.name)
        running_total_exam2 += row['points']

# Mark which to keep or remove and why
df['final_points'] = df['points']
df['keep_reason'] = ""

df.loc[~df.index.isin(selected_exam1 + selected_exam2), 'final_points'] = 0
df.loc[~df.index.isin(selected_exam1 + selected_exam2), 'keep_reason'] = "Does not fit within point budget"

df.loc[df.index.isin(selected_exam1 + selected_exam2), 'keep_reason'] = "Fits point budget and ranked by edge/difficulty"


# Save processed file for export if needed
df.to_csv("final_exam_selection.csv", index=False)
