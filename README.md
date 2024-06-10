# Conway's Game of Life Simulation

This simulation uses a cellular automaton called Conway's Game of Life to mimic artificial life in a computer.

## How it Works

1. **Initialization**:
   - Define the size of the grid where the simulation will take place (`grid_size`).
   - Create an initial random grid where cells are either alive (1) or dead (0).

2. **Rules**:
   - The simulation follows simple rules for cell survival, death, and birth:
     - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
     - Any live cell with two or three live neighbors lives on to the next generation.
     - Any live cell with more than three live neighbors dies, as if by overpopulation.
     - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

3. **Updating the Grid**:
   - For each generation, update the grid based on the rules:
     - Count the number of live neighbors for each cell.
     - Apply the rules to determine the next state of each cell.

4. **Animation**:
   - Visualize the grid and its evolution using Matplotlib's animation functionality.
     - The `update` function is called for each frame of the animation, updating the grid and displaying it.
     - The animation continues for a specified number of frames (`frames`) with a specified interval (`interval`).

## Running the Simulation

1. **Setup**:
   - Make sure you have Python installed on your system along with the necessary libraries (`numpy` and `matplotlib`).

2. **Execution**:
   - Copy the provided Python code into a `.py` file and execute it using a Python interpreter.
   - The simulation window will display the evolution of the artificial life based on the rules of Conway's Game of Life.

3. **Customization**:
   - You can adjust parameters such as the grid size, initial conditions, and animation settings to customize the simulation further.

Enjoy exploring the emergent behaviors of artificial life in this simulation!
