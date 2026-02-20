from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.title("My SnaKie!")
screen.bgcolor("black")
screen.tracer(0)

#get the snake moving.
snake = Snake()

#generate the food
food = Food()

#generate the scoreboard
score = ScoreBoard()

#get the screen to listen
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
    
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_pos()
        score.clear()
        score.increase_score()
        snake.extend_snake()

    #detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295  or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        score.clear()
        score.game_over()
    
    #detect collision with self
    for snake_ in snake.snake[1:]:
        if snake.head.distance(snake_) < 10:
            game_is_on = False
            score.game_over()
    

screen.exitonclick()