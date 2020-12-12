class InsufficientIngredients(Exception):
    pass

class CoffeeMachine:
    coffees = {
        'espresso': {
            'water': 250,
            'milk': 0,
            'beans': 16,
            'cost': 4
        },
        'latte': {
            'water': 350,
            'milk': 75,
            'beans': 20,
            'cost': 7
        },
        'cappuccino': {
            'water': 200,
            'milk': 100,
            'beans': 12,
            'cost': 6
        },
    }
    def __init__(self, water:int = 0, milk:int = 0, beans:int = 0, cups:int = 0, money:int = 0):
        self.water:int = water
        self.milk:int = milk
        self.beans:int = beans
        self.cups:int = cups
        self.money:int = money

    def show_state(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def buy(self, coffee: str):
        amount = self.coffees[coffee]
        if self.cups >= 1 and self.water >= amount['water'] and self.beans >= amount['beans'] and self.milk >= amount['milk']:
            self.cups -= 1
            self.money += amount['cost']
            self.beans -= amount['beans']
            self.water -= amount['water']
            self.milk -= amount['milk']
            print('I have enough resources, making you a coffee!')
        else:
            sorry_message = "Sorry, not enough "
            missing_ingredients = []
            if self.water < amount['water']:
                missing_ingredients.append('water')
            if self.beans < amount['beans']:
                missing_ingredients.append('beans')
            if self.milk < amount['milk']:
                missing_ingredients.append('milk')
            if self.cups < 1:
                missing_ingredients.append('cups')
            sorry_message += ", ".join(missing_ingredients) + '!'
            print(sorry_message)


    def fill(self, water, milk, beans, cups):
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups

    def take(self):
        print(f"\nI gave you ${self.money}")
        self.money = 0

# Initial Conditions
water:int = 400
milk:int = 540
beans:int = 120
cups:int = 9
money:int = 550
coffeemachine = CoffeeMachine(water, milk, beans, cups, money)
while True:
    try:
        command = input("Write action (buy, fill, take, remaining, exit):")
        if command == 'remaining':
            coffeemachine.show_state()
        elif command == 'buy':
            choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            if choice == 'back':
                continue
            else:
                choice = int(choice)
            coffeemachine.buy(['espresso', 'latte', 'cappuccino'][choice-1])
        elif command == 'fill':
            # Amount of water
            water = int(input("Write how many ml of water do you want to add:"))
            # Amount of milk
            milk = int(input("Write how many ml of milk do you want to add:"))
            # Amount of coffee beans
            beans = int(input("Write how many grams of coffee beans do you want to add:"))
            # Amount of cups
            cups = int(input("Write how many disposable cups of coffee do you want to add:"))
            coffeemachine.fill(water, milk, beans, cups)
        elif command == 'take':
            coffeemachine.take()
        elif command == 'exit':
            break
    except ValueError:
        print('Enter a Number')
