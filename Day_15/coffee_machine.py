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
    },
}
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 2. Check if there are enough resources to make the coffee.
def check_resources(choice, resources):
    """Check for available resources."""
    for item, required_amount in MENU[choice]["ingredients"].items():
        if resources[item] < required_amount:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: 3. Process the coins.
def process_coins():
    """Process the coins. Return the total amount of coins inserted by the user"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return round(total, 2)


# TODO: 4. Check if the transactions are successful.
def check_transactions(transactions, choice):
    """Check for transactions. Return True if the transactions are successful, False otherwise."""
    global money
    if transactions < MENU[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif transactions >= MENU[choice]["cost"]:
        change = transactions - MENU[choice]["cost"]
        money += MENU[choice]["cost"]
        print(f"Here is ${change} in change.")
        return True


# TODO: 5. Make the coffee.
def make_coffee(resources, choice):
    """Make the coffee. Return the coffee of choice."""
    for items in resources:
        # Loop through the resources and subtract the amount of resources used
        resources[items] -= MENU[choice]["ingredients"].get(items, 0)
    # print the choice of coffee
    print(f"Here is your {choice} ☕. Enjoy!")


# TODO: 1. Print report of all coffee machine resources
def user_input():
    """Take in a user input and return the input as a string"""
    is_true = True
    # Check for user input
    while is_true:
        choices = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # Check IF user input is off, report, or a menu item
        if choices == "off":
            return False
        elif choices == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        else:
            # Check if user input is in the menu
            if choices in MENU:
                # Check if there are enough resources by using the function defined above
                if check_resources(choices, resources):
                    # process the coins and check the transactions
                    transactions = process_coins()
                    if check_transactions(transactions, choices):
                        make_coffee(resources, choices)
                else:
                    # continue the loop if there are not enough resources
                    continue
            else:
                # print an error message if the user input is not in the menu
                print("Invalid input. Please try again.")
                continue


user_input()
