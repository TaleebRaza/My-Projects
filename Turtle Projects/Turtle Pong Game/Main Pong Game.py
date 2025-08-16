import time
from turtle import Screen
from Paddle import Paddle
from ScoreBoard import Scoreboard
from Ball import Ball
from time import sleep

WIDTH, HEIGHT = 800, 800
TURTLE_SPEED = 40
BALL_SPEED = 10
FRAME_DELAY = 0.016
MARGIN = 10

# paddle_direction (-1) = Left
# paddle_direction (1) = Right

display = Screen()

display.setup(WIDTH, HEIGHT)
display.bgcolor("black")
display.listen()
display.tracer(0)


paddle_left = Paddle(screen_width=WIDTH, screen_height=HEIGHT, speed=TURTLE_SPEED, gap_from_edges=MARGIN, paddle_direction=-1)
paddle_right = Paddle(screen_width=WIDTH, screen_height=HEIGHT, speed=TURTLE_SPEED, gap_from_edges=MARGIN, paddle_direction=1)



display.onkey(fun=paddle_right.move_paddle_up, key="Up")
display.onkey(fun=paddle_right.move_paddle_down, key="Down")
display.onkey(fun=paddle_left.move_paddle_up, key="w")
display.onkey(fun=paddle_left.move_paddle_down, key="s")

score_left = 0
score_right = 0

scoreboard_left = Scoreboard(paddle=-1, gap_from_edges=MARGIN * 2, height=HEIGHT, width=WIDTH, score=score_left)
scoreboard_right = Scoreboard(paddle=1, gap_from_edges=MARGIN * 2, height=HEIGHT, width=WIDTH, score=score_right)


ball = Ball(WIDTH, HEIGHT)
display.update()




display.exitonclick()