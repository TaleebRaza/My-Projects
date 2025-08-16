from turtle import Turtle
from random import choice, uniform

class Ball(Turtle):
    def __init__(self, width, height):
        super().__init__("circle")

        self.direction_y = self.direction_x = 0
        self.screen_width, self.screen_height = width, height
        self.initialize_ball()

    def initialize_ball(self):
        self.penup()
        self.color("white")
        self.direction_y, self.direction_x = choice((1, -1)), choice((1, -1))

    def move_ball(self, speed):

        new_x = self.xcor() + self.direction_x * speed
        new_y = self.ycor() + self.direction_y * speed

        self.setposition(new_x, new_y)
        self.check_for_walls()

    def check_for_walls(self):
        if abs(self.xcor()) >= abs(self.screen_width // 2 - 20):
            self.direction_x *= -1
            self.direction_x += uniform(-0.2, 0.2)

            edge_x = (self.screen_width // 2 - 20) * (1 if self.xcor() > 0 else -1)
            self.setx(edge_x)

        if abs(self.ycor()) >= abs(self.screen_height // 2 - 20):
            self.direction_y *= -1
            self.direction_y += uniform(-0.2, 0.2)

            edge_y = (self.screen_width // 2 - 20) * (1 if self.ycor() > 0 else -1)
            self.sety(edge_y)

