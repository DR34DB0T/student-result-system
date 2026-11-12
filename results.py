MIN_SUBJECTS = 5

def calculate_total(student):
    return sum(student.scores.values())

def calculate_average(student):
    if not student.scores:
        return 0.0
    return calculate_total(student) / len(student.scores)

def assign_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

def has_enough_subjects(student):
    return len(student.scores) >= MIN_SUBJECTS

def validate_score(raw):
    """Convert input to a float between 0 and 100, or raise ValueError ."""
    try:
        score = float(raw)
    except ValueError:
        raise ValueError("Score must be a number.")
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")
    return score

def get_report_data(student):
    """Bundle everything a report card needs into one dictionary."""
    avg = calculate_average(student)
    return {
        "total": calculate_total(student),
        "average": round(avg, 2), 
        "grade": assign_grade(avg),
    }
