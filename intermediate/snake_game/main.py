from turtle import Screen, Turtle
import turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic: Snake Game")

#TODO: Create snake body - 3 turtle objects next to each other
starting_positions = [(0,0), (-20,0), (-40,0)]
snake_body = []

for i in range(0, len(starting_positions)):
    snake_body.append(Turtle(shape="square"))
    snake_body[i].color("white")
    snake_body[i].goto(starting_positions[i])

screen.exitonclick()