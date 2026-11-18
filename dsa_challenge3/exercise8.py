from collections import deque


def shortest_path(graph, start, target):
    queue = deque([[start]])

    visited = {start}

    while queue:

        path = queue.popleft()

        current = path[-1]

        if current == target:
            return path

        for neighbour in graph.get(current, []):

            if neighbour not in visited:

                visited.add(neighbour)

                queue.append(path + [neighbour])

    return None


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

print(shortest_path(graph, "A", "F"))