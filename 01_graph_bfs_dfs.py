from collections import deque

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],

    'E': ['K', 'L'],
    'F': ['M'],
    'G': ['N'],
    'H': ['O', 'P'],
    'I': ['Q'],
    'J': ['R'],

    'K': [],
    'L': ['S'],
    'M': ['T'],
    'N': [],
    'O': ['U'],
    'P': [],
    'Q': [],
    'R': ['V'],
    'S': [],
    'T': [],
    'U': [],
    'V': []
}


def BFS(start, target):
    queue = deque([start])
    visited = set()
    steps = 0
    checks = 0

    print("\n--- BFS Search ---")

    while queue:
        current = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        steps += 1

        print("Visit:", current)

        if current == target:
            print("Target found!")
            print("Steps:", steps)
            print("Checks:", checks)
            return

        for neighbor in graph[current]:
            checks += 1
            print("  Check:", neighbor)

            if neighbor not in visited:
                queue.append(neighbor)

    print("Target not found")
    print("Steps:", steps)
    print("Checks:", checks)


def DFS(start, target):
    stack = [start]
    visited = set()
    steps = 0
    checks = 0

    print("\n--- DFS Search ---")

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        steps += 1

        print("Visit:", current)

        if current == target:
            print("Target found!")
            print("Steps:", steps)
            print("Checks:", checks)
            return

        for neighbor in reversed(graph[current]):
            checks += 1
            print("  Check:", neighbor)

            if neighbor not in visited:
                stack.append(neighbor)

    print("Target not found")
    print("Steps:", steps)
    print("Checks:", checks)


# Take Start and Target from the user
start = input("Enter Start Node: ").upper()
target = input("Enter Target Node: ").upper()

BFS(start, target)
DFS(start, target)
