from dataclasses import dataclass


@dataclass
class Cell:
    x: int
    y: int
    north: bool = True
    east: bool = True
    south: bool = True
    west: bool = True

    visited: bool = False


class Maze:
    def __init__(self, width, height, entry, exit_p):
        self.width = width
        self.height = height
        self.entry = entry
        self.exit_p = exit_p
        self.grid = []

        for y in range(height):
            row = []

            for x in range(width):
                cell = Cell(x, y)
                row.append(cell)

            self.grid.append(row)

    def get_cell(self, x, y):
        return self.grid[y][x]

    def is_inside(self, x, y):
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False
        return True

    def remove_wall(self, first, second):
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

    def reset(self):
        """Restore every cell to its initial state."""

        for row in self.grid:
            for cell in row:
                cell.north = True
                cell.east = True
                cell.south = True
                cell.west = True
                cell.visited = False

    def get_unvisited_neighbors(self, cell):
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

    def get_accessible_neighbors(self, cell):
        neighbors = []

        if not cell.north:
            if self.is_inside(cell.x, cell.y - 1):
                north = self.get_cell(cell.x, cell.y - 1)
                neighbors.append(north)

        if not cell.east:
            if self.is_inside(cell.x + 1, cell.y):
                east = self.get_cell(cell.x + 1, cell.y)
                neighbors.append(east)

        if not cell.south:
            if self.is_inside(cell.x, cell.y + 1):
                south = self.get_cell(cell.x, cell.y + 1)
                neighbors.append(south)

        if not cell.west:
            if self.is_inside(cell.x - 1, cell.y):
                west = self.get_cell(cell.x - 1, cell.y)
                neighbors.append(west)

        return neighbors
