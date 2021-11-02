from turtle import Turtle, Screen
from functions import random_color
 
screen = Screen()
arrow = Turtle()
arrow.speed(10)
screen.colormode(255)

num_circles = 30
num_drawn = 0
heading = arrow.heading()
angle = 360/num_circles

while num_drawn != num_circles:
    arrow.color(random_color())
    arrow.circle(100)
    arrow.setheading(arrow.heading() + angle)
    num_drawn += 1 
    
#arrow.circle(100)
screen.exitonclick()