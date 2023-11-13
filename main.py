global MENU, resources, coins
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}
def take_order():
    status = "on"
    while status == "on":
        order = input("What would you like? (espresso/latte/cappuccino): \n")
        if order == "espresso" or order == "latte" or order == "cappuccino":
            check_resources(order)
            take_order()
        elif order == "report":
            report()
            take_order()
        else:
            status = "off"



def report():
    print(resources)

def check_resources(order):
    for i in resources:
        resource = "sufficient"
        if resources[i] < MENU[order]["ingredients"][i]:
            print(f"Sorry, there is not enough {i}!")
            resource = "insufficient"

    if resource == "sufficient":
        payment(order)

def payment(order):
    print(f"Please insert ${MENU[order]['cost']}")
    pennies = int(input("How many pennies?\n"))
    nickels = int(input("How many nickels?\n"))
    dimes = int(input("How many dimes?\n"))
    quarters = int(input("How many quarters?\n"))
    payment_made = (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)
    if payment_made > MENU[order]["cost"]:
        change = payment_made - MENU[order]["cost"]
        change = round(change, 2)
        print(f"Here is ${change} in change\n")
        make_coffee(order)

    elif payment_made < MENU[order]["cost"]:
        print("Sorry that's not enough money. Money refunded")

    else:
        make_coffee(order)

def make_coffee(order):
    for i in resources:
        resources[i] = resources[i] - MENU[order]["ingredients"][i]

    print(f"Here is your {order}. Enjoy!")


take_order()