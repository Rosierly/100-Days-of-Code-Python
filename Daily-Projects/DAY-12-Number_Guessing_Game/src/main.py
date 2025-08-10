from art import logo
import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def set_difficulty() -> int:
    """Returns a number of attempts based on chosen difficulty."""
    while True:
        difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty_level == "easy":
            return EASY_LEVEL_ATTEMPTS
        elif difficulty_level == "hard":
            return HARD_LEVEL_ATTEMPTS
        else:
            print("That's not a valid answer please try again.\n")


def get_guess() -> int:
    """Gets a valid number from the user between 1 and 100 and returns it."""
    while True:
        guess = input("Make a guess: ")
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= 100:
                return guess
        print("That's not a valid number. Please try again.")


def game():
    """Runs a round of the Number Guessing Game."""
    print(f"{logo}\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    attempts = set_difficulty()  # set the number of attempts based on the user's chosen difficulty level
    random_num = random.randint(1, 100)  # generate a random number between 1 and 100

    # Main game loop
    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        user_guess = get_guess()

        if user_guess > random_num:
            print("Too high.")
        elif user_guess < random_num:
            print("Too low.")
        else:
            print(f"\nYou got it! The answer was {random_num}.")
            return  # exit the function if guessed correctly
        attempts -= 1  # decrease attempts after a wrong guess

    # if there are no remaining attempts
    print(f"\nYou've run out of guesses. The answer was {random_num}.")


game()
