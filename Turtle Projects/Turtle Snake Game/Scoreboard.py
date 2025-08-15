from turtle import Turtle

ALIGN = "center"
FONT = ("courier", 15, "normal")

class Scoreboard(Turtle):
    """
    Displays and updates the score in the snake game.
    Inherits from the Turtle class for easy text drawing.
    """

    def __init__(self, height, width):
        """
        Initialize the scoreboard at the top center of the screen.

        Args:
            height (int): Height of the game screen in pixels.
            width (int): Width of the game screen in pixels.
                         (Currently unused but kept for potential future positioning logic.)
        """
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, height // 2 - 30)
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        """
        Increase the score by 1 and update the display.
        """
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self, text):
        """
        Display a game-over message in the center of the screen.

        Args:
            text (str): The message to display (e.g., 'GAME OVER').
        """
        self.home()
        self.write(arg=text, align=ALIGN, font=("courier", 25, "bold"))
