from turtle import Turtle, Screen

mike = Turtle()
screen = Screen()


# turtle moves forward
def moves_forward():
    mike.forward(10)


# turtle moves backward
def moves_backwards():
    mike.backward(10)


# screen is cleared and turtle gets back to its origin point
def clear_screen():
    mike.clear()
    mike.reset()


# turtle turns counter clockwise
def turn_counter_clockwise():
    new_heading = mike.heading() + 10
    mike.setheading(new_heading)


# turtle turns clockwise
def turn_clockwise():
    new_heading = mike.heading() - 10
    mike.setheading(new_heading)


screen.listen()
screen.onkeypress(key="w", fun=moves_forward)
screen.onkeypress(key="s", fun=moves_backwards)
screen.onkeypress(key="c", fun=clear_screen)
screen.onkeypress(key="a", fun=turn_counter_clockwise)
screen.onkeypress(key="d", fun=turn_clockwise)

screen.exitonclick()
