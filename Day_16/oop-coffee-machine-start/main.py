from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money = MoneyMachine()
coffee = CoffeeMaker()
menu = Menu()
# menu_item = MenuItem()
is_true = True

# money.report()
# coffee.report()

while is_true:
    opt = menu.get_items()
    user = input(f"What would you like? {opt}: ")
    if user == "off":
        is_true = False
    elif user == "report":
        money.report()
        coffee.report()
    else:
        drink = menu.find_drink(user)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)
