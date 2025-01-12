import tkinter as tk
from tkinter import ttk
import random


class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x500")

        self.user_score = 0
        self.computer_score = 0

        # Main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Score display
        self.score_var = tk.StringVar(value="Score - You: 0 Computer: 0")
        ttk.Label(main_frame, textvariable=self.score_var, font=("Arial", 14)).grid(
            row=0, column=0, columnspan=3, pady=20
        )

        # Result display
        self.result_var = tk.StringVar(value="Make your choice!")
        ttk.Label(main_frame, textvariable=self.result_var, font=("Arial", 12)).grid(
            row=1, column=0, columnspan=3, pady=20
        )

        # Choices display
        self.choices_var = tk.StringVar(value="")
        ttk.Label(main_frame, textvariable=self.choices_var, font=("Arial", 12)).grid(
            row=2, column=0, columnspan=3, pady=20
        )

        # Buttons
        style = ttk.Style()
        style.configure("Game.TButton", font=("Arial", 11), padding=10)

        ttk.Button(
            main_frame,
            text="Rock ✊",
            style="Game.TButton",
            command=lambda: self.play("Rock"),
        ).grid(row=3, column=0, padx=5, pady=20)
        ttk.Button(
            main_frame,
            text="Paper ✋",
            style="Game.TButton",
            command=lambda: self.play("Paper"),
        ).grid(row=3, column=1, padx=5, pady=20)
        ttk.Button(
            main_frame,
            text="Scissors ✌",
            style="Game.TButton",
            command=lambda: self.play("Scissors"),
        ).grid(row=3, column=2, padx=5, pady=20)

        # Reset button
        ttk.Button(main_frame, text="Reset Score", command=self.reset_score).grid(
            row=4, column=0, columnspan=3, pady=20
        )

    def play(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        self.choices_var.set(
            f"You chose: {user_choice}\nComputer chose: {computer_choice}"
        )

        # Game logic
        if user_choice == computer_choice:
            self.result_var.set("It's a tie!")
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors")
            or (user_choice == "Paper" and computer_choice == "Rock")
            or (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            self.result_var.set("You win!")
            self.user_score += 1
        else:
            self.result_var.set("Computer wins!")
            self.computer_score += 1

        self.update_score()

    def update_score(self):
        self.score_var.set(
            f"Score - You: {self.user_score} Computer: {self.computer_score}"
        )

    def reset_score(self):
        self.user_score = 0
        self.computer_score = 0
        self.update_score()
        self.result_var.set("Score reset! Make your choice!")
        self.choices_var.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
