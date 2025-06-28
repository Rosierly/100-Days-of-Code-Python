from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def get_valid_inputs():
    """Prompt user for valid direction, message, and shift number input."""
    error_message = "Invalid input. Please try again."

    # Get valid direction input
    while True:
        shift_direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if shift_direction in ("encode", "decode"):
            break
        print(error_message)

    # Get message input
    user_message = input("Type your message:\n").lower()

    # Get valid shift number
    while True:
        shift_number = input("Type the shift number:\n")
        if shift_number.isdigit():
            break
        print(error_message)

    return shift_direction, user_message, int(shift_number)


def run_caesar_cipher(shift_direction, user_message, shift_number):
    """Apply caesar cipher to encode or decode the given message."""
    final_message = ""

    # Reverse the shift_number for decoding
    if shift_direction == "decode":
        shift_number *= -1

    # Shift each character in the message
    for character in user_message:
        if character in alphabet:
            initial_index = alphabet.index(character)
            shifted_index = (initial_index + shift_number) % len(alphabet)  # Limit shift_index to alphabet size
            final_message += alphabet[shifted_index]
        else:  # Leave characters that aren't in the alphabet unchanged
            final_message += character

    print(f"Here's the {shift_direction}d result: {final_message}")

    # Ask the user if they want to run the program again
    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if go_again == 'yes':
        start_program()
    else:
        print("Goodbye!")


def start_program():
    """Start the Caesar cipher program."""
    direction, text, shift = get_valid_inputs()
    run_caesar_cipher(direction, text, shift)


print(logo)
start_program()
