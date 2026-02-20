from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width = 600, height = 500)
screen.title("My Snakey")
screen.bgcolor("black")
screen.tracer(0)

#get the snake moving.
snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    #get snake to move.
    snake.move()  
    


screen.exitonclick()