from turtle import Turtle
from random import uniform, choice

class Ball(Turtle):
    def __init__(self, width, height):
        super().__init__("circle")

        self.direction_y = self.direction_x = 0
        self.screen_width, self.screen_height = width, height
        self.initialize_ball()

    def initialize_ball(self):
        self.penup()
        self.color("white")
        self.direction_y, self.direction_x = 0, choice((1, -1))

    def move_ball(self, speed, left_paddle, right_paddle):

        new_x = self.xcor() + self.direction_x * speed
        new_y = self.ycor() + self.direction_y * speed

        self.setposition(new_x, new_y)

        return self.check_for_collisions(left_paddle, right_paddle)

    def check_for_collisions(self, left_paddle, right_paddle):
        if self.xcor() >= self.screen_width // 2 - 15:
            return "left"
        elif self.xcor() <= (self.screen_width * -1) // 2 + 15:
            return "right"

        if abs(self.ycor()) >= abs(self.screen_height // 2 - 20):
            self.direction_y *= -1
            self.direction_y += uniform(-0.2, 0.2)

            edge_y = (self.screen_height // 2 - 20) * (1 if self.ycor() > 0 else -1)
            self.sety(edge_y)

        if ((self.xcor() < (-self.screen_width) // 2 + 40) and (left_paddle.ycor() - 40 < self.ycor() < left_paddle.ycor() + 40)) or ((self.xcor() > self.screen_width // 2 - 40) and (right_paddle.ycor() - 40 < self.ycor() < right_paddle.ycor() + 40)):
            self.direction_x *= -1
            self.direction_x += uniform(-0.2, 0.2)

        return None

    def ball_refresh(self):
        self.home()
        self.direction_y, self.direction_x = choice((1, -1)), choice((1, -1))
