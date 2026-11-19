def has_cycle(graph):
    visited = set()
    active = set()

    def dfs(node):

        if node in active:
            return True

        if node in visited:
            return False

        visited.add(node)
        active.add(node)

        for neighbour in graph.get(node, []):

            if dfs(neighbour):
                return True

        active.remove(node)

        return False

    for node in graph:

        if node not in visited:

            if dfs(node):
                return True

    return False


graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}

print(has_cycle(graph))