"""Create a game of Rock Paper and Scissors"""

import random
print("Welcome to the game of Rock, Paper, Scissors!")

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""
 
paper ="""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""  
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""  

HumanChoice = input("What is your choice? ")

choices = ["rock","paper", "scissors"]
CPUchoice = random.choice(choices)
print(f"Your choice is {HumanChoice},the cpu choice is {CPUchoice}")

#Declare human or cpu winner depending on choice.

if HumanChoice == "rock" and CPUchoice == "scissors":
    print(rock) 
    print(scissors)
    print("you win")
elif HumanChoice == "scissors" and CPUchoice == "paper":
    print(scissors)
    print(paper)
    print("You win!")
elif HumanChoice == "paper" and CPUchoice == "rock":
    print(paper) 
    print(rock)
    print("You win!") 
elif HumanChoice == CPUchoice:
    print("its a tie")
else:
    print("You loose!")