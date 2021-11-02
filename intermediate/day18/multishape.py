from turtle import Turtle, Screen
import random 

screen = Screen()
timmy = Turtle()

screen.colormode(255)
screen.screensize(2000,2000)

# Draw a beautiful multishape figure with random colors each time 

min_sides = 3 
max_sides = 30
FULL_DEGREE = 360
timmy.pensize(2)

def draw_shape(num_sides):
    angle = FULL_DEGREE/num_sides
    for i in range(num_sides):
        timmy.right(angle)
        timmy.forward(100)
        
def random_color():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    random_color = (r,g,b)
    return random_color

while min_sides != max_sides:
    new_color = random_color()
    timmy.color(new_color)
    draw_shape(num_sides=min_sides) 
    min_sides +=1   

screen.exitonclick()