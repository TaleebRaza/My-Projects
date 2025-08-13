from turtle import Turtle, Screen
from Snake import Snake
from time import sleep

TURTLE_SPEED = 20

display = Screen()
display.bgcolor("Black")
display.title("Snake Game")

display.tracer(0)

snake = Snake()

display.listen()
display.onkey(snake.up, "Up")
display.onkey(snake.down, "Down")
display.onkey(snake.left, "Left")
display.onkey(snake.right, "Right")


running = True
while running:
    display.update()
    sleep(0.1)
    snake.move(TURTLE_SPEED)



display.exitonclick()