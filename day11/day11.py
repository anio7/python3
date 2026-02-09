#Write a program that plays blackJack
import random
import bj
print(bj)

def dealCard():
    """Returns a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] 
    card = random.choice(card)
    return card
def calcScore(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)   
    return sum(cards)

def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "lose, opponent has BlackJack"
    elif user_score == 0:
        return "Win with a BlackJack"
    elif user_score > 21:
        return "You went over. You lose!"
    elif comp_score >21:
        return "Opponent went over. You win."
    elif user_score > comp_score:
        return "You win"
    else:
        return "You lose"
def play_game():
    user_cards = []
    comp_cards = []
    comp_score = -1 
    user_score = -1
    

    for _ in range(2):
        user_cards.append(dealCard)
        comp_cards.append(dealCard)
        
    while not is_game_over:
        user_score  = calcScore(user_cards)
        comp_score = calcScore(comp_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Your cards: {comp_cards}, current score: {comp_score}")


        if user_score == 0 or comp_score == 0 or user_score> 21:
            is_game_over = True
        else:
            user_should_deal = input("Type y to get another card, type n to pass: ")
            if user_should_deal == "y":
                user_cards.append(dealCard())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(dealCard())
        comp_score = calcScore(comp_cards)
        
    print(compare(user_score,comp_score))


while input("do you want to play another game of blackJack!") == "y":
    play_game()