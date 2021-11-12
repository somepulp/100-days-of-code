from turtle import Screen, Turtle, shape
import time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic: Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.5)

    snake.move()

screen.exitonclick()
