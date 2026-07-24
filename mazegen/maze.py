from dataclasses import dataclass


@dataclass
class Cell:
    """Represent a single cell in the maze.

    Each cell stores its position, the state of its four surrounding
    walls, and whether it has been visited during maze generation.
    """
    x: int
    y: int
    north: bool = True
    east: bool = True
    south: bool = True
    west: bool = True

    visited: bool = False


class Maze:
    """Represent the maze and provide operations on its cells."""
    def __init__(
            self,
            width: int,
            height: int,
            entry: tuple[int, int],
            exit_p: tuple[int, int]) -> None:
        """Initialize a maze with the specified dimensions.

        Args:
            width: Width of the maze in cells.
            height: Height of the maze in cells.
            entry: Coordinates of the maze entrance.
            exit_p: Coordinates of the maze exit.
        """

        self.width = width
        self.height = height
        self.entry = entry
        self.exit_p = exit_p
        self.grid = []

        self.pattern_cells: set[tuple[int, int]] = set()

        for y in range(height):
            row = []

            for x in range(width):
                cell = Cell(x, y)
                row.append(cell)

            self.grid.append(row)

    def get_cell(self, x: int, y: int) -> Cell:
        """Return the cell at the specified coordinates.

        Args:
            x: Horizontal coordinate of the cell.
            y: Vertical coordinate of the cell.

        Returns:
            The cell located at the given coordinates.
        """
        return self.grid[y][x]

    def is_inside(self, x: int, y: int) -> bool:
        """Check whether coordinates are inside the maze.

        Args:
            x: Horizontal coordinate.
            y: Vertical coordinate.

        Returns:
            True if the coordinates are inside the maze,
            otherwise False.
        """
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False
        return True

    def remove_wall(self, first: Cell, second: Cell) -> None:
        """Remove the wall between two adjacent cells.

        Args:
            first: The first adjacent cell.
            second: The second adjacent cell.

        Returns:
            None.
        """
        if second.x == first.x + 1:
            first.east = False
            second.west = False

        elif second.x == first.x - 1:
            first.west = False
            second.east = False

        elif second.y == first.y + 1:
            first.south = False
            second.north = False

        elif second.y == first.y - 1:
            first.north = False
            second.south = False

    def reset(self) -> None:
        """Reset the maze to its initial state.

        Restores all walls and marks every cell as unvisited.

        Returns:
            None.
        """

        for row in self.grid:
            for cell in row:
                cell.north = True
                cell.east = True
                cell.south = True
                cell.west = True
                cell.visited = False

    def get_unvisited_neighbors(self, cell: Cell) -> list[Cell]:
        """Return all unvisited neighboring cells.

        Args:
            cell: The cell whose neighbors are searched.

        Returns:
            A list of neighboring cells that have not been visited.
        """
        neighbors = []

        if self.is_inside(cell.x, cell.y - 1):
            north = self.get_cell(cell.x, cell.y - 1)
            if not north.visited:
                neighbors.append(north)

        if self.is_inside(cell.x + 1, cell.y):
            east = self.get_cell(cell.x + 1, cell.y)
            if not east.visited:
                neighbors.append(east)

        if self.is_inside(cell.x, cell.y + 1):
            south = self.get_cell(cell.x, cell.y + 1)
            if not south.visited:
                neighbors.append(south)

        if self.is_inside(cell.x - 1, cell.y):
            west = self.get_cell(cell.x - 1, cell.y)
            if not west.visited:
                neighbors.append(west)

        return neighbors

    def get_accessible_neighbors(self, cell: Cell) -> list[Cell]:
        """Return neighboring cells connected by open passages.

        Cells belonging to the reserved "42" pattern are excluded.

        Args:
            cell: The cell whose accessible neighbors are searched.

        Returns:
            A list of neighboring cells that can be reached directly
            from the given cell.
        """
        neighbors = []

        if not cell.north and self.is_inside(cell.x, cell.y - 1):
            north = self.get_cell(cell.x, cell.y - 1)
            if (north.x, north.y) not in self.pattern_cells:
                neighbors.append(north)

        if not cell.east and self.is_inside(cell.x + 1, cell.y):
            east = self.get_cell(cell.x + 1, cell.y)
            if (east.x, east.y) not in self.pattern_cells:
                neighbors.append(east)

        if not cell.south and self.is_inside(cell.x, cell.y + 1):
            south = self.get_cell(cell.x, cell.y + 1)
            if (south.x, south.y) not in self.pattern_cells:
                neighbors.append(south)

        if not cell.west and self.is_inside(cell.x - 1, cell.y):
            west = self.get_cell(cell.x - 1, cell.y)
            if (west.x, west.y) not in self.pattern_cells:
                neighbors.append(west)

        return neighbors
