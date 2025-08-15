from turtle import Screen
from Snake import Snake
from time import sleep
from Food import Food
from Scoreboard import Scoreboard

TURTLE_SPEED = 20
WIDTH, HEIGHT = 800, 800

# Initialize the game screen
display = Screen()
display.bgcolor("Black")
display.title("Snake Game")
display.setup(width=WIDTH, height=HEIGHT)
display.tracer(0)

# Create game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard(height=HEIGHT, width=WIDTH)

# Bind keyboard controls
display.listen()
display.onkey(snake.up, "Up")
display.onkey(snake.down, "Down")
display.onkey(snake.left, "Left")
display.onkey(snake.right, "Right")

# Game loop
running = True
while running:
    """
    Main game loop:
    - Updates screen and moves snake
    - Detects collisions with food, wall, and self
    - Ends game on collision events
    """
    display.update()
    sleep(0.1)
    snake.move(TURTLE_SPEED)

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh_position(HEIGHT, WIDTH)
        snake.increase_length()
        scoreboard.increase_score()

    # Detect collision with wall
    if (
        snake.snake_head.xcor() >= WIDTH // 2
        or snake.snake_head.xcor() <= -WIDTH // 2
        or snake.snake_head.ycor() >= HEIGHT // 2
        or snake.snake_head.ycor() <= -HEIGHT // 2
    ):
        running = False
        scoreboard.game_over("Game Over - Collided With Wall")

    # Detect collision with tail
    if snake.detect_tail():
        running = False
        scoreboard.game_over("Game Over - Collided With Body")

# Wait for user to click before closing
display.exitonclick()
