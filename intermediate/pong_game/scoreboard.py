from turtle import Turtle

class GameBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,300)
        self.color("white")
        self.pensize(5)
        self.setheading(270)
        self.ht()
    
    def draw_lines(self):
        for i in range(20):
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)

class Score(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.goto(position)
        self.color("White")
        self.ht()
        self.score = 0
        self.update_score()
        
    def update_score(self):
        self.write(f"{self.score}", align="center", font=("Bit5x3", 60, "normal")) 
           
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
        