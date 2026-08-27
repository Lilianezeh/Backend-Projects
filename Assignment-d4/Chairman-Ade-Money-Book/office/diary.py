import json
from datetime import datetime


def add_diary_entry(diary):
    """Add a new entry to the estate diary."""

    entry = input("Enter diary entry: ").strip()

    if not entry:
        print("Diary entry cannot be empty.")
        return False

    current_time = datetime.now()

    diary_entry = {
        "date": current_time.strftime("%d/%m/%Y"),
        "time": current_time.strftime("%H:%M"),
        "entry": entry
    }

    diary.append(diary_entry)

    print("Diary entry added successfully.")
    return True


def display_diary(diary):
    """Display all diary entries."""

    print("\n---Estate Diary---")

    if not diary:
        print("No diary entries found.")
        return

    for diary_entry in diary:
        print(
            f"\nDate: {diary_entry['date']}"
            f"\nTime: {diary_entry['time']}"
            f"\nEntry: {diary_entry['entry']}"
        )


def save_diary(diary):
    """Save diary entries to a JSON file."""

    try:
        with open("data/diary.json", "w") as file:
            json.dump(diary, file, indent=4)

        print("Diary saved successfully.")
        return True

    except OSError:
        print("Unable to save diary records.")
        return False
    

def load_diary():
    """Load diary entries from the JSON file."""
    
    try:
        with open("data/diary.json", "r") as file:
            diary = json.load(file)
            
        print("Diary loaded successfully.")
        return diary
    
    except FileNotFoundError:
        print("No diary file found. starting with an empty list.")
        return[]
    
    except json.JSONDecodeError:
        print("Sorry, the diary records are corrupted.")
        return[]
