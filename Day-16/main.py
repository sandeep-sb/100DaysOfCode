# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.home()
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.speed("fastest")
# counter = 0
# for item in range(1,301):
#     timmy.circle(counter)
#     timmy.right(90)
#     counter += 1
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",
                 ["Pikachu", "Squirtle", "Charminder"]
                 )
table.add_column("Pokemom Type",
                 ["Electric", "Water", "Fire"]
                 )
table.align = "l"
print(table)