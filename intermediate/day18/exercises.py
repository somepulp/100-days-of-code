from turtle import Turtle, Screen
screen = Screen()

timmy = Turtle()
timmy.shape('turtle')
timmy.color('forestgreen')
timmy.pensize(2)
# Draw a square
timmy.forward(100)
while round(timmy.ycor()) != 0 or round(timmy.xcor()) != 0:
    timmy.right(90)
    timmy.forward(100)

timmy.reset()

# Draw a dashed line
counter = 0
num_dashes = 20
while counter != num_dashes:
    timmy.pendown()    
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    counter +=1 

timmy.reset()

# Draw a beautiful multishape figure with random colors each time 
import random 
screen.colormode(255)
screen.screensize(2000,2000)
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
#while num_sides != 4:
    


screen.exitonclick()
