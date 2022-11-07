from turtle import Turtle, Screen
from padle import Padle
from ball import Ball
import time
from scoreboard import Scoreboard

########################################
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)
#########################################


r_padle = Padle((350, 0))
l_padle = Padle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()




screen.listen()
#player 1
screen.onkey(r_padle.go_up, "Up")
screen.onkey(r_padle.go_down, "Down")

#player 2
screen.onkey(l_padle.go_up, "w")
screen.onkey(l_padle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.05)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 380:
        ball.restat()
        ball.bounce_x()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.restat()
        ball.bounce_x()
        scoreboard.r_point()

    if ball.distance(r_padle) < 50 and ball.xcor() > 320 or ball.distance(l_padle) < 50 and  ball.xcor() < -320:
        ball.bounce_x()

screen.exitonclick()