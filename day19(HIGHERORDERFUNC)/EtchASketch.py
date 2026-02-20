from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
    
def move_back():
    tim.back(10)
    
def turn_left():
    tim.lt(10)
    # new_heading = tim.heading() + 10
    # tim.setheading(new_heading)
    
def turn_right():
    tim.rt(10)
    # new_heading = tim.heading() - 10
    # tim.setheading(new_heading)
    
def clear():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(move_back,"s")
screen.onkey(clear, "c")
screen.exitonclick()