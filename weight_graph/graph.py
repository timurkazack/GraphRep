from typing import TypeVar, Generic, List, Optional
from edge import Edge

V = TypeVar('V') # тип вершин графа

class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []):
       self._vertices: List[V] = vertices
       self._edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self):
       return len(self._vertices)  # Количество вершин

    @property
    def edge_count(self):
       return sum(map(len, self._edges))  # Количество ребер


    # Добавляем вершину в граф и возвращаем ее индекс
    def add_vertex(self, vertex: V):
        self._vertices.append(vertex)
        self._edges.append([])  # Добавляем пустой список для ребер
        return self.vertex_count - 1  # Возвращаем индекс по добавленным вершинам


    # Это ненаправленный граф,
    # поэтому мы всегда добавляем вершины в обоих направлениях
    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())


    # Добавляем ребро, используя индексы вершин (удобный метод)
    def add_edge_by_indices(self, u: int, v: int):
        edge: Edge = Edge(u, v)
        self.add_edge(edge)


    # Добавляем ребро, просматривая индексы вершин (удобный метод)
    def add_edge_by_vertices(self, first: V, second: V):
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)


    # Поиск вершины по индексу
    def vertex_at(self, index: int):
        return self._vertices[index]

    # Поиск индекса вершины в графе
    def index_of(self, vertex: V):
        return self._vertices.index(vertex)

    # Поиск вершин, с которыми связана вершина с заданным индексом
    def neighbors_for_index(self, index: int):
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    # Поиск индекса вершины; возвращает ее соседей (удобный метод)
    def neighbors_for_vertex(self, vertex: V):
        return self.neighbors_for_index(self.index_of(vertex))

    # Возвращает все ребра, связанные с вершиной, имеющей заданный индекс
    def edges_for_index(self, index: int):
        return self._edges[index]

    # Поиск индекса вершины; возвращает ее ребра (удобный метод)
    def edges_for_vertex(self, vertex: V):
        return self.edges_for_index(self.index_of(vertex))

    # Упрощенный красивый вывод графа
    def __str__(self) -> str:
     desc: str = ""
     for i in range(self.vertex_count):
        desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
     return desc

