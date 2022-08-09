from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffeeMaker = CoffeeMaker()
user_choice = ""
moneyMachine = MoneyMachine()
menu = Menu()


while not user_choice == "off":
    user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    menuItem = menu.find_drink(user_choice)
    if user_choice == "report":
        coffeeMaker.report()
    elif menuItem is not None:
        if coffeeMaker.is_resource_sufficient(menuItem):
            if moneyMachine.make_payment(menuItem.cost):
                coffeeMaker.make_coffee(menuItem)
            
