coffee_machine = {
    "water": 100,
    "milk": 100,
    "coffee_powder": 50
}

menu = [
    {"name": "Cappuccino", "water": 10, "milk": 10, "coffee_powder": 3, "price": 70},
    {"name": "Mocha", "water": 15, "milk": 7, "coffee_powder": 7, "price": 80},
    {"name": "Latte", "water": 5, "milk": 15, "coffee_powder": 10, "price": 30}
]

def check(drink):
    for i in ["water", "milk", "coffee_powder"]:
        if coffee_machine[i] < drink[i]:
            return False
    return True

ans = input("Would you like some coffee?")
while ans.lower() == "yes":
    try:
        choice = int(input("Select one: 1. Cappuccino, 2. Mocha, 3. Latte: "))
        if choice not in [1, 2, 3]:
            raise ValueError("Invalid choice")

        drink = menu[choice - 1]
        if not check(drink):
            print("Sorry, not enough ingredients for", drink["name"])
            continue
            
    except ValueError as ve:
        print("Error:", ve)
    
    except Exception as e:
        print("Something went wrong:", e)
    
    else:
        coffee_machine["water"] -= drink["water"]
        coffee_machine["milk"] -= drink["milk"]
        coffee_machine["coffee_powder"] -= drink["coffee_powder"]
        print(f"Here is your {drink['name']}! Please pay Rs {drink['price']}.")

    finally:
        ans = input("Would you like some more coffee?")