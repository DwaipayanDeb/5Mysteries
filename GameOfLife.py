import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define grid size
grid_size = 50

# Create initial random grid
grid = np.random.choice([0, 1], size=(grid_size, grid_size))

# Define rules for cell survival, death, and birth
def update_grid(grid):
    new_grid = grid.copy()
    for i in range(grid_size):
        for j in range(grid_size):
            # Count the number of live neighbors for each cell
            neighbors = np.sum(grid[max(0, i-1):min(grid_size, i+2), max(0, j-1):min(grid_size, j+2)]) - grid[i, j]
            # Apply rules
            if grid[i, j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i, j] = 0  # Cell dies due to underpopulation or overcrowding
            elif neighbors == 3:
                new_grid[i, j] = 1  # Cell is born due to reproduction
    return new_grid

# Function to update the grid for each generation
def update(frameNum, img, grid):
    new_grid = update_grid(grid)
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img

# Create animation
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='Greys')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid), frames=100, interval=50, save_count=50)

plt.show()
