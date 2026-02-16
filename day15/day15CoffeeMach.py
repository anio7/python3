import time


#create variables for program.

#price of the drinks
drink_price = {"espresso":4, "latte":3, "cappuccino": 5}

#drink information
e_drink = {"Water": 100, "Milk": 80, "Coffee":40}
l_drink = {"Water": 200, "Milk": 60, "Coffee":30}
c_drink = {"Water": 150, "Milk": 70, "Coffee":50}

#print a report of the machine supply status
report = {"Water": 1000,"Milk": 500, "Coffee": 200, "Money": 0}
    
#write code that displays the resources depleting in the machine.
def machine_report(user_prompt):    
    if user_prompt == "espresso":
        report["Water"] = report["Water"] - e_drink["Water"]
        report["Milk"] = report["Milk"] - e_drink["Milk"]
        report["Coffee"] = report["Coffee"] - e_drink["Coffee"]
        report["Money"] = report["Money"] + drink_price[user_prompt]
    elif user_prompt == "latte":
        report["Water"] = report["Water"] - l_drink["Water"]
        report["Milk"] = report["Milk"] - l_drink["Milk"]
        report["Coffee"] = report["Coffee"] - l_drink["Coffee"]
        report["Money"] = report["Money"] + drink_price[user_prompt]
    else:
        report["Water"] = report["Water"] - c_drink["Water"]
        report["Milk"] = report["Milk"] - c_drink["Milk"]
        report["Coffee"] = report["Coffee"] - c_drink["Coffee"]
        report["Money"] = report["Money"] + drink_price[user_prompt]

    another_drink = input("Would you like another drink: ")
    if another_drink == "yes":
        another_drink = input("Please choose another drink: ")
    else:
        print_report = input("Would you like a display a report: ")
        if print_report == "yes":
            print(report)
def paymentMethods():
    print("Please choose payment method: ")
    print("How would you like to pay: ")
    quarters = int(input("how many quarters: "))
    dimes    = int(input("How many dimes: "))
    nickles  = int(input("How many nickles: "))
    pennies  = int(input("how much pennies: "))
    
    quarters = quarters * 0.25
    dimes    = dimes * 0.10
    nickles  = nickles * 0.05
    pennies  = (quarters + dimes + nickles) * 0.01 
    total = quarters + dimes +  nickles + pennies
    print(f"your total is : £{total} for {user_prompt}")
#prompt the user by asking "what would you like?" and display price from the data records

machine_report(user_prompt)
resources = True
while resources:
    user_prompt = input("What would you like to drink? espresso/latte/cappuccino: ")
    print(f"since you chose {user_prompt}, the price is £{drink_price[user_prompt]}")
    paymentMethods()
    another_drink = input("Would you like another drink: ")
    if another_drink == "yes":
        
        paymentOptions = ["quarters","dimes","nickles","pennies"]
        if paymentType in paymentOptions:
            print(f"your total bill is £{total} for {user_prompt}")    

#turn the coffee machine by entering off
keep_on = True
while keep_on:
    turn_off =input("Would you like to keep the machine running or power down:off ")
    if turn_off == "off":
        keep_on = False
        print("Powering off.")
        for i in range(0,3):
            time.sleep(3)
            print(".")
        print("GOODBYE!")
    






