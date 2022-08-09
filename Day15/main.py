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
    "money": 0
}

coins = {
    "quarter" : 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01
}


# 1. Print Report 
# 2. Check sufficient Resources
# 3. Accept coins & check transaction successful
# 4. Make coffee
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def check_sufficient_resources(user_choice):
    if user_choice == "espresso":
        if resources['water'] > MENU[user_choice]['ingredients']['water']:
            if resources['coffee'] > MENU[user_choice]['ingredients']['coffee']:
                return True
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("Sorry there is not enough water")
            return False
    elif user_choice == "latte" or user_choice == "cappuccino":
        if resources['water'] > MENU[user_choice]['ingredients']['water']:
            if resources['coffee'] > MENU[user_choice]['ingredients']['coffee']:
                if resources['milk'] > MENU[user_choice]['ingredients']['milk']:
                    return True
                else:
                    print("Sorry there is not enough milk.")
                    return False
            else:
                print("Sorry there is not enough coffee.")
                return False       
        else:
            print("Sorry there is not enough water.")
            return False

def accept_money(user_choice):
    print("Please insert coins.")
    quarters = float(input("How many quarters: "))
    dimes = float(input("How many dimes: "))
    nickels = float(input("How many nickels: "))
    pennies = float(input("How many pennies: "))

    complete_amount = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    print(complete_amount)
    if complete_amount > MENU[user_choice]['cost']:
        remaining_amount = round(complete_amount - MENU[user_choice]['cost'],2)
        print(f"Here is your ${remaining_amount} in change")
        print(f"Here is your {user_choice}. Enjoy!")
        resources["coffee"] -= MENU[user_choice]['ingredients']['coffee']
        resources["water"] -= MENU[user_choice]['ingredients']['water']
        resources["money"] += MENU[user_choice]['cost']
        if user_choice in ["latte", "cappuccino"]:
            resources["milk"] -= MENU[user_choice]['ingredients']['milk']
    else:
        print("Sorry that's not enough money. Money refunded")

user_choice = ""

while not user_choice == "off":
    user_choice = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    if user_choice == "report":
        print_report()
    elif user_choice in ["espresso", "latte", "cappuccino"]:
        if check_sufficient_resources(user_choice.lower()):
            accept_money(user_choice)

