from turtle import Screen, Turtle


screen = Screen()
screen.setup(width = 600, height = 500)
screen.title("My Snakey")
screen.bgcolor("black")

snake = Turtle()
snake.shape("circle")
snake.color("white")


def move_f():
    snake.fd(10)
def move_b():
    snake.back(10)
def move_l():
    snake.lt(90)
def move_r():
    snake.rt(90)
    
    
screen.listen()
screen.onkey(move_f,"w")
screen.onkey(move_b,"s")
screen.onkey(move_l,"a")
screen.onkey(move_f,"d")
screen.exitonclick()