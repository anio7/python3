    """ This is a program for a coffee machine using Object Oriented Programming - classes
    """



from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#create objects for your classes

menu          = Menu()
coffee_maker  = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
#bind the object.method of the coffeeMaker to a variable to print details by calling method
#or print it right away.

while is_on:
    options = menu.get_items()
    print(options)
    prompt = input(f"what would you like? {options}")
    if prompt == "off":
        is_on = False
        print("Switching off.")
        for _ in range(0,3):  #'_' as a placeholder for i
            time.sleep(3)
        print(".")
        print("GOODBYE!") 
    elif prompt == "report":
        #print report for coffee maker
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(prompt)
        if coffee_make.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            