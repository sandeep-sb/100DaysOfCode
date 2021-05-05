from turtle import Turtle
FONT = ("Courier", 20, "normal")
ALIGN = "center"


# Scoreboard class for the creation and display of scorecard.
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # Creation of scoreboard
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    # Updates the scoreboard after each miss from either player
    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(f"Score = {self.l_score}", align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(f"Score = {self.r_score}", align=ALIGN, font=FONT)

    # Increases the points of left player by 1.
    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    # Increases the points of right player by 1.
    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    # Displays the winner after one player crosses 5 point mark.
    def game_over(self):
        self.clear()
        if self.l_score > self.r_score:
            self.write("Game Over. Player A won", align=ALIGN, font=FONT)
        else:
            self.write("Game Over. Player B won", align=ALIGN, font=FONT)
