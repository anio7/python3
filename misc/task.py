#Write a program that asks the user for input and checks if its an even number

#ask user for input
numToCheck = int(input("Please enter a num: "))

#check if number is even using conditional statements
if numToCheck % 2 == 0:
    print(f"The number you've entered is {numToCheck} and it is even")
else:
    print(f"The number you've entered is {numToCheck} and it is odd")