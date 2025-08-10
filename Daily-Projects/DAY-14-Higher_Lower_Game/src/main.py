from art import logo, vs
from game_data import data
import random
import os

DEBUG = False  # Set to True to enable debug hints and see follower counts during the game (for testing purposes)


def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_random_entry(existing_entry=None):  # default parameter
    """Returns a random entry from the data list, different from existing_entry if provided."""
    while True:
        entry = random.choice(data)  # Pick a random dictionary from the data list
        if entry != existing_entry:  # Ensure it's not the same as existing_entry (if given)
            return entry


def format_entry(entry, label="A"):
    """Returns a formatted string based on entry details and comparison label."""
    labels = {"A": "Compare A", "B": "Against B"}
    order = labels[label]
    name = entry["name"]
    description = entry["description"]
    country = entry["country"]
    return f"{order}: {name}, {description}, from {country}."


def get_valid_user_answer():
    """Prompts user until a valid answer is given and returns it."""
    while True:
        user_guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()
        if user_guess in ["a", "b"]:
            return user_guess
        print("Invalid Input. Please try again.")  # Prompt user again if invalid


def is_user_correct(follower_count_a, follower_count_b, user_guess):
    """Returns True if user_answer matches the entry with more followers, otherwise False."""
    # Determine which entry has more followers
    if follower_count_a > follower_count_b:
        right_answer = "a"
    else:
        right_answer = "b"
    # Compare user answer with correct answer
    return user_guess == right_answer


def play_game():
    """Main function to play the Higher Lower Game."""
    score = 0  # Initialize score
    entry_a = get_random_entry()  # Get initial random entry
    print(logo)

    # Main game loop
    while True:
        # Get a second entry that is not identical to entry_a
        entry_b = get_random_entry(entry_a)

        # Display entries A and B
        print(format_entry(entry_a, label="A"))
        print(vs)
        print(format_entry(entry_b, label="B"))

        # Get follower counts for both entries
        followers_a = entry_a["follower_count"]
        followers_b = entry_b["follower_count"]

        # Show follower counts when DEBUG mode is enabled (DEBUG = True)
        if DEBUG:
            print(f"\n  (DEBUG Hint) Followers A: {followers_a}, Followers B: {followers_b}")

        # Get user's guess
        user_answer = get_valid_user_answer()

        # Clear console output and print logo
        clear_console()
        print(logo)

        # Check if the user's guess was correct
        if not is_user_correct(followers_a, followers_b, user_answer):
            # If wrong, print final score & end the game
            print(f"Sorry, that's wrong. Final score: {score}.")
            input("Press `Enter` to Exit...")
            return
        # If correct, increase score and prepare for next round
        score += 1
        if user_answer == "b":
            entry_a = entry_b
        print(f"You're right! Current score: {score}.")


play_game()

