#############################################
# Author:                                   #
# Created date:                             #
# Last update:                              #
#############################################
import networkx as nx  # Graph handling library required for representation
import matplotlib.pyplot as plt  # Graph handling library required for representation
import math  # Library needed to be able to use the math.inf value (infinity)
import queue
from node import Node  # Import Node class


# Graph class has:
# A set of nodes
# A dictionary :  node : (adjacent node,peso)
# A flag for directed graph

class Graph:

    # Graph constructor
    def __init__(self, directed=False):
        self.nodes = set()
        self.directed = directed
        self.graph = dict()

    # Returns the string representation of a graph
    def __str__(self):
        out = ""
        for key in self.graph.keys():
            out = out + str(key) + ": " + str(self.graph[key]) + "\n"
        return out

    # Add edge to the graph, with weight
    def add_edge(self, n1, n2, weight):  # node1 and node2 are coordinates
        if n1 not in self.nodes:
            self.nodes.add(n1)
            self.graph[n1] = set()

        if n2 not in self.nodes:
            self.nodes.add(n2)
            self.graph[n2] = set()

        self.graph[n1].add((n2, weight))

        # If the graph is undirected, put the inverse edge
        if not self.directed:
            self.graph[n2].add((n1, weight))

    # Show edges
    def show_edges(self):
        out = ""
        for node in self.graph.keys():
            for (adjacent, weight) in self.graph[node]:
                out = out + str(node) + " -> " + str(adjacent) + " weight : " + str(weight) + "\n"
        return out

    # Return edge cost
    def get_arc_cost(self, node1, node2):
        edges = self.graph[node1]
        for (adjacent, weight) in edges:
            if adjacent == node2:
                return weight
        return math.inf

    # Return the cost of a path
    def path_cost(self, path):
        cost = 0
        i = 1
        while i < len(path):
            cost = cost + self.get_arc_cost(path[i-1], path[i])
            i = i + 1
        return cost

    def search_dfs(self, start, end, path=None, visited=None):
        if path is None:
            path = []
        if visited is None:
            visited = set()

        visited.add(start)
        path.append(start)

        if start == end:
            return path, self.path_cost(path)

        for (adjacent, weight) in self.graph[start]:
            if adjacent not in visited:
                result = self.search_dfs(adjacent, end, path, visited)
                if result is not None:
                    return result

        path.pop()
        return None

        # BFS search, returns path and the path cost
    def search_bfs(self, start, end):
        path = []
        visited = set()
        queue = []
        parent = dict()

        visited.add(start)
        queue.append(start)
        parent[start] = None

        if start == end:
            return path, 0

        while len(queue) != 0:
            node = queue.pop(0)
            for (adjacent, weight) in self.graph[node]:

                if adjacent == end:
                    parent[adjacent] = node
                    aux = adjacent
                    while aux is not None:
                        path.append(aux)
                        aux = parent[aux]

                    path.reverse()
                    return path, self.path_cost(path)

                if adjacent not in visited:
                    visited.add(adjacent)
                    parent[adjacent] = node
                    queue.append(adjacent)

        return None

    # Draw the graph
    def graph_draw(self):
        list_nodes = self.nodes
        g = nx.Graph()

        for node in list_nodes:
            g.add_node(node)
            for (adjacent, peso) in self.graph[node]:
                g.add_edge(node, adjacent, weight=peso)

        # Drawing
        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()
