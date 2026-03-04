from turtle import Turtle

FONT = ("Courier", 80, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.color("white") 
        self.hideturtle()
        
        #variables for the score
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self): 
        #get the turtle to write the score
        self.clear()
        self.goto(-100,200)  
        self.write(f"{self.l_score}",align= "center",font = FONT)
        self.goto(100,200)
        self.write(f"{self.r_score}",align= "center",font = FONT)
    
    def increase_r_score(self):
        self.r_score += 1
        self.update_scoreboard()
    
    def increase_l_score(self):
        self.l_score += 1
        self.update_scoreboard()
           
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!!!",align= "center",font = ("Arial", 40, "normal"))
        self.color("red")