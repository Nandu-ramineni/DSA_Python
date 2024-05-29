class Graph:
    def __init__(self):
        self.vertices = {}
    def insert_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
    def insert_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)
    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].remove(vertex2)
            self.vertices[vertex2].remove(vertex1)
    def delete_vertex(self, vertex):
        if vertex in self.vertices:
            del self.vertices[vertex]
            for v in self.vertices:
                if vertex in self.vertices[v]:
                    self.vertices[v].remove(vertex)
                    
                
                    
                    
G=Graph()
G.insert_vertex('A')
G.insert_vertex('B')
G.insert_vertex('C')
G.insert_vertex('D')
G.insert_vertex('E')
G.insert_edge('A','B')
G.insert_edge('A','C')
G.insert_edge('B','D')
G.insert_edge('C','D')
G.insert_edge('D','E')
print(G.vertices)
G.delete_vertex('D')
print(G.vertices)
G.delete_edge('A','C')
print(G.vertices)

