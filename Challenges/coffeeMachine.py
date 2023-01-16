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


def process_coins():
    total = 0
    total += int(input("Enter the number of quaters")) * 0.25
    total += int(input("Enter the number of dimes")) * 0.1
    total += int(input("Enter the number of nickles")) * 0.05
    total += int(input("Enter the number of pennies")) * 0.01
    return total


def coffee_Preparation():
    is_on = True
    money = 0
    change = 0
    while is_on:
        item = input("Type of drink (espresso, latte or cappuccino")
        if item == "espresso" or item == "latte" or item == "cappuccino":
            for i in MENU[item]['ingredients']:
                if resources[i] < MENU[item]['ingredients'][i]:
                    print(f"{i} is less")
                    break
                else:
                    money = process_coins()
                    if money < MENU[item]['cost']:
                        print("Less Money.! Try something else")
                        break
                    else:
                        print(f"{item} is being prepared")
                        change = money - MENU[item]['cost']
                        for j in resources:
                            resources[j] -= MENU[item]['ingredients'][j]
                        print(f"Your change is {change}")
                        break
        elif item == "report":
            for i in resources:
                print(i, resources[i])
        elif item == "off":
            is_on = False


coffee_Preparation()