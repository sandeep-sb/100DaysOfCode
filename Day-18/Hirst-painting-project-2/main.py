# import colorgram
#
# rgb_color_list = []
#
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color_tuple = (r, g, b)
#     rgb_color_list.append(new_color_tuple)
#
# print(rgb_color_list)

# Hirst Painting Project-----Part 2
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184),
              (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
              (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

ralph = Turtle()
ralph.speed("fastest")
ralph.hideturtle()
ralph.penup()
ralph.setx(-250)
ralph.sety(-250)
num_of_dots = 100
for dots in range(1, num_of_dots + 1):
    ralph.setheading(0)
    ralph.pendown()
    ralph.color(random.choice(color_list))
    ralph.dot(20)
    ralph.penup()
    ralph.forward(50)
    if dots % 10 == 0:
        ralph.setheading(90)
        ralph.forward(50)
        ralph.setheading(180)
        ralph.forward(500)









    # My IMPLEMENTATION

    # if row % 2 == 0:
    #     for column in range(10):
    #         ralph.pendown()
    #         ralph.dot(20, random.choice(color_list))
    #         ralph.penup()
    #         ralph.forward(50)
    #     ralph.backward(50)
    #     ralph.setheading(90)
    #     ralph.penup()
    #     ralph.forward(50)
    #     ralph.setheading(180)
    # else:
    #     for column in range(10):
    #         ralph.pendown()
    #         ralph.dot(20, random.choice(color_list))
    #         ralph.penup()
    #         ralph.forward(50)
    #     ralph.backward(50)
    #     ralph.setheading(90)
    #     ralph.penup()
    #     ralph.forward(50)
    #     ralph.setheading(0)

screen = Screen()
screen.exitonclick()