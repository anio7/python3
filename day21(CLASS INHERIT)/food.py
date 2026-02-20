from turtle import Turtle
import random

#inherit from the turtle class
class Food(Turtle):
    def __init__(self):
        #call the turtle __init__ method and initialize the ATTRIBUTES
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.speed("fastest")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid= 0.5)
        self.refresh_pos()
        
    
    def refresh_pos(self):
        rand_x = random.randint(-280,280)
        rand_y = random.randint(-280,280)
        self.goto(rand_x,rand_y)
        