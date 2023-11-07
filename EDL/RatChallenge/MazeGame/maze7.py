import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Solver")

def read_maze(filename):
    # Reads a maze from a file.
    with open(filename, "r") as f:
        maze = []
        for line in f:
            maze.append(list(line.strip()))  # Use a list to represent each row

    return maze

def mark_visited(maze, row, col):
    # Marks a cell as visited.
    maze[row][col] = "."

def draw_maze(maze, cell_size):
    # Draws the maze on the screen.
    for row, row_data in enumerate(maze):
        for col, char in enumerate(row_data):
            if char == "1":
                # Draw a wall
                pygame.draw.rect(
                    screen, BLACK, (col * cell_size, row * cell_size, cell_size, cell_size)
                )
            elif char == "c":
                # Draw the exit
                pygame.draw.rect(
                    screen, GREEN, (col * cell_size, row * cell_size, cell_size, cell_size)
                )
            elif char == "m":
                # Draw the rat
                pygame.draw.rect(
                    screen, RED, (col * cell_size, row * cell_size, cell_size, cell_size)
                )
            elif char == ".":
                # Draw a visited cell
                pygame.draw.rect(
                    screen, WHITE, (col * cell_size, row * cell_size, cell_size, cell_size)
                )
            else:
                # Draw an empty cell
                pygame.draw.rect(
                    screen, WHITE, (col * cell_size, row * cell_size, cell_size, cell_size)
                )

def get_neighbors(maze, row, col):
    neighbors = []

    # Right neighbor
    if col + 1 < len(maze[0]):
        neighbors.append((row, col + 1))
    # Left neighbor
    if col - 1 >= 0:
        neighbors.append((row, col - 1))
    # Down neighbor
    if row + 1 < len(maze):
        neighbors.append((row + 1, col))
    # Up neighbor
    if row - 1 >= 0:
        neighbors.append((row - 1, col))

    return neighbors

def solve_maze(maze):
    start = None
    cheese = None

    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == "m":
                start = (row, col)
            if maze[row][col] == "c":
                cheese = (row, col)

    if start and cheese:
        queue = [(start, [])]
        visited = set()

        while queue:
            (row, col), path = queue.pop(0)
            cell_value = maze[row][col]

            if cell_value == "c":
                for r, c in path:
                    mark_visited(maze, r, c)
                return True

            if (row, col) in visited:
                continue

            visited.add((row, col))

            # Check neighbors
            neighbors = get_neighbors(maze, row, col)

            for (n_row, n_col) in neighbors:
                n_value = maze[n_row][n_col]

                if n_value == "0" or n_value == "c":
                    new_path = path + [(row, col)]
                    queue.append(((n_row, n_col), new_path))

    return False

cell_size = 20
running = True
clock = pygame.time.Clock()  # Create a clock object

maze = read_maze("maze.txt")  # Read the maze from a file

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Exit when the ESC key is pressed
                running = False

    draw_maze(maze, cell_size)

    if not solve_maze(maze):
        print("No solution found")
        running = False

    pygame.display.flip()
    clock.tick(0.1)  # Limit the frame rate to 1 FPS (1 step per second)

pygame.quit()
