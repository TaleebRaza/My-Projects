from turtle import Screen
from Snake import Snake
from time import sleep
from Food import Food
from Scoreboard import Scoreboard

# Constants
TURTLE_SPEED = 20  # Number of pixels the snake moves per step
WIDTH, HEIGHT = 800, 800  # Dimensions of the game window

# -----------------------------
# Initialize the game screen
# -----------------------------
display = Screen()
display.bgcolor("Black")  # Set background color
display.title("Snake Game")  # Set window title
display.setup(width=WIDTH, height=HEIGHT)  # Set window size
display.tracer(0)  # Turn off automatic screen updates (manual updates for smoother animation)

# -----------------------------
# Create game objects
# -----------------------------
snake = Snake()  # The snake player
food = Food()  # The food object
scoreboard = Scoreboard(height=HEIGHT)  # Scoreboard at top of the screen

# -----------------------------
# Bind keyboard controls
# -----------------------------
display.listen()  # Enable listening for keyboard input
display.onkey(snake.up, "Up")     # Move snake up
display.onkey(snake.down, "Down") # Move snake down
display.onkey(snake.left, "Left") # Move snake left
display.onkey(snake.right, "Right") # Move snake right

# -----------------------------
# Main game loop
# -----------------------------
running = True
while running:
    """
    Main game loop:
    - Updates screen and moves snake
    - Detects collisions with food, wall, and self
    - Ends game on collision events
    """
    display.update()  # Refresh the screen
    sleep(0.1)  # Control game speed
    snake.move(TURTLE_SPEED)  # Move the snake forward

    # -----------------------------
    # Detect collision with food
    # -----------------------------
    if snake.snake_head.distance(food) < 15:
        # Snake ate the food
        food.refresh_position(HEIGHT, WIDTH)  # Move food to a new random spot
        snake.increase_length()  # Grow the snake
        scoreboard.increase_score()  # Increase score by 1
        scoreboard.update_board()  # Refresh scoreboard display

    # -----------------------------
    # Detect collision with wall
    # -----------------------------
    if (
        snake.snake_head.xcor() >= WIDTH // 2
        or snake.snake_head.xcor() <= -WIDTH // 2
        or snake.snake_head.ycor() >= HEIGHT // 2
        or snake.snake_head.ycor() <= -HEIGHT // 2
    ):
        # Snake hit a wall
        print("wall")
        scoreboard.reset_game()  # Reset score (and update high score if needed)
        snake.reset_snake()  # Reset snake to starting position
        scoreboard.update_board(height=HEIGHT, alt_text="Game Over - Collided With Wall")

    # -----------------------------
    # Detect collision with tail
    # -----------------------------
    elif snake.detect_tail():
        # Snake hit its own body
        print("tail")
        scoreboard.reset_game()  # Reset score (and update high score if needed)
        snake.reset_snake()  # Reset snake to starting position
        scoreboard.update_board(height=HEIGHT, alt_text="Game Over - Collided With Body")

# -----------------------------
# Wait for user to exit
# -----------------------------
display.exitonclick()  # Keep window open until clicked
