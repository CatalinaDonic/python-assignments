import tkinter as tk
from random import randrange


class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number")

        self.comp_number = randrange(1, 21)
        self.attempts = 0

        # GUI stuff
        self.message_label = tk.Label(root, text="The computer chose a number between 1 and 20.", font=("Arial", 12))
        self.message_label.pack(pady=10)

        self.input_label = tk.Label(root, text="Enter your guess:")
        self.input_label.pack()

        self.input_entry = tk.Entry(root)
        self.input_entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_guess)
        self.submit_button.pack(pady=5)

        self.new_game_button = tk.Button(root, text="New Game", command=self.new_game)
        self.new_game_button.pack(pady=5)

        self.show_number_button = tk.Button(root, text="Show Number", command=self.show_number)
        self.show_number_button.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=10)

        # Bind the Enter key to submit the guess
        self.input_entry.bind("<Return>", self.submit_guess_event)

    def submit_guess(self):
        user_input = self.input_entry.get()
        if not user_input.isdigit():
            self.result_label.config(text="Please enter a number between 0 to 20")
            return

        my_number = int(user_input)
        self.attempts += 1

        if my_number < self.comp_number:
            self.result_label.config(text="The number is bigger")
        elif my_number > self.comp_number:
            self.result_label.config(text="The number is smaller")
        else:
            self.result_label.config(
                text=f"You win! It took you {self.attempts} attempts."
            )

    def submit_guess_event(self, event):
        # submit_guess when Enter is pressed
        self.submit_guess()

    def new_game(self):
        self.comp_number = randrange(1, 21)
        self.attempts = 0
        self.result_label.config(text="")
        self.message_label.config(text="The computer chose a new number between 1 and 20.")
        self.input_entry.delete(0, tk.END)

    def show_number(self):
        self.result_label.config(text=f"The number is {self.comp_number}.")


if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
