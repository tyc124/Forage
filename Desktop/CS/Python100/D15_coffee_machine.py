#Python 100 - 15
#Coffee machine project

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

report = {
    "water": 200,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def check_resources(order):
    resources = MENU[order]['ingredients']
    check = False

    if report['water'] >= resources['water']:
        if report['coffee'] >= resources['coffee']:
            if 'milk' in resources.keys():
                if report['milk'] >= resources['milk']:
                    check = True
                    return check
                else:
                    print('Sorry there is not enough milk.')
            else:
                 check = True
                 return check
        else:
            print('Sorry there is not enough coffee.')
    else:
        print('Sorry there is not enough water.')
            

def process_coins():
    quarters = input('Please insert quarters: ')
    dimes = input('Please insert dimes: ')
    nickles = input('Please insert nickles: ')
    pennies = input('Please insert pennies: ')

    return int(quarters) * 0.25 + int(dimes) * 0.10 + int(nickles) * 0.05 + int(pennies) * 0.01
    

def coffee_machine(request):
    if request == 'report':
        print(report)
    elif request in MENU.keys():
        if check_resources(request) == True:
            total = process_coins()
            if total >= MENU[request]['cost']:
                report['money'] += MENU[request]['cost']
                report['water'] -= MENU[request]['ingredients']['water']
                report['coffee'] -= MENU[request]['ingredients']['coffee']
                if 'milk' in MENU[request]['ingredients'].keys():
                    report['milk'] -= MENU[request]['ingredients']['milk']
                print(r'Here is your %s. Enjoy!' % request)
                total -= MENU[request]['cost']
                if total > 0:
                    print('Here is your %f dollars in exchange.' % total)
            else:
                print('Not enough money.')
    else:
        print('We are not offering this coffee. Sorry.')


request = input('What would you like? (espresso/latte/cappuccino): ')

while request != 'off':
    coffee_machine(request)
    request = input('What would you like? (espresso/latte/cappucino): ')