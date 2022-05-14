from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier', 16, 'normal', 'bold')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./data.txt") as file: 
            self.high_score = int(file.read()) 
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.ht()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}",align=ALIGN, font=FONT)


    def increase_score(self):
        self.score +=1 
        self.update_scoreboard()

    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./data.txt",'w') as file:
                file.write(f"{self.high_score}") 
        self.score = 0 
        self.update_scoreboard()