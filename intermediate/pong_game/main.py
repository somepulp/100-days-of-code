from turtle import Screen
from paddle import Paddle
from scoreboard import GameBoard, Score
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Classic: Pong Game")
screen.tracer(0)

right_paddle = Paddle(350)
left_paddle = Paddle(-350)
board = GameBoard()
#board.draw_lines()

left_score = Score((-150, 225))
right_score = Score((150, 225))

ball = Ball()
#screen.update()

screen.listen()
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")

#screen.update()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect when ball hits wall
    if abs(ball.ycor()) > 280:
        ball.bounce_y()
    
    # Detect when ball hits either paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 1.001
         
    # Detect when ball misses right paddle - reset but also reverse direction
    if ball.xcor() > 370:
        left_score.increase_score()
        ball.reset_position()
    
    if ball.xcor() < -380:
        right_score.increase_score()
        ball.reset_position()
        
screen.exitonclick()