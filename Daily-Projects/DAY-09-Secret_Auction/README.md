# Day 9 - Secret Auction Program

A program that simulates a blind auction. Multiple users can enter their bids anonymously, and at the end, the highest bidder wins.

### How it works:
- Prompts each user for their name and bid amount.
- Asks if there are more bidders, and if so, clears the screen for the next bidder.
- Stores each bid in a dictionary with the bidder’s name as the key and the bid as the value.
- Once bidding ends, the program finds the highest bid.
- If multiple people placed the same highest bid, it declares a tie.
- Displays the winner(s) and the winning bid.

---

### What I learned:
- **Dictionaries**: Used to store key-value pairs (e.g., names and bids).
- **Defining/Retrieving/Adding/Editing dictionary items**: Assign values to keys, update existing entries.
- **Looping through a dictionary**: Iterate over keys and retrieve associated values.
- **KeyError**: Happens when accessing a non-existent key in a dictionary.
- **Difference between Lists and Dictionaries**:
  - Lists store ordered collections of items and allow duplicates.
  - Dictionaries store unordered key-value pairs and keys must be unique.
- **len() with dictionaries**: Returns the number of key-value pairs.
- **eval() function**: Evaluates a string as Python code (e.g., expressions, list literals).
- **Nesting**:
  - Lists in dictionaries.
  - Dictionaries in dictionaries.
  - Dictionaries in lists.
  - Lists in lists.
- **.items() method**: Returns key-value pairs for looping.
- **max() function with dictionaries**: Finds the highest value or key using `max(dictionary, key=dictionary.get)`.


---

See [NOTES.md](./NOTES.md) for detailed explanations of each concept.

