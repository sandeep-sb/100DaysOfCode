# from turtle import Turtle, Screen
#
# mike = Turtle()
# screen = Screen()
#
#
# # turtle moves forward
# def moves_forward():
#     mike.forward(10)
#
#
# # turtle moves backward
# def moves_backwards():
#     mike.backward(10)
#
#
# # screen is cleared and turtle gets back to its origin point
# def clear_screen():
#     mike.clear()
#     mike.reset()
#
#
# # turtle turns counter clockwise
# def turn_counter_clockwise():
#     new_heading = mike.heading() + 10
#     mike.setheading(new_heading)
#
#
# # turtle turns clockwise
# def turn_clockwise():
#     new_heading = mike.heading() - 10
#     mike.setheading(new_heading)
#
#
# screen.listen()
# screen.onkeypress(key="w", fun=moves_forward)
# screen.onkeypress(key="s", fun=moves_backwards)
# screen.onkeypress(key="c", fun=clear_screen)
# screen.onkeypress(key="a", fun=turn_counter_clockwise)
# screen.onkeypress(key="d", fun=turn_clockwise)
#
# screen.exitonclick()

##########################################################################################
#Turtle Race
import random
from turtle import Turtle, Screen


is_race_on = False
turtle_color = ["blue", "green", "red", "yellow", "orange"]
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Who will win the race? Enter a color: ")
y_axis = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_number in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color[turtle_number])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis[turtle_number])
    new_turtle.pendown()
    new_turtle.speed("fastest")
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {turtle.pencolor()} turtle has won.")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle has won.")
        turtle.penup()        
        turtle.forward(random.randint(0, 6))












# tim1 = Turtle(shape="turtle")
# tim1.color(turtle_color[0])
# tim1.penup()
# tim1.goto(x=-430, y=-330)
# tim2 = Turtle(shape="turtle")
# tim2.color(turtle_color[1])
# tim2.penup()
# tim2.goto(x=-430, y=-315)
# tim3 = Turtle(shape="turtle")
# tim3.color(turtle_color[2])
# tim3.penup()
# tim3.goto(x=-430, y=-300)
# tim4 = Turtle(shape="turtle")
# tim4.color(turtle_color[3])
# tim4.penup()
# tim4.goto(x=-430, y=-285)
# tim5 = Turtle(shape="turtle")
# tim5.color(turtle_color[4])
# tim5.penup()
# tim5.goto(x=-430, y=-270)



screen.exitonclick()
