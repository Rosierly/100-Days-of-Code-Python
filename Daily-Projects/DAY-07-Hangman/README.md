#  Day 7 – Hangman Game | Conditional Logic, Loops & Imports

---

## 📚 What I Learned

Today was about building a fully interactive game using loops, conditionals, string/list manipulation, and custom modules.

-  Flowchart-style logic to guide step-by-step program structure
-  `while` loops for continuous input and gameplay
-  Handling user input with validation
-  Using `in` and `not in` to check membership in strings/lists
-  Creating and using custom Python modules (`import from`)
-  Displaying game state dynamically with ASCII art and feedback
-  Modular function design to break down complex logic into smaller parts

---

## 🛠 Project: Hangman – Console Game

A classic hangman game where players attempt to guess a hidden word one letter at a time. Built for the console with difficulty levels and progressive visual feedback.

- Asks the user to choose a **difficulty level** (easy/normal/hard)
- Pulls a random word from a categorized dictionary (`words.py`)
- Tracks and displays **guessed letters** and **remaining lives**
- Validates user input:
  - Only allows single alphabetical characters
  - Prevents duplicate guesses
- Uses **ASCII art** to show the hangman's progress
- Reveals correct guesses in-place, hides the rest with underscores
- Ends the game on win or loss with a custom message
