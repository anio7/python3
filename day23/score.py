from turtle import Turtle

LEVEL = 1
FONT = ("Courier",24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(-320,325)
        
        self.level = LEVEL
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level} ", align = "left", font = FONT)
        
        
    def increase_level(self):    
        self.level + 1
        self.update_score()
        
    def game_over(self):
        self.write("GameOver")