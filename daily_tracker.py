# Import datetime so we can automatically capture today's date
from datetime import datetime

# Import csv so we can save your daily progress into a CSV file
import csv

# Import os so we can check whether the CSV file already exists
import os


# This is the private file where your daily progress will be saved
file_name = "daily_progress.csv"


# These are your upgraded AI Life OS daily check-in questions
# Each key becomes a column in the CSV file
daily_entry = {
    # Automatically stores today's date in YYYY-MM-DD format
    "date": datetime.now().strftime("%Y-%m-%d"),

    # Tracks your physical/mental energy
    "energy_level": input("Energy level today (1-10): "),

    # Captures your main focus for the day
    "main_goal": input("What was your main goal today? "),

    # Tracks progress in AI, Python, automation, or product-building
    "ai_python_product": input("What did you do for AI/Python/product-building today? "),

    # Tracks work, career, leadership, or becoming secure/permanent
    "work_career": input("What did you do for work/career/leadership today? "),

    # Tracks gym, food, sleep, health, or body transformation
    "health_body": input("What did you do for gym/health/body/food/sleep today? "),

    # Tracks faith, prayer, purity, obedience, and mindset
    "faith_purity_mindset": input("What did you do for faith/prayer/purity/mindset today? "),

    # Captures your biggest positive moment
    "biggest_win": input("What was your biggest win today? "),

    # Captures blocker, temptation, distraction, or weakness
    "blocker_temptation": input("What was your biggest blocker/temptation/distraction today? "),

    # Checks whether you drifted from your standards or priorities
    "drift_today": input("Did you drift today? If yes, where and why? "),

    # Tracks discipline even when motivation was low
    "disciplined_action": input("Did you take one disciplined action even when you did not feel like it? "),

    # Tracks the environment that helped or hurt you
    "environment": input("What environment helped or hurt you today? "),

    # Identifies one behaviour to stop
    "thing_to_stop": input("What is one thing you need to stop doing? "),

    # Defines tomorrow's next step
    "next_step": input("What is your next step for tomorrow? "),

    # Ends with prayer/reflection
    "prayer_reflection": input("What is one prayer or reflection for tonight? ")
}


# Check whether the CSV file already exists
file_exists = os.path.isfile(file_name)


# Open the CSV file in append mode
# This adds a new row every time you run the tracker
with open(file_name, mode="a", newline="", encoding="utf-8") as file:

    # Create a CSV writer using the dictionary keys as column names
    writer = csv.DictWriter(file, fieldnames=daily_entry.keys())

    # If the CSV file does not exist yet, add the column headers
    if not file_exists:
        writer.writeheader()

    # Save today's answers as a new row
    writer.writerow(daily_entry)


# Confirm the entry has been saved
print("AI Life OS daily check-in saved successfully.")