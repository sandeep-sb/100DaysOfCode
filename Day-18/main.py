import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
# timmy.color("red")
# timmy.shape("turtle")
# for _ in range(10):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)


# Turtle draws shapes


# color = ["spring green", "hot pink", "dark red", "medium violet red", "dark violet", "tomato", "dodger blue",
#          "gold2", "IndianRed2", "LightSeaGreen", "magenta", "MidnightBlue", "purple", "burlywood4"]

# def draw_turtle_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# num_sides = 3
# for shape_side_num in range(3, 11):
#     timmy.pencolor(random.choice(color))
#     draw_turtle_shapes(shape_side_num)

# Move turtle randomly generating random colors from the list.

# color = ["spring green", "hot pink", "dark red", "medium violet red", "dark violet", "tomato", "dodger blue",
#          "gold2", "IndianRed2", "LightSeaGreen", "magenta", "MidnightBlue", "purple", "burlywood4"]
# distance = 20
# direction_list = [0, 90, 180, 270]
# timmy.pensize(10)
#
# timmy.speed("fastest")
# def move_timmy():
#     timmy.color(random.choice(color))
#     timmy.setheading(random.choice(direction_list))
#     timmy.forward(50)
#
#
# for _ in range(100):
#     move_timmy()

# Move turtle randomly generating random colors from turtle library.

distance = 20
direction_list = [0, 90, 180, 270]
timmy.pensize(10)
timmy.speed("fastest")

turtle.colormode(255)


def create_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def move_timmy():
    timmy.color(create_color())
    timmy.setheading(random.choice(direction_list))
    timmy.forward(50)


for _ in range(100):
    move_timmy()

screen = Screen()
screen.exitonclick()
