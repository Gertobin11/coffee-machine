
MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24
        },
        'cost': 2.5
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24
        },
        'cost': 3.0
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}

def check_ingredients(item):
    """ Check if there is enough ingrediants in resources """
    ingredients = MENU[item]['ingredients'].items()
    for ingredient, price in ingredients:
        print(ingredient)
        if ingredient in resources.keys():
            if resources[ingredient] < price:
                print('Not enough Ingrediants, Please select a different drink')
                choose_drink()



def print_resources(items):
    """ List the available resources """
    for itm in items.items():
        print(f'{itm[0]} - {itm[1]}')

def recalculate_resources(item):
    """ Recalculate the resources after the purchase """
    ingredients = MENU[item]['ingredients'].items()
    for ingredient in ingredients:
        if ingredient[0] in resources.keys():
            math = resources[ingredient[0]] - ingredient[1]
            resources[ingredient[0]] = math


def choose_drink():
    while True:
        choice = input('Please select a drink (Espresso/Cappucino/Latte): ')
        if choice.lower() == 'Espresso'.lower():
            check_ingredients(choice)
            pay_for_drink('espresso')
        elif choice.lower() == 'Latte'.lower():
            check_ingredients(choice)
            pay_for_drink('latte')
        elif choice.lower() == 'Cappuccino'.lower():
            check_ingredients(choice)
            pay_for_drink('cappuccino')
        elif choice.lower() == 'Report'.lower():
            print_resources(resources)
        else:
            print('Please enter a valid response')
    
    

def pay_for_drink(drink):
    entered_money = 0
    drink_cost = MENU[drink]["cost"]
    print(f'Please enter ${drink_cost}')
    while True:
        try:
            pennys = int(input("How many pennys will you put in: ")) * .01
            nickel = int(input("How many nickels will you put in: ")) * .05
            dime = int(input("How many dimes will you put in: ")) * .1
            quarter = int(input("How many quarters will you put in: ")) * .25
            break
        except ValueError:
            print('Please enter a number only')
    entered_money = sum([pennys, nickel, dime, quarter])
    while entered_money < drink_cost:
        print('Not enough coins, Please enter more')
        try:
            pennys = int(input("How many pennys will you put in: ")) * .01
            nickel = int(input("How many nickels will you put in: ")) * .05
            dime = int(input("How many dimes will you put in: ")) * .1
            quarter = int(input("How many quarters will you put in: ")) * .25
            break
        except ValueError:
            print('Please enter a number only')
        entered_money += sum([pennys, nickel, dime, quarter])
    change = entered_money - drink_cost
    resources['money'] += drink_cost
    if change > 0:
        print(f"Please take your ${round(change, 2)} change")
    print(f'Please enjoy your warm {drink} \u2615')
    recalculate_resources(drink)


choose_drink()