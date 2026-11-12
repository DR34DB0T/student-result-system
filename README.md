# Student Result Management System

A menu-driven Python application for managing student records and
academic results. Built as the final project for Introduction to
Python Programming at New Horizon.


## Features

- Add, view, search, update and delete students
- Record scores for at least five subjects per student
- Calculate totals, averages and grades (A-F)
- Display individual report cards
- Sort students by average or by name
- Show class statistics (highest, lowest, class average)
- Save reports to a text file
- Data saved to and loaded from `data/students.json`
- Delete student profiles that aren't needed

## Requirements

- Python 3.8 or higher
- No external libraries (standard library only)

## How to Run

1. Clone the repository:
   git clone https://github.com/DR34DB0T/student-result-system.git
2. Go into the folder:
   cd student-result-system
3. Start the program:
   python main.py

## Project Structure

    student_result_system/
    ├── main.py        # Entry point and main menu
    ├── student.py     # Student class
    ├── results.py     # Totals, averages and grading
    ├── storage.py     # Load and save JSON data
    ├── reports.py     # Report generation
    ├── data/
    │   └── students.json
    └── README.md

## Grading Scale

| Average | Grade |
|---------|-------|
| 70-100  | A     |
| 60-69   | B     |
| 50-59   | C     |
| 40-49   | D     |
| 0-39    | F     |

## Python Concepts Used

- Variables, data types and type conversion
- Flow control (if/elif/else, for and while loops)
- Lists and dictionaries
- Functions with parameters and return values
- Sorting
- Exception handling (try/except)
- File handling with JSON
- Modules (code split across multiple files)
- Object-Oriented Programming (Student class)
- Dates and times (datetime)

## Future Improvements

- Tkinter graphical interface
- Export reports to CSv
