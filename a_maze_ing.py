import sys
from parser import parse_config
from maze import Maze
from maze_generator import MazeGenerator
from solver import MazeSolver
from writer import write_maze
from renderer import render_maze


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        return

    try:
        config_file = sys.argv[1]
        # Read configuration
        config = parse_config(config_file)

        # Create maze
        maze = Maze(
            config.width,
            config.height,
            config.entry,
            config.exit_p,
        )

        # Generate maze
        generator = MazeGenerator(
            maze,
            config.perfect,
            config.seed,
        )
        generator.generate()

        solver = MazeSolver(maze)

        path = solver.solve()

        render_maze(maze, path)

        write_maze(maze, config.output_file)

        print(f"Maze written to {config.output_file}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
