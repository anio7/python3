""" Write a program that ciphers password inputted by a user."""
import logo
print(logo)

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
        
        #this is to make sure that you never go outside of the boundaries of the list.
        newPos %= len(alphaBet)
    print(f"your encrypted message is: {ciphText}")

#TODO- create a function called decrypt which is the reverse to encrypt.     
def decrypt(origText, shiftNum):
    decrypText = ""
    for i in origText:
        newPos = alphaBet.index(i)
        # print(f"{i} at index {pos}") #shows the position of the original text
        
        #reverse the shift by minus 
        origPos = newPos - shiftNum
        #adds letters to empty string by adding their index value from newPos which is alphaBet[alphaBet.index(i) + shiftNum]
        decrypText += alphaBet[origPos]
        
        #this is to make sure that you never go outside of the boundaries of the list.
        origPos %= len(alphaBet)
    print(f"your decrypted message is: {decrypText}") 
    
def my_caesar():
    ans = input("What would you like to do- encrypt or decrypt: ")
    if ans == "e" or "encrypt":
        encrypt(origText, shiftNum)
    else:
        decrypt(origText, shiftNum)
            
        
alphaBet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
        #   "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
print("Welcome to Caesar Cipher!\nWhere we decode and encode your messages!")
origText = input("Please enter your message:\n ").lower()
shiftNum = int(input("Please type the amount of letter shift you would like: "))
print(f"The amount letter shift you would like is {shiftNum}!")
# caesar(origText, shiftNum, encode_or_decode)
my_caesar()

# #to get the user to restart we will need a while loop with its condition
should_continue = True
while should_continue:
    origText = input("Please enter your message:\n ").lower()
    shiftNum = int(input("Please type the amount of letter shift you would like: "))
    my_caesar()
    
    restart = input("Would you like to go again").lower()
    if restart == "no" or "n":
        should_continue = False
        print("Goodbye")
    

# def caesar(origText, shiftNum, encode_or_decode):
#     output_text = ""
#     for i in origText:
#         if i not in alphaBet:
#             output_text += i
#         else:
#             if encode_or_decode == "decode":
#                 shiftNum *= -1
#         newPos = alphaBet.index(i)
#         origPos = newPos - shiftNum
#         #adds letters to empty string by adding their index value from newPos which is alphaBet[alphaBet.index(i) + shiftNum]
#         decrypText += alphaBet[origPos]
        
#         #this is to make sure that you never go outside of the boundaries of the list.
#         origPos %= len(alphaBet)
        
#     print(f"Here is the {encode_or_decode}d result: {output_text}")
    

    
    

