""" Write a program that ciphers password inputted by a user."""

print("""
                                                                               88             88
                                                                               ""             88
                                                                                              88                                                                                            88
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88            8b         88 88       d8 88       88 8PP""""""" 88 
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88            "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88             `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88 
                                                                                  88
                                                                                  88
                                                                                  88  
                                                                                                            
                                                                                                            """)
print("Welcome to Caesar Cipher!\n Where we decode and encode your messages!")
origText = input("Please enter your message:\n ").lower()
shiftNum = int(input("Please type the amount of letter shift you would like: "))
print(f"The amount letter shift you would like is {shiftNum}!")

#to encode message we must first iterate through it and add it to an empty list
#we need the spaces to stay where they are inside of the message.

alphaBet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
        #   "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#Todo - Create a function called encrypt() that takes original message and encrypts its data by shifting its letters
#TODO - Inside of the encrypt(), shift each letter of the original text by the shift amount given and print encrypted text

def encrypt(origText, shiftNum):
    #create variable to store 
    ciphText = ""
    #loop through each letter to find the index in alphaBet
    for i in origText:
        pos = alphaBet.index(i)
        # print(f"{i} at index {pos}") #shows the position of the original text
        
        #save new index position to variable
        newPos = pos + shiftNum
        #adds letters to empty string by adding their index value from newPos which is alphaBet[alphaBet.index(i) + shiftNum]
        ciphText += alphaBet[newPos]
    print(f"your encrypted message is: {ciphText}")         
encrypt(origText, shiftNum)   
    
    