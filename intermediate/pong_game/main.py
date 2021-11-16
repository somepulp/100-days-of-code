from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import GameBoard, Score
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Classic: Pong Game")
screen.tracer(0)

board = GameBoard()
board.draw_lines()

left_score = Score(-150, 225)
right_score = Score(150, 225)

right_paddle = Paddle(350)
left_paddle = Paddle(-350)
#screen.update()
ball = Ball()

screen.listen()
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")

screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")

#screen.update()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
screen.exitonclick()