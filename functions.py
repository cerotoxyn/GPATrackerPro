"""
Author:  Cierra Danielson
Date written: 12/10/2024
Assignment: Final Project
Short Desc: Grade point average calculator

functions.py: Contains the core functionality for GPA tracker.
github.com/cerotoxyn/GPATrackerPro
"""

# Gradebook and Gradepoints
gradebook = {}
gradepoints = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "D-": 0.7,
    "F": 0.0
}

def add_course(course_name, credits):
    """Adds a course to the gradebook."""
    if course_name and course_name.upper() not in gradebook:
        gradebook[course_name.upper()] = {"grade": None, "credits": credits}
        return True
    return False

def assign_grade(course_name, grade):
    """Assigns a grade to an existing course."""
    course_name = course_name.upper()
    grade = grade.upper()
    if course_name in gradebook:
        if grade in gradepoints:
            gradebook[course_name]["grade"] = grade
            return True
        return "Invalid Grade"
    return "Course Not Found"

def calculate_gpa():
    """Calculates the GPA based on grades and credits."""
    total_point = sum(
        gradepoints[course["grade"]] * course["credits"]
        for course in gradebook.values()
        if course["grade"] is not None
    )
    total_credit = sum(course["credits"] for course in gradebook.values())
    return round(total_point / total_credit, 2) if total_credit else 0.0