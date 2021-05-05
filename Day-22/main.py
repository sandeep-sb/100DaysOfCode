from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

# Creates a new screen with the following specifications
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

# Objects of Paddle class, Ball class, Scoreboard class created.
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Event listener is activated on the screen.
screen.listen()
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)

# Shows the initial score 0-0 after creation of screen and
# before the start of the game.
scoreboard.update_scoreboard()


is_on = True
sec = 0.1
while is_on:
    time.sleep(sec)
    screen.update()
    ball.move()

    # Detect collision with the walls
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect collision with the paddle
    if (ball.xcor() > 320 and ball.distance(right_paddle) < 50) or (
            ball.xcor() < -320 and ball.distance(left_paddle) < 50):
        ball.bounce_x()
        # Increases the sleep time everytime the ball collides with
        # the paddle
        sec *= 0.9
        time.sleep(sec)

    # Detect if the ball is out of bounds on the right side
    if ball.xcor() > 400 or ball.ycor() > 300:
        ball.reset_position()
        scoreboard.l_point()
    # Detect if the ball is out of bounds on the left side
    elif ball.xcor() < -400 or ball.ycor() < -300:
        ball.reset_position()
        scoreboard.r_point()

    # Prints the final score of the game after one player has lost
    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        scoreboard.game_over()
        is_on = False

screen.exitonclick()
