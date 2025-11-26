import tkinter as tk
from tkinter import messagebox, scrolledtext
import os

def load_data():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'studentMarks.txt')
    if not os.path.exists(file_path):
        messagebox.showerror("Error", "studentMarks.txt not found in the script's folder.")
        return []
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    num_students = int(lines[0].strip())
    students = []
    for line in lines[1:1 + num_students]:
        parts = line.strip().split(',')
        code = int(parts[0])
        name = parts[1]
        marks = [int(x) for x in parts[2:5]]
        exam = int(parts[5])
        students.append({'code': code, 'name': name, 'marks': marks, 'exam': exam})
    return students

def get_grade(percent):
    if percent >= 70:
        return 'A'
    elif percent >= 60:
        return 'B'
    elif percent >= 50:
        return 'C'
    elif percent >= 40:
        return 'D'
    else:
        return 'F'

def display_student(student, text_area):
    text_area.delete(1.0, tk.END)
    name = student['name']
    code = student['code']
    coursework = sum(student['marks'])
    exam = student['exam']
    total = coursework + exam
    percent = (total / 160) * 100
    grade = get_grade(percent)
    text_area.insert(tk.END, f"Student Name: {name}\n")
    text_area.insert(tk.END, f"Student Number: {code}\n")
    text_area.insert(tk.END, f"Total Coursework Mark: {coursework}\n")
    text_area.insert(tk.END, f"Exam Mark: {exam}\n")
    text_area.insert(tk.END, f"Overall Percentage: {percent:.2f}%\n")
    text_area.insert(tk.END, f"Grade: {grade}\n")

def view_all(students, text_area):
    text_area.delete(1.0, tk.END)
    total_percent = 0
    for student in students:
        name = student['name']
        code = student['code']
        coursework = sum(student['marks'])
        exam = student['exam']
        total = coursework + exam
        percent = (total / 160) * 100
        total_percent += percent
        grade = get_grade(percent)
        text_area.insert(tk.END, f"Student Name: {name}\n")
        text_area.insert(tk.END, f"Student Number: {code}\n")
        text_area.insert(tk.END, f"Total Coursework Mark: {coursework}\n")
        text_area.insert(tk.END, f"Exam Mark: {exam}\n")
        text_area.insert(tk.END, f"Overall Percentage: {percent:.2f}%\n")
        text_area.insert(tk.END, f"Grade: {grade}\n\n")
    avg_percent = total_percent / len(students) if students else 0
    text_area.insert(tk.END, f"Number of students: {len(students)}\n")
    text_area.insert(tk.END, f"Average percentage: {avg_percent:.2f}%\n")

def view_individual(students, text_area, root):
    select_win = tk.Toplevel(root)
    select_win.title("Select Student")
    tk.Label(select_win, text="Enter Student Name or Code:").pack(pady=5)
    entry = tk.Entry(select_win)
    entry.pack(pady=5)
    
    def on_select():
        query = entry.get().strip()
        selected = None
        for s in students:
            if s['name'].lower() == query.lower() or str(s['code']) == query:
                selected = s
                break
        if selected:
            select_win.destroy()
            display_student(selected, text_area)
        else:
            messagebox.showerror("Error", "Student not found")
    
    tk.Button(select_win, text="Select", command=on_select).pack(pady=5)

def view_highest(students, text_area):
    if not students:
        messagebox.showinfo("Info", "No students found.")
        return
    highest = max(students, key=lambda s: sum(s['marks']) + s['exam'])
    display_student(highest, text_area)

def view_lowest(students, text_area):
    if not students:
        messagebox.showinfo("Info", "No students found.")
        return
    lowest = min(students, key=lambda s: sum(s['marks']) + s['exam'])
    display_student(lowest, text_area)

def main():
    students = load_data()
    root = tk.Tk()
    root.title("Student Marks Manager")
    root.geometry("600x500")
    
    frame = tk.Frame(root)
    frame.pack(pady=10)
    
    tk.Button(frame, text="View All Records", command=lambda: view_all(students, text_area)).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(frame, text="View Individual Record", command=lambda: view_individual(students, text_area, root)).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(frame, text="Highest Score", command=lambda: view_highest(students, text_area)).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(frame, text="Lowest Score", command=lambda: view_lowest(students, text_area)).grid(row=1, column=1, padx=5, pady=5)
    
    text_area = scrolledtext.ScrolledText(root, height=20, width=80)
    text_area.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
