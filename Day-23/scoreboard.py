from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.create_scoreboard()

    def create_scoreboard(self):
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.goto(x=-180, y=250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.hideturtle()
        self.goto(x=0,y=0)
        self.write("Game Over", align="center", font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_scoreboard()
