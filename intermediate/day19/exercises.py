#Instructions: 
# Build turtle racing game with several turtles. 
# Winner is first to the end of the screen
from turtle import Turtle, Screen
import random 

# New turtle definition
def new_turtle(clr, ypos, shp = "turtle"):
    new_turtle = Turtle(shape = shp)
    new_turtle.penup()
    new_turtle.color(str(clr))
    new_turtle.goto(x=-240, y=ypos)
    all_turtles.append(new_turtle)


screen = Screen()
#setup the width and height of the screen
screen.setup(width=500, height=400)
user_color = screen.textinput(title="Select a turtle", 
                 prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "PaleVioletRed", "green", "blue", "purple"]
all_turtles = []
yp = -75
is_race_on = False

for i in range(len(colors)):
    new_turtle(clr=colors[i], ypos= yp)
    incr = 30
    yp += incr

if user_color:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)
        if turtle.xcor() >= 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if user_color == winner_color:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winner_color} turtle is the winner!")
            

screen.exitonclick()