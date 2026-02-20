class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, source, target):
        self.vertices[source].append(target)

my_graph = Graph()
my_graph.add_vertex("Youssef")
my_graph.add_vertex("Ali")

my_graph.add_edge("Youssef", "ML")
my_graph.add_edge("Youssef", "LLM")
my_graph.add_edge("Ali", "Web")

print(my_graph.vertices)
