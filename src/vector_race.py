import math
from graph import Graph
from node import Node


class VectorRace:

    def __init__(self, mapa=None):
        self.map_file = mapa
        self.game_map = dict()
        self.graph = Graph(True)
        self.start = None
        self.goal = set()
        self.moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

    def parser(self):
        file = open(self.map_file, "r")  # Open file for read
        lines = file.readlines()  # Read file lines
        file.close()  # Close file
        line_index = 1  # Counter for the number of lines

        lines.reverse()
        for line in lines:  # Go through all the lines
            line_length = len(line)
            for i in range(line_length):  # Go through all the characters in a line
                match line[i]:
                    case '#':  # '#' (Wall)
                        self.game_map[(i + 1, line_index)] = '#'
                    case '-':  # '-' (Track)
                        self.game_map[(i + 1, line_index)] = '-'
                    case 'F':  # 'F' (End)
                        self.goal.add((i + 1, line_index))
                        self.game_map[(i + 1, line_index)] = 'F'
                    case 'P':  # 'P' (Start)
                        self.start = (i + 1, line_index)
                        self.game_map[(i + 1, line_index)] = 'P'

            line_index += 1  # Next line

    def graph_heuristic(self, final):
        for n in self.graph.nodes:
            self.graph.heuristic[n] = math.sqrt(pow(n.coord[0]+final[0], 2) + pow(n.coord[1]+final[1], 2))

    def advance_vertical(self, start_node, final_node, director):
        node = start_node
        if director[1] > 0:
            inc = 1
        else:
            inc = -1

        while node != final_node:
            node_temp = (node[0], node[1] + inc)
            if self.game_map[node_temp] == '#':
                final_node = node
            elif self.game_map[node_temp] == 'F':
                node = node_temp
                final_node = node_temp
            else:
                node = node_temp

        return final_node

    def advance_horizontal(self, start_node, final_node, director):
        node = start_node
        if director[0] > 0:
            inc = 1
        else:
            inc = -1

        while node != final_node:
            node_temp = (node[0] + inc, node[1])
            if self.game_map[node_temp] == '#':
                final_node = node
            elif self.game_map[node_temp] == 'F':
                node = node_temp
                final_node = node_temp
            else:
                node = node_temp

        return final_node

    def advance_diagonal(self, start_node, final_node, director):
        alpha = director[1] / director[0]
        beta = start_node[1] - alpha * start_node[0]
        node = start_node
        previous_node = start_node

        while node != final_node:
            cd = director[0] > 0 and director[1] > 0
            ce = director[0] < 0 and director[1] > 0
            bd = director[0] > 0 and director[1] < 0
            be = director[0] < 0 and director[1] < 0

            if cd:
                if alpha < 1:
                    node_temp = (node[0] + 0.5, alpha * (node[0] + 0.5) + beta)
                elif alpha > 1:
                    node_temp = ((node[1] + 0.5 - beta) / alpha, node[1] + 0.5)
                else:
                    node_temp = (node[0] + 0.5, node[1] + 0.5)
            elif ce:
                if alpha > -1:
                    node_temp = (node[0] - 0.5, alpha * (node[0] - 0.5) + beta)
                elif alpha < -1:
                    node_temp = ((node[1] + 0.5 - beta) / alpha, node[1] + 0.5)
                else:
                    node_temp = (node[0] - 0.5, node[1] + 0.5)
            elif bd:
                if alpha > -1:
                    node_temp = (node[0] + 0.5, alpha * (node[0] + 0.5) + beta)
                elif alpha < -1:
                    node_temp = ((node[1] - 0.5 - beta) / alpha, node[1] - 0.5)
                else:
                    node_temp = (node[0] + 0.5, node[1] - 0.5)
            else:
                if alpha < 1:
                    node_temp = (node[0] - 0.5, alpha * (node[0] - 0.5) + beta)
                elif alpha > 1:
                    node_temp = ((node[1] - 0.5 - beta) / alpha, node[1] - 0.5)
                else:
                    node_temp = (node[0] - 0.5, node[1] - 0.5)

            sp = str(node_temp[0]).split(".")
            x_dec = int(sp[1])
            sp = str(node_temp[1]).split(".")
            y_dec = int(sp[1])

            if x_dec == 5 and y_dec == 5:

                if cd or be:
                    pos_x = math.trunc(node_temp[0])
                    pos_y = math.ceil(node_temp[1])
                    pos = (pos_x, pos_y)
                    if self.game_map[pos] == '#':
                        node = previous_node
                        final_node = previous_node
                    elif self.game_map[pos] == 'F':
                        node = pos
                        final_node = pos
                    else:
                        pos_x = math.ceil(node_temp[0])
                        pos_y = math.trunc(node_temp[1])
                        pos = (pos_x, pos_y)
                        if self.game_map[pos] == '#':
                            node = previous_node
                            final_node = previous_node
                        elif self.game_map[pos] == 'F':
                            node = pos
                            final_node = pos
                        else:
                            previous_node = (round(node[0]), round(node[1]))
                            node = node_temp

                elif ce or bd:
                    pos_x = math.ceil(node_temp[0])
                    pos_y = math.ceil(node_temp[1])
                    pos = (pos_x, pos_y)
                    if self.game_map[pos] == '#':
                        node = previous_node
                        final_node = previous_node
                    elif self.game_map[pos] == 'F':
                        node = pos
                        final_node = pos
                    else:
                        pos_x = math.trunc(node_temp[0])
                        pos_y = math.trunc(node_temp[1])
                        pos = (pos_x, pos_y)
                        if self.game_map[pos] == '#':
                            node = previous_node
                            final_node = previous_node
                        elif self.game_map[pos] == 'F':
                            node = pos
                            final_node = pos
                        else:
                            previous_node = (round(node[0]), round(node[1]))
                            node = node_temp

            elif x_dec == 5:
                if node_temp[0] > node[0]:
                    p_x = math.trunc(node_temp[0])
                    pos_x = math.ceil(node_temp[0])
                else:
                    p_x = math.ceil(node_temp[1])
                    pos_x = math.trunc(node_temp[0])
                pos_y = round(node_temp[1])
                pos = (pos_x, pos_y)
                if self.game_map[pos] == '#':
                    node = previous_node
                    final_node = previous_node
                elif self.game_map[pos] == 'F':
                    node = pos
                    final_node = pos
                else:
                    previous_node = (p_x, pos_y)
                    node = node_temp

            elif y_dec == 5:
                pos_x = round(node_temp[0])
                if node_temp[1] > node[1]:
                    p_y = math.trunc(node_temp[1])
                    pos_y = math.ceil(node_temp[1])
                else:
                    p_y = math.ceil(node_temp[1])
                    pos_y = math.trunc(node_temp[1])
                pos = (pos_x, pos_y)
                if self.game_map[pos] == '#':
                    node = previous_node
                    final_node = previous_node
                elif self.game_map[pos] == 'F':
                    node = pos
                    final_node = pos
                else:
                    previous_node = (pos_x, p_y)
                    node = node_temp
            else:
                pos = (round(node_temp[0]), round(node_temp[1]))
                if self.game_map[pos] == '#':
                    node = previous_node
                    final_node = previous_node
                elif self.game_map[pos] == 'F':
                    node = pos
                    final_node = pos
                else:
                    previous_node = pos
                    node = node_temp

        return final_node

    def try_next_position(self, start_node, final_node):
        director = (final_node[0] - start_node[0], final_node[1] - start_node[1])

        if director[0] == 0 and director[1] == 0:
            node = final_node
        elif director[0] == 0:
            node = self.advance_vertical(start_node, final_node, director)
        elif director[1] == 0:
            node = self.advance_horizontal(start_node, final_node, director)
        else:
            node = self.advance_diagonal(start_node, final_node, director)

        return node

    def expand(self, node):  # Get adjacency list of a graph
        return_list = []

        x = node.coord[0]
        y = node.coord[1]
        vx = node.vel[0]
        vy = node.vel[1]

        for mv in self.moves:
            vel = (vx + mv[0], vy + mv[1])
            pos = (x + vx + mv[0], y + vy + mv[1])
            ns_coord = self.try_next_position(node.coord, pos)
            if ns_coord == pos:
                return_list.append((Node(pos, vel), 1))
            elif ns_coord in self.goal:
                return_list.append((Node(ns_coord, vel), 1))
            else:
                return_list.append((Node(ns_coord, (0, 0)), 25))

        return return_list

    def create_graph(self):  # Creates the most adequate graph for the existing dictionary
        states = set()
        visited = set()
        states.add(Node(self.start, (0, 0)))
        visited.add(Node(self.start, (0, 0)))

        while len(states) > 0:
            state = states.pop()
            visited.add(state)
            result_states = self.expand(state)

            for st, cost in result_states:
                self.graph.add_edge(state, st, cost)
                if st not in visited and (st.coord not in self.goal):
                    states.add(st)

    def search_dfs_race(self):
        return self.graph.search_dfs(Node(self.start, (0, 0)), self.goal)

    def search_bfs_race(self):
        return self.graph.search_bfs(Node(self.start, (0, 0)), self.goal)

    def search_greedy(self):
        return self.graph.search_greedy(Node(self.start, (0, 0)), self.goal)

    def search_star_a(self):
        return self.graph.search_star_a(Node(self.start, (0, 0)), self.goal)
