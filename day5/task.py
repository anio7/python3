##Create a basic for loop
fruits = ["apple","peach","pear"]
for i in fruits:
    print(i)
    print(i + "-pie")

#Create a program to give the sum of all the numbers in a list.
studentScores = [150,142,185,120,171,149,24,59,68,199,78,65,89]
totalSum = sum(studentScores)

sum = 0
for i in studentScores:
    sum += i
print(sum)
print(max(studentScores))

#Create a program to find the maximum number in a list.
#Use this technique when hold all the intermediate values which are values that will be used in code.
maxNum = 0
for i in studentScores:
    if i > maxNum: # this evaluates if i greater than maxNum, if so it maxNum becomes i
        maxNum = i
print(maxNum)

#create a program to count the sum of numbers within a range.
sum_ = 0
for i in range(1,101):
    sum_ +=i
    print(sum) #prints every step of the addition during the loop
print(sum) #prints the result of the loop