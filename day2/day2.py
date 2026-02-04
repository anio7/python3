"""Write a program that generates a bill tip

1.it must take the total bill
2.ask give a tip in percentage of the bill
3.amount of people paying the bill"""

print("Welcome to the tip calculator!")
totalBill = float(input("What is the total bill:\n"))
tipAmount = int(input("How much tip percent would you like to give- 10,12 or 15:\n"))
people    = int(input("How much people to split the bill:\n"))

# this is the tip as a percent and amount
tipAsPercent = tipAmount/100
tipOffBill = totalBill * tipAsPercent

eachPay = (totalBill+tipOffBill)/people
print(f"each person pays:${eachPay:.2f}") #you can use round as well for the decimal place