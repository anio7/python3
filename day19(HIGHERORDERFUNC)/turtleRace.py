from turtle import Turtle, Screen
import random

screen = Screen()

#setup the size of the screen
screen.setup(width = 700,height = 500)
screen.title("Welcome to the greatest race of your life!")

#ask for user input
user_bet = screen.textinput(title = "Bets please", prompt = "Please place a bet: ")
colors = ["red","orange","yellow","green","blue","indigo","violet"]
y_positions = [-150,-100,-50, 0, 50, 100, 150]
all_turtles = []


#position turtles
for turtle_index in range(0, 6):
    #place turtle at the edge of the screen
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.goto(x = -230, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True
    
while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() >330:
            is_race_on = False 
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You have won {user_bet} turtle is a winner")
            else:
                print(f"You have lost {win_color} turtle is a winner")
        rand_distance = random.randint(1,10)
        turtle.fd(rand_distance)


screen.exitonclick()