"""Write a program that functions as a calculator.This is the advance version!

It takes 2 numbers and an arithmetic operator."""

print("Welcome to our calculator")

#to receive multiple inputs we use split to split the string inputs
num1,num2 = input("please input 2 numbers: , ").split()
num1,num2 = int(num1),int(num2)
arithOpp = input("please input your operator symbol: ")


#use match case when using multiple simple 
match arithOpp:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = num1 * num2    
        
        
print(f"you have entered: {num1} {arithOpp} {num2}")
print(f"the result is {result}")

#p.s error handling wasn't included in this calculator app.