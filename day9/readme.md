Day9 is about dictionary and nesting.
to create or wipe a dictionary we use curly brackets-
dic_Name = {} #empty dictionary

to receive items from a dictionary you use the key in square brackets
dic_name[key_name]

to add items to a dictionary we do something similar and whatever is on the RHS of the "=" is added to the dictionary
dic_name[key_name] = ""

for iteration through a dictionary there is a special way to get the key or value using

for i in dic_name:
    do something
    to get the keys printed print(i)
    to get the values printed print(dic_name[i])