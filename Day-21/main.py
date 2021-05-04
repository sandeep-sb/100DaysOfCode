from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=snake.up, key="Up")
screen.onkeypress(fun=snake.down, key="Down")
screen.onkeypress(fun=snake.right, key="Right")
screen.onkeypress(fun=snake.left, key="Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #   Detect collision with food.
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.refresh()

    #   Detect collision with the wall.
    if snake.snake_head.xcor() > 285 or snake.snake_head.xcor() < -285 or snake.snake_head.ycor() > 285 or snake.snake_head.ycor() < -285:
        is_game_on = False
        scoreboard.game_over()

    #   Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
