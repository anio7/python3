from turtle import Turtle

#create a paddle class
class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        #create the attributes for the class
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.pu()
        self.goto(pos)

    #create methods for direction and prevent going back in original direction   
    def go_up(self):
        new_y = self.ycor()+20
        self.goto([self.xcor(),new_y])
    def go_down(self):
        new_y = self.ycor()-20
        self.goto([self.xcor(),new_y])   
    