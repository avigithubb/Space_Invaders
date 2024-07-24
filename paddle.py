from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, x, y, on_key_right, on_key_left):
        super().__init__()
        self.penup()
        self.shape("square")

        self.shape("images/defender_2.gif")
        self.width = 0.5
        self.len = 0.5
        self.shapesize(stretch_len=self.len, stretch_wid=self.width)

        self.color("white")
        # self.shape("images/invaders.gif")
        self.goto(x=x, y=y)

        Screen().listen()

        Screen().onkey(key=on_key_right, fun=self.move_right)
        Screen().onkey(key=on_key_left, fun=self.move_left)

    def move_right(self):
        self.goto(self.xcor() + 20, -250)

    def move_left(self):
        self.goto(self.xcor() - 20, -250)

