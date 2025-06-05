from search.bfs import abstract_bfs as bfs

class Edge:
    # Ребро
    def __init__(self, fr, to):
        self.fr = fr
        self.to = to

    def __str__(self):
        return f"{self.fr} <-> {self.to}"

    def reversed(self):
        return Edge(fr=self.to, to=self.fr)


class Graph:

    def __init__(self, vertexs: list):
        self._vertexs = vertexs
        self._edges = []

    def add_vertex(self, vertex):
        self._vertexs.append(vertex)

    def _add_edge(self, edge):
        self._edges.append(edge)
        self._edges.append(edge.reversed())

    def add_edge_by_indices(self, fr, to):
        self._add_edge(Edge(fr, to))

    def add_edge_by_vertex(self, vertex_fr, vertex_to):
        fr = self._vertexs.index(vertex_fr)
        to = self._vertexs.index(vertex_to)
        self.add_edge_by_indices(fr, to)

    def get_vertexs(self):
        return self._vertexs.copy()

    def get_edges(self):
        out = ""
        for i in self._edges:
            out += str(i)
            out += "\n"
        return out

    # количество ребер
    def edge_count(self):
        return len(self._edges)

    # количество вершин
    def vertex_count(self):
        return len(self._vertexs)

    # Вершина по индексу 0 -> "Иркутск"
    def vertex_at(self, index):
        return self._vertexs[index]

    # Индекс по вершине "Иркутск" -> 0
    def index_of(self, vertex):
        return self._vertexs.index(vertex)

    # Все соседние вершины, которые связаны с данным индексом
    def neighbours_for_index(self, index):
        eds = []
        for e in self._edges:
            if e.to == index:
                eds.append(e.fr)
        return list(map(self.vertex_at, eds))
        out = f"{index} ->"
        for edge in self._edges:
            if edge.fr == index:
                out += " " + str(self.vertex_at(edge.to))
            elif edge.to == index:
                out += " " + str(self.vertex_at(edge.fr))
        return out


    def neighbours_for_index2(self, index):
        eds = []
        for e in self._edges:
            if e.to == index:
                eds.append(e.fr)
        return eds
        out = []
        for edge in self._edges:
            if edge.fr == index:
                out.append(edge.to)
            elif edge.to == index:
                out.append(edge.fr)
        return out


    # Все соседние вершины, которые связаны с данной вершиной
    def neighbours_for_vertex(self, vertex):
        return self.neighbours_for_index(self.index_of(vertex))

    # Все ребра, связанные с вершиной, имеющей данный индекс
    def edges_for_index(self, index):
        out = []
        for edge in self._edges:
            if edge.fr == index: out.append(str(edge))
        return out

    # Все ребра, связанные с вершиной
    def edges_for_vertex(self, vertex):
        return self.edges_for_index(self._vertexs.index(vertex))

    def __str__(self):
        return self.get_edges()

if __name__ == "__main__":
    gr = Graph(["Irk.", "Ang."])
    #print(f"Vertexs: {gr.get_vertexs()}")
    gr.add_vertex("Nov.")
    #print(f"Vertexs: {gr.get_vertexs()}")
    gr.add_edge_by_vertex("Ang.", "Irk.")
    gr.add_edge_by_indices(0, 2)
    gr.add_vertex("Yso.")
    gr.add_edge_by_indices(2, 3)
    print(bfs("Irk.", lambda x: x == "Yso.", gr.neighbours_for_vertex))
    print(gr.neighbours_for_index2(0))