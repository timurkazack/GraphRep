from __future__ import annotations
from dataclasses import dataclass
from edge import Edge

class WeightedEdge(Edge):
    weight: float
    def reversed(self):
        return WeightedEdge(self.v, self.u, self.weight)
    # так можно упорядочить ребра по весу и найти ребро с минимальным весом
    def __lt__(self, other: WeightedEdge) -> bool:
        return self.weight < other.weight
    def __str__(self) -> str:
        return f"{self.u} {self.weight}> {self.v}"