from __future__ import annotations
from dataclasses import dataclass

class Edge:
    u = int() # вершина "откуда"
    v = int() # вершина "куда"

    def reversed(self):
        return Edge(self.v, self.u)
    def __str__(self):
        return f"{self.u} -> {self.v}"