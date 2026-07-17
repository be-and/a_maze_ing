from maze import Maze
import random


class MazeGenerator:
    def __init__(
                self,
                maze: Maze,
                perfect: bool = True,
                seed: int | None = None):
        self.maze = maze
        self.perfect = perfect

        if seed is not None:
            random.seed(seed)

    def generate(self):
        self.maze.reset()

        self.create_42_pattern()

        entry_x, entry_y = self.maze.entry
        start = self.maze.get_cell(entry_x, entry_y)

        start.visited = True

        stack = [start]

        while stack:
            current = stack[-1]

            neighbors = []

            for cell in self.maze.get_unvisited_neighbors(current):
                if (cell.x, cell.y) not in self.pattern_cells:
                    neighbors.append(cell)

            if neighbors:
                next_cell = random.choice(neighbors)

                self.maze.remove_wall(current, next_cell)

                next_cell.visited = True

                stack.append(next_cell)
            else:
                stack.pop()
        for x, y in self.pattern_cells:
            cell = self.maze.get_cell(x, y)

            cell.north = True
            cell.east = True
            cell.south = True
            cell.west = True

            if self.maze.is_inside(x, y - 1):
                north = self.maze.get_cell(x, y - 1)
                north.south = True

            if self.maze.is_inside(x + 1, y):
                east = self.maze.get_cell(x + 1, y)
                east.west = True

            if self.maze.is_inside(x, y + 1):
                south = self.maze.get_cell(x, y + 1)
                south.north = True

            if self.maze.is_inside(x - 1, y):
                west = self.maze.get_cell(x - 1, y)
                west.east = True

            for row in self.maze.grid:
                for cell in row:
                    cell.visited = False

            if not self.perfect:
                self.reduce_dead_ends()

    def is_dead_end(self, cell):

        open_sides = 0

        if not cell.north:
            open_sides += 1

        if not cell.east:
            open_sides += 1

        if not cell.south:
            open_sides += 1

        if not cell.west:
            open_sides += 1

        return open_sides == 1

    def reduce_dead_ends(self):

        for y in range(self.maze.height):

            for x in range(self.maze.width):

                cell = self.maze.get_cell(x, y)

                if not self.is_dead_end(cell):
                    continue

                possible_neighbors = []

                if self.maze.is_inside(x + 1, y):

                    east = self.maze.get_cell(x + 1, y)

                    if cell.east:

                        possible_neighbors.append(east)

                if self.maze.is_inside(x, y + 1):

                    south = self.maze.get_cell(x, y + 1)

                    if cell.south:

                        possible_neighbors.append(south)

                if self.maze.is_inside(x - 1, y):

                    west = self.maze.get_cell(x - 1, y)

                    if cell.west:

                        possible_neighbors.append(west)

                if self.maze.is_inside(x, y - 1):

                    north = self.maze.get_cell(x, y - 1)

                    if cell.north:

                        possible_neighbors.append(north)

                if possible_neighbors:

                    neighbor = random.choice(possible_neighbors)

                    self.maze.remove_wall(cell, neighbor)

    def create_42_pattern(self) -> None:
        """Reserve the cells used to draw the '42'."""

        self.pattern_cells = set()

        if self.maze.width < 10 or self.maze.height < 7:
            print("Maze too small to draw the 42 pattern.")
            return

        patter_width = 7
        pattern_height = 5

        start_x = (self.maze.width - patter_width) // 2
        start_y = (self.maze.height - pattern_height) // 2
        start_y = self.maze.height // 2 - 2

        four = [
            (1, 0), (3, 0),
            (1, 1), (3, 1),
            (1, 2), (2, 2), (3, 2),
            (3, 3),
            (3, 4),
        ]

        two = [
            (5, 0), (6, 0), (7, 0),
            (7, 1),
            (5, 2), (6, 2), (7, 2),
            (5, 3),
            (5, 4), (6, 4), (7, 4),
        ]

        for dx, dy in four + two:
            x = start_x + dx
            y = start_y + dy

            if (x, y) == self.maze.entry:
                raise ValueError("ENTRY cannot be inside the 42 pattern.")

            if (x, y) == self.maze.exit_p:
                raise ValueError("EXIT cannot be inside the 42 pattern.")

            self.pattern_cells.add((start_x + dx, start_y + dy))

        self.maze.pattern_cells = self.pattern_cells
