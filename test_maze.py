from maze import Maze
from maze_generator import MazeGenerator


print("\n========== Maze Constructor ==========")

maze = Maze(4, 3, (0, 0), (3, 2))

print("Width:", maze.width)
print("Height:", maze.height)
print("Entry:", maze.entry)
print("Exit:", maze.exit_p)

print("\n========== Grid ==========")

for row in maze.grid:
    print(row)
    print("\n")


print("\n========== get_cell() ==========")

cell = maze.get_cell(2, 1)
print(cell)


print("\n========== is_inside() ==========")

print("(2,1):", maze.is_inside(2, 1))
print("(-1,0):", maze.is_inside(-1, 0))
print("(5,1):", maze.is_inside(5, 1))


print("\n========== remove_wall() ==========")

print("\nEast")
maze = Maze(3, 3, (0, 0), (2, 2))
first = maze.get_cell(0, 0)
second = maze.get_cell(1, 0)
maze.remove_wall(first, second)
print(first)
print(second)

print("\nWest")
maze = Maze(3, 3, (0, 0), (2, 2))
first = maze.get_cell(1, 0)
second = maze.get_cell(0, 0)
maze.remove_wall(first, second)
print(first)
print(second)

print("\nNorth")
maze = Maze(3, 3, (0, 0), (2, 2))
first = maze.get_cell(0, 1)
second = maze.get_cell(0, 0)
maze.remove_wall(first, second)
print(first)
print(second)

print("\nSouth")
maze = Maze(3, 3, (0, 0), (2, 2))
first = maze.get_cell(0, 0)
second = maze.get_cell(0, 1)
maze.remove_wall(first, second)
print(first)
print(second)


print("\n========== get_unvisited_neighbors() ==========")

print("\nCenter Cell")
maze = Maze(3, 3, (0, 0), (2, 2))
cell = maze.get_cell(1, 1)

neighbors = maze.get_unvisited_neighbors(cell)

print("Number of neighbors:", len(neighbors))

for neighbor in neighbors:
    print(neighbor)


print("\nCorner Cell")
maze = Maze(3, 3, (0, 0), (2, 2))
cell = maze.get_cell(0, 0)

neighbors = maze.get_unvisited_neighbors(cell)

print("Number of neighbors:", len(neighbors))

for neighbor in neighbors:
    print(neighbor)


print("\nVisited Neighbor Test")
maze = Maze(3, 3, (0, 0), (2, 2))

maze.get_cell(1, 0).visited = True

cell = maze.get_cell(1, 1)

neighbors = maze.get_unvisited_neighbors(cell)

print("Number of neighbors:", len(neighbors))

for neighbor in neighbors:
    print(neighbor)


print("\n========== MazeGenerator ==========")

maze = Maze(3, 3, (1, 1), (2, 2))

generator = MazeGenerator(maze, seed=42)
generator.generate()

print("Entry:", maze.entry)
print("Exit:", maze.exit_p)

print("\nEntry Cell:")
print(maze.get_cell(1, 1))

print("\nAll Cells:")

for row in maze.grid:
    for cell in row:
        print(cell)

print("\n========== Visited Cells ==========")

for row in maze.grid:
    for cell in row:
        print(cell)

print("\n============North wall============")

maze = Maze(3, 3, (0, 0), (2, 2))
cell = maze.get_cell(1, 1)
neighbors = maze.get_accessible_neighbors(cell)
print(neighbors)

print("\n============Remove North wall============")
maze = Maze(3, 3, (0, 0), (2, 2))

current = maze.get_cell(1, 1)
north = maze.get_cell(1, 0)

maze.remove_wall(current, north)

neighbors = maze.get_accessible_neighbors(current)

print(neighbors)
