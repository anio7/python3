We will be learning about loops

for loops - (used for printing out items one by one)

for loops are best for list.
for item in list_of_items: --> this reminds me just like javascript! using for ..in.
#do something

to better understand this think of saying for item index in list, print the item/value at that index.

Another form of the for loop is range. Which prints the number between a and b excluding b. Step is the number it steps by.
for number in range(a,b,step):
print(number)

you can also you:
for i in range(0, varName)
do something

there is also the variables that are created to hold intermediate values

sum = 0
for i in range(0,10):
sum += i

for char in range(0,varNum):
word += random.choice(var)

Using while loops work when the condition remains true - the condition is always written before the while loop.

#condition
while something_is_true:
do something


When to use for loop and while loop:
Use a for loop are great for iterating over something and you need to do something with each item.
While loops are better for running infinite loops