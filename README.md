*This project has been created as part of the 42 curriculum by nakhatoo and bandrade.*

# A-Maze-ing

# DESCRIPTION

A-Maze-ing is a Python application that generates random mazes from a configuration file. It supports both perfect mazes and Pac-Man style mazes, computes the shortest path between two points, exports the maze using hexadecimal wall encoding, and provides an ASCII visualization in the terminal.

## Features

- Generates perfect and non-perfect mazes
- Uses Iterative Backtracking (DFS)
- Computes the shortest path with BFS
- Exports hexadecimal maze files
- Supports configuration files
- Renders the maze in ASCII
- Validates output with the provided analyzer


# INSTRUCTIONS

## Requirements

- Python 3.10 or later

## Running the Application

```bash
python3 a_maze_ing.py config.txt
```

Replace `config.txt` with any valid configuration file.



## Configuration File Format

The configuration file contains one `KEY=VALUE` pair per line.

Example:

```text
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=False
SEED=42
```

## Configuration Keys

| Key | Description |
|------|-------------|
| WIDTH | Maze width |
| HEIGHT | Maze height |
| ENTRY | Entry coordinates |
| EXIT | Exit coordinates |
| OUTPUT_FILE | Output filename |
| PERFECT | Generate a perfect maze or a Pac-Man maze |
| SEED | Optional random seed |



## Maze Generation Algorithm

The project uses the **Iterative Backtracking (Depth-First Search)** algorithm.

The maze is generated using the following steps:

1. Start from the entry cell.
2. Mark it as visited.
3. Randomly choose an unvisited neighbour.
4. Remove the wall between both cells.
5. Continue until every cell has been visited.
6. Backtrack whenever no unvisited neighbours remain.

When `PERFECT=False`, additional walls are removed to reduce dead ends and create multiple independent routes.

## Why DFS?

Iterative Backtracking (Depth-First Search) was chosen because it efficiently generates connected mazes while ensuring that every cell is reachable. An explicit stack is used instead of recursion, avoiding recursion depth limitations and providing better control over the generation process. This approach naturally produces perfect mazes and can be extended to create additional routes for the non-perfect mode.


## Maze Solving

The shortest path is computed using Breadth-First Search (BFS), which guarantees the shortest path in an unweighted grid. Once found, the path is converted to the required direction format (N, E, S, W) before being written to the output file.

## Maze solver: Iterative BFS Algorithm

1. Start from the entry cell.
2. Mark it as visited and add it to a queue.
3. Take the first cell from the queue.
4. If it is the exit, stop the search.
5. Add all accessible, unvisited neighbours to the queue.
6. Mark each neighbour as visited.
7. Store its parent so the path can be reconstructed later.
8. Repeat until the exit is found or the queue becomes empty.
9. Reconstruct the shortest path by following the parent links from the exit back to the  entry.


## Output File Format

The output file contains:

- hexadecimal wall representation
- blank line
- entry coordinates
- exit coordinates
- shortest path using `N`, `E`, `S`, `W`

Example:

```text
95395539555515515113
854693C69553C53C56AA
...

0,0
19,14
SSEEENNW...
```



## Reusable Code

The maze generation logic is distributed as a reusable Python package named `mazegen`. The package contains the core classes responsible for creating, generating, and solving mazes independently of the main application.

The package is organized into the following modules:

- `maze.py`
- `maze_generator.py`
- `solver.py`

Keeping the maze logic separate from the configuration parser, renderer, and output writer allows it to be reused in other Python projects.

## Importing the Package

The package exposes its main classes through a simple public API:

```python
from mazegen import Maze, MazeGenerator, MazeSolver
```

A `Maze` object can be generated using `MazeGenerator` and then passed to `MazeSolver` to compute the shortest path. Since the package is independent of the rest of the application, it can also be integrated into other projects.


## Building and Testing the Package

The package can be built and tested in a clean Python environment using the following steps:

```bash
# Remove previous build artifacts
rm -rf build dist *.egg-info

# Build the package
python3 -m build

# Verify the generated distribution files
ls dist

# Create and activate a virtual environment
python3 -m venv test_env
source test_env/bin/activate

# Install the package
pip install dist/mazegen-1.0.0-py3-none-any.whl

# Leave the project directory
cd ..

# Start Python
python3
```

Inside the Python interpreter:

```python
import mazegen

print(mazegen.__file__)

from mazegen import Maze, MazeGenerator, MazeSolver

print(Maze)
print(MazeGenerator)
print(MazeSolver)

exit()
```

Return to the project directory and run the application:

```bash
cd a_maze_ing
make run
```

## Team Responsibilities

### nakhatoo

- Maze structure
- Cell implementation
- DFS maze generation
- Maze solver
- Documentation
- Project integration
- Testing

### bandrade

- Configuration parser
- Rendering
- Output writer
- ASCII visualization
- Documentation
- Visuals
- Testing


## Testing

The project was tested by:

- Generating mazes of multiple sizes,
- Validating perfect and non-perfect generation,
- Checking hexadecimal outputs,
- Running the provided `maze_analyzer.py`.



## AI Usage

AI tools were used to support the development process by:

- clarifying project requirements,
- explaining Python concepts,
- answering implementation-related questions.

# RESOURCES

- Python Documentation  
  https://docs.python.org/3/

- Python dataclasses  
  https://youtu.be/Y9mxx1Mer0I?si=KWNle5sRhtUNnCsH

- Python typing  
  https://docs.python.org/3/library/typing.html

- Breadth-First Search
  https://youtu.be/xlVX7dXLS64?si=6WV2e9c2F6TVd-K0

- Depth-First Search
  https://youtu.be/PMMc4VsIacU?si=G2NcJC8d8dsTSJU9

- Recursive Backtracking Maze Generation
  https://en.wikipedia.org/wiki/Maze_generation_algorithm


## Project Planning

### Initial plan:

- Design maze structure
- Implement DFS generator
- Implement BFS solver
- Parse configuration file
- Generate hexadecimal output
- Add visualization
- Test and integrate modules

### Development Process

The work was divided between two team members. One member focused on maze generation and solving, while the other implemented configuration parsing, output generation, and visualization. After individual development, both parts were integrated and tested together.