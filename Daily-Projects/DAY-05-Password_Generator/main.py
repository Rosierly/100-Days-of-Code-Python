import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def check_user_input(required_character: str):
    """Prompt user for a digit input for the given character type."""
    while True:
        user_input = input(f"How many {required_character} would you like in your password?\n ")
        if user_input.isdigit():
            return int(user_input)
        print("Invalid input. Please try again.")


def choose_characters(character_list: list, number_of_characters: int):
    """Return a list of random characters from the given list."""
    result = []
    for num in range(number_of_characters):
        result.append(random.choice(character_list))
    return result


print("Welcome to the PyPassword Generator!")

# Get user input for each character type
input_letters = check_user_input("letters")
input_symbols = check_user_input("symbols")
input_numbers = check_user_input("numbers")

# Build password list
password = []
password += choose_characters(letters, input_letters)
password += choose_characters(symbols, input_symbols)
password += choose_characters(numbers, input_numbers)

# Shuffle the characters to randomize order
random.shuffle(password)

# Convert list of characters into a string password
# 1st Way
password = ''.join(password)
# 2nd Way
new_password = ""
for char in password:
    new_password += char

print(password)

