# 1.Makes 3 hot flavors
#  Espresso
#  Latte
#  Cappuccino

# 2.Coin Operated
#  Penny = 1 cent
#  Nickel = 5 cents
#  Dime = 10 cents
#  Quarter = 25 cents

# TODO :Program Requirements
#  1.Print report (show remaining resources in the machine)
#  2.Check if the resources are sufficient
#  3.Process coins
#  4.Check if the transaction is successful
#  5.Make coffee (update resources accordingly)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def get_report():
    """Return a formatted report of current resource amounts and available money."""
    unit_by_resource = {
        "water": "ml",
        "milk": "ml",
        "coffee": "g",
    }

    formatted_report = ""
    for ingredient in resources:
        amount = resources[ingredient]
        unit = unit_by_resource.get(ingredient, "")
        formatted_report += f"{ingredient.title()}: {amount}{unit}\n"
    formatted_report += f"Money: ${money:.2f}"

    return formatted_report


def add_resources():
    """Adds specified amount to a chosen resource and updates the `resources` dictionary."""
    global resources

    valid_ingredients = ["water", "milk", "coffee"]
    while True:
        ingredient_to_add = input("Choose what type of ingredient you want to add: ").lower()
        if ingredient_to_add in valid_ingredients:
            break
        print(f"That's not a valid ingredient. Choose one of {valid_ingredients}.")

    amount = 0
    while True:
        try:
            amount = int(input("How much would you like to add? "))
        except ValueError:
            print("Invalid amount. Please try again.")
        else:
            break

    resources[ingredient_to_add] += amount
    print(f"{ingredient_to_add.title()} has been added.")
    print(get_report())


def get_coin(type_of_coin: str) -> int:
    """Prompts user to input the amount of a specific coin."""
    while True:
        try:
            amount_of_coin = int(input(f"How many {type_of_coin}?: "))
            if amount_of_coin < 0:
                print("Please enter a positive number for the amount of inserted coins.")
                continue  # Restart loop if invalid
        except ValueError:
            print("That's not a valid amount of coins. Please try again.")
        else:
            return amount_of_coin


def process_coins(selected_coffee: str) -> bool:
    """Checks if inserted coins cover the coffee cost and returns True if they do, otherwise False."""
    global money
    cost_of_coffee = MENU[selected_coffee]["cost"]

    print(f"Your cost of your coffee is ${cost_of_coffee:.2f}\nPlease insert coins.")
    quarters = get_coin("quarters")
    dimes = get_coin("dimes")
    nickels = get_coin("nickels")
    pennies = get_coin("pennies")

    total_amount = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

    if total_amount < cost_of_coffee:
        print(f"Sorry that's not enough money. Your money ${total_amount:.2f} has been refunded.")
        return False
    else:
        money += cost_of_coffee  # update the money in the machine
        change = total_amount - cost_of_coffee
        print(f"Here is ${change:.2f} in change.")
        return True


def efficient_resources(selected_coffee: str) -> bool:
    """Verifies if there are enough resources to make the coffee and returns True or False."""
    # Check each required ingredient against available resources
    for ingredient, amount_available in resources.items():
        amount_needed = MENU[selected_coffee]["ingredients"].get(ingredient, 0)  # accessing the inner dict first
        if amount_available < amount_needed:
            print(f"Insufficient resources. Sorry there is not enough {ingredient}.")
            return False  # early exit if any ingredient is insufficient
    return True  # after the for loop is completed, and all ingredients are checked


def update_resources(selected_coffee: str):
    """Subtracts the amount of the ingredients used to makes the coffee from the `resources` dictionary."""
    global resources
    for ingredient, amount_needed in MENU[selected_coffee]["ingredients"].items():
        resources[ingredient] -= amount_needed


def make_coffee(selected_coffee: str):
    """Prepares coffee and updates resources."""
    update_resources(selected_coffee)
    print(f"Here is your {selected_coffee} ☕️. Enjoy!")


def coffee_machine():
    """Runs the main coffee machine loop."""
    while True:
        user_input = input(" What would you like? (espresso/latte/cappuccino): ").lower()

        if user_input in MENU:  # checks against the top-level keys (ex."espresso")
            if efficient_resources(user_input):
                is_money_enough = process_coins(user_input)
                if is_money_enough:
                    make_coffee(user_input)
        elif user_input == "off":
            return  # turn off the machine -> exit the function
        elif user_input == "report":
            print(get_report())
        elif user_input == "add":
            add_resources()
        else:
            print("Invalid Input. Please try again.")


coffee_machine()

