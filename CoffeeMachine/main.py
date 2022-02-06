from CoffeeMachine import menu


def insert_coins():
    print("Insert coins.")
    quarters = int(input("How many quarters? "))
    quarters = 0.25 * quarters
    dimes = int(input("How many dimes? "))
    dimes = 0.10 * dimes
    nickels = int(input("How many nickels? "))
    nickels = 0.05 * nickels
    pennies = int(input("How many pennies? "))
    pennies = 0.01 * pennies
    return quarters + nickels + dimes + pennies


def espresso():
    if menu.resources['water'] < 100:
        print("Sorry there is not enough water.")
    elif menu.resources['coffee'] < 18:
        print("Sorry there is not enough coffee.")
    else:
        inserted = insert_coins()
        if inserted < menu.MENU['espresso']['cost']:
            print("Sorry that's not enough money. Money refunded.")
            return
        menu.resources['water'] -= 100
        menu.resources['coffee'] -= 18
        menu.money += 1.5
        if inserted > menu.MENU['espresso']['cost']:
            change = round(inserted - menu.MENU['espresso']['cost'],2)
            print(f"Here is ${change} dollars in change.")
        print("Here is your Espresso. Enjoy!")


def latte():
    if menu.resources['water'] < 200:
        print("Sorry there is not enough water.")
    elif menu.resources['coffee'] < 24:
        print("Sorry there is not enough coffee.")
    elif menu.resources['milk'] < 150:
        print("Sorry there is not enough milk.")
    else:
        inserted = insert_coins()
        if inserted < menu.MENU['latte']['cost']:
            print("Sorry that's not enough money. Money refunded.")
            return
        menu.resources['water'] -= 200
        menu.resources['coffee'] -= 24
        menu.resources['milk'] -= 150
        menu.money += 2.5
        if inserted > menu.MENU['latte']['cost']:
            change = round(inserted - menu.MENU['latte']['cost'],2)
            print(f"Here is ${change} dollars in change.")
        print("Here is your latte. Enjoy!")


def cappuccino():
    if menu.resources['water'] < 250:
        print("Sorry there is not enough water.")
    elif menu.resources['coffee'] < 24:
        print("Sorry there is not enough coffee.")
    elif menu.resources['milk'] < 100:
        print("Sorry there is not enough milk.")
    else:
        inserted = insert_coins()
        if inserted < menu.MENU['cappuccino']['cost']:
            print("Sorry that's not enough money. Money refunded.")
            return
        menu.resources['water'] -= 250
        menu.resources['coffee'] -= 24
        menu.resources['milk'] -= 100
        menu.money += 3.0
        if inserted > menu.MENU['cappuccino']['cost']:
            change = round(inserted - menu.MENU['cappuccino']['cost'],2)
            print(f"Here is ${change} dollars in change.")
        print("Here is your cappuccino. Enjoy!")


def report():
    info = menu.resources
    print(f" Water: {info['water']}ml\n Milk: {info['milk']}ml \n Coffee: {info['coffee']}g \n Money: ${menu.money} ")


order = "on"

while order != 'off':
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == 'report':
        report()
    if order == 'espresso':
        espresso()
    if order == 'latte':
        latte()
    if order == 'cappuccino':
        cappuccino()
