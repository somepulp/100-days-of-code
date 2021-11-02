from turtle import Turtle, Screen
import random 
from functions import random_color

screen = Screen()
timmy = Turtle()

screen.colormode(255)
screen.screensize(2000,2000)

# Random Walk:
# pick direction from nort, east, south, west, then pick a color, then walk 
directions = {
    "north": 0,
    "east": 90,
    "south": 180,
    "west":270
}


def random_direction():
   return random.choice(list(directions.keys()))

def increase_pensize(turtle, mod):
    turtle.pensize(turtle.pensize() + mod)
# increase thickness of pensize
#timmy.pensize()

def random_walk(turtle, screen, steps, speed = 10):
    timmy.shape('classic')
    screen.colormode(255)
    current_step = 0
    # set turtle speed
    turtle.speed(speed)
    # set initial pensize
    #turtle.pensize(10)
    # walk number of random steps before stopping
    while current_step != steps: 
        chosen_direction = random_direction()
        turtle.color(random_color())
        turtle.setheading(directions[chosen_direction])
        turtle.forward(15)
        increase_pensize(turtle, 0.001)
        current_step += 1 

random_walk(turtle=timmy, screen=screen, steps= 2000, speed=10)

screen.exitonclick()