class graph:
    def _init_(self):
        self.matrix=[]
        self.vertices=[]
    def insert_vertex(self,vertex):
        self.vertices.append(vertex)
        row=[]
        for i in range(len(self.vertices)-1):
            row.append(0)
        self.matrix.append(row)
        for each_row in self.matrix:
            each_row.append(0)
    def add_edge(self,start,end,wt):
        start_index=self.vertices.index(start)
        end_index=self.vertices.index(end)

        self.matrix[start_index][end_index]=wt
        self.matrix[end_index][start_index]=wt                
g1=graph()
g1.insert_vertex('A')
g1.insert_vertex('B')
g1.insert_vertex('C')
print(g1.vertices)
print(g1.matrix)
g1.add_edge('A','B',4)
print(g1.matrix)