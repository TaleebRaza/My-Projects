from turtle import Turtle
from random import randint

class Food(Turtle):
    """
    Represents the food object in a snake game.
    Inherits from the Turtle class and is positioned randomly on the screen.
    """

    def __init__(self):
        """
        Initialize the food object with a small blue circle shape
        and place it at the default starting position.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto(100, 100)

    def refresh_position(self, height, width):
        """
        Move the food to a new random position within the given boundaries.

        Args:
            height (int): Height of the game screen in pixels.
            width (int): Width of the game screen in pixels.
        """
        self.goto(
            randint((-width // 2) + 20, (width // 2) - 20),
            randint((-height // 2) + 20, (height // 2) - 20)
        )
