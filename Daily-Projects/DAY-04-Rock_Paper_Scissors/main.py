from ascii_art import rock, paper, scissors
import random

choices = [rock, paper, scissors]


def check_input(prompt_text: str, valid_answers: list) -> int:
    """Prompts the user until a valid input is received, then returns it as an integer."""
    user_input = input(prompt_text).strip()
    while user_input not in valid_answers:
        user_input = input("That's not a valid answer. Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
    else:
        return int(user_input)


def determine_winner(user: int, computer: int) -> None:
    """Determines and prints the result of the game."""
    if ((user == 0 and computer == 2) or
            (user == 1 and computer == 0) or
            (user == 2 and computer == 1)):
        print("You win!")
    elif user == computer:
        print("It's a draw.")
    else:
        print("You lose.")


def game():
    """Main game loop: handles input, computer choice, winner check, and replay."""
    # User's choice
    user_choice_index = check_input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ",
                                    ["0", "1", "2"])
    print(choices[user_choice_index])

    # Computer's choice
    computer_choice_index = random.randint(0, len(choices) - 1)
    print(f"Computer chose:\n{choices[computer_choice_index]}")

    # Winner
    determine_winner(user_choice_index, computer_choice_index)

    # Play again
    keep_playing = input("Do you want to play again? Type 'Y' for yes or 'N' for no: ").upper()
    if keep_playing == "Y":
        game()  # recursion
    else:
        print("\nGoodbye!")


game()
