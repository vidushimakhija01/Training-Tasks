coffee_machine = {
    "water":100,
    "milk":100,
    "coffee_powder":50
}
menu = [
    {"name": "Cappuccino", "water": 10, "milk": 10, "coffee_powder": 3, "price": 70},
    {"name": "Mocha", "water": 15, "milk": 7, "coffee_powder": 7, "price": 80},
    {"name": "Latte", "water": 5, "milk": 15, "coffee_powder": 10, "price": 30}
]
def check(drink):
    for i in ["water","milk","coffee_powder"]:
        if coffee_machine[i] < drink[i]:
            return False
    return True
    

ans = input("Would you like some coffee ?")
while (ans.lower() == "yes"):
    choice = int(input("select one : 1.Cappucino, 2.Mocha, 3.Latte"))
    match choice:
        case 1:
            result = check(menu[0])
            drink = menu[0]
        case 2:
            result = check(menu[1])
            drink = menu[1]
        case 3:
            result = check(menu[2])
            drink = menu[2]
    if(result):
        coffee_machine["water"] -= drink["water"]
        coffee_machine["milk"] -= drink["milk"]
        coffee_machine["coffee_powder"] -= drink["coffee_powder"]
        print('here is your coffee please pay Rs',drink["price"])
    ans = input("Would you like some coffee ?")