from turtle import Turtle,Screen
from player import Player
from score import ScoreBoard
from car_man import CarMan
import time

#create objects for the classes
turt = Turtle()
screen = Screen()
score = ScoreBoard()
player = Player()
car = CarMan()

#get the screen to listen for keypress
screen.listen()
screen.onkey(player.move_up,"Up")
screen.onkey(player.move_down,"Down")

#while the game is on
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    
    car.create_car()
    car.move_cars()
    
    #detect if the turtle collides with a car
    for cars in car.all_cars:
        if car.distance(player)< 20:
            game_on = False
            
    if player.is_at_finish():
        player.go_to_start()
        car.level_up()

#design the screen 
screen.setup(width = 700, height = 700)
screen.tracer(0)
screen.exitonclick()