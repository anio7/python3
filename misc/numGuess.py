"""Write a program that generates a random number for the user to guess"""
#put some more lines to ask if they want to continue playing.


import random #this import helps to retrieve a random number between 2 numbers or a range of numbers
print("Im thinking of a number! Can you guess what it is:")

comGuess = random.randint(1,100)

#to keep the user guessing we must create a while loop because we need it to be true until it breaks.


while comGuess:
    humanGuess = int(input("What number do you think it is: "))
    if humanGuess == comGuess:
        print("You've guessed correctly!")
        break
    elif humanGuess > comGuess:
        print("You've guessed too high!")
    else:
        print("You've guessed too low")
print("congratulations you've it!")


#>>>missing code<<<
