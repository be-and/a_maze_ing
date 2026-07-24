from .maze import Maze, Cell


class MazeSolver:
    """Find the shortest path through a maze.

    The solver uses a breadth-first search (BFS) algorithm to find the
    shortest path from the maze entry to the exit. The resulting path
    can also be converted into cardinal directions.
    """

    def __init__(self, maze: Maze):
        """Initialize the maze solver.

        Args:
            maze: The maze to solve.
        """
        self.maze = maze

    def solve(self) -> list[tuple[int, int]]:
        """Find the shortest path through the maze.

        Uses a breadth-first search (BFS) to explore all reachable cells
        until the maze exit is found. The shortest path is reconstructed
        by following the recorded parent of each visited cell.

        Returns:
            A list of `(x, y)` coordinates representing the shortest path
            from the maze entry to the exit. Returns an empty list if no
            path exists.
        """

        entry_x, entry_y = self.maze.entry
        start = self.maze.get_cell(entry_x, entry_y)

        queue: list[Cell] = [start]

        visited: set[tuple[int, int]] = set()
        visited.add((start.x, start.y))

        parents: dict[tuple[int, int], tuple[int, int]] = {}

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

        path: list[tuple[int, int]] = []

        current_pos = self.maze.exit_p

        while current_pos != self.maze.entry:

            path.append(current_pos)

            current_pos = parents[current_pos]

        path.append(self.maze.entry)

        path.reverse()

        return path

    def path_to_directions(self, path: list[tuple[int, int]]) -> str:
        """Convert a path into cardinal directions.

        Each pair of consecutive coordinates is converted into one of the
        four cardinal directions: North (N), East (E), South (S), or
        West (W).

        Args:
            path: A list of `(x, y)` coordinates representing a path
                through the maze.

        Returns:
            A string containing the sequence of movement directions.
        """

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
