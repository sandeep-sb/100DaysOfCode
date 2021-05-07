import time
from turtle import Screen

import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=tim.move)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.car_create()
    cars.move_car()

    # Respawn tim after crossing the finish line
    if tim.is_at_finish_line():
        tim.respawn()
        cars.increase_speed()
        score.increase_score()

    # Detect collision with car
    for car in cars.all_cars:
        if car.distance(tim) < 20:
            score.game_over()
            game_is_on = False


screen.exitonclick()
