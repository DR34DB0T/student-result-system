import os 
from datetime import datetime

import results

REPORT_DIR = "reports"

def sort_by_average(students):
    return sorted(students, key=results.calculate_average, reverse=True)

def sort_by_name(students):
    return sorted(students, key=lambda s: s.name.lower())

def build_summary(students):
    """Return a text table of all students with total, average and grade."""
    lines = [f"{'ID':<10}{'Name':<22}{'Total':>8}{'Average':>10}{'Grade':>7}",
            "-" * 57]
    for s in students:
        d = results.get_report_data(s)
        lines.append(f"{s.student_id:<10}{s.name[:20]:<22}"
                    f"{d['total']:>8}{d['average']:>10}{d['grade']:>7}")
    return "\n".join(lines)

def class_statistics(students):
    """Return stats for students who have scores, or None if nobody does."""
    scored = [s for s in students if s.scores]
    if not scored:
        return None 
    average = [results.calculate_average(s)for s in scored]
    best = max(scored, key=results.calculate_average)
    worst = min(scored, key=results.calculate_average)
    return{
        "count": len(scored), 
        "class_average": round(sum(average) / len(average), 2),
        "highest": (best.name, round(results.calculate_average(best), 2)),
        "lowest": (worst.name, round(results.calculate_average(worst), 2)),
    }

def build_statistics(students):
    stats = class_statistics(students)
    if stats is None:
        return "No scores recorded yet."
    return (f"Students with scores: {stats['count']}\n"
            f"Class average: {stats['class_average']}\n"
            f"Highest average: {stats['highest'][1]}{stats['highest'][0]}\n"
            f"Lowest average: {stats['lowest'][1]} ({stats['lowest'][0]})")

def save_report(students):
    """Save the ranked summary and statistics to a timestamped text file"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    path = os.path.join(REPORT_DIR, f"report_{timestamp}.txt")
    try:
        os.makedirs(REPORT_DIR, exist_ok=True)
        with open(path, "w") as f:
            f.write("STUDENT RESULT REPORT\n")
            f.write(f"Generated: {datetime.now():%Y-%m-%d %H:%M}\n\n")
            f.write(build_summary(sort_by_average(students)))
            f.write("\n\nCLASS STATISTICS\n")
            f.write(build_statistics(students))
            f.write("\n")
    except OSError as e:
        print(f"Could not save report: {e}")
        return None
    return path
