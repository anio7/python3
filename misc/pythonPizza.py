"""Write a Pizza Delivery program"""
#todo: work out how much they need to pay based on their size choice.
#todo:work out how much to add to their bill based on their pepperoni choice.
#todo:work out their final amount based on whether if they want extra cheese.
print("Welcome to a python Pizza Deliveries")

#Create variables for code.
pizzaCost = 0
pizzaSize    = input("What size of pizza do you want: s/m,l/xl ")
print("""
      Small   - £10
      Medium  - £12
      Large   - £15
      X-Large - £17
      Toppings- £3
      """)
toppings = input("Would you like any toppings? y/n")

#tell the user how much they have to pay because of the size of the pizza
match pizzaSize:
    case "s":
        pizzaCost +=10
    case "m":
        pizzaCost +=12
    case "l":
        pizzaCost +=15
    case "xl":
        pizzaCost +=17
if toppings == "y":
        topBoth = input("would you like both toppings? y/n ")
        if topBoth == "y":
            pizzaCost += 6
        else:
            topping_ = input("choose your toppings: Pepperoni or ExtraCheese").lower()
            if topping_ == "pepperoni" or "extracheese":
                pizzaCost +=3
if toppings == "y":
    print(f"The pizza size you choose is {pizzaSize}, with toppings therefore the cost is £{pizzaCost}")
else:
    print(f"The pizza size you choose is {pizzaSize}, the cost is £{pizzaCost}")
