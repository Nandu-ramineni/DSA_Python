from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            if node in self.graph:
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

    def delete_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)

    def update_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)

# Example usage:
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)

print("BFS traversal:")
g.bfs(1)

# Delete an edge
g.delete_edge(2, 4)

# Update an edge
g.update_edge(3, 7)

print("\nUpdated BFS traversal:")
g.bfs(1)