# Import pandas so we can read the progress CSV file
import pandas as pd

# This is the private progress file created by daily_tracker.py
file_name = "daily_progress.csv"

# Read the progress data
df = pd.read_csv(file_name)

# Get the last 7 entries only
recent_entries = df.tail(7)

# Convert the recent entries into text so AI can understand them
progress_text = recent_entries.to_string(index=False)

# Create a coaching prompt that can be pasted into ChatGPT or Claude
prompt = f"""
You are my personal AI life, career, and productivity coach.

Here is my recent progress data from my daily tracker:

{progress_text}

Please analyse this like a serious coach and mentor.

Tell me:
1. What patterns do you notice?
2. What am I doing well?
3. Where am I drifting or losing focus?
4. What are my top 3 priorities for the next 7 days?
5. What one habit should I improve immediately?
6. What should I stop doing?
7. What should I pray/reflect on this week?
8. Give me a short, direct action plan.

Be honest, practical, and specific.
"""

# Print the prompt so I can copy and paste it into ChatGPT or Claude
print("\n==============================")
print(" AI REVIEW PROMPT")
print("==============================\n")
print(prompt)