import turtle
import random
from turtle import Turtle, Screen

timmy = Turtle()
# timmy.color("red")
timmy.shape("turtle")
# for _ in range(10):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)


color = ["spring green", "hot pink", "dark red", "medium violet red", "dark violet", "tomato", "dodger blue"]


def draw_turtle_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


num_sides = 3
for shape_side_num in range(3, 11):
    timmy.pencolor(random.choice(color))
    draw_turtle_shapes(shape_side_num)

screen = Screen()
screen.exitonclick()
