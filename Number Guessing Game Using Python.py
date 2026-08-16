import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Number Guessing Game")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.config(bg="#f0f8ff")

        self.secret_number = 0
        self.attempts_left = 0
        self.score = 100

        self.setup_widgets()

    def setup_widgets(self):
        self.title_label = tk.Label(self.root, text="Number Guessing Game", font=("Helvetica", 16, "bold"), bg="#f0f8ff")
        self.title_label.pack(pady=10)

        self.difficulty_label = tk.Label(self.root, text="Choose Difficulty", font=("Helvetica", 12), bg="#f0f8ff")
        self.difficulty_label.pack()

        self.difficulty_var = tk.StringVar(value="Easy")
        difficulties = [("Easy", 10), ("Medium", 7), ("Hard", 5)]

        for text, val in difficulties:
            tk.Radiobutton(self.root, text=text, variable=self.difficulty_var, value=text,
                           font=("Helvetica", 10), bg="#f0f8ff").pack(anchor="center")

        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game, bg="#4CAF50", fg="white", width=15)
        self.start_button.pack(pady=10)

        self.info_label = tk.Label(self.root, text="", font=("Helvetica", 12), bg="#f0f8ff")
        self.info_label.pack(pady=10)

        self.guess_entry = tk.Entry(self.root, font=("Helvetica", 12), width=10, justify='center')
        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess, state="disabled", bg="#2196F3", fg="white")

        self.guess_entry.pack(pady=5)
        self.guess_button.pack()

        self.reset_button = tk.Button(self.root, text="New Game", command=self.reset_game, bg="#FF9800", fg="white", state="disabled")
        self.reset_button.pack(pady=5)

    def start_game(self):
        self.secret_number = random.randint(1, 100)
        difficulty = self.difficulty_var.get()

        if difficulty == "Easy":
            self.attempts_left = 10
        elif difficulty == "Medium":
            self.attempts_left = 7
        else:
            self.attempts_left = 5

        self.score = 100
        self.info_label.config(text="I'm thinking of a number between 1 and 100.")
        self.guess_button.config(state="normal")
        self.reset_button.config(state="normal")

    def check_guess(self):
        guess = self.guess_entry.get()
        try:
            guess = int(guess)
            if guess < 1 or guess > 100:
                messagebox.showwarning("Invalid", "Please enter a number between 1 and 100.")
                return
        except ValueError:
            messagebox.showwarning("Invalid", "Please enter a valid number.")
            return

        self.attempts_left -= 1
        self.score -= 10

        if guess < self.secret_number:
            feedback = "Too low! Try again."
        elif guess > self.secret_number:
            feedback = "Too high! Try again."
        else:
            messagebox.showinfo("🎉 Correct!", f"You guessed it! Score: {self.score + 10}")
            self.guess_button.config(state="disabled")
            return

        if self.attempts_left > 0:
            self.info_label.config(text=f"{feedback} Attempts left: {self.attempts_left}")
        else:
            self.info_label.config(text=f"Game Over! The number was {self.secret_number}.")
            self.guess_button.config(state="disabled")

    def reset_game(self):
        self.guess_entry.delete(0, tk.END)
        self.info_label.config(text="")
        self.guess_button.config(state="disabled")
        self.start_game()

# Run the game
root = tk.Tk()
app = NumberGuessingGame(root)
root.mainloop()
