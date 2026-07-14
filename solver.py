from maze import Maze


class MazeSolver:
    def __init__(self, maze: Maze):
        self.maze = maze

    def solve(self):
        entry_x, entry_y = self.maze.entry
        start = self.maze.get_cell(entry_x, entry_y)

        queue = [start]

        visited = set()
        visited.add((start.x, start.y))

        parents = {}

        while queue:

            current = queue.pop(0)

            current_pos = (current.x, current.y)

            if (current_pos) == self.maze.exit_p:
                break

            neighbors = self.maze.get_accessible_neighbors(current)

            for neighbor in neighbors:

                neighbor_pos = (neighbor.x, neighbor.y)

                if neighbor_pos not in visited:

                    parents[neighbor_pos] = current_pos

                    visited.add(neighbor_pos)

                    queue.append(neighbor)

        if (
            self.maze.exit_p not in parents
            and self.maze.exit_p != self.maze.entry
        ):
            return []

        path = []

        current = self.maze.exit_p

        while current != self.maze.entry:

            path.append(current)

            current = parents[current]

        path.append(self.maze.entry)

        path.reverse()

        return path

    def path_to_directions(self, path):
        """Convert a path of coordinates into N, E, S, W directions."""

        directions = []

        for i in range(len(path) - 1):
            x1, y1 = path[i]
            x2, y2 = path[i + 1]

            if x2 == x1 and y2 == y1 - 1:
                directions.append("N")

            elif x2 == x1 + 1 and y2 == y1:
                directions.append("E")

            elif x2 == x1 and y2 == y1 + 1:
                directions.append("S")

            elif x2 == x1 - 1 and y2 == y1:
                directions.append("W")

        return "".join(directions)
