from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, screen_width, screen_height, speed, gap_from_edges, paddle_direction):
        super().__init__("square")  # shape set here
        self.width = screen_width
        self.height = screen_height
        self.turtle_speed = speed

        self.initialize_paddle(gap_from_edges, paddle_direction)

    def initialize_paddle(self, gap_from_edges, paddle_direction):
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=0.5)
        self.penup()
        self.goto(paddle_direction * (self.width // 2 - gap_from_edges), 0)

    def move_paddle_up(self):
        _, y = self.position()
        self.sety(min(y + self.turtle_speed, self.height // 2 - 10))

    def move_paddle_down(self):
        _, y = self.position()
        self.sety(max(y - self.turtle_speed, -self.height // 2 + 10))

