"""
Author:  Cierra Danielson
Date written: 12/10/2024
Assignment: Final Project
Short Desc: Grade point average calculator

gui_utils.py: Contains GUI-related functionality for GPA Tracker.
github.com/cerotoxyn/GPATrackerPro
"""

import tkinter as tk
from tkinter import ttk, messagebox
from functions import add_course, assign_grade, calculate_gpa, gradebook

def open_course_management():
    """Opens the course management window."""
    def handle_add_course():
        course = entry_course.get().strip()
        credits = entry_credits.get().strip()
        if not course or not credits.isdigit():
            messagebox.showerror("Error", "Course name and valid credits are required.")
            return
        credits = int(credits)
        if add_course(course, credits):
            messagebox.showinfo("Success", f"Course '{course}' added with {credits} credits!")
            update_course_list()
            update_combo_courses()
            entry_course.delete(0, tk.END)
            entry_credits.delete(0, tk.END)
        else:
            messagebox.showerror("Error", f"Course '{course}' could not be added.")

    def handle_assign_grade():
        course = combo_courses.get().strip()
        grade = entry_grade.get().strip()
        if not course or not grade:
            messagebox.showerror("Error", "Please select a course and enter a valid grade.")
            return
        result = assign_grade(course, grade)
        if result is True:
            messagebox.showinfo("Success", f"Grade '{grade}' assigned to {course}.")
            update_course_list()
            entry_grade.delete(0, tk.END)
        else:
            messagebox.showerror("Error", result)

    def update_course_list():
        tree.delete(*tree.get_children())
        for course, data in gradebook.items():
            grade = data["grade"] if data["grade"] else "Not Graded"
            tree.insert("", tk.END, values=(course, grade, data["credits"]))

    def update_combo_courses():
        combo_courses['values'] = list(gradebook.keys())

    course_window = tk.Toplevel()
    course_window.title("Manage Courses")
    course_window.geometry("700x500")
    course_window.resizable(False, False)

    tk.Label(course_window, text="Add Course:").grid(row=0, column=0, padx=10, pady=5)
    entry_course = tk.Entry(course_window)
    entry_course.grid(row=0, column=1, padx=10, pady=5)
    tk.Label(course_window, text="Credits:").grid(row=0, column=2, padx=10, pady=5)
    entry_credits = tk.Entry(course_window)
    entry_credits.grid(row=0, column=3, padx=10, pady=5)
    tk.Button(course_window, text="Add Course", command=handle_add_course).grid(row=0, column=4, padx=10, pady=5)

    tk.Label(course_window, text="Assign Grade:").grid(row=1, column=0, padx=10, pady=5)
    combo_courses = ttk.Combobox(course_window, values=list(gradebook.keys()))
    combo_courses.grid(row=1, column=1, padx=10, pady=5)
    entry_grade = tk.Entry(course_window)
    entry_grade.grid(row=1, column=2, padx=10, pady=5)
    tk.Button(course_window, text="Assign Grade", command=handle_assign_grade).grid(row=1, column=3, padx=10, pady=5)

    tree = ttk.Treeview(course_window, columns=("Course", "Grade", "Credits"), show="headings")
    tree.heading("Course", text="Course")
    tree.heading("Grade", text="Grade")
    tree.heading("Credits", text="Credits")
    tree.grid(row=2, column=0, columnspan=5, pady=10, sticky="nsew")
    update_course_list()

def open_gpa_results():
    """Opens the GPA results window."""
    gpa = calculate_gpa()
    results_window = tk.Toplevel()
    results_window.title("GPA Results")
    results_window.geometry("400x300")
    results_window.resizable(False, False)

    tk.Label(results_window, text=f"Your GPA: {gpa:.2f}", font=("Helvetica", 16)).pack(pady=20)

    tree = ttk.Treeview(results_window, columns=("Course", "Grade", "Credits"), show="headings")
    tree.heading("Course", text="Course")
    tree.heading("Grade", text="Grade")
    tree.heading("Credits", text="Credits")
    tree.pack(pady=10, fill=tk.BOTH, expand=True)

    for course, data in gradebook.items():
        grade = data["grade"] if data["grade"] else "Not Graded"
        tree.insert("", tk.END, values=(course, grade, data["credits"]))

    tk.Button(results_window, text="Close", command=results_window.destroy).pack(pady=10)