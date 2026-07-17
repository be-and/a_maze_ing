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

        config = parse_config(config_file)

        maze = Maze(
            config.width,
            config.height,
            config.entry,
            config.exit_p,
        )

        generator = MazeGenerator(
            maze,
            config.perfect,
            config.seed,
        )

        generator.generate()

        solver = MazeSolver(maze)

        show_path = True

        message = ""

        while True:

            path = solver.solve()

            if show_path:
                render_maze(maze, path)
            else:
                render_maze(maze)

            MENU = "\033[38;5;153m"
            TITLE = "\033[38;5;217m"
            RESET = "\033[0m"

            print(f"\n{TITLE}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{RESET}")
            print(f"{TITLE}┃{'A-MAZE-ING':^38}┃{RESET}")
            print(f"{TITLE}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}")

            print(f"{MENU}[1]{RESET} Generate new maze")
            print(f"{MENU}[2]{RESET} Show / Hide path")
            print(f"{MENU}[3]{RESET} Change wall colour")
            print(f"{MENU}[4]{RESET} Save maze")
            print(f"{MENU}[5]{RESET} Exit")

            if message:
                print(f"\n{message}")
                message = ""

            choice = input(f"\n{MENU}Choice: {RESET}")

            if choice == "1":
                generator.generate()
                message = "New maze generated!"

            elif choice == "2":
                show_path = not show_path

                if show_path:
                    message = "Shortest path shown."
                else:
                    message = "Shortest path hidden."

            elif choice == "3":
                message = "Not implemented yet."

            elif choice == "4":
                write_maze(maze, config.output_file)
                message = f"Maze written to {config.output_file}"

            elif choice == "5":
                break

            else:
                message = "Invalid option."

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
