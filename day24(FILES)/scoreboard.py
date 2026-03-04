from turtle import Turtle

ALIGNMENT = "CENTER"
FONT = ("Arial",14,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
            
        
        #create the turtle color and position
        self.color("yellow")
        self.pu()
        self.goto(0,200)
        
        #get the turtle to write the score
        self.write(f"SCORE: {self.score}", align = ALIGNMENT, font = FONT)
        self.hideturtle()
        self.update_scoreboard()
           
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align = ALIGNMENT, font = FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.score = self.score
            with open("data.txt", mode = "w") as data:
                data.write({self.high_score})
        self.score = 0
        self.update_scoreboard() 
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        