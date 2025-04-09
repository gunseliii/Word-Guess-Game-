import tkinter as tk
from tkinter import messagebox
import random

class WordGame:
    def __init__(self, words):
        self.words = words
        self.reset_game()

    def reset_game(self):
        self.word = random.choice(self.words)
        self.guessed = ['_' for _ in self.word]
        self.lives = 6
        self.guesses = []

    def guess_letter(self, letter):
        if letter in self.guesses:
            return
        self.guesses.append(letter)
        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.guessed[i] = letter
        else:
            self.lives -= 1

    def is_game_over(self):
        return self.lives == 0 or '_' not in self.guessed

    def is_winner(self):
        return '_' not in self.guessed

class WordGameGUI:
    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.master.title("🎉 Word Guessing Game 🎉")
        self.master.configure(bg="#f0f8ff")
        self.title_label = tk.Label(master, text="🔤 Guess the Word!", font=("Comic Sans MS", 24, "bold"), bg="#f0f8ff", fg="#2c3e50")
        self.title_label.pack(pady=10)
        self.word_label = tk.Label(master, text=' '.join(self.game.guessed), font=("Courier", 28), bg="#f0f8ff", fg="#1abc9c")
        self.word_label.pack(pady=10)
        self.lives_label = tk.Label(master, text=f"Lives left: {self.game.lives}", font=("Arial", 16), bg="#f0f8ff", fg="#e74c3c")
        self.lives_label.pack()
        self.entry = tk.Entry(master, font=("Arial", 14), width=5, justify='center')
        self.entry.pack(pady=5)
        self.guess_button = tk.Button(master, text="Guess", command=self.make_guess, bg="#3498db", fg="white", font=("Arial", 12, "bold"))
        self.guess_button.pack(pady=5)
        self.reset_button = tk.Button(master, text="Play Again", command=self.reset_game, bg="#9b59b6", fg="white", font=("Arial", 12, "bold"))
        self.reset_button.pack(pady=5)

    def make_guess(self):
        letter = self.entry.get().lower()
        self.entry.delete(0, tk.END)
        if letter and letter.isalpha() and len(letter) == 1:
            self.game.guess_letter(letter)
            self.word_label.config(text=' '.join(self.game.guessed))
            self.lives_label.config(text=f"Lives left: {self.game.lives}")
            if self.game.is_game_over():
                if self.game.is_winner():
                    messagebox.showinfo("🎉 You Won!", f"Congrats! The word was: {self.game.word}")
                else:
                    messagebox.showerror("💀 Game Over", f"You lost! The word was: {self.game.word}")
                self.disable_inputs()

    def disable_inputs(self):
        self.guess_button.config(state='disabled')
        self.entry.config(state='disabled')

    def reset_game(self):
        self.game.reset_game()
        self.word_label.config(text=' '.join(self.game.guessed))
        self.lives_label.config(text=f"Lives left: {self.game.lives}")
        self.guess_button.config(state='normal')
        self.entry.config(state='normal')

if __name__ == "__main__":
    words = ['python', 'developer', 'computer', 'coding', 'interface', 'hangman']
    game = WordGame(words)
    root = tk.Tk()
    gui = WordGameGUI(root, game)
    root.mainloop()