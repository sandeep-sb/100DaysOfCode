from turtle import Turtle

SPEED = "fastest"
SHAPE = "square"
COLOR = "white"


# Paddle class for the creation of left and right paddles.
class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        # Creation of paddle with specifications
        self.shape(SHAPE)
        self.speed(SPEED)
        self.penup()
        self.setposition(pos)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color(COLOR)

    # Moves the paddle upwards by 20 pixels
    def move_up(self):
        if self.ycor() < 240:
            y_cor = self.ycor()
            self.goto(x=self.xcor(), y=y_cor + 20)

    # Moves the paddle downwards by 20 pixels
    def move_down(self):
        if self.ycor() > -240:
            y_cor = self.ycor()
            self.goto(x=self.xcor(), y=y_cor - 20)
