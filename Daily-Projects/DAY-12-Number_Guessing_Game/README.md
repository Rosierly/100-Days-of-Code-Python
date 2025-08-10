# Day 12 - Number Guessing Game

A fun number guessing game where the player chooses a difficulty, then tries to guess a secret number between 1 and 100 before running out of attempts.

### How it works:
- Displays a welcome message along with the game logo.
- Asks the player to choose a difficulty level: Easy (10 attempts) or Hard (5 attempts).
- Generates a random number between 1 and 100.
- Prompts the player to guess the number, validating input to ensure it’s between 1 and 100.
- Gives hints after each guess (“Too high” or “Too low”).
- Decreases the number of remaining attempts for wrong guesses.
- Ends the game when the player guesses correctly or runs out of attempts.

---

### What I learned:
- **Namespaces: Local vs. Global Scope**: How variable accessibility is determined by where it’s defined, and how local variables differ from global ones.
- **There is no Block Scope in Python**: Variables defined in `if`, `for`, or `while` blocks are still accessible outside those blocks (unless inside a function).
- **How to Modify a Global Variable**: Using the `global` keyword or returning a value from a function to change a global variable.
- **Python Constants and Global Scope**: Naming conventions for constants (UPPERCASE) and why they’re usually defined in the global scope.

---

See [NOTES.md](./NOTES.md) for detailed explanations of each concept.
