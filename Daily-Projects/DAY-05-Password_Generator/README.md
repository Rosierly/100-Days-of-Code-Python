#  Day 5 – Loops & Randomization | Password Generator 🔐

---

## 📚 What I Learned

Today I practiced using Python's loop structures, list handling, and the random module to build interactive and dynamic programs. Here’s what I covered:

- `for` loops to iterate through lists, strings, or ranges
- `range(start, stop, step)` to generate number sequences for iteration
- Input validation using `.isdigit()` to ensure users enter numbers
- Randomization techniques with `random.choice()` and `random.shuffle()`
- Creating modular code using functions to keep logic organized
- Using built-in functions:
  - `sum()` for total values
  - `max()` to find the highest number
  - `len()` to count elements
- Combining and manipulating lists using:
  - `+` operator for concatenation
  - `.extend()` to merge in-place
  - `.append()` in loops
- Working with strings:
  - `.join()` to convert lists into strings
  - `.strip()` and `.split()` for string formatting

---

## 🛠 Project: Password Generator

A command-line program that generates a strong, customizable password based on user-defined criteria.

- Prompts user for how many **letters**, **symbols**, and **numbers** they want
- Ensures input is numeric using input validation
- Uses Python’s `random` module to select characters from predefined pools
- Shuffles all selected characters to ensure a randomized password
- Converts the result into a clean string using `join()`
- Modular structure with separate functions for:
  - Checking user input
  - Selecting characters
  - Building and displaying the password
