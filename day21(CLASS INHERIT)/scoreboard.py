from turtle import Turtle

ALIGNMENT = "CENTER"
FONT = ("Arial",14,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        
        #create the turtle color and position
        self.color("yellow")
        self.pu()
        self.goto(0,200)
        
        #get the turtle to write the score
        self.write(f"SCORE: {self.score}", align = ALIGNMENT, font = FONT)
        self.hideturtle()
           
    
    def increase_score(self):
        self.score += 1
        self.write(f"SCORE: {self.score}", align = "center", font = ("Arial",14,"normal"))
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!!!\nYour Score is {self.score}" ,align= ALIGNMENT,font = ("Arial", 20, "normal"))
        self.color("red")
        
        