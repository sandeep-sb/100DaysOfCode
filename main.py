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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


# TODO: 1.Print report of all the coffee machine resources
def resource_report():
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"money: ${money}")


# TODO: 2.Check if the current rersources are sufficient
def resource_check(water, milk, coffee, coffee_resource_required):
    if user_choice == "espresso":
        if water < coffee_resource_required['water']:
            print("Sorry there is not enough water.")
        elif coffee < coffee_resource_required['coffee']:
            print("Sorry there is not enough coffee.")
        else:
            return True
    else:
        if water < coffee_resource_required['water']:
            print("Sorry there is not enough water.")
        elif coffee < coffee_resource_required['coffee']:
            print("Sorry there is not enough coffee.")
        elif milk < coffee_resource_required['milk']:
            print("Sorry there is not enough milk.")
        else:
            return True
    return False


# TODO: 3.Process how many coins user has input and are they sufficient to buy that particular coffee
def process_coins():
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickels?: "))
    penny = int(input("How many penny?: "))
    money_collected = round((quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01), 2)
    check_transaction(money_collected)


# TODO: 4.Check transaction successful
def check_transaction(money_collected):
    if money_collected < MENU[user_choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        global money
        money = MENU[user_choice]["cost"]
        money_collected -= MENU[user_choice]["cost"]
        print(f"Here is ${money_collected} in change.")
        print(f"Here is your {user_choice} ☕ Enjoy!\n")


# TODO: 5.Make coffee
def make_coffee(choice):
    water = resources["water"]
    coffee = resources["coffee"]
    milk = resources["milk"]

    modify_resources = resource_check(water, milk, coffee, MENU[choice]["ingredients"])
    if modify_resources is True:
        resources["water"] -= MENU[choice]["ingredients"]['water']
        resources["coffee"] -= MENU[choice]["ingredients"]['coffee']
        if choice != "espresso":
            resources["milk"] -= MENU[choice]["ingredients"]['milk']

        process_coins()


while resources["water"] != 0:
    user_choice = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    if user_choice == "report":
        resource_report()
    elif user_choice == "off":
        print("The coffee machine is turning off for maintenance")
        exit()
    else:
        make_coffee(user_choice)
