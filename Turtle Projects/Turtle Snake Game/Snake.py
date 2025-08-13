from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake_segments = [Turtle("square") for _ in range(3)]
        self.snake_head = self.snake_segments[0]
        self.initialize_snake()
        self.snake_head.color("red", "red")


    def initialize_snake(self):
        for x, segment in enumerate(self.snake_segments):
            segment.penup()
            segment.color("white")
            segment.shapesize(stretch_wid=0.5, stretch_len=0.5)

            segment.goto(x, 0)

    def move(self, steps):
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment - 1].xcor()
            new_y = self.snake_segments[segment - 1].ycor()

            self.snake_segments[segment].goto(new_x, new_y)
        self.snake_head.forward(steps)

    def detect_tail(self):
        for segment in self.snake_segments[1:]:
            if self.snake_head.distance(segment) < 5:
                return True
        return False

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def increase_length(self):
        self.snake_segments.append(Turtle("square"))
        self.snake_segments[-1].color("white")
        self.snake_segments[-1].shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.snake_segments[-1].penup()
        self.snake_segments[-1].goto(self.snake_segments[-2].xcor(), self.snake_segments[-2].ycor())
