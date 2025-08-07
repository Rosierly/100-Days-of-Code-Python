from words import words_dictionary  # Dictionary with words categorized by difficulty
from art import stages, logo
import random


def define_word() -> str:
    """Prompts the user to select a difficulty level and returns a random word from the corresponding word list."""
    while True:
        difficulty = input('Choose one level of difficulty.\nType "Easy", "Normal" or "Hard": ').lower()
        if difficulty in words_dictionary:
            print("\n************************************************************************\n")
            return random.choice(words_dictionary[difficulty])
        print("INVALID INPUT! Please try again.\n")


def generate_blank_slots_list(word: str) -> list:
    """Returns a list of underscores for each letter in the given word."""
    slots = []
    for _ in word:
        slots.append("_")
    return slots


def get_valid_guess() -> str:
    """Takes, validates, and returns a single letter guess from the user."""
    global guessed_letters
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) > 1:
            print("Please enter one character at a time.\n")
        elif not guess.isalpha():
            print("Be careful. Only alphabetical letters are allowed.\n")
        elif guess in guessed_letters:
            print("You've already guessed that letter. Don't worry, you won't lose a life.\n")
        else:
            guessed_letters.append(guess)
            return guess


def display_word():
    """Prints the current state of the word with already guessed letters."""
    revealed_letters = " ".join(letter_slots)
    print(f"Word to guess: {revealed_letters}")


def display_lives_left():
    """Prints hangman stage and lives left."""
    print(f"{stages[lives_left]}\n"
          f"**************************** {lives_left}/6 LIVES LEFT ****************************\n")


# Welcome message
print(f"{logo}\nWelcome to the Hangman Game!\nGood luck!\n")

# Game setup
lives_left = len(stages) - 1  # Total number of lives is based on stages
guessed_letters = []  # To keep track of all the guessed letters
random_word = define_word()  # Select random word based on chosen difficulty
letter_slots = generate_blank_slots_list(random_word)  # Initialize hidden word slots as underscores

# Main game loop
while True:
    user_guess = get_valid_guess()

    if user_guess in random_word:
        # Reveal all occurrences of the guessed letter
        for index_num in range(len(random_word)):
            if random_word[index_num] == user_guess:
                letter_slots[index_num] = user_guess
        # Check for win condition
        if "_" not in letter_slots:
            print(f"\nThe word was '{random_word}'.\n YOU WIN!")
            break

    elif user_guess not in random_word:
        lives_left -= 1
        print(f"\n'{user_guess}' is not in the word.")
        # Check for loss condition
        if lives_left == 0:
            print(" YOU LOSE.")
            break

    # Display current game state
    display_word()
    display_lives_left()
