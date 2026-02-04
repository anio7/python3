#Write a program that generates a random name to pay the bill for food
import random


friends = ["Alice","Bob","Charlie","David","Emmanuel"]
random.choice(friends)

#random.choice was chosen because it returns a random selected element from a specified sequence
friendsInd = random.randint(0,4)
print(friends[friendsInd])

friendsInd = random.randint(0,len(friends)) #this mysteriously works 
print(friends[friendsInd])