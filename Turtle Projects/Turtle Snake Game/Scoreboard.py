from turtle import Turtle

ALIGN = "center"
FONT = ("courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self, height, width):
        super().__init__()

        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, height//2 - 30)
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self, text):
        self.home()
        self.write(arg=text, align=ALIGN, font=("courier", 25, "bold"))
