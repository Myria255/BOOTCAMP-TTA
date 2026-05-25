#Conway’s Game of Life

class Conway():
    def __init__(self, grid):
        self.grid = grid

    def next_generation(self):
        new_grid = [[0 for _ in range(len(self.grid[0]))] for _ in range(len(self.grid))]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                neighbors = self.count_neighbors(i, j)
                if self.grid[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_grid[i][j] = 0
                    else:
                        new_grid[i][j] = 1
                else:
                    if neighbors == 3:
                        new_grid[i][j] = 1
        self.grid = new_grid

    def count_neighbors(self, i, j):
        count = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < len(self.grid) and 0 <= nj < len(self.grid[0]):
                    count += self.grid[ni][nj]
        return count
    
    def get_grid(self):
        return self.grid
# Example usage
initial_grid = [    [0, 1, 0],
                [0, 0, 1],
                [            1, 1, 1]]
conway = Conway(initial_grid)
print("Initial Grid:")
for row in conway.get_grid():
    print(row)
for _ in range(5):
    conway.next_generation()
print("\nNext Generation:")
for row in conway.get_grid():
    print(row)
    
#Representation du jeu

try:
    import pygame
except ImportError:
    pygame = None

import random  
import time

if pygame is not None:
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")
    CELL_SIZE = 10
    GRID_WIDTH = WIDTH // CELL_SIZE 
    GRID_HEIGHT = HEIGHT // CELL_SIZE

    def create_grid():
        return [[random.choice([0, 1]) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    def draw_grid(grid):
        for i in range(GRID_HEIGHT):
            for j in range(GRID_WIDTH):
                color = (255, 255, 255) if grid[i][j] == 1 else (0, 0, 0)
                pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def count_neighbors(grid, i, j):
        count = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < GRID_HEIGHT and 0 <= nj < GRID_WIDTH:
                    count += grid[ni][nj]
        return count

    def next_generation(grid):
        new_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        for i in range(GRID_HEIGHT):
            for j in range(GRID_WIDTH):
                neighbors = count_neighbors(grid, i, j)
                if grid[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_grid[i][j] = 0
                    else:
                        new_grid[i][j] = 1
                else:
                    if neighbors == 3:
                        new_grid[i][j] = 1
        return new_grid

    grid = create_grid()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_grid(grid)
        pygame.display.flip()
        grid = next_generation(grid)
        time.sleep(0.1)
    pygame.quit()
else:
    print("pygame is not installed; skipping graphical simulation.")
