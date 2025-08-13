from turtle import Screen
from Snake import Snake
from time import sleep
from Food import Food
from Scoreboard import Scoreboard

TURTLE_SPEED = 20
WIDTH, HEIGHT = 800, 800

display = Screen()
display.bgcolor("Black")
display.title("Snake Game")
display.setup(width=WIDTH, height=HEIGHT)

display.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard(height=HEIGHT, width=WIDTH)

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

    # Detecting collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh_position(HEIGHT, WIDTH)
        snake.increase_length()
        scoreboard.increase_score()

    if snake.snake_head.xcor() >= WIDTH//2 or snake.snake_head.xcor() <= -WIDTH//2 or snake.snake_head.ycor() >= HEIGHT//2 or snake.snake_head.ycor() <= -HEIGHT//2:
        running = False
        scoreboard.game_over("Game Over - Collided With Wall")

    if snake.detect_tail():
        running = False
        scoreboard.game_over("Game Over - Collided With Body")



display.exitonclick()