"""create a program that will guide the user to the treasure hidden inside of the castle and away from danger!"""
print("""
                         _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'

       
       """)
print("Welcome to the treasure Hunt!\nYour mission is to find the treasure!")
while True:
    
    crossRoad = input("You're at a cross-road, where do you want to go? Left or Right? ").lower()
    if crossRoad == "left":
        print("you have come to a lake. There is an island in the middle of the lake")
    else:
        print("I'm sorry but you've fallen into a deep hole, so game-over")
        break
        
    choice = input("Would you like to swim to the island or wait on a? ")
    if choice == "wait":
        print("you arrive at the island unharmed. There is a house with three doors.")
    else:
        print("You've been attacked by a trout, so game-over")
        break
    
    doors = input("Which door will you choose - red, blue or yellow").lower()
    if doors == "red" or " ":
        print("You've been burnt by fire, so game-over")
        break
    elif doors == "blue":
        print("You've been eaten by beast, so game-over")
        break
    else:
        print("You've found the treasure!!!")
        break