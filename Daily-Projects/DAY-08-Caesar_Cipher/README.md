# Day 8 – Caesar Cipher | Functions, Inputs & Arguments

---

## 📚 What I Learned

Today I focused on writing flexible, reusable functions and using arguments effectively to control program behavior.

-  Defined functions that accept **multiple inputs** (parameters)
-  Learned the difference between **parameters vs arguments**
-  Practiced **positional vs keyword arguments**
-  Used methods like `.count()` and `.index()` for working with strings/lists
-  Applied built-in math rounding methods: `math.ceil()` and `math.floor()`

---

## 🛠 Project: Caesar Cipher

A simple encoder/decoder that shifts letters in the alphabet by a given amount. The user can choose to encode or decode a message with a custom shift amount.

- Supports **encryption and decryption**
- Accepts **multi-word messages** with symbols, numbers, and spaces preserved
- Validates all user inputs:
  - Must choose between `"encode"` or `"decode"`
  - Shift must be a number
- Supports **replay** with an option to re-run the program
- Handles shift numbers larger than the alphabet using `%` to loop back
