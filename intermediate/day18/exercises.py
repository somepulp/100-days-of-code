from turtle import Turtle, Screen
screen = Screen()

timmy = Turtle()
timmy.shape('turtle')
timmy.color('forestgreen')
# timmy.pensize(2)
# # Draw a square
# timmy.forward(100)
# while round(timmy.ycor()) != 0 or round(timmy.xcor()) != 0:
#     timmy.right(90)
#     timmy.forward(100)

# timmy.reset()

# # Draw a dashed line
# counter = 0
# num_dashes = 20
# while counter != num_dashes:
#     timmy.pendown()    
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     counter +=1 

# timmy.reset()

# # Draw a beautiful multishape figure with random colors each time 
import random 
screen.colormode(255)
screen.screensize(2000,2000)
# min_sides = 3 
# max_sides = 30
# FULL_DEGREE = 360
# timmy.pensize(2)

# def draw_shape(num_sides):
#     angle = FULL_DEGREE/num_sides
#     for i in range(num_sides):
#         timmy.right(angle)
#         timmy.forward(100)
def random_color():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    random_color = (r,g,b)
    return random_color

# while min_sides != max_sides:
#     new_color = random_color()
#     timmy.color(new_color)
#     draw_shape(num_sides=min_sides) 
#     min_sides +=1   

timmy.reset()

## Random Walk:
# pick direction from nort, east, south, west, then pick a color, then walk 
directions = {
    "north": 0,
    "east": 90,
    "south": 180,
    "west":270
}
#set fastest speed 
#timmy.speed(10)
#original_pensize = timmy.pensize() 

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
        turtle.right(directions[chosen_direction])
        turtle.forward(15)
        increase_pensize(turtle, 0.001)
        current_step += 1 

random_walk(turtle=timmy, screen=screen, steps= 2000, speed=5)

screen.exitonclick()