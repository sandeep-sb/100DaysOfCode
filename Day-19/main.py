from turtle import Turtle, Screen

mike = Turtle()
screen = Screen()


def moves_forward():
    mike.forward(10)


screen.listen()
screen.onkey(key="space", fun=moves_forward)


screen.exitonclick()
