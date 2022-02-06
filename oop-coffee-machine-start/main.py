from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
_menu = Menu()
order = "on"

while order != 'off':
    menu = _menu.get_items()
    order = input(f"What would you like? {menu}:")
    if order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order == 'off':
        order = 'off'
    else:
        choice = _menu.find_drink(order_name=order)
        if coffee_maker.is_resource_sufficient(choice) and money_machine.make_payment(choice.cost):
            coffee_maker.make_coffee(choice)
