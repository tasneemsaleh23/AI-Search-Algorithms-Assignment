from collections import deque

maze = [
    "###                 #########",
    "#   ###################   # #",
    "# ####                # # # #",
    "# ################### # # # #",
    "#                     # # # #",
    "##################### # # # #",
    "#   ##                # # # #",
    "# # ## ### ## ######### # # #",
    "# #    #   ##B#         # # #",
    "# # ## ################ # # #",
    "### ##             #### # # #",
    "### ############## ## # # # #",
    "###             ##    # # # #",
    "###### ######## ####### # # #",
    "###### ####             #   #",
    "A      ######################"
]


def find_position(maze, target):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == target:
                return row, col


def bfs_maze(maze):

    start = find_position(maze, 'A')
    target = find_position(maze, 'B')

    queue = deque([start])

    visited = set()
    visited.add(start)

    parent = {start: None}

    explored_cells = 0

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    print("--- Maze BFS Search ---")

    while queue:

        current = queue.popleft()
        explored_cells += 1

        print("Explore:", current)

        if current == target:
            print("B found!")
            break

        row, col = current

        for dr, dc in directions:

            new_row = row + dr
            new_col = col + dc

            # Check boundaries
            if new_row < 0 or new_row >= len(maze):
                continue

            if new_col < 0 or new_col >= len(maze[0]):
                continue

            # Wall
            if maze[new_row][new_col] == '#':
                continue

            new_cell = (new_row, new_col)

            # Avoid repeated cells
            if new_cell in visited:
                continue

            visited.add(new_cell)
            parent[new_cell] = current

            queue.append(new_cell)

    # Build the path
    path = []

    if target in parent:

        current = target

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

    print("\nNumber of explored cells:", explored_cells)

    print("\nFinal Path:")
    print(path)

    # Print maze with path
    result = [list(row) for row in maze]

    for row, col in path:

        if result[row][col] != 'A' and result[row][col] != 'B':
            result[row][col] = '.'

    print("\nMaze with Path:")

    for row in result:
        print(''.join(row))


bfs_maze(maze)