from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.color("white")
        
    
    def move(self):
        self.goto(self.xcor()+10, self.ycor()+10)