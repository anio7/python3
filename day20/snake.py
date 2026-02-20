from turtle import Turtle

START_POS = [(0,0),(-10,0),(-20,0)]
MOVE_DIS = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    #create ATTRIBUTES & METHODS
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
     
    def create_snake(self):
        for pos in START_POS:
            new_snake = Turtle("circle")
            new_snake.color("white")
            new_snake.pu()
            new_snake.goto(pos)
            self.snake.append(new_snake)
    
    #create a method for movement       
    def move(self):
        for seg_num in range(len(self.snake)-1 ,0,-1):
            new_x = self.snake[seg_num -1].xcor()
            new_y = self.snake[seg_num -1].ycor()
            self.snake[seg_num].goto(new_x,new_y)
        self.head.fd(MOVE_DIS)
    
    #create methods for direction and prevent going back in original direction   
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)  
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    