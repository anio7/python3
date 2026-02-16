#import time for sleep function
import time
#create variables for program.

#Menu information since its a constant
MENU = {"espresso":{"ingredients":{"Water": 100, "Milk": 80, "Coffee":40},"cost": 2.5},
        "latte"   :{"ingredients":{"Water": 200, "Milk": 60, "Coffee":30},"cost": 4.5},
      "cappuccino":{"ingredients":{"Water": 150, "Milk": 70, "Coffee":50},"cost": 3.5}}

#print a report of the machine supply status
resource = {"Water": 1000,"Milk": 500, "Coffee": 200, "Money": 0}
profit = 0

#create relevant functions for the program using variables stated
"""function describing the switching off of the machine"""
def off():
    print("Switching off.")
    for _ in range(0,3):  #'_' as a placeholder for i
        time.sleep(3)
        print(".")
    print("GOODBYE!")         
    
"""function describing if money is sufficient"""
def is_resource_sufficient(drink_ingredients):
    for value in drink_ingredients:
        if drink_ingredients[value] >= resource[value]:
            print(f"sorry there is not enough {value}:{drink_ingredients[value]}.")
            return False    
    return True
"""function displaying report information"""
def report():
    print("This is a report of the remaining resources in this machine")
    print("the resources remaining are.."
          f"{resource["Water"]}ml of water\n"
          f"{resource["Milk"]}g of Milk and "
          f"{resource["Coffee"]}g of Coffee\n"
          f"£{profit} of money.")   
         
"""function describing payment method"""      
def process_coins(): 
    total = 0       
    #prompt user for payment using loop system
    for _ in range(0,1):
        print(f"your total is £{total}")
        quarters = int(input("how many quarters: "))
        print(f"amount of quarters inserted = {quarters}\n"
              f"therefore: {quarters} * 0.25 = {quarters * 0.25}")
        total += quarters * 0.25
        
        print(f"your total is £{total}")
        dimes    = int(input("How many dimes: "))
        print(f"amount of quarters inserted = {dimes}\n"
              f"therefore: {dimes} * 0.10 = {dimes * 0.25}")
        total += dimes * 0.10
        
        print(f"your total is £{total}")
        nickles  = int(input("How many nickles: "))
        print(f"amount of nickles inserted = {nickles}\n"
              f"therefore: {nickles} * 0.05 = {nickles * 0.25}")
        total += nickles* 0.05
        
        print(f"your total is £{total}")
        pennies  = int(input("how much pennies: "))
        print(f"amount of quarters inserted = {pennies}\n"
              f"therefore: {pennies} * 0.25 = {pennies * 0.25}")
        total += pennies* 0.01
    
    
    #this is one way to calculate total
    # print("Please choose payment method: ")
    # print("How would you like to pay: ")
    # quarters = int(input("how many quarters: "))* 0.25
    # dimes    = int(input("How many dimes: "))* 0.10
    # nickles  = int(input("How many nickles: "))* 0.05
    # pennies  = int(input("how much pennies: "))* 0.01 
    
    #this is another way to calculate total
    # total = round(quarters + dimes +  nickles + pennies,2)
    # print(f"your total is : £{total}")
    # total = int(input("how many quarters: "))* 0.25
    # total += int(input("How many dimes: "))* 0.10
    # total += int(input("How many nickles: "))* 0.05
    # total += int(input("how much pennies: "))* 0.01
    return total

"""function describing if transaction is successful"""    
def is_transaction_successful (money_received, drink_price):
    """ Return true when the payment is accepted or False if money insufficient"""   
    if money_received >= drink_price:
        change = round(money_received - drink_price,2)
        print(f"the drink cost {drink_price} and here is your {change}")
        global profit
        profit += drink_price
        return True
    else:
        print("Sorry that's not enough money")
        return False
    
"""function describing make coffee and minus resources""" 
def make_coffee(drink_name, drink_ingredients):
    for value in drink_ingredients:
        resource[value] -= drink_ingredients[value]
    print(f"Here is your {drink_name}☕️")   

#create the a coffee machine program
print("Welcome!")
is_on = True
# while is_on:
    choice = input("What you like to do? (power off/report/pour drink)").lower()
    
    #if the user chooses 'off' it powers off with a sleep timer of 3 sec
    if choice == "off":
        is_on = False 
        off()
          
    #if the user chooses report it reports the resources available.
    elif choice == "report":
        report()
    
    #if the user chooses pour it asks which drink they would like
    else:
        #prompt the user and display user choice, ingredients and drink price
        prompt = input("What would you like to drink? (espresso/latte/cappuccino)")
        drink_ingredients = MENU[prompt]["ingredients"]
        drink_price = MENU[prompt]["cost"]
        print(f"since you chose {prompt} the price is £{drink_price}")
        
         #  #check if resources are sufficient then require payment
        if is_resource_sufficient(drink_ingredients) == True:
            
            payment = process_coins()
            if is_transaction_successful(payment,drink_price):
                make_coffee(prompt,drink_ingredients)
        
        
    
