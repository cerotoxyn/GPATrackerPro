"""
Author:  Cierra Danielson
Date written: 12/10/2024
Assignment: Final Project
Short Desc: Grade point average calculator

main.py: Entry point for the GPA tracker application.
github.com/cerotoxyn/GPATrackerPro
"""

import tkinter as tk
from gui_utils import open_course_management, open_gpa_results
from functions import add_course, calculate_gpa
import os

def main():
    """Launches the main application window."""
    root = tk.Tk()
    root.title("GPA Tracker")
    root.geometry("400x300")
    root.iconbitmap("icon.ico")  
    root.resizable(False, False)

    tk.Label(root, text="GPA Tracker", font=("Helvetica", 20)).pack(pady=20)
    tk.Button(root, text="Manage Courses", command=open_course_management).pack(pady=10)
    tk.Button(root, text="View GPA", command=open_gpa_results).pack(pady=10)
    tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()