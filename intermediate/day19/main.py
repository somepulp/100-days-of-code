from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
screen.listen()
# NOTE: to bind a keystroke to an event, we use an event listener
screen.onkey(key="space", fun=move_forward)
# NOTE: onkey is a higher-order function as it takes a function as an input
screen.exitonclick()