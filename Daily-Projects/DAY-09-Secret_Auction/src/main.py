from art import logo
import os


def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_bid():
    """Prompts user for name, bid amount, and checks if more bidders will enter."""

    # Ask for a unique name
    while True:
        user_name = input("What is your name?: ")
        if user_name not in bids_dict:
            break
        print("That name has already been used. Please enter a different name.")

    # Ask for a valid bid amount
    bid_amount = None
    while True:
        try:
            bid_amount = float(input("What is your bid?: $"))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please type a number.")

    # Ask if there are other bidders
    while True:
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if other_bidders in ['yes', 'no']:
            return user_name, bid_amount, other_bidders
        print("Invalid input. Please try again.")


def add_bid_to_dict(bids_dictionary, user_name, bid_amount):
    """Adds a bidder's name and bid amount to the dictionary."""
    bids_dictionary[user_name] = bid_amount


def get_highest_bid():
    """Returns the highest bid and corresponding bidder(s), handling ties."""
    highest_bid = 0
    top_bidder = None

    # Find the highest bid
    for bidder, amount in bids_dict.items():
        if amount > highest_bid:
            highest_bid = amount
            top_bidder = bidder

    # Check if multiple bidders have the highest bid
    equality, equal_bidders = check_equality(highest_bid)
    if equality:
        top_bidder = ', '.join(equal_bidders)

    return top_bidder, highest_bid


def check_equality(highest_bid):
    """Checks if more than one bidder has placed the same highest bid."""
    equal_bidders = []
    for bidder in bids_dict:
        if bids_dict[bidder] == highest_bid:
            equal_bidders.append(bidder)
    return len(equal_bidders) > 1, equal_bidders


# --- Program Start ---
print(logo)
bids_dict = {}

while True:
    name, bid, more_bidders = get_bid()
    add_bid_to_dict(bids_dict, name, bid)
    clear_console()  # otherwise: print("\n" * 100)
    if more_bidders == "no":
        winner, winning_bid = get_highest_bid()

        # Print result with tie check
        if ", " in winner:
            print(f"It's a tie. The winners are {winner} with a bid of ${winning_bid}.")
        else:
            print(f"The winner is {winner} with a bid of ${winning_bid}.")

        input("\n\nPress Enter to Exit...")
        break

