from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow","green","blue","purple"]
START_DIST = 5
MOVE_INCREMENT = 10


class CarMan(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = START_DIST 
        
    def create_car(self):
        rand_chance = random.randint(1,6)
        if rand_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len = 2,stretch_wid = 1)
            new_car.pu()
            new_car.color(random.choice(COLORS))
            
            rand_y = random.randint(-300,300)
            new_car.goto(300, rand_y)
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        
    def level_up(self):
        self.car_speed += MOVE_INCREMENT