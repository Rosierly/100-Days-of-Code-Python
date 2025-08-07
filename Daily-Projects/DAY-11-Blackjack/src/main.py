# HOUSE RULES
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

from art import logo
import random
import os

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def add_card(hand, num_of_cards):
    """Add a specified number of random cards to a hand and adjust Ace if needed."""
    for n in range(num_of_cards):
        hand.append(random.choice(CARDS))
    # Check for Ace and adjust if over 21
    if sum(hand) > 21 and 11 in hand:
        current_index = hand.index(11)
        hand[current_index] = 1


def display_cards(user_hand, dealer_hand, final_hand=False):
    """Print user and dealer hands and scores (based on game stage)."""
    if final_hand:
        print(f"   Your final hand: {user_hand}, final score: {sum(user_hand)}")
        print(f"   Computer's final hand: {dealer_hand}, final score: {sum(dealer_hand)}")
    else:
        print(f"    Your cards: {user_hand}, current score: {sum(user_hand)}")
        print(f"    Computer's first card: {dealer_hand[0]}")


def determine_winner(user_hand, dealer_hand):
    """Compare scores and print the result of the game."""
    user_score = sum(user_hand)
    dealer_score = sum(dealer_hand)

    # Covers the case where you have 21 with just two cards (natural Blackjack)
    # A natural Blackjack beats a regular 21 (made with more than two cards)
    user_natural = user_score == 21 and len(user_hand) == 2
    dealer_natural = dealer_score == 21 and len(dealer_hand) == 2

    if user_natural and dealer_natural:
        print("It's a draw. Both have natural Blackjacks.")
    elif user_natural:
        print("Congratulations! You won with a natural Blackjack.")
    elif dealer_natural:
        print("You lose. Dealer has a natural Blackjack.")
    elif user_score == dealer_score:
        print("It's a draw.")
    elif user_score > 21:
        print("You went over. You lose.")
    elif dealer_score > 21:
        print("The dealer went over. You win.")
    elif user_score > dealer_score:
        print("You win.")
    elif user_score < dealer_score:
        print("You lose.")


def run_blackjack():
    """Run one round of the Blackjack game."""
    print(logo)
    user_cards = []
    dealer_cards = []

    # Initial deal: 2 cards each
    add_card(user_cards, 2)
    add_card(dealer_cards, 2)
    display_cards(user_cards, dealer_cards)

    # User turn
    while sum(user_cards) <= 21:
        another_card = input("Type 'y' to get another card, or type anything else to pass: ")
        if another_card == "y":
            add_card(user_cards, 1)
            display_cards(user_cards, dealer_cards)
        else:
            break

    # Dealer draws until at least 17
    while sum(dealer_cards) < 17:
        add_card(dealer_cards, 1)

    # Final hands and result
    display_cards(user_cards, dealer_cards, final_hand=True)
    determine_winner(user_cards, dealer_cards)


# Main game loop
while True:
    answer = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if answer != "y":
        break
    clear_console()
    run_blackjack()

