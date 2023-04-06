from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    request = input(f'What would you like? ({options}):')
    if request == 'off':
        is_on = False
    elif request == 'report':
        money.report()
        coffee.report()
    else:
        drink = menu.find_drink(request) #drink is a menu item
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)