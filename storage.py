import json
import os

from student import Student

DATA_FILE = os.path.join("data", "students.json")

def save_students(students):
    """Write all students to the JSON file."""
    try:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w") as f:
            json.dump([s.to_dict()for s in students], f, indent=4)
    except OSError as e:
        print(f"Could not save data: {e}")

def load_students():
    """Read students from the JSON file. Return [] if nothing usable is found."""
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Data file is corrupted. Starting with an empty list.")
        return []
    else:
        return [Student.from_dict(item) for item in data]