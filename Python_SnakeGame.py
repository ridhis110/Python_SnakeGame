import pygame
import random

'''pygame: Used for creating the game window, handling input, and drawing graphics.
random: Used to generate random positions for the apple.'
'''

# Initialize pygame
pygame.init()

# Screen dimensions
"""WIDTH, HEIGHT: Define the size of the game window.
CELL_SIZE: Determines how big each snake segment and apple will be.
"""
WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20  # Size of snake and apple blocks

# Colors
"""Colors are defined in RGB format (Red, Green, Blue).
BLACK is used as the background color.
GREEN is the snake's color.
RED is the apple’s color.
WHITE is used for text.
"""
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Initialize screen
"""pygame.display.set_mode((WIDTH, HEIGHT)): Creates a 500x500 pixel window.
pygame.display.set_caption(): Sets the title of the game window."""

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake and Apple Game")

# Snake initial position and direction
"""The snake is a list of (x, y) coordinates.
The first element snake[0] represents the head of the snake.
snake_dir stores the direction in which the snake moves:
(CELL_SIZE, 0) → Right
(-CELL_SIZE, 0) ← Left
(0, CELL_SIZE) ↓ Down
(0, -CELL_SIZE) ↑ Up"""

snake = [(100, 100), (90, 100), (80, 100)]  # Snake body (list of tuples)
snake_dir = (CELL_SIZE, 0)  # Moving right initially

# Apple initial position
"""The apple's position is chosen randomly within the grid.
It ensures the apple aligns perfectly with the snake's movement grid."""

apple = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
         random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

# Game variables
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font(None, 36)

# Game loop

running = True
while running:
    """running = True: This variable keeps the game running.
while running:: Starts an infinite loop to continuously update the game."""
    screen.fill(BLACK)  # Clear screen screen. 
    """fill(BLACK): Fills the screen with black before drawing anything.
Why? This prevents old frames from leaving trails and ensures a fresh display."""

    # Event handling (keyboard inputs)
    for event in pygame.event.get(): #pygame.event.get(): Retrieves all events (like key presses, closing the window, etc.).The loop goes through each event one by one.
        if event.type == pygame.QUIT: #pygame.QUIT: This happens when the user clicks the close button (X) on the game window
            running = False
        elif event.type == pygame.KEYDOWN: #pygame.KEYDOWN: Detects when a key is pressed down
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                snake_dir = (0, -CELL_SIZE)
                """pygame.K_UP: Checks if the Up Arrow key is pressed.
snake_dir != (0, CELL_SIZE): Prevents moving up if the snake is already moving down.
snake_dir = (0, -CELL_SIZE): Moves the snake up (negative y-direction)."""
            elif event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                snake_dir = (0, CELL_SIZE)
                """pygame.K_DOWN: Checks if the Down Arrow key is pressed.
snake_dir != (0, -CELL_SIZE): Prevents moving down if the snake is already moving up.
snake_dir = (0, CELL_SIZE): Moves the snake down (positive y-direction)."""
            elif event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                snake_dir = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                snake_dir = (CELL_SIZE, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)  # Add new head
    """snake[0]: Gets the current head position (e.g., (100, 100)).
snake_dir[0]: Represents movement in the X direction (horizontal).
snake_dir[1]: Represents movement in the Y direction (vertical).
The new head is created by adding the direction values to the current head’s coordinates:

snake[0][0] + snake_dir[0]: Updates the X-coordinate.
snake[0][1] + snake_dir[1]: Updates the Y-coordinate."""

    # Check for collision with apple
    if new_head == apple:
        score += 1
        apple = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                 random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
    else:
        snake.pop()  # Remove last part of snake to maintain length

    # Check for collisions (wall or itself)
    if (new_head[0] < 0 or new_head[0] >= WIDTH or 
        new_head[1] < 0 or new_head[1] >= HEIGHT or 
        new_head in snake[1:]):
        running = False  # End game

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # Draw apple
    pygame.draw.rect(screen, RED, (apple[0], apple[1], CELL_SIZE, CELL_SIZE))

    # Display score
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    # Update display and control speed
    pygame.display.flip()
    clock.tick(10)  # Limit FPS to 10

pygame.quit()
print(f"Game Over! Final Score: {score}")
