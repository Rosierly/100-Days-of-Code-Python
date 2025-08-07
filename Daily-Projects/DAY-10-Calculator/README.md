# Day 10 - Calculator Program

A calculator program that performs continuous operations (+, -, *, /) and allows the user to keep calculating with the previous result or start over.

### How it works:
- Prompts the user to input two numbers and select an operator.
- Validates all inputs (numbers and operator symbols).
- Performs the corresponding arithmetic operation and returns the result.
- After the result is displayed, the user can choose to:
  - Continue calculating with the result.
  - Start a new calculation (recursively restarts the program).
  - Exit the program.
- Handles division by zero safely with an error message and retry.

---

### What I learned:
- **Functions with Outputs**: Using `return` to send values back from a function, enabling reuse and logic chaining.
- **Return vs Print**:
  - `return` sends data out of a function.
  - `print` only displays it but doesn’t make it reusable.
- **Built-in Functions & Output**:
  - Functions like `len()` return a value that can be stored or passed around.
  - Their outputs can replace function calls dynamically in expressions.
- **Function Output as Input**: You can use the result of one function as the input to another.
- **title() Method**: Capitalizes the first letter of each word in a string.
- **Return Statement**:
  - Used to exit a function and optionally return a value.
  - Stops execution of the function immediately.
  - Any code after `return` in the same block is ignored.
- **Multiple Return Values**: A function can return more than one value (e.g., a result and a string message).
- **Docstrings**: Document functions using triple-quoted strings to describe their purpose and behavior.
  > Also used for **multi-line comments** when not assigned or returned.
- **Recursion**:
  - A function calling itself.
  - Useful for restarting or repeating logic (e.g., restarting the calculator).
  - Must have a **base case** to prevent infinite recursion.
- **Flags**: Boolean variables used to control loops or logic flow.
- **Assigning Functions to Variables**: Store function references in variables or data structures like dictionaries, then call them dynamically.

---

See [NOTES.md](./NOTES.md) for detailed explanations of each concept.
