from turtle import Turtle

class Snake:
    """
    Represents the snake in a classic snake game.
    Handles snake creation, movement, direction changes, growth,
    and collision detection with its own tail.
    """

    def __init__(self):
        """
        Initialize the snake with 3 segments and set up the head.
        """
        self.snake_segments = [Turtle("square") for _ in range(3)]
        self.snake_head = self.snake_segments[0]
        self.initialize_snake()
        self.snake_head.color("red", "red")

    def initialize_snake(self):
        """
        Position the initial snake segments in a horizontal line.
        Each segment is set up with the desired shape, size, and color.
        """
        for x, segment in enumerate(self.snake_segments):
            segment.penup()
            segment.color("white")
            segment.shapesize(stretch_wid=0.5, stretch_len=0.5)
            segment.goto(x, 0)

    def move(self, steps):
        """
        Move the snake forward by a given number of steps.

        Args:
            steps (int): Number of pixels to move forward.
        """
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment - 1].xcor()
            new_y = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto(new_x, new_y)
        self.snake_head.forward(steps)

    def detect_tail(self):
        """
        Check if the snake's head has collided with its own tail.

        Returns:
            bool: True if collision detected, False otherwise.
        """
        for segment in self.snake_segments[1:]:
            if self.snake_head.distance(segment) < 5:
                return True
        return False

    def up(self):
        """
        Change the snake's direction to 'up' unless it's currently moving down.
        """
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        """
        Change the snake's direction to 'down' unless it's currently moving up.
        """
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def left(self):
        """
        Change the snake's direction to 'left' unless it's currently moving right.
        """
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def right(self):
        """
        Change the snake's direction to 'right' unless it's currently moving left.
        """
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def increase_length(self):
        """
        Add a new segment to the snake at the position of the last segment.
        """
        self.snake_segments.append(Turtle("square"))
        self.snake_segments[-1].color("white")
        self.snake_segments[-1].shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.snake_segments[-1].penup()
        self.snake_segments[-1].goto(
            self.snake_segments[-2].xcor(),
            self.snake_segments[-2].ycor()
        )
