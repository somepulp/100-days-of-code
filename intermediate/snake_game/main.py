from turtle import Screen, Turtle, shape
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic: Snake Game")
screen.tracer(0)

#Created snake body - 3 turtle objects next to each other
starting_positions = [(0,0), (-20,0), (-40,0)]
snake_body = []

for pos in starting_positions:
    new_leg = Turtle(shape = "square")
    new_leg.color("white")
    new_leg.penup()
    new_leg.goto(pos)
    snake_body.append(new_leg)

#TODO: Move the snake body - continuously
game_on = True

while game_on:
    screen.update()
    time.sleep(0.5)
    for leg_num in range(len(snake_body)-1, 0, -1):
        new_x = snake_body[leg_num-1].xcor()
        new_y = snake_body[leg_num-1].ycor()
        snake_body[leg_num].goto(x=new_x, y=new_y)
    
    snake_body[0].forward(20)

screen.exitonclick()
