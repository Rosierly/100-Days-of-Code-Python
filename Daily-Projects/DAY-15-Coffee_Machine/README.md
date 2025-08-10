# Day 15 - Coffee Machine Program

A simulation of a coin-operated coffee machine that can serve espresso, latte, or cappuccino while tracking resources and processing payments.

### How it works:
- Offers a menu with three drinks: espresso, latte, and cappuccino, each with specific ingredient requirements and prices.
- Keeps track of available resources (water, milk, coffee) and total money earned.
- **Available commands:**
  - `espresso`, `latte`, `cappuccino` — order a drink.
  - `report` — display the current resources and total money.
  - `add` — add more resources to the machine.
  - `off` — turn off the coffee machine.
- Checks if enough resources are available before making a drink.
- Processes coins and verifies if the inserted amount covers the cost.
- Provides change if overpaid and refunds if underpaid.
- Deducts used ingredients when a drink is successfully made.

---

### What I learned:
- **Dictionaries - get() Method**: Safely retrieves a value from a dictionary —including nested dictionaries—, returning a default value if the key doesn’t exist, avoiding `KeyError`.
- **Dictionaries - items() Method with a `for` Loop**: Iterates over key-value pairs to access both simultaneously.
- **Formatting Numbers to 2 Decimal Places**: Using `:.2f` for display formatting and `round()` for numeric rounding.
- **String Formatting with format() Method**: Inserts variables into strings using `{}` placeholders.
- **How to add TODOs in your code**: Use `# TODO:` comments to mark pending tasks and track them in the IDE’s TODO tab.
- **How to bring up the Emoji Keyboard on Windows and Mac**: Shortcuts for quickly inserting emojis.
- **PyCharm Keyboard Shortcuts (Windows)**: Essential key combinations for running, debugging, navigating, editing, and refactoring in PyCharm.

---

See [NOTES.md](./NOTES.md) for detailed explanations of each concept.
