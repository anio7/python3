import guess
print(guess)

import random

#set global variables to be used throughout the code
EASY_LEVEL_TURNS = 10
NORMAL_LEVEL_TURNS = 7
HARD_LEVEL_TURNS = 5

#create a way to get the lives using global variables and return statements
def set_difficulty():
    level = input("Please select your level!: 'easy','normal','hard")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "normal":
        return NORMAL_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

#create a function that compares the user guess and the actual guess to turns remaining
def check_ans(user_guess, actual_ans,turns):
    """checks ans against guess and returns the number of turns remaining"""
    print(f" the user guessed: {user_guess}")
    if user_guess > actual_ans:
        print("Too high. Guess again")
        return turns - 1
    elif user_guess < actual_ans:
        print("Too low. Guess again")
        return turns - 1
    else:
        print(f"You guessed it! The answer was {actual_ans}")         

#create a function that controls the game play
def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100") 
    turns = set_difficulty()
    user_guess = int(input("What number do you think it is: "))
    #create a program for guessing a random number between a range and assign to variable
    actual_ans = random.choice(range(0,100)) 
    print(f" the number is {actual_ans}")
        
    #create a while loop that keeps the game running until the user gets the right number or lives run out
    while user_guess != actual_ans and turns != 0:
        
        print(f"you have {turns} attempts remaining to guess the number!")
        user_guess = int(input("What number do you think it is: "))
        
        #save turns as decrement towards zero
        turns = check_ans(user_guess,actual_ans,turns)
        if turns == 0:
            print("you lose")
        print(f"the user guessed {user_guess} and user has {turns} turns remaining")
    print("game over")
game()
    

    