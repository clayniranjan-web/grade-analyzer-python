# ===========================
# Project: Student Grade Analyzer
# Description: Analyses student scores, computes averages,
#             finds the topper, flags anyone below passing.
# ===========================


# ---- Constants ----
# Minimum average score required to pass
passing_marks = 60

# ---- Data ----
# Each student is a dict with a name and a list of subject scores
students = [
    {"name": "Clay", "scores": [85, 90, 78]},
    {"name": "Priya", "scores": [55, 60, 48]},
    {"name": "Rohit", "scores": [92, 88, 95]},
    {"name": "Simran", "scores": [40, 55, 38]},
    {"name": "Dev", "scores": [70, 75, 80]}
]


# ---- Functions ----

def calculate_avg(scores):
    """Returns the average of a list of scores, rounded to 1 decimal."""
    avg_score = round(sum(scores)/len(scores), 1)
    return avg_score



def find_topper(students):
    """Returns the name and average of the highest scoring student."""
    topper_name = ""
    highest_avg = 0
    for student in students:
        student_avg = calculate_avg(student["scores"])
        if student_avg > highest_avg:
            highest_avg = student_avg
            topper_name = student["name"]
    return topper_name, highest_avg



def flag_failing(students):
    """Returns a list of student names whose average is below PASSING_MARKS."""
    failing = []
    for student in students:
        student_average = calculate_avg(student["scores"])
        if student_average < passing_marks:
            failing.append(student["name"])
    return failing



def print_report(students, topper_name, highest_avg, failing):
    """Prints the full formatted grade report."""
    print("-" * 30)
    print(f"{'Name':<10} | {'Avg' :<6} | Status")
    print("-" * 30)
    for student in students:
        student_average = calculate_avg(student['scores'])
        # Determine pass/fail status based on PASSING_MARKS threshold
        status = '👍Pass' if student_average >= passing_marks else '😲Fail'
        print(f"{student['name']:<10} | {student_average:<6} | {status}")
    print("-" * 30)
    print(f"🏆Topper: {topper_name} with {highest_avg} marks")
    print(f"❌ Failing:{failing}")




def main():
    """Runs the grade analyzer."""
    topper_name, highest_avg = find_topper(students)
    failing = flag_failing(students)
    print_report(students, topper_name, highest_avg, failing)

if __name__ == "__main__":
    main()