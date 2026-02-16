#import art
from HLlogo import HLlogo,vs
import random 

#data missing from this python file.
from game_data import data
   
#create your functions for your code.
def format_data(account):
    account_name = account_a["name"]
    account_desc = account_a["description"]
    account_country = account_a["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_ans(user_input, a_followers, b_followers):
    if a_followers > b_followers:
        return user_input == "a"
    else:
        return user_input == "b"

#start your game.
print(HLlogo)
print("Welcome to Higher or Lower")

#create your variables for your code.
score = 0
account_b = random.choice(data)

#create a while loop to keep the user playing until they guess wrong.
continue_game = True
while continue_game:
    #generate a random account from the game data
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    
    #account a becomes b once you win the round
    account_a = account_b
    account_b = random.choice(data)
    if account_a ==account_b:
        account_b = random.choice(data)    
        
    #ask user to make a guess
    user_input = input("Do you think has more followers: A or B ").lower()

    #check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_ans(user_input, a_follower_count,b_follower_count)
    if is_correct:
        score +=1
        print(f"You're right! Correct score is {score}")
    else:
        print(f"Sorry, that's wrong! Final score is {score}")
        continue_game = False
        print("Good bye")
