from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffeeMaker = CoffeeMaker()
user_choice = ""
moneyMachine = MoneyMachine()
menu = Menu()


while not user_choice == "off":
    user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if user_choice == "off":
        print("Shutting Down Coffee Maker")
    elif user_choice == "report":
        coffeeMaker.report()
    elif menu.find_drink(user_choice) is not None:
        menuItem = menu.find_drink(user_choice)
        if coffeeMaker.is_resource_sufficient(menuItem):
            if moneyMachine.make_payment(menuItem.cost):
                coffeeMaker.make_coffee(menuItem)
