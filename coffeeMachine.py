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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    pass

def coffee_Preparation():
    is_on = True
    while is_on:
        item = input("Type of drink (espresso, latte or cappuccino")
        if item == "espresso" or item == "latte" or item == "cappuccino":
            for i in MENU[item]['ingredients']:
                if resources[i] < MENU[item]['ingredients'][i]:
                    print(f"{i} is less")
                    break
                else:
                    print(f"{item} is being prepared")
                    for i in resources:
                        resources[i] -= MENU[item]['ingredients'][i]
                    break
        elif item == "report":
            for i in resources:
                print(i, resources[i])
        elif item == "off":
            is_on = False


coffee_Preparation()