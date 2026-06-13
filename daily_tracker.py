# Import datetime so we can automatically capture today's date
from datetime import datetime

# Import csv so we can save our progress into a CSV file
import csv

# Import os so we can check whether the CSV file already exists
import os


# This is the file where your daily progress will be saved
file_name = "daily_progress.csv"


# This dictionary stores all the answers you type in
# Each item has a column name on the left and your answer on the right
questions = {
    # Automatically stores today's date in YYYY-MM-DD format
    "date": datetime.now().strftime("%Y-%m-%d"),

    # Tracks your energy level for the day
    "energy_level": input("Energy level today (1-10): "),

    # Captures your main focus or goal for the day
    "main_goal": input("What is your main goal today? "),

    # Tracks anything you learned or built related to AI
    "ai_learning": input("What did you learn or build in AI today? "),

    # Tracks progress related to work, career, applications, leadership, etc.
    "work_progress": input("What progress did you make at work/career? "),

    # Tracks health actions like gym, food, sleep, walking, etc.
    "health": input("What did you do for health/gym/food? "),

    # Tracks prayer, mindset, reflection, gratitude, discipline, etc.
    "faith_mindset": input("Prayer/reflection/mindset note: "),

    # Captures your biggest win for the day
    "biggest_win": input("Biggest win today: "),

    # Captures the biggest problem or blocker you faced
    "blocker": input("Biggest blocker today: "),

    # Captures the next action you should take
    "next_step": input("What is the next best action? ")
}


# Check whether the CSV file already exists
# If it does not exist, we need to create it and add column headers
file_exists = os.path.isfile(file_name)


# Open the CSV file in append mode
# Append mode means new entries will be added at the bottom instead of replacing old data
with open(file_name, mode="a", newline="", encoding="utf-8") as file:

    # Create a CSV writer that knows the column names from our dictionary
    writer = csv.DictWriter(file, fieldnames=questions.keys())

    # If this is the first time creating the file, write the column headers
    if not file_exists:
        writer.writeheader()

    # Save today's answers as a new row in the CSV file
    writer.writerow(questions)


# Show confirmation message after saving
print("Daily progress saved successfully.")