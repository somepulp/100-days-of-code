#Instructions: 
# movement: W - forward, S - backwards
# orientation: A - counter-clockwise, D - clockwise 
# clear: C - clear screen

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
    
def move_backward():
    tim.backward(10)

def counter_clockwise():
    tim.setheading(tim.heading()+10)
    
def clockwise():
    tim.setheading(tim.heading()-10)

def clean():
    screen.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clean)

screen.exitonclick()