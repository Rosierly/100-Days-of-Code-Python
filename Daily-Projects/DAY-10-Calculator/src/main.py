from art import logo
import os


def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_number(order_of_number):
    """Prompt the user to enter a valid number and return it."""
    while True:
        try:
            num = float(input(f"What's the {order_of_number} number?: "))
        except ValueError:
            print("Invalid Input. Please type a valid number.")
        else:
            return num


def get_operator():
    """Prompt the user to pick one of the accepted operators and return it."""
    while True:
        operator_sign = input("+\n-\n*\n/\nPick an operation: ")
        if operator_sign in ["+", "-", "*", "/"]:
            return operator_sign
        print(f"Invalid Input. {operator_sign} is not one of the above operators.")


def calculate(num1, num2, operator_sign):
    """Perform a calculation using the selected operator and return the result."""
    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2,
    }
    calculation_result = operations[operator_sign]
    return f"{num1} {operator_sign} {num2} = {calculation_result}", calculation_result


def run_calculator():
    """Main function for the calculator program."""
    print(logo)
    first_number = get_number("first")
    while True:
        operator = get_operator()
        second_number = get_number("next")

        # Handle division by zero
        if operator == '/' and second_number == 0:
            print(f"Error: Division by zero. Please try again. Your first number is {first_number}")
            continue

        output, result = calculate(first_number, second_number, operator)
        print(f"{output}\n\n")

        # Ask the user if they want to continue with this result or start fresh
        go_again = input(f"Type 'y' to continue calculating with {result}, "
                         f"or type 'n' to start a new calculation: ").strip().lower()
        if go_again == "y":
            first_number = result  # Use previous result as first number
        elif go_again == "n":
            clear_console()
            run_calculator()  # Start fresh
        else:  # Any other input exits the program
            print("Goodbye!")
            return


run_calculator()

