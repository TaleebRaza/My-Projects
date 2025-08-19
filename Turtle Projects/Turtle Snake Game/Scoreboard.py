from turtle import Turtle

# Constants for text formatting
ALIGN = "center"
FONT = ("courier", 15, "normal")

class Scoreboard(Turtle):
    """
    Displays and updates the score in the Snake game.

    Inherits:
        Turtle: Used to draw text on the game screen.
    """

    def __init__(self, height):
        """
        Initialize the scoreboard at the top center of the screen.

        Args:
            height (int): Height of the game screen in pixels.
        """
        super().__init__()
        self.score = 0
        self.high_score = self.initialize_high_score()  # Load saved high score (or 0 if not available)
        self.color("white")
        self.hideturtle()  # Hide the turtle icon, only use text
        self.penup()
        # Place scoreboard near the top of the game window
        self.goto(0, height // 2 - 30)
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def create_or_set_high_score(self):
        """
        Save the current high score to a file.
        Overwrites the file each time this method is called.
        """
        with open("Your Text File Name.txt", mode="w") as file:
            file.write(str(self.high_score))

    def initialize_high_score(self):
        """
        Load the high score from file.

        Returns:
            int: The stored high score if the file exists and is valid,
                 otherwise 0 if the file is missing or invalid.
        """
        try:
            with open("Your Text File Name.txt", mode="r") as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0

    def update_board(self, height = None, alt_text = None):
        """
        Update the scoreboard display.

        Args:
            height (int, optional): Height of the screen (unused unless alt_text provided).
            alt_text (str, optional): Custom message to display instead of the score.
                                      Useful for showing "Game Over" messages.
        """
        self.clear()  # Remove previous text
        if alt_text is None and height is None:
            # Normal scoreboard update (show score + high score)
            self.write(arg=f"Score: {self.score}  -  High Score = {self.high_score}",
                       align=ALIGN, font=FONT)
        else:
            # Custom message (e.g., "Game Over")
            self.write(arg=alt_text, align=ALIGN, font=FONT)

    def reset_game(self):
        """
        Reset the game state:
        - Save new high score if the player beat the old one.
        - Reset the current score to 0.
        """
        if self.score > self.high_score:
            self.high_score = self.score
            self.create_or_set_high_score()  # Save updated high score to file

        self.score = 0  # Reset current score

    def increase_score(self):
        """
        Increase the player's score by 1 and refresh the scoreboard display.
        """
        self.score += 1
        self.update_board()
