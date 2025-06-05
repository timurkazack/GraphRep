from typing import TypeVar, Generic, List, Tuple
from graph import Graph
from weighted_edge import WeightedEdge

V = TypeVar('V') # тип вершин в графе

class WeightedGraph(Generic[V], Graph[V]):
    def __init__(self, vertices: List[V] = []):
       self._vertices: List[V] = vertices
       self._edges: List[List[WeightedEdge]] = [[] for _ in vertices]

    def add_edge_by_indices(self, u: int, v: int, weight: float):
       edge: WeightedEdge = WeightedEdge(u, v, weight)
       self.add_edge(edge) # вызываем версию суперкласса

    def add_edge_by_vertices(self, first: V, second: V, weight: float):
       u: int = self._vertices.index(first)
       v: int = self._vertices.index(second)
       self.add_edge_by_indices(u, v, weight)

    def neighbors_for_index_with_weights(self, index: int):
       distance_tuples: List[Tuple[V, float]] = []
       for edge in self.edges_for_index(index):
           distance_tuples.append((self.vertex_at(edge.v), edge.weight))
       return distance_tuples

    def __str__(self) -> str:
       desc: str = ""
       for i in range(self.vertex_count):
           desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index_with_weights(i)}\n"
       return desc