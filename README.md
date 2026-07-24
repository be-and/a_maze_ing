*This project has been created as part of the 42 curriculum by nakhatoo and bandrade.*

# A-Maze-ing

## Description

A-Maze-ing is a Python project that generates random mazes from a configuration file.

The program supports two generation modes:

- **Perfect maze** (`PERFECT=True`): exactly one unique path exists between any two cells.
- **Pac-Man maze** (`PERFECT=False`): multiple independent routes are created, making the maze suitable for a Pac-Man style game.

The generated maze is written to a text file using hexadecimal wall encoding and includes the shortest path from the entrance to the exit.

The generated maze can also be visualized directly in the terminal using an ASCII renderer, making it easier to inspect the maze structure and solution.

---

# Features

<<<<<<< HEAD
- Maze generation using Recursive Backtracking (Depth-First Search)
=======
- Maze generation using Iterative Backtracking (Depth-First Search)
>>>>>>> 3ce77e3 (final version)
- Random generation with optional seed
- Perfect and non-perfect maze generation
- Shortest path calculation using Breadth-First Search (BFS)
- Hexadecimal maze encoding
- Configuration file support
- ASCII maze visualization
- Automatic maze validation with the provided analyzer

---

# Instructions

## Requirements

- Python 3.10 or later

## Run the program

```bash
python3 a_maze_ing.py config.txt
```

Replace `config.txt` with any valid configuration file.

---

# Configuration File Format

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

---

# Maze Generation Algorithm

<<<<<<< HEAD
This project uses the **Recursive Backtracking (Depth-First Search)** algorithm.
=======
This project uses the **Iterative Backtracking (Depth-First Search)** algorithm.
>>>>>>> 3ce77e3 (final version)

Algorithm overview:

1. Start from the entry cell.
2. Mark it as visited.
3. Randomly choose an unvisited neighbour.
4. Remove the wall between both cells.
5. Continue until every cell has been visited.
6. Backtrack whenever no unvisited neighbours remain.

When `PERFECT=False`, additional walls are removed to reduce dead ends and create multiple independent routes.

---

# Why DFS?

<<<<<<< HEAD
Recursive Backtracking was chosen because:

- it is simple to implement,
- it generates perfect mazes efficiently,
- it produces natural-looking corridors,
- it is well suited for grid-based maze generation.
=======
Iterative Backtracking was chosen because:

I used iterative Depth-First Search because it efficiently generates a perfect maze by exploring one path as far as possible before backtracking. I implemented it iteratively with an explicit stack instead of recursion to avoid recursion depth limits and to have better control over the algorithm. It also satisfies the project requirement to generate a connected maze where every cell is reachable.
>>>>>>> 3ce77e3 (final version)

---

# Maze Solving

The shortest path is calculated using **Breadth-First Search (BFS)**.

BFS guarantees the shortest path in an unweighted grid.

The resulting coordinate path is converted into the required direction format:

```
N E S W
```

before being written to the output file.

<<<<<<< HEAD
=======
# Iterative BFS Algorithm (Maze Solver)

1. Start from the entry cell.
2. Mark it as visited and add it to a queue.
3. Take the first cell from the queue.
4. If it is the exit, stop the search.
5. Add all accessible, unvisited neighbours to the queue.
6. Mark each neighbour as visited.
7. Store its parent so the path can be reconstructed later.
8. Repeat until the exit is found or the queue becomes empty.
9. Reconstruct the shortest path by following the parent links from the exit back to the  entry.

>>>>>>> 3ce77e3 (final version)
---

# Output File Format

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

---

# Reusable Code

The maze generation logic is separated into reusable modules.

Main reusable classes:

- `Maze`
- `MazeGenerator`
- `MazeSolver`

These modules can be reused independently in future projects.

---

# Team Responsibilities

## \<nakhatoo\>

- Maze structure
- Cell implementation
- DFS maze generation
- BFS maze solver
- Documentation
- Project integration
- Testing

## \<bandrade\>

- Configuration parser
<<<<<<< HEAD
=======
- Rendering
>>>>>>> 3ce77e3 (final version)
- Output writer
- ASCII visualization
- Documentation
- Project integration
- Testing

---

# Testing

The project was tested by:

- generating mazes of multiple sizes,
- validating perfect and non-perfect generation,
- verifying shortest paths,
- checking hexadecimal output,
- running the provided `maze_analyzer.py`.

---

# AI Usage

AI was used as an assistant for:

- understanding project requirements,
- understanding algorithms,
- explaining Python concepts.

---

# Resources

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

---

# Project Planning

Initial plan:

- Design maze structure
- Implement DFS generator
- Implement BFS solver
- Parse configuration file
- Generate hexadecimal output
- Add visualization
- Test and integrate modules

Project evolution:

The work was divided between two team members. One member focused on maze generation and solving, while the other implemented configuration parsing, output generation, and visualization. After individual development, both parts were integrated and tested together.

---
