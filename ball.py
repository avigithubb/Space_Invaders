from turtle import Turtle, Screen


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.plus = 1
        self.shape("circle")
        self.color("#88D66C")
        self.speed(self.plus)

        self.shapesize(stretch_wid=0.6, stretch_len=0.2)
        self.penup()
        self.goto(0, -230)
        self.new_y = 10
        self.new_x = 0
        # self.move()

    def move(self):
        new_x = self.xcor() + 0
        new_y = self.ycor() + self.new_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.new_y *= -1

