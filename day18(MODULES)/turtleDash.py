from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")


for _ in range(15):
    tim.fd(10)
    tim.pu()
    tim.fd(10)
    tim.pd()
    # tim.pd
    # tim.lt(90)


screen = Screen()
screen.exitonclick()