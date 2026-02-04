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

choice1= input("You're at a cross-road, where do you want to go? Left or Right? ")
if choice1 == "left":
        choice2 = input('You\'ve come to a lake.' 
                        'There is an island in the middle of the lake'
                        'Type "wait to wait for a boat.'
                        'Type "swim to swim across.').lower()
        if choice2 =="wait":
            choice3 = input("You arrive at the island unharmed. "
                            "There is a house with three doors. "
                            "One red, one yellow and one blue "
                            "Which color do you choose? ").lower()
            if choice3 == "yellow":
                print("Congratulations!!! You've found the treasure!!!")
            elif choice3 == "red":
                print("You've been burnt by fire, so game-over")
            else:
                print("You've been eaten by beast, so game-over")
        else:
            print("You've been attacked by a trout, so game-over")
        
else:
        print("I'm sorry but you've fallen into a deep hole, so game-over")
