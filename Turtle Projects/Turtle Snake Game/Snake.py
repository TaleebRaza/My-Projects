from turtle import Turtle


class Snake:
    """
    Represents the snake in a classic snake game.

    Responsibilities:
    - Create and initialize the snake with multiple segments
    - Move the snake forward
    - Handle direction changes (up, down, left, right)
    - Detect collisions with its own tail
    - Grow when food is eaten
    - Reset when the game restarts
    """

    def __init__(self):
        """
        Initialize the snake object.
        - Starts with 3 segments
        - Sets the head as the first segment
        """
        self.snake_segments = None
        self.snake_head = None
        self.create_snake()

    def create_snake(self):
        """
        Create the initial snake with 3 square segments.
        The head is marked in red.
        """
        self.snake_segments = [Turtle("square") for _ in range(3)]
        self.snake_head = self.snake_segments[0]
        self.initialize_snake()
        self.snake_head.color("red", "red")  # Head is red for visibility

    def initialize_snake(self):
        """
        Position the initial snake segments in a horizontal line.
        Each segment:
        - Has no pen trail
        - Is white
        - Is scaled down (0.5 x 0.5)
        - Starts at coordinates (0, 0), (1, 0), (2, 0)
        """
        for x, segment in enumerate(self.snake_segments):
            segment.penup()
            segment.color("white")
            segment.shapesize(stretch_wid=0.5, stretch_len=0.5)
            segment.goto(x, 0)

    def move(self, steps):
        """
        Move the snake forward by a given number of steps.
        Each segment follows the previous one.

        Args:
            steps (int): Number of pixels the snake moves forward.
        """
        # Move each segment to the position of the segment ahead of it
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment - 1].xcor()
            new_y = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto(new_x, new_y)

        # Move the head forward
        self.snake_head.forward(steps)

    def detect_tail(self):
        """
        Check if the snake's head has collided with its own tail.

        Returns:
            bool: True if the head is closer than 5 pixels to any body segment.
        """
        for segment in self.snake_segments[1:]:  # Skip the head
            if self.snake_head.distance(segment) < 5:
                return True
        return False

    # ---------------- Direction Controls ----------------
    def up(self):
        """Turn snake 'up' (90°) unless currently going 'down'."""
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        """Turn snake 'down' (270°) unless currently going 'up'."""
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def left(self):
        """Turn snake 'left' (180°) unless currently going 'right'."""
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def right(self):
        """Turn snake 'right' (0°) unless currently going 'left'."""
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    # ---------------- Growth ----------------
    def increase_length(self):
        """
        Add a new segment to the snake.
        The new segment spawns at the position of the last segment.
        """
        self.snake_segments.append(Turtle("square"))
        self.snake_segments[-1].color("white")
        self.snake_segments[-1].shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.snake_segments[-1].penup()
        self.snake_segments[-1].goto(
            self.snake_segments[-2].xcor(),
            self.snake_segments[-2].ycor()
        )

    # ---------------- Reset ----------------
    def reset_snake(self):
        """
        Reset the snake for a new game:
        - Hide old segments
        - Clear segment list
        - Recreate a new snake with 3 segments
        """
        for segment in self.snake_segments:
            segment.hideturtle()  # Hide existing body parts
        self.snake_segments.clear()
        self.create_snake()
