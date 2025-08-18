from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 10, "bold")

class Scoreboard(Turtle):
    def __init__(self, paddle: int, gap_from_edges, height, width):
        super().__init__()

        self.screen_height, self.screen_width = height, width
        self.score = 0
        self.initialize_score(gap_from_edges, paddle)

    def initialize_score(self, gap_from_edges, paddle):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(paddle * 20, self.screen_height // 2 - gap_from_edges)
        self.write(f"- 0 -", align=ALIGN, font=FONT)

    def increase_score(self):
        self.undo()
        # super().clear()
        self.score += 1
        self.change_color()
        self.write(f"- {self.score} -", align=ALIGN, font=FONT)

    def change_color(self):
        if self.score <= 10:
            self.color("red")
        elif 10 < self.score <= 30:
            self.color("green")
        else:
            self.color("yellow")
