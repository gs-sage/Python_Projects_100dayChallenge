# process coins
# check if user has enough money
# return change if user has enough money
def user_coffee_change(takes_list, user_input):
    """Takes a list and user input and provides the user coffee and change"""
    print(user_input)
    if user_input in ["espresso", "latte", "cappuccino"]:
        print("Please insert coins")
        total_cost = takes_list[user_input]["cost"]
        quarters = float(input("How many quarters? "))
        dimes = float(input("How many dimes? "))
        nickels = float(input("How many nickels? "))
        pennies = float(input("How many pennies? "))
        total_coins = round((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01), 2)
        print(f"${total_coins}")
        if total_coins >= total_cost:
            print(f"Your change is ${total_coins - total_cost}")
            return True
        else:
            print("Not enough money. Money refunded.")
            return False
    else:
        print("Please enter a valid choice.")
        return False

def coffee_report(resource_list, menu_list, user_input):
    """Takes two list and user input and then subtracts the resource amount and returns the final dictionary"""
    print(resource_list)
    if user_input in ["latte", "cappuccino"]:
        resource_list["water"] = resource_list["water"] - menu_list[user_input]["ingredients"]["water"]
        resource_list["milk"] = resource_list["milk"] - menu_list[user_input]["ingredients"]["milk"]
        resource_list["coffee"] = resource_list["coffee"] - menu_list[user_input]["ingredients"]["coffee"]
        # print(f"Current resources available : {resource_list}")

    elif user_input == "espresso":
        resource_list["water"] = resource_list["water"] - menu_list[user_input]["ingredients"]["water"]
        resource_list["coffee"] = resource_list["coffee"] - menu_list[user_input]["ingredients"]["coffee"]
        # print(f"Current resources available : {resource_list}")

    return resource_list

# check resources
def enough_resource(resource_dict, menu_resource, user_input):
    """Checks if the machine has enough resources for the selected drink."""
    if user_input in ["espresso", "latte", "cappuccino"]:
        for key in menu_resource[user_input]["ingredients"]:
            if resource_dict.get(key, 0) < menu_resource[user_input]["ingredients"][key]:
                print(f"Sorry, there is not enough {key}.")
                return False
        # If all ingredients are sufficient
        return True
    else:
        print("Invalid drink selection.")
        return False


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

while True:
    # ask for input from user
    user_coffee = input("What would you like? (espresso/latte/cappuccino) : ").lower()

    if user_coffee in MENU:
        if enough_resource(resources, MENU, user_coffee):
            if user_coffee_change(MENU, user_coffee):
                resources = coffee_report(resources, MENU, user_coffee)
                money += MENU[user_coffee]["cost"]
                print(f"Here is your {user_coffee}. Enjoy :)")

    # turn off the coffee machine
    if user_coffee == "off":
        print("Coffee machine is shutting down. Have a great day!")
        break

    # print report from input
    elif user_coffee == "report":
        for resource, amount in resources.items():
            print(f"{resource.capitalize()} : {amount}")
        print(f"Money : {money}")
