"""
    P.S - if you iterate through a string and concatenate to a empty list it splits the string into a list of strings.
        - if you iterate through a list and concatenate to a empty string it joins the list and becomes a string
"""

splitStr = []
letter = "true love"

#iterate through letter to split it
for i in letter:
    splitStr += i
print(splitStr)

def loveCalc(name1,name2):
#count how many times the letter occurs
    name1 = name1.strip()
    count1 = 0
    for i in name1:
        if i in splitStr:
            if i == "":
                count1 = count1
        #if the character occurs start counting the character
        print(f"{i} occurs {count1} times")
        count1 +=1
    count1 = str(count1)      
    print(count1)
    print(type(count1))    

    count2 = 0
    name2 = name2.strip()
    for i in name2:
        if i in splitStr:
            if i == "":
                count2 = count2
        #if the character occurs start counting the character
        print(f"{i} occurs {count2} times")
        count2 +=1        
    count2 = str(count2)      
    print(count2)
    print(type(count2))
    loveScore = str(count1 + count2)
    print(f"the total love -score is {loveScore}")
    
loveCalc("anderson","niomi")