"""write a program to generate a password"""
import random

#ask for user input
AmtOfLetters = int(input("How many letters would you like in your password? "))
AmtOfNumbers = int(input("How many numbers would you like"))
AmtOfSymbols = int(input("How many symbols would you like? "))

#since there are 26 letters in the alphabet you can start with that
#there are 10 numbers in total

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                 'n','o','p','q','r','s','t','u','v','w','x','y','z',
                 'A','B','C','D','E','F','G','H','I','J','K','L','M',
                 'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ["!","@","#","$","%","^","&","*","(",")","+"]

#use the random.choice() to randomly choose from the range given, then add that letter to the password variable.
password = ""  
for char in range(0,AmtOfLetters):
    password += random.choice(letters)    
for char in range(0,AmtOfNumbers):
    password += random.choice(numbers)   
for char in range(0,AmtOfSymbols):
    password += random.choice(symbols)  
print(password)

#hardlevel - best way to do this is a list for the shuffling 
passwordList = []
for char in range(0,AmtOfLetters):
    passwordList.append(random.choice(letters))
for char in range(0,AmtOfNumbers):
    passwordList.append(random.choice(numbers))   
for char in range(0,AmtOfSymbols):
    passwordList.append(random.choice(symbols)) 
print(passwordList)
encryptPass = random.shuffle(passwordList)

#after shuffling the list loop through the list to form a string.
finPassword = ""
for char in passwordList:
    finPassword += char #add char to variable.
print(f"your password is {finPassword}")