import gavel
print( gavel)

#welcome the user into 
print("Welcome to the silent bidding program")

#create a function to store highest bidder
def highestBid(bidDic):
    winner = ""
    highBid = 0
    for bidder in bidDic:
        
        #bidAmt would be equal to the value (bidDic[bidder]) of the dictionary and since highBid starts at 0, 
        # it automatically checks if its higher in value and stores it to highBid
        bidAmt = bidDic[bidder]
        if bidAmt > highBid:
            highBid = bidAmt
            winner = bidder
    print(f"the highest bidder was {winner} with £{highBid}")

#bids was placed outside of the loop to store values because iteration would delete the values every time.
bids ={}

#create a while loop and its condition = True for the continuous running.
bidding = True
while bidding:
    
    #create variables to be used in the function later
    name = input("What is your name? ")
    bid = int(input("what is your bid:£ "))
    
    #save data into a dictionary {name:price} since values unknown
    bids[name] = bid 
    
    #ask if they wanna continue bidding. If not ...condition becomes false and highestBid function activates with a good bye message.
    bidAgain = input("does anyone want to bid: y/n ").lower()
    if bidAgain =="n":
        bidding = False
        highestBid(bids)
        print("good bye")

