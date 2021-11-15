from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xpos, ypos=0):
        super().__init__(shape="square")
        print(self.shapesize())
        self.resizemode("user")
        self.penup()
        self.color("white")
        self.goto(xpos, ypos)
        self.width
        self.shapesize(stretch_len=1, stretch_wid=5)
        
    def down(self):
        self.goto(self.xcor(), self.ycor() - 10)
        
    def up(self):
        self.goto(self.xcor(), self.ycor() + 10)