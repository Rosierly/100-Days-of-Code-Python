# Day 14 - Higher Lower Game

A game where the player is shown two public figures, brands, or entities and must guess which one has more social media followers.

### How it works:
- Displays the game logo and selects a random entry (A) from the dataset.
- Chooses another random entry (B) that is not the same as A.
- Shows both entries with their name, description, and country.
- Optionally shows follower counts if `DEBUG` mode is enabled.
- Prompts the player to guess who has more followers by typing `A` or `B`.
- If the guess is correct, the score increases and the game continues with the correct choice as the new "A".
- If the guess is wrong, the game ends and the final score is displayed.

---

### What I learned:
- **Setting a Default Parameter**: Giving a function parameter a predefined value to use when no argument is passed, allowing for flexible function calls.

---

See [NOTES.md](./NOTES.md) for detailed explanations of each concept.
