import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maths Quiz")  # Changed title to Maths Quiz
        self.root.geometry("600x400")  # Set a fixed size for better layout
        self.root.configure(bg="black")  # Black background
        self.difficulty = None
        self.score = 0
        self.question_num = 0
        self.current_a = None
        self.current_b = None
        self.current_op = None
        self.attempt = 1
        
        self.display_menu()

    def display_menu(self):
        self.menu_frame = tk.Frame(self.root, bg="white", bd=5, relief="ridge")
        self.menu_frame.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(self.menu_frame, text="Welcome to the Maths Quiz!", font=("Arial", 16, "bold"), bg="white", fg="black").pack(pady=5)  # Updated welcome message
        tk.Label(self.menu_frame, text="Select a difficulty level to start:", font=("Arial", 14), bg="white", fg="black").pack(pady=5)
        tk.Label(self.menu_frame, text="DIFFICULTY LEVEL", font=("Arial", 18, "bold"), bg="white", fg="black").pack(pady=10)
        tk.Button(self.menu_frame, text="1. Easy", command=lambda: self.set_difficulty("easy"), width=20, height=2, relief="raised", bd=10, bg="white", fg="black", font=("Arial", 12, "bold")).pack(pady=5)
        tk.Button(self.menu_frame, text="2. Moderate", command=lambda: self.set_difficulty("moderate"), width=20, height=2, relief="raised", bd=10, bg="white", fg="black", font=("Arial", 12, "bold")).pack(pady=5)
        tk.Button(self.menu_frame, text="3. Advanced", command=lambda: self.set_difficulty("advanced"), width=20, height=2, relief="raised", bd=10, bg="white", fg="black", font=("Arial", 12, "bold")).pack(pady=5)

    def set_difficulty(self, diff):
        self.difficulty = diff
        self.menu_frame.destroy()
        self.start_quiz()

    def start_quiz(self):
        self.quiz_frame = tk.Frame(self.root, bg="white", bd=5, relief="ridge")
        self.quiz_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.next_question()

    def next_question(self):
        if self.question_num >= 10:
            self.display_results()
            return
        self.question_num += 1
        self.attempt = 1
        self.current_op = self.decide_operation()
        self.current_a, self.current_b = self.random_int()
        self.display_problem()

    def random_int(self):
        if self.difficulty == "easy":
            min_val, max_val = 0, 9
        elif self.difficulty == "moderate":
            min_val, max_val = 10, 99
        else:  # advanced
            min_val, max_val = 1000, 9999
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val)
        if self.current_op == '-':
            if a < b:
                a, b = b, a  # Ensure a >= b for subtraction
        return a, b

    def decide_operation(self):
        return random.choice(['+', '-'])

    def display_problem(self):
        self.problem_label = tk.Label(self.quiz_frame, text=f"{self.current_a} {self.current_op} {self.current_b} =", font=("Arial", 16, "bold"), bg="white", fg="black")
        self.problem_label.pack(pady=10)
        self.answer_entry = tk.Entry(self.quiz_frame, font=("Arial", 14), width=20, bg="white", fg="black")
        self.answer_entry.pack(pady=5)
        self.submit_button = tk.Button(self.quiz_frame, text="Submit", command=self.check_answer, width=15, height=2, relief="raised", bd=5, bg="white", fg="black", font=("Arial", 12, "bold"))
        self.submit_button.pack(pady=10)

    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            correct = self.is_correct(user_answer)
            if correct:
                if self.attempt == 1:
                    self.score += 10
                else:
                    self.score += 5
                messagebox.showinfo("Correct", "Good job!")
                self.clear_question()
                self.next_question()
            else:
                if self.attempt == 1:
                    self.attempt = 2
                    messagebox.showerror("Wrong", "Try again.")
                    self.answer_entry.delete(0, tk.END)
                else:
                    correct_answer = self.current_a + self.current_b if self.current_op == '+' else self.current_a - self.current_b
                    messagebox.showerror("Wrong", f"Correct answer is {correct_answer}")
                    self.clear_question()
                    self.next_question()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def is_correct(self, answer):
        if self.current_op == '+':
            return answer == self.current_a + self.current_b
        else:
            return answer == self.current_a - self.current_b

    def clear_question(self):
        self.problem_label.destroy()
        self.answer_entry.destroy()
        self.submit_button.destroy()

    def display_results(self):
        self.quiz_frame.destroy()
        rank = self.get_rank()
        messagebox.showinfo("Results", f"Your score: {self.score}/100\nRank: {rank}")
        self.ask_replay()

    def get_rank(self):
        if self.score > 90:
            return "A+"
        elif self.score > 80:
            return "A"
        elif self.score > 70:
            return "B"
        elif self.score > 60:
            return "C"
        else:
            return "D"

    def ask_replay(self):
        replay = messagebox.askyesno("Play Again?", "Do you want to play again?")
        if replay:
            self.reset()
            self.display_menu()
        else:
            self.root.quit()

    def reset(self):
        self.difficulty = None
        self.score = 0
        self.question_num = 0
        self.current_a = None
        self.current_b = None
        self.current_op = None
        self.attempt = 1

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
