from maze import Maze

RESET = "\033[0m"

WALL = "\033[38;5;228m"     # yellow
ENTRY = "\033[38;5;157m"    # green
EXIT = "\033[38;5;204m"     # red
PATH = "\033[38;5;217m"     # pink
PATTERN = "\033[38;5;39m"   # blue

HORIZONTAL = "━━━"
VERTICAL = "┃"


def render_top(maze: Maze) -> None:
    """Draw the top border of the maze."""

    top = "┏"

    for x in range(maze.width):
        top += HORIZONTAL

        if x == maze.width - 1:
            top += "┓"
        else:
            top += "┳"

    print(f"{WALL}{top}{RESET}")


def render_row(
    maze: Maze,
    y: int,
    path: set[tuple[int, int]] | None = None,
) -> None:
    """Draw one row of maze cells."""

    line = f"{WALL}{VERTICAL}{RESET}"

    for cell in maze.grid[y]:

        position = (cell.x, cell.y)

        if position == maze.entry:
            content = f"{ENTRY} E {RESET}"

        elif position == maze.exit_p:
            content = f"{EXIT} X {RESET}"

        elif position in maze.pattern_cells:
            content = f"{PATTERN}███{RESET}"

        elif path is not None and position in path:
            content = f"{PATH} █ {RESET}"

        else:
            content = "   "

        line += content

        if cell.east:
            line += f"{WALL}{VERTICAL}{RESET}"
        else:
            line += " "

    print(line)


def render_bottom(maze: Maze, y: int) -> None:
    """Draw the bottom walls of one maze row."""

    if y == maze.height - 1:
        left = "┗"
        middle = "┻"
        right = "┛"
    else:
        left = "┣"
        middle = "╋"
        right = "┫"

    bottom = left

    for x, cell in enumerate(maze.grid[y]):

        if cell.south:
            bottom += HORIZONTAL
        else:
            bottom += "   "

        if x == maze.width - 1:
            bottom += right
        else:
            bottom += middle

    print(f"{WALL}{bottom}{RESET}")


def render_maze(
    maze: Maze,
    path: list[tuple[int, int]] | None = None,
) -> None:
    """Render the maze in ASCII."""

    render_top(maze)

    path_set = set(path) if path is not None else None

    for y in range(maze.height):
        render_row(maze, y, path_set)
        render_bottom(maze, y)
