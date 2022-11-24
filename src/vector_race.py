from graph import Graph
from node import Node

class VectorRace:

    def __init__(self, mapa=None):
        self.mapa = mapa
        self.dic = dict()  # Dictionary for saving the map (Line index, Column index) : Character
        self.graph = Graph(True)
        self.start = None
        self.goal = list()
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
                        self.goal.append((i, n_lines))
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

        for mv in self.moves:
            vel = (vx + mv[0], vy + mv[1])
            pos = (x + vx + mv[0], y + vy + mv[1])
            ns_coord = self.go_to_next_state(node.coord, pos)
            if ns_coord == pos:
                return_list.append((Node(pos, vel), 1))
            elif ns_coord in self.goal:
                return_list.append((Node(ns_coord, vel), 1))
            else:
                return_list.append((Node(ns_coord, (0, 0)), 25))

        return return_list

    def go_to_next_state(self, ant_pos, next_pos):
        mid_pos = ant_pos
        if ant_pos[0] < next_pos[0]:
            mid_pos = (ant_pos[0]+1, ant_pos[1])
        elif ant_pos[0] > next_pos[0]:
            mid_pos = (ant_pos[0]-1, ant_pos[1])
        elif ant_pos[1] < next_pos[1]:
            mid_pos = (ant_pos[0], ant_pos[1]+1)
        elif ant_pos[1] > next_pos[1]:
            mid_pos = (ant_pos[0], ant_pos[1]-1)

        if self.dic[mid_pos] == 1:
            return ant_pos
        elif self.dic[mid_pos] == 2:
            return mid_pos
        elif mid_pos == next_pos:
            return next_pos
        else:
            return self.go_to_next_state(mid_pos, next_pos)

    def acrescentaHeuristica(self):
        for node in self.graph.nodes:
            self.graph.m_h[node.coord] = self.graph.calculaHeuristica(node.coord,self.goal[0])


    def create_graph(self):  # Creates the most adequate graph for the existing dictionary
        states = []
        visited = []
        states.append(Node(self.start, (0, 0)))
        visited.append(Node(self.start, (0, 0)))

        while len(states) > 0:
            state = states.pop()
            result_states = self.expand(state)

            for st, cost in result_states:
                self.graph.add_edge(state, st, cost)
                if (st not in visited) and (st.coord not in self.goal):
                    states.append(st)
                    visited.append(state)

    def search_dfs_race(self):
        return self.graph.search_dfs(Node(self.start, (0, 0)), Node(self.goal[0], (1, 1)))

    def search_bfs_race(self):
        return self.graph.search_bfs(Node(self.start, (0, 0)), Node(self.goal[0], (2, -1)))

    def search_greedy(self):
        return self.graph.greedy(Node(self.start, (0, 0)), Node(self.goal[0], (1, 1)))
