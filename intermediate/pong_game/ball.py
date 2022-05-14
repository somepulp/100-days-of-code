from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.color("white")
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 0.002
        
    
    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
        
    def bounce_y(self):
        self.y_move *= -1 
        
    
    def bounce_x(self):
        self.x_move *= -1 
        
    def reset_position(self):
        self.move_speed = 0.002
        self.goto((0,0))
        self.bounce_x()
    