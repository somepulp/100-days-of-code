from turtle import Turtle, Screen
import random

brush = Turtle()
screen = Screen()


colors_list = [(34, 108, 167), (223, 229, 235), (227, 233, 230), (245, 77, 36), (112, 163, 211),
                   (153, 57, 85), (219, 156, 94), (201, 60, 27), (24, 133, 55), (246, 204, 84), 
                   (190, 151, 47), (225, 119, 152), (46, 53, 121), (221, 68, 97), (113, 199, 156), 
                   (147, 37, 30), (253, 202, 0), (91, 113, 192), (74, 40, 32), (248, 153, 143), 
                   (111, 41, 49), (155, 212, 203), (53, 174, 163), (38, 31, 67), (154, 210, 219), 
                   (43, 33, 45), (35, 55, 46), (99, 93, 2)]

# paint a painting with 10 by 10 rows of spots
# dots 20 in size, spaced apart by 50 paces

# First row: 

screen.colormode(255)
#screen.screensize(2000,2000)
screen.setup(width=1, height=1, startx=None, starty=None)

brush.penup()
brush.setposition(-200, -200)
start_position = brush.position()
rows = 10 
cols = 12 
for row in range(rows):
    for col in range(cols):
        brush.dot(20, random.choice(colors_list))
        brush.forward(50)
    brush.setposition(start_position + (0, 50))
    start_position = brush.position()

screen.exitonclick()