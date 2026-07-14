from maze import Maze


def render_top(maze: Maze) -> None:
    """Draw the top border of the maze."""

    top = "+"

    for _ in range(maze.width):
        top += "---+"

    print(top)


def render_row(
    maze: Maze,
    y: int,
    path: set[tuple[int, int]] | None = None,
) -> None:
    """Draw one row of maze cells."""

    line = "|"

    for cell in maze.grid[y]:

        position = (cell.x, cell.y)

        if position == maze.entry:
            content = " E "

        elif position == maze.exit_p:
            content = " X "

        elif path is not None and position in path:
            content = " . "

        else:
            content = "   "

        line += content

        if cell.east:
            line += "|"
        else:
            line += " "

    print(line)


def render_bottom(maze: Maze, y: int) -> None:
    """Draw the bottom walls of one maze row."""

    bottom = "+"

    for cell in maze.grid[y]:

        if cell.south:
            bottom += "---+"
        else:
            bottom += "   +"

    print(bottom)


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
