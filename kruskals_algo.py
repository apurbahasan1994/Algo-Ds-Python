class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in self.vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[yroot] += 1


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = []
        self.nodes = []
        self.MST = []

    def add_edge(self, source, dest, weight):
        self.graph.append([source, dest, weight])

    def add_nodes(self, node):
        self.nodes.append(node)

    def print_solution(self):
        for s, d, w in self.MST:
            print(f"{s} {d} - {w}")

    def kruskals(self):
        i, e = 0, 0
        dst = DisjointSet(self.nodes)
        self.graph.sort(key=lambda item: item[2])
        while e < self.V-1:  # edges are V-1 in tree, so no cycle.
            s, d, w = self.graph[i]
            i += 1
            x = dst.find(s)
            y = dst.find(d)

            if x != y:
                e += 1
                self.MST.append([s, d, w])
                dst.union(s, d)
        self.print_solution()


g = Graph(5)
g.add_nodes("A")
g.add_nodes("B")
g.add_nodes("C")
g.add_nodes("D")
g.add_nodes("E")
g.add_edge("A", "B", 5)
g.add_edge("A", "C", 13)
g.add_edge("A", "E", 15)
g.add_edge("B", "A", 5)
g.add_edge("B", "C", 10)
g.add_edge("B", "D", 8)
g.add_edge("C", "A", 13)
g.add_edge("C", "B", 10)
g.add_edge("C", "E", 20)
g.add_edge("C", "D", 6)
g.add_edge("D", "B", 8)
g.add_edge("D", "C", 6)
g.add_edge("E", "A", 15)
g.add_edge("E", "C", 20)
g.kruskals()
