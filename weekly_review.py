# Import pandas so we can read and analyse the CSV file
import pandas as pd

# This is the file created by daily_tracker.py
file_name = "daily_progress.csv"

# Read the daily progress CSV file into a table called df
df = pd.read_csv(file_name)

# Convert the date column into a real date format
df["date"] = pd.to_datetime(df["date"])

# Sort entries by date, newest last
df = df.sort_values("date")

# Get the last 7 entries from the tracker
recent_entries = df.tail(7)

# Convert energy level into numbers so we can calculate average energy
recent_entries["energy_level"] = pd.to_numeric(
    recent_entries["energy_level"],
    errors="coerce"
)

# Calculate key summary numbers
total_days_tracked = len(recent_entries)
average_energy = recent_entries["energy_level"].mean()

# Print the weekly review
print("\n==============================")
print("        WEEKLY REVIEW")
print("==============================\n")

print(f"Days tracked: {total_days_tracked}")
print(f"Average energy level: {average_energy:.1f}/10")

print("\n--- Recent Wins ---")
for win in recent_entries["biggest_win"]:
    print(f"- {win}")

print("\n--- Common Blockers ---")
for blocker in recent_entries["blocker"]:
    print(f"- {blocker}")

print("\n--- Next Actions ---")
for action in recent_entries["next_step"]:
    print(f"- {action}")

print("\nReview complete.")