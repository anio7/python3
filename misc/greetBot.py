"""Write a program to greet someone by name

1.Ask for the user name
2.Generate a personalized greeting
"""

print("Welcome to chatbot")

def greetBot(Name = input("what is your name: ")):
    print(f"Nice to meet you {Name.title() }.\ni'm so glad to have met you!\nWelcome!")

#invoke the function to get the greeting
greetBot()