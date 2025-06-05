from heapq import heappush, heappop

graph = {
  'A': { 'B': 1, 'C': 4},
  'B': { 'A': 1, 'C': 2},
  'C': { 'A': 4, 'B': 2}
}
def dijkstra(graph, start):
  distances = {vertex: float('infinity') for vertex in graph}
  distances[start] = 0
  paths = {}
  queue = [(0, start)]

  while queue:
    current_distance, current_vertex = heappop(queue)

    if current_distance > distances[current_vertex]:
      continue

    for neightbour, weight in graph[current_vertex].items():
      distance = current_distance + weight

      if distance < distances[neightbour]:
        distances[neightbour] = distance
        paths[neightbour] = current_vertex
        heappush(queue, (distance, neightbour))
  return distances, paths

print(dijkstra(graph, 'A'))