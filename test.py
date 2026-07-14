from maze import Maze
from maze_generator import MazeGenerator
from solver import MazeSolver


maze = Maze(
    width=10,
    height=10,
    entry=(0, 0),
    exit_p=(9, 9),
)

generator = MazeGenerator(
    maze,
    perfect=True,
    seed=42,
)

generator.generate()

solver = MazeSolver(maze)

path = solver.solve()

directions = solver.path_to_directions(path)

assert len(path) > 0

assert path[0] == maze.entry

assert path[-1] == maze.exit_p

for move in directions:
    assert move in "NESW"

print("All tests passed!")
