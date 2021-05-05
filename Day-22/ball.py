from turtle import Turtle

SIZE = 20
COLOR = "white"


# Ball class for the creation of pong ball.
class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        # Creation of ball with specifications
        self.shape("circle")
        self.fillcolor(COLOR)
        self.penup()
        self.x_cor = 10
        self.y_cor = 10

    # Moves the ball
    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)

    # Deflects the ball if collided with uppper or lower walls.
    def bounce_y(self):
        self.y_cor *= -1

    # Deflects the ball if it collides with either of the two paddles
    def bounce_x(self):
        self.x_cor *= -1

    # Resets the ball to its original position and changes its direction for the new chance.
    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
