import tkinter as tk
import random


class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.secret_number = random.randint(1, 20)
        self.guess_count = 0
        self.best_score = None

        self.label = tk.Label(root, text="Guess a number between 1 and 20:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.button = tk.Button(
            root, text="Submit Guess", bg="#4CAF50", fg="white", command=self.check_guess)
        self.button.pack(pady=5)

        self.reset_button = tk.Button(
            root, text="Reset Game", bg="#2196F3", fg="white", command=self.reset_game)
        self.reset_button.pack(pady=5)

        self.score_label = tk.Label(root, text="Best Score: None")
        self.score_label.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.guess_count += 1

            if guess < self.secret_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.secret_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(
                    text=f"Correct! You guessed in {self.guess_count} tries.")
                if self.best_score is None or self.guess_count < self.best_score:
                    self.best_score = self.guess_count
                    self.score_label.config(
                        text=f"Best Score: {self.best_score}")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

    def reset_game(self):
        self.secret_number = random.randint(1, 20)
        self.guess_count = 0
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
