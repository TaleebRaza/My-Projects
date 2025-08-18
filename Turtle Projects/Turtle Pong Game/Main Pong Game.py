from turtle import Screen, Turtle
from Paddle import Paddle
from ScoreBoard import Scoreboard
from Ball import Ball
from time import sleep

# Constants To Use Further
WIDTH, HEIGHT = 800, 800
TURTLE_SPEED = 40
FRAME_DELAY = 0.016
MARGIN = 20

# Below two comments just to help understand direction
# paddle_direction (-1) = Left
# paddle_direction (1) = Right

# Initialize Screen
display = Screen()

# Setup screen size, background color, and disable tracer
display.setup(WIDTH, HEIGHT)
display.bgcolor("black")
display.listen()
display.tracer(0)

# Create paddle, ball, scoreboard objects
paddle_left = Paddle(screen_width=WIDTH, screen_height=HEIGHT, speed=TURTLE_SPEED, gap_from_edges=MARGIN, paddle_direction=-1)
paddle_right = Paddle(screen_width=WIDTH, screen_height=HEIGHT, speed=TURTLE_SPEED, gap_from_edges=MARGIN, paddle_direction=1)

ball = Ball(width=WIDTH, height=HEIGHT)

scoreboard_left = Scoreboard(paddle=-1, gap_from_edges=MARGIN, width=WIDTH, height=HEIGHT)
scoreboard_right = Scoreboard(paddle=1, gap_from_edges=MARGIN, width=WIDTH, height=HEIGHT)

# Setup Controls
display.listen()
display.onkey(fun=paddle_left.move_paddle_up, key="w")
display.onkey(fun=paddle_left.move_paddle_down, key="s")
display.onkey(fun=paddle_right.move_paddle_up, key="Up")
display.onkey(fun=paddle_right.move_paddle_down, key="Down")

def user_information():
    # helper turtle
    helping_text = Turtle()
    helping_text.hideturtle()
    helping_text.color("white")
    helping_text.penup()
    helping_text.goto(0, helping_text.ycor() + 50)

    # inform user
    helping_text.write(arg="W/S for left paddle, ↑/↓ for right paddle", align="center",)
    display.update()
    sleep(2)
    helping_text.undo()

    helping_text.write(arg="The Game Will Begin in Two Seconds", align="center")
    display.update()
    sleep(2)
    helping_text.undo()

# main game loop
def main():
    game_running = True
    ball_speed = 5

    user_information()


    while game_running:

        display.update()
        sleep(FRAME_DELAY)
        wall_hit = ball.move_ball(speed=ball_speed, left_paddle=paddle_left, right_paddle=paddle_right)

        # checking which wall the ball hit
        if wall_hit is not None:
            if wall_hit == "left":
                scoreboard_right.increase_score()
            elif wall_hit == "right":
                scoreboard_left.increase_score()
            ball.ball_refresh()
            display.update()
            sleep(1)

main()

display.exitonclick()