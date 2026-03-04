from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

TOTAL = 5

#screen setup
screen = Screen()
screen.setup(width = 600, height = 600)
screen.title("Ping_ponG!")
screen.bgcolor("black")
screen.tracer(0)

#create a score board
score = ScoreBoard()

#create paddle positions using the paddle class which takes position as a tuple.
r_paddle = Paddle((280,0))
l_paddle = Paddle((-285,0))

#create a ball starting at pos(0,0)
ball = Ball()

#get the screen to listen to keyboard inputs 
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    
    #detect collision with wall
    if ball.ycor() > 290. or ball.ycor() < -290:
        ball.wall_bounce()
        
    #detect collision with paddles
    if ball.distance(r_paddle) <= 30 and ball.xcor() > 250 or ball.distance(l_paddle) <= 30 and ball.xcor() > -290:
        ball.bounce_paddle()
        
    #if r_paddle misses left side score increments
    if ball.xcor() > 300:
        ball.reset_pos()
        score.increase_l_score()
    #if l_paddle misses left side score increments
    elif ball.xcor() < -300:
        ball.reset_pos()
        score.increase_r_score()
        
    #if a score is greater than the total
    if score.r_score or score.l_score >= TOTAL:
        game_is_on = False
        score.game_over()
    
    
screen.exitonclick()