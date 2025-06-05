def bfs(graph, start, finish):
    visited = {start: None}
    queue = [start]
    while queue:
        cur_node = queue.pop(0)
        if cur_node == finish:
            return visited
        if cur_node in graph:
            for next_node in graph[cur_node]:
                if next_node not in visited:
                    queue.append(next_node)
                    visited[next_node] = cur_node
    return "Path not locate!"


class Node:
    def __init__(self, state, parent):
        self.parent = parent
        self.state = state

    def __str__(self):
        if self.parent:
            return str(self.parent) + " -> " + str(self.state)
        else:
            return str(self.state)


#node = Node("Moscow", None)
#node_child = Node("Yaroslavl", node)
#node_child_child = Node("Rostov", node_child)

def abstract_bfs(initial, finish_test, successors):
    visited = {initial}
    queue = [Node(initial, None)]
    while queue:
        cur_node = queue.pop(0)

        if finish_test(cur_node.state):
            return cur_node

        for next_node in successors(cur_node.state):
            if next_node not in visited:
                queue.append(Node(next_node, cur_node))
                visited.add(next_node)

    return None

