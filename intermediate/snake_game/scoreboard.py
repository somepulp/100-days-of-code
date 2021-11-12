from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier', 16, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.ht()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}",align=ALIGN, font=FONT)
    
    def increase_score(self):
        self.clear()
        self.score +=1 
        self.update_scoreboard()
        