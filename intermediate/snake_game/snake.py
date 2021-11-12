from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake():
    # initializing the snake creates the snake body 
    def __init__(self):
        self.snake_body = []
        self.create_snake()
    
    def create_snake(self):    
        for pos in STARTING_POSITIONS:
            new_leg = Turtle(shape = "square")
            new_leg.color("white")
            new_leg.penup()
            new_leg.goto(pos)
            self.snake_body.append(new_leg)
            
    def move(self):
        for leg_num in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[leg_num-1].xcor()
            new_y = self.snake_body[leg_num-1].ycor()
            self.snake_body[leg_num].goto(x=new_x, y=new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

