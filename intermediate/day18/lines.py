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

screen.exitonclick()