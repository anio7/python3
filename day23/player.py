from turtle import Turtle

STARTING_POINT = (0,-350)
MOVE_DIS = 10
FIN_LINE = 320
MOVE_COR = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.go_to_start()
        self.setheading(90)
            
    def move_up(self):
        self.fd(MOVE_DIS)
    def move_down(self):
        self.back(MOVE_DIS)
    
    def go_to_start(self):
        self.goto(STARTING_POINT)
        
    def is_at_finish(self):
        if self.ycor() > FIN_LINE:
            game_on = False