from typing import TextIO

from maze import Cell, Maze


def encode_cell(cell: Cell) -> str:
    """Convert a cell into its hexadecimal representation."""

    value = 0

    if cell.north:
        value += 1

    if cell.east:
        value += 2

    if cell.south:
        value += 4

    if cell.west:
        value += 8

    return format(value, "X")


def encode_row(maze: Maze, y: int) -> str:
    """Convert one row of the maze into hexadecimal."""

    row = ""

    for cell in maze.grid[y]:
        row += encode_cell(cell)

    return row


def write_grid(file: TextIO, maze: Maze) -> None:
    """Write the maze grid using hexadecimal encoding."""

    for y in range(maze.height):
        file.write(encode_row(maze, y))
        file.write("\n")

# def write_maze(maze, path, output_file):
#     ...
