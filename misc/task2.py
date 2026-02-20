"""
Write a Nested conditional statement to check the height and age of a person taking a 
rollercoaster ride and ask them if they would like a photo. Give them the total.
"""

print("Welcome to a rollercoaster ride!")

#create your variables for the conditional statement
age = int(input("What is your age:"))
height = int(input("What is your height in cm: "))
bill = 0

#ask about their height
if height >= 120:
    print("You can ride the rollercoaster")
    if age <= 12:
        bill = 5
        print("Child tickets are £5")
    elif age <= 18:
        bill = 7
        print("Teenager are £7")
    else:
        bill = 10
        print("Adults pay £10")
    
    #ask if they would like a photo
    withPhoto = input("Would you like your photo taken? y/n: ")
    if withPhoto == "y":
        bill +=3
    
    #print total bill    
    print(f"Your total is £{bill}")
else:
    print("I'm sorry but you cannot ride this rollercoaster!")