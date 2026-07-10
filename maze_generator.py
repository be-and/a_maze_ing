import random


class MazeGenerator:
    def __init__(self, maze, seed=None):
        self.maze = maze

        if seed is not None:
            random.seed(seed)

    def generate(self):
        entry_x, entry_y = self.maze.entry
        start = self.maze.get_cell(entry_x, entry_y)

        start.visited = True

        stack = []
        stack.append(start)

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
