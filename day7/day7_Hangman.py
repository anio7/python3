"""Create a hangMan game"""
#import random module for randomness
import random

#create a list of words to choose from randomly
wordList=["live","love","laugh", "aardvark","baboon","camel" ]

##randomly choose a word from the word list
chosenWord = random.choice(wordList)
print(chosenWord)

#placeholder for letters in chosenWord
placeholder = ""
for i in range(len(chosenWord)):
    #since its a string you use += for the concatenation of the "_" together
    placeholder += "_" 
print(placeholder)

#Create variables to be used in program
lives = 6
correctLet = []
gameOver = False

#use a while loop to make the user guess again while counting the amount of lives.

while not gameOver:
    print(f"The amount of lives you have are {lives}")
##ask the user to guess the letter and assign letter to word.
    userGuess = input("Can you please guess a letter in the word?\n ").lower()
    print(f"the letter you've guessed is: {userGuess}")
    
#Create a display variable that puts the letter in the right position and _ in the wrong one.
    if userGuess in correctLet:
        print(f"you already tried this letter: {userGuess}. Please try another letter")

    display = ""
    for i in chosenWord:
        #using a for loop for the iteration if the userGuess is right, it displays it & appends letter to list (correctLet) 
        if i == userGuess:
            display += i
            correctLet.append(i)
            
        #also by using the in keyword within the elif it displays everything in the correctLet once the condition is true.
        elif i in correctLet:
            display += i
        else:
            display +="_"
    print(display)
    
    if userGuess not in chosenWord:
        lives -=1
        print(f"You've guessed this letter:{userGuess} which is incorrect, you lost one life")
        print(f"You have {lives} remaining!")
        if lives == 0:
            gameOver = True
            print("You lose")
    
    #print message if all the letters are figured out
    if "_" not in display:
        gameOver = True
        print("you win!")
        
    playAgain = input("Do you want to play again? y/n ")
    if playAgain == "y":
        play()
print("Game over")


