from turtle import Turtle, Screen
from paddle import *
from ball import *
from scoreboard import *
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.go_up)
screen.onkeypress(key="Down", fun=r_paddle.go_down)

screen.onkeypress(key="w", fun=l_paddle.go_up)
screen.onkeypress(key="s", fun=l_paddle.go_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    a = 0

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_Y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or \
            (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_X()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
