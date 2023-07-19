from turtle  import Turtle 


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score()
        
    def score(self):
        self.sum = 0
        self.color("yellow")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.write(arg=f"score: {self.sum}",align="center", move = True,font=("Arial", 24," normal"))
        
    def incerease_score(self):
        self.sum += 1
        self.clear()
        self.goto(0,250)
        self.write(arg=f"score: {self.sum}",align="center", move = True,font=("Arial", 24," normal"))   
        
    def end(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center",  font=("Arial", 24," normal"))     
        
        