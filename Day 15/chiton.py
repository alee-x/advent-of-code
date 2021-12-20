import numpy as np
from queue import PriorityQueue


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight


def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


def fileread():
    fname = "input.txt"
    paths = []
    with open(fname, "r") as fr:
        for line in fr.read().splitlines():
            tmp = [int(x) for x in line]
            paths.append(np.array(tmp))
    return np.array(paths)


def partone():
    paths = fileread()
    shape = paths.shape
    g = Graph(shape[0]*shape[1])
    for i in range(shape[0]):
        for j in range(shape[1]):
            v_a = [-1, 0, 1]
            h_a = [-1, 0, 1]
            if i == 0 and j == 0:
                continue


if __name__ == "__main__":
    partone()
