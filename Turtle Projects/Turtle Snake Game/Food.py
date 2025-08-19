from turtle import Turtle
import random


class Food(Turtle):
    """
    Represents the food object in the Snake game.
    Inherits from Turtle to use shapes and coordinates easily.

    Responsibilities:
    - Appear as a small colored dot
    - Randomly relocate on the screen when eaten
    """

    def __init__(self):
        """
        Initialize the food object:
        - Shape: circle
        - Color: blue
        - Size: scaled down (0.5 x 0.5)
        - No pen trail
        - Spawn at a random position initially
        """
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make it smaller
        self.penup()
        self.speed("fastest")
        self.refresh_position(800, 800)  # Default screen size

    def refresh_position(self, height, width):
        """
        Move the food to a random position within screen bounds.
        Ensures food does not appear outside the playable area.

        Args:
            height (int): Height of the game window
            width (int): Width of the game window
        """
        # Generate random x, y positions within boundaries
        rand_x = random.randint(-width // 2 + 20, width // 2 - 20)
        rand_y = random.randint(-height // 2 + 20, height // 2 - 20)
        self.goto(rand_x, rand_y)
