import pygame
import sys

# Initialize the Sudoku grid (0 represents empty cells)
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 540, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRID_SIZE = WIDTH // 9

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")


# Function to draw the Sudoku grid
def draw_grid():
    for i in range(10):
        thickness = 2 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (i * GRID_SIZE, 0), (i * GRID_SIZE, HEIGHT), thickness)
        pygame.draw.line(screen, BLACK, (0, i * GRID_SIZE), (WIDTH, i * GRID_SIZE), thickness)


# Function to draw the numbers on the grid
def draw_numbers():
    font = pygame.font.Font(None, 36)
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                text = font.render(str(grid[i][j]), True, BLACK)
                text_rect = text.get_rect(center=(j * GRID_SIZE + GRID_SIZE // 2, i * GRID_SIZE + GRID_SIZE // 2))
                screen.blit(text, text_rect)


# Function to check if a number is valid at a given position
def is_valid(row, col, num):
    # Check the row and column
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    # Check the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


# Function to solve the Sudoku puzzle using backtracking
def solve_sudoku():
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(i, j, num):
                        grid[i][j] = num
                        draw_grid()
                        draw_numbers()
                        pygame.display.flip()
                        pygame.time.delay(100)

                        if solve_sudoku():
                            return True

                        grid[i][j] = 0
                        draw_grid()
                        draw_numbers()
                        pygame.display.flip()
                        pygame.time.delay(100)

                return False

    return True


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    draw_grid()
    draw_numbers()

    if not solve_sudoku():
        print("No solution exists!")

    pygame.display.flip()

pygame.quit()
sys.exit()
