import sys
from parser import parse_config
<<<<<<< HEAD
from maze import Maze
from maze_generator import MazeGenerator
from solver import MazeSolver
=======
from mazegen import Maze, MazeGenerator, MazeSolver
>>>>>>> 3ce77e3 (final version)
from writer import write_maze
from renderer import render_maze


<<<<<<< HEAD
def main():
=======
def main() -> None:
    """Run the maze application."""
>>>>>>> 3ce77e3 (final version)
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

<<<<<<< HEAD
=======
        wall_color = "yellow"

>>>>>>> 3ce77e3 (final version)
        while True:

            path = solver.solve()

            if show_path:
<<<<<<< HEAD
                render_maze(maze, path)
            else:
                render_maze(maze)
=======
                render_maze(maze, path, wall_color)
            else:
                render_maze(maze, None, wall_color)
>>>>>>> 3ce77e3 (final version)

            MENU = "\033[38;5;153m"
            TITLE = "\033[38;5;217m"
            RESET = "\033[0m"

<<<<<<< HEAD
=======
            current_colour = wall_color.capitalize()

>>>>>>> 3ce77e3 (final version)
            print(f"\n{TITLE}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓{RESET}")
            print(f"{TITLE}┃{'A-MAZE-ING':^38}┃{RESET}")
            print(f"{TITLE}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{RESET}")

            print(f"{MENU}[1]{RESET} Generate new maze")
            print(f"{MENU}[2]{RESET} Show / Hide path")
<<<<<<< HEAD
            print(f"{MENU}[3]{RESET} Change wall colour")
=======
            print(f"{MENU}[3]{RESET} Change wall colour ({current_colour})")
>>>>>>> 3ce77e3 (final version)
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
<<<<<<< HEAD
                message = "Not implemented yet."
=======

                print("\nChoose wall colour:\n")

                colours = ["yellow", "lilac", "green", "orange"]

                for i, colour in enumerate(colours, start=1):
                    current = " (current)" if colour == wall_color else ""
                    print(f"[{i}] {colour.capitalize()}{current}")

                colour = input("\nChoice: ")

                if colour == "1":
                    wall_color = "yellow"

                elif colour == "2":
                    wall_color = "lilac"

                elif colour == "3":
                    wall_color = "green"

                elif colour == "4":
                    wall_color = "orange"

                else:
                    message = "Invalid colour."
                    continue

                message = f"Wall colour changed to {wall_color.capitalize()}."
>>>>>>> 3ce77e3 (final version)

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
