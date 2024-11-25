import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.score = 0
        self.current_question_index = 0
        
        # Define the questions and answers
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
            {"question": "What is 5 + 3?", "options": ["6", "7", "8", "9"], "answer": "8"},
            {"question": "What color is the sky?", "options": ["Blue", "Green", "Red", "Yellow"], "answer": "Blue"},
        ]
        
        # Setup the UI
        self.question_label = tk.Label(self.root, text="", font=('Helvetica', 16))
        self.question_label.pack(pady=20)
        
        self.option_buttons = []
        for _ in range(4):  # For 4 options
            btn = tk.Button(self.root, text="", width=20, height=2, font=('Helvetica', 12), command=lambda idx=len(self.option_buttons): self.check_answer(idx))
            btn.pack(pady=5)
            self.option_buttons.append(btn)
        
        self.next_button = tk.Button(self.root, text="Next", width=20, height=2, font=('Helvetica', 12), command=self.next_question)
        self.next_button.pack(pady=20)
        
        # Display the first question
        self.display_question()
    
    def display_question(self):
        """Display the current question and its options."""
        question = self.questions[self.current_question_index]
        
        self.question_label.config(text=question["question"])
        
        for idx, option in enumerate(question["options"]):
            self.option_buttons[idx].config(text=option)
        
    def check_answer(self, selected_index):
        """Check the user's answer and provide feedback."""
        correct_answer = self.questions[self.current_question_index]["answer"]
        selected_answer = self.questions[self.current_question_index]["options"][selected_index]
        
        if selected_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Correct answer!")
        else:
            messagebox.showerror("Incorrect", f"Wrong answer! The correct answer is {correct_answer}.")
        
    def next_question(self):
        """Move to the next question or finish the quiz."""
        self.current_question_index += 1
        
        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            messagebox.showinfo("Quiz Finished", f"You completed the quiz! Your score is {self.score}/{len(self.questions)}.")
            self.root.quit()  # Close the app after the quiz is finished

# Create the main Tkinter window
root = tk.Tk()

# Create the QuizApp instance
quiz_app = QuizApp(root)

# Run the Tkinter event loop
root.mainloop()
