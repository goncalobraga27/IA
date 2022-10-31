from graph import Graph
from node import Node
import math


class VectorRace:

    def __init__(self, mapa=None):
        self.mapa = mapa
        self.dic = dict()  # Dictionary for saving the map (Line index, Column index) : Character
        self.graph = Graph(True)
        self.start = None
        self.goal = set()
        self.moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

        #   ----> x
        #   |
        #   v y

    def parser(self):
        file = open(self.mapa, "r")  # Open file for read
        lines = file.readlines()  # Read file lines
        file.close()  # Close file
        n_lines = 0  # Counter for the number of lines

        for line in lines:  # Go through all the lines
            line_length = len(line)
            for i in range(line_length):  # Go through all the characters in a line
                match line[i]:
                    case '#':  # '#' (Wall) is 1
                        self.dic[(i, n_lines)] = 1
                    case '-':  # '-' (Track) is 0
                        self.dic[(i, n_lines)] = 0
                    case 'F':  # 'F' (End) is 2
                        self.dic[(i, n_lines)] = 2
                        self.goal.add((i, n_lines))
                    case 'P':  # 'P' (Start) is -1
                        self.dic[(i, n_lines)] = -1
                        self.start = (i, n_lines)

            n_lines = n_lines + 1  # Next line

    def expand(self, node):  # Get adjacency list of a graph
        return_list = []

        x = node.coord[0]
        y = node.coord[1]
        vx = node.vel[0]
        vy = node.vel[1]

        if self.dic[node.coord] != 1:
            for mv in self.moves:
                vel = (vx + mv[0], vy + mv[1])
                pos = (x + vx + mv[0], y + vy + mv[1])
                if pos in self.dic.keys():
                    return_list.append(Node(pos, vel))

        return return_list  # Return adjacency list

    """
    def find_near_start(self, node_ant, node_now ):
        coord = (0, 0)
        dist = 100
        if self.dic[node_ant] == 0:
                temp = math.sqrt(math.pow(node_ant[0] + node_now[0], 2) + math.pow(node_ant[1] + node_now[1], 2))
                if dist > temp:
                    dist = temp
                    coord = key
    """

    def create_graph(self):  # Creates the most adequate graph for the existing dictionary
        states = []
        visited = []
        states.append(Node(self.start, (0, 0)))

        while len(states) > 0:
            state = states.pop()
            result_states = self.expand(state)

            for st in result_states:
                if (st not in visited) and (st.coord not in self.goal) and (self.dic[st.coord] != 1):
                    states.append(st)
                if self.dic[st.coord] == 1:
                    self.graph.add_edge(state, st, 25)
                    # self.graph.add_edge(st, , 0)
                else:
                    self.graph.add_edge(state, st, 1)

            visited.append(state)

    def search_dfs_race(self):
        return self.graph.search_dfs(Node(self.start, (0, 0)), Node(self.goal.pop(), (1, 1)))

    def search_bfs_race(self):
        return self.graph.search_bfs(Node(self.start, (0, 0)), Node(self.goal.pop(), (1, 1)))

