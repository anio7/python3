# Prints to console using print()
print("Welcome to the Band Name Generator")

# takes an input and assigns a variable to it for later use.
city = input("what is the name of the city you grew up in:\n")
petName = input("What is the name of your first pet:\n")

# When you press enter your band name will be generated.
# this uses string concatenation
print("Your band name is " +city +" " +petName)

#this uses f-strings or formatted string.It is neater this way to write code.
print(f"Your band name is {city}_{petName}")