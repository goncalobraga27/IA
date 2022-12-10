import math
from graph import Graph
from node import Node


class VectorRace:

    def __init__(self):  # Constructor of the object VectorRace
        self.show_map = list()
        self.game_map = dict()
        self.graph = Graph(True)
        self.start = None
        self.goal = list()
        self.moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

    @staticmethod
    def parser(circuit_file):  # This function do the parsing of the file .txt that contains the map of the game.
        race = VectorRace()
        file = open(circuit_file, "r")  # Open file for read
        lines = file.readlines()  # Read file lines
        file.close()  # Close file
        line_index = 1  # Counter for the number of lines

        lines.reverse()
        for line in lines:  # Go through all the lines
            line_length = len(line)
            for i in range(line_length):  # Go through all the characters in a line
                match line[i]:
                    case 'X':  # '#' (Wall)
                        race.game_map[(i + 1, line_index)] = 'X'
                    case '-':  # '-' (Track)
                        race.game_map[(i + 1, line_index)] = '-'
                    case 'F':  # 'F' (End)
                        race.goal.append((i + 1, line_index))
                        race.game_map[(i + 1, line_index)] = 'F'
                    case 'P':  # 'P' (Start)
                        race.start = (i + 1, line_index)
                        race.game_map[(i + 1, line_index)] = 'P'

            line_index += 1  # Next line

        return race

    def show_parser(self, circuit_file):  # This function do the parsing of the file .txt that contains the map of
        # the game.
        file = open(circuit_file, "r")  # Open file for read
        lines = file.readlines()  # Read file lines
        file.close()  # Close file
        line_index = 0  # Counter for the number of lines

        for line in lines:  # Go through all the lines
            self.show_map.append(list())
            for c in line:  # Go through all the characters in a line
                match c:
                    case 'X':  # '#' (Wall)
                        self.show_map[line_index].append('X')
                    case '-':  # '-' (Track)
                        self.show_map[line_index].append('-')
                    case 'F':  # 'F' (End)
                        self.show_map[line_index].append('F')
                    case 'P':  # 'P' (Start)
                        self.show_map[line_index].append('P')

            line_index += 1  # Next line

    def print_map(self, path=None):
        if path is None:
            path = []

        y_max = len(self.show_map)
        tam = len(path)
        i = 0
        for node in path:
            if (i != 0) and (i != tam-1) and (node.coord != self.start):
                self.show_map[y_max - node.coord[1]][node.coord[0] - 1] = 'C'
            i += 1

        out = ""
        for line in self.show_map:
            for c in line:
                out = out + c + " "
            out = out + "\n"

        tam = len(path)
        i = 0
        for node in path:
            if (i != 0) and (i != tam-1) and (node.coord != self.start):
                self.show_map[y_max - node.coord[1]][node.coord[0] - 1] = '-'
            i += 1
        return out

    def graph_heuristic(self):  # This function calculate the heuristic for every node of the graph
        final = self.goal[0]
        for n in self.graph.nodes:
            self.graph.heuristic[n] = math.sqrt(pow(n.coord[0] + final[0], 2) + pow(n.coord[1] + final[1], 2))

    def find_close_walls(self, node):
        vn1 = (-node.vel[1], node.vel[0])
        vn2 = (node.vel[1], -node.vel[0])

        wall1 = self.try_next_position(node.coord, (node.coord[0] + 100*vn1[0], node.coord[1] + 100*vn1[1]))
        wall2 = self.try_next_position(node.coord, (node.coord[0] + 100*vn2[0], node.coord[1] + 100*vn2[1]))

        return wall1, wall2

    # This function calculate the heuristic_wall for every node of the graph
    def graph_heuristic_wall(self):
        for n in self.graph.nodes:
            if n.coord not in self.goal:
                wall1, wall2 = self.find_close_walls(n)
                self.graph.heuristic[n] = abs(math.sqrt(pow(n.coord[0] + wall1[0], 2) + pow(n.coord[1] + wall1[1], 2)) - math.sqrt(pow(n.coord[0] + wall2[0], 2) + pow(n.coord[1] + wall2[1], 2)))
            else:
                self.graph.heuristic[n] = 0

    def advance_vertical(self, start_node, final_node,
                         director):  # This function returns the final node when moving in the vertical
        node = start_node
        if director[1] > 0:
            inc = 1
        else:
            inc = -1

        while node != final_node:
            node_temp = (node[0], node[1] + inc)
            if self.game_map[node_temp] == 'X':
                final_node = node
            elif self.game_map[node_temp] == 'F':
                node = node_temp
                final_node = node_temp
            else:
                node = node_temp

        return final_node

    def advance_horizontal(self, start_node, final_node,
                           director):  # This function returns the final node when moving in the horizontal
        node = start_node
        if director[0] > 0:
            inc = 1
        else:
            inc = -1

        while node != final_node:
            node_temp = (node[0] + inc, node[1])
            if self.game_map[node_temp] == 'X':
                final_node = node
            elif self.game_map[node_temp] == 'F':
                node = node_temp
                final_node = node_temp
            else:
                node = node_temp

        return final_node

    def advance_diagonal(self, start_node, final_node,
                         director):  # This function returns the final node when moving in the diagonal
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
                    if self.game_map[pos] == 'X':
                        node = previous_node
                        final_node = previous_node
                    elif self.game_map[pos] == 'F':
                        node = pos
                        final_node = pos
                    else:
                        pos_x = math.ceil(node_temp[0])
                        pos_y = math.trunc(node_temp[1])
                        pos = (pos_x, pos_y)
                        if self.game_map[pos] == 'X':
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
                    if self.game_map[pos] == 'X':
                        node = previous_node
                        final_node = previous_node
                    elif self.game_map[pos] == 'F':
                        node = pos
                        final_node = pos
                    else:
                        pos_x = math.trunc(node_temp[0])
                        pos_y = math.trunc(node_temp[1])
                        pos = (pos_x, pos_y)
                        if self.game_map[pos] == 'X':
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
                    p_x = math.ceil(node_temp[0])
                    pos_x = math.trunc(node_temp[0])
                pos_y = round(node_temp[1])
                pos = (pos_x, pos_y)
                if self.game_map[pos] == 'X':
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
                if self.game_map[pos] == 'X':
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
                if self.game_map[pos] == 'X':
                    node = previous_node
                    final_node = previous_node
                elif self.game_map[pos] == 'F':
                    node = pos
                    final_node = pos
                else:
                    previous_node = pos
                    node = node_temp

        return final_node

    def try_next_position(self, start_node, final_node):  # This function returns the next position of the new state
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

    def search_dfs_race(self):  # This function do the dfs search algorithm for the graph of the race
        return self.graph.search_dfs(Node(self.start, (0, 0)), self.goal)

    def search_bfs_race(self):  # This function do the bfs search algorithm for the graph of the race
        return self.graph.search_bfs(Node(self.start, (0, 0)), self.goal)

    def search_greedy_Distance_Heuristic(self):  # This function do the greedy algorithm for the graph of the race
        return self.graph.search_greedy_Distance_Heuristic(Node(self.start, (0, 0)), self.goal)

    def search_star_a_Distance_Heuristic(self):  # This function do the "a star" algorithm for the graph of the race
        return self.graph.search_star_a_Distance_Heuristic(Node(self.start, (0, 0)), self.goal)

    def search_greedy_Wall_Heuristic(self):  # This function do the greedy algorithm for the graph of the race
        return self.graph.search_greedy_Distance_Heuristic(Node(self.start, (0, 0)), self.goal)

    def search_star_a_Wall_Heuristic(self):  # This function do the "a star" algorithm for the graph of the race
        return self.graph.search_star_a_Distance_Heuristic(Node(self.start, (0, 0)), self.goal)
