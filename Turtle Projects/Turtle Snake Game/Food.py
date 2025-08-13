from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto(100, 100)

    def refresh_position(self, height, width):
        self.goto(randint((-width // 2) + 20, (width // 2) - 20), randint((-height // 2) + 20, (height // 2) - 20))
