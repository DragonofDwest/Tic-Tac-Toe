# water_tank = 400
# milk_tank = 540
# coffee_bean_bag = 120
# disposable_cups = 9
# cash = 550
#
#
# def stock():
#     print(f"The coffee machine has: \n{water_tank} of water \n{milk_tank} of milk")
#     print(f"{coffee_bean_bag} of coffee beans \n{disposable_cups} of disposable cups")
#     print(f"{cash} of money")
#
#
# stock()
#
#
# operation = input('\nWrite action (buy, fill, take):\n>')
# if operation == "buy":
#     coffee_maker = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: \n >')
#     if coffee_maker == "1":
#         disposable_cups -= 1
#         water_tank -= 250
#         milk_tank -= 0
#         coffee_bean_bag -= 16
#         cash += 4
#         stock()
#     elif coffee_maker == "2":
#         disposable_cups -= 1
#         water_tank -= 350
#         milk_tank -= 75
#         coffee_bean_bag -= 20
#         cash += 7
#         stock()
#     elif coffee_maker == "3":
#         disposable_cups -= 1
#         water_tank -= 200
#         milk_tank -= 100
#         coffee_bean_bag -= 12
#         cash += 6
#         stock()
#
#
# elif operation == "take":
#     print('i gave you $' + str(cash) + '\n')
#     cash -= cash
#     stock()
# elif operation == "fill":
#     extra_water = int(input('Write how many ml of water do you want to add: \n>'))
#     extra_milk = int(input('Write how many ml of milk do you want to add: \n>'))
#     extra_coffee = int(input('Write how many grams of coffee beans do you want to add: \n>'))
#     extra_cup = int(input('Write how many disposable cups of coffee do you want to add: \n>'))
#
#     water_tank += extra_water
#     milk_tank += extra_milk
#     coffee_bean_bag += extra_coffee
#     disposable_cups += extra_cup
#     print('\n')
#     stock()

class Coffee:
    def __init__(self, water_tank=400, milk_tank=540, coffee_bean_bag=120, disposable_cups=9, cash=550):
        self.water_tank = water_tank
        self.milk_tank = milk_tank
        self.coffee_bean_bag = coffee_bean_bag
        self.disposable_cups = disposable_cups
        self.cash = cash

    def stock(self):
        print(f"The coffee machine has: \n{self.water_tank} of water \n{self.milk_tank} of milk")
        print(f"{self.coffee_bean_bag} of coffee beans \n{self.disposable_cups} of disposable cups")
        print(f"{self.cash} of money")

    def operate(self):
        while True:
            operation = input('\nWrite action (buy, fill, take, remaining, exit):\n>')
            if operation == "buy":
                coffee_maker = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: \n >')
                if coffee_maker == "1":
                    if self.water_tank < 250:
                        print("Sorry, not enough water!")
                    elif self.coffee_bean_bag < 16:
                        print("Sorry, not enough coffee beans!")
                    elif self.disposable_cups < 1:
                        print("Sorry, not enough disposable cups!")
                    else:
                        print("I have enough resources, making you a coffee!")
                        self.disposable_cups -= 1
                        self.water_tank -= 250
                        self.milk_tank -= 0
                        self.coffee_bean_bag -= 16
                        self.cash += 4

                elif coffee_maker == "2":
                    if self.water_tank < 350:
                        print("Sorry, not enough water!")
                    elif self.milk_tank < 75:
                        print("Sorry, not enough milk!")
                    elif self.coffee_bean_bag < 20:
                        print("Sorry, not enough coffee beans!")
                    elif self.disposable_cups < 1:
                        print("Sorry, disposable cups")
                    else:
                        print("I have enough resources, making you a coffee!")
                        self.disposable_cups -= 1
                        self.water_tank -= 350
                        self.milk_tank -= 75
                        self.coffee_bean_bag -= 20
                        self.cash += 7

                elif coffee_maker == "3":
                    if self.water_tank < 200:
                        print("Sorry, not enough water!")
                    elif self.milk_tank < 100:
                        print("Sorry, not enough milk!")
                    elif self.coffee_bean_bag < 12:
                        print("Sorry, not enough coffee beans!")
                    elif self.disposable_cups < 1:
                        print("Sorry, disposable cups")
                    else:
                        print("I have enough resources, making you a coffee!")
                        self.disposable_cups -= 1
                        self.water_tank -= 200
                        self.milk_tank -= 100
                        self.coffee_bean_bag -= 12
                        self.cash += 6

            elif operation == "take":
                print('i gave you $' + str(self.cash) + '\n')
                self.cash -= self.cash

            elif operation == "fill":
                extra_water = int(input('Write how many ml of water do you want to add: \n>'))
                extra_milk = int(input('Write how many ml of milk do you want to add: \n>'))
                extra_coffee = int(input('Write how many grams of coffee beans do you want to add: \n>'))
                extra_cup = int(input('Write how many disposable cups of coffee do you want to add: \n>'))

                self.water_tank += extra_water
                self.milk_tank += extra_milk
                self.coffee_bean_bag += extra_coffee
                self.disposable_cups += extra_cup
                print('\n')

            elif operation == "remaining":
                self.stock()

            elif operation == "exit":
                break


coffee_machine = Coffee()
coffee_machine.operate()
