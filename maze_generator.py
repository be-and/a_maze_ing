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
        entry_x, entry_y = self.maze.entry
        start = self.maze.get_cell(entry_x, entry_y)

        start.visited = True

        stack = [start]

        while stack:
            current = stack[-1]

            neighbors = self.maze.get_unvisited_neighbors(current)

            if neighbors:
                next_cell = random.choice(neighbors)

                self.maze.remove_wall(current, next_cell)

                next_cell.visited = True

                stack.append(next_cell)
            else:
                stack.pop()

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
