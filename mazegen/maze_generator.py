from .maze import Maze, Cell
import random


class MazeGenerator:
    """Generate perfect or imperfect mazes.

    The maze is generated using an iterative depth-first search (DFS)
    algorithm. Optionally, additional passages can be carved to reduce
    dead ends and create an imperfect maze. The generator also reserves
    cells for the required "42" pattern.
    """
    def __init__(
                self,
                maze: Maze,
                perfect: bool = True,
                seed: int | None = None):
        """Initialize the maze generator.

    Args:
        maze: The maze to generate.
        perfect: Whether to generate a perfect maze. If False,
            additional passages are carved to reduce dead ends.
        seed: Seed for the random number generator. If provided,
            maze generation becomes reproducible.
    """
        self.maze = maze
        self.perfect = perfect

        if seed is not None:
            random.seed(seed)

    def generate(self) -> None:
        """Generate the maze.

        Creates the reserved "42" pattern, carves passages using an
        iterative depth-first search algorithm, restores the pattern
        walls, resets the visited state of all cells, and optionally
        reduces dead ends to produce an imperfect maze.

        Returns:
            None.
        """
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

    def is_dead_end(self, cell: Cell) -> bool:
        """Determine whether a cell is a dead end.

        A dead-end cell has exactly one open passage.

        Args:
            cell: The cell to examine.

        Returns:
            True if the cell has exactly one open side,
            otherwise False.
        """

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

    def count_dead_ends(self) -> int:
        """Count the dead-end cells in the maze.

        Returns:
            The total number of dead-end cells.
        """
        count = 0

        for row in self.maze.grid:
            for cell in row:
                if self.is_dead_end(cell):
                    count += 1

        return count

    def reduce_dead_ends(self) -> None:
        """Reduce the number of dead ends.

        Randomly removes walls from dead-end cells until at most two
        dead ends remain or no more valid walls can be removed.

        Returns:
            None.
        """

        while self.count_dead_ends() > 2:

            removed = False

            for y in range(self.maze.height):

                for x in range(self.maze.width):

                    cell = self.maze.get_cell(x, y)

                    if (cell.x, cell.y) in self.pattern_cells:
                        continue

                    if not self.is_dead_end(cell):
                        continue

                    possible_neighbors = []

                    if self.maze.is_inside(x + 1, y):
                        east = self.maze.get_cell(x + 1, y)
                        if (
                            cell.east
                            and (east.x, east.y) not in self.pattern_cells
                        ):
                            possible_neighbors.append(east)

                    if self.maze.is_inside(x, y + 1):
                        south = self.maze.get_cell(x, y + 1)
                        if (
                            cell.south
                            and (south.x, south.y) not in self.pattern_cells
                        ):
                            possible_neighbors.append(south)

                    if self.maze.is_inside(x - 1, y):
                        west = self.maze.get_cell(x - 1, y)
                        if (
                            cell.west
                            and (west.x, west.y) not in self.pattern_cells
                        ):
                            possible_neighbors.append(west)

                    if self.maze.is_inside(x, y - 1):
                        north = self.maze.get_cell(x, y - 1)
                        if (
                            cell.north
                            and (north.x, north.y) not in self.pattern_cells
                        ):
                            possible_neighbors.append(north)

                    if possible_neighbors:
                        neighbor = random.choice(possible_neighbors)
                        self.maze.remove_wall(cell, neighbor)

                        removed = True
                        break

                if removed:
                    break

            if not removed:
                break

    def create_42_pattern(self) -> None:
        """Reserve the cells used to draw the "42" pattern.

        Calculates a suitable position for the pattern, validates that
        it does not overlap the maze entry or exit, and stores the
        reserved cells so they remain enclosed during maze generation.

        Raises:
            ValueError: If the maze entry or exit lies inside the
                reserved "42" pattern.

        Returns:
            None.
        """

        self.pattern_cells = set()

        if self.maze.width < 10 or self.maze.height < 7:
            print("Maze is too small to draw the 42 pattern.")
            return

        pattern_width = 7
        pattern_height = 5

        start_x = (self.maze.width - pattern_width) // 2
        start_y = (self.maze.height - pattern_height) // 2

        four = [
            (0, 0), (2, 0),
            (0, 1), (2, 1),
            (0, 2), (1, 2), (2, 2),
            (2, 3),
            (2, 4),
        ]

        two = [
            (4, 0), (5, 0), (6, 0),
            (6, 1),
            (4, 2), (5, 2), (6, 2),
            (4, 3),
            (4, 4), (5, 4), (6, 4),
        ]

        start_x = self.find_best_pattern_position(
            start_x,
            start_y,
            four,
            two,
        )

        for dx, dy in four + two:
            x = start_x + dx
            y = start_y + dy

            if (x, y) == self.maze.entry:
                raise ValueError("ENTRY cannot be inside the 42 pattern.")

            if (x, y) == self.maze.exit_p:
                raise ValueError("EXIT cannot be inside the 42 pattern.")

            self.pattern_cells.add((start_x + dx, start_y + dy))

        self.maze.pattern_cells = self.pattern_cells

    def covers_center(
        self,
        start_x: int,
        start_y: int,
        four: list[tuple[int, int]],
        two: list[tuple[int, int]],
    ) -> bool:
        """Check whether the pattern covers the maze center.

        Args:
            start_x: Leftmost x-coordinate of the pattern.
            start_y: Topmost y-coordinate of the pattern.
            four: Relative coordinates forming the digit "4".
            two: Relative coordinates forming the digit "2".

        Returns:
            True if the pattern covers the center of the maze,
            otherwise False.
        """

        center = (self.maze.width // 2, self.maze.height // 2)

        for dx, dy in four + two:
            if (start_x + dx, start_y + dy) == center:
                return True
        return False

    def fits_in_maze(
        self,
        start_x: int,
        start_y: int,
        four: list[tuple[int, int]],
        two: list[tuple[int, int]],
    ) -> bool:
        """Check whether the pattern fits inside the maze.

        Args:
            start_x: Leftmost x-coordinate of the pattern.
            start_y: Topmost y-coordinate of the pattern.
            four: Relative coordinates forming the digit "4".
            two: Relative coordinates forming the digit "2".

        Returns:
            True if every pattern cell lies inside the maze,
            otherwise False.
        """

        for dx, dy in four + two:
            x = start_x + dx
            y = start_y + dy

            if not self.maze.is_inside(x, y):
                return False

        return True

    def is_valid_pattern_position(
        self,
        start_x: int,
        start_y: int,
        four: list[tuple[int, int]],
        two: list[tuple[int, int]],
    ) -> bool:
        """Determine whether a pattern position is valid.

        A valid position keeps the pattern inside the maze and
        prevents it from covering the maze center.

        Args:
            start_x: Leftmost x-coordinate of the pattern.
            start_y: Topmost y-coordinate of the pattern.
            four: Relative coordinates forming the digit "4".
            two: Relative coordinates forming the digit "2".

        Returns:
            True if the position is valid, otherwise False.
        """

        return (
            self.fits_in_maze(start_x, start_y, four, two)
            and not self.covers_center(
                start_x,
                start_y,
                four,
                two,
            )
        )

    def find_best_pattern_position(
        self,
        start_x: int,
        start_y: int,
        four: list[tuple[int, int]],
        two: list[tuple[int, int]],
    ) -> int:
        """Find the best horizontal position for the "42" pattern.

        Searches for the nearest valid horizontal position,
        starting from the centered location and moving left and
        right until a valid position is found.

        Args:
            start_x: Preferred horizontal position.
            start_y: Vertical position of the pattern.
            four: Relative coordinates forming the digit "4".
            two: Relative coordinates forming the digit "2".

        Returns:
            The horizontal coordinate where the pattern should
            be placed.
        """

        original_x = start_x
        max_offset = self.maze.width

        for offset in range(max_offset):

            candidate_x = original_x - offset

            if self.is_valid_pattern_position(
                candidate_x,
                start_y,
                four,
                two,
            ):
                return candidate_x

            if offset != 0:
                candidate_x = original_x + offset

                if self.is_valid_pattern_position(
                    candidate_x,
                    start_y,
                    four,
                    two,
                ):
                    return candidate_x

        return original_x
