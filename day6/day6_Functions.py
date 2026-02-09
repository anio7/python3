"""Create a simple greet function that ask the user for input and greets them"""

#to create a function you must first write the def keyword followed by the function name
#most functions with parameters need to have variables to store values as arguments for the the function.
def greet(name):
    print(f"hello {name}")

#ask for user input
name = input("What is your name: ")

#call the function by typing out the name of the function along with any parameters if necessary.
greet(name)
