from graph import Graph


class Parser:

    def __init__(self, mapa=None):
        self.mapa = mapa
        self.dic = dict()  # Dictionary for saving the map (Line index, Column index) : Character

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
                        self.dic[(n_lines, i)] = 1
                    case '-':  # '-' (Track) is 0
                        self.dic[(n_lines, i)] = 0
                    case 'F':  # 'F' (End) is 2
                        self.dic[(n_lines, i)] = 2
                    case 'P':  # 'P' (Start) is -1
                        self.dic[(n_lines, i)] = -1

            n_lines = n_lines + 1  # Next line

        return self.dic  # Return the map in a new format

    def get_adjacency_list(self, key):  # Get adjacency list of a graph
        return_list = []
        for k in self.dic:  # Go through all the keys; key is a coordinate
            if (self.dic[k] == 0) or (self.dic[k] == 2) or (self.dic[k] == -1):  # Verify is the node can be adjacent
                if (k[0] == (key[0] + 1)) and (k[1] == key[1]):  # Verify if is adjacent to the given node
                    return_list.append(k)  # Put the node in the list
                elif (k[0] == (key[0] - 1)) and (k[1] == (key[1])):
                    return_list.append(k)
                elif (key[0] == (k[0])) and (k[1] == (key[1]) + 1):
                    return_list.append(k)
                elif (key[0] == (k[0])) and (k[1] == (key[1]) - 1):
                    return_list.append(k)
                elif (k[0] == (key[0] + 1)) and (k[1] == (key[1]) + 1):
                    return_list.append(k)
                elif (k[0] == (key[0] + 1)) and (k[1] == (key[1]) - 1):
                    return_list.append(k)
                elif (k[0] == (key[0] - 1)) and (k[1] == (key[1]) - 1):
                    return_list.append(k)
                elif (k[0] == (key[0] - 1)) and (k[1] == (key[1]) + 1):
                    return_list.append(k)

        return return_list  # Return adjacency list

    def create_graph(self):  # Creates the most adequate graph for the existing dictionary
        g = Graph()  # Create a graph
        for key in self.dic:  # Go through the dictionary
            match self.dic[key]:
                case 0:  # If the node belongs to the track
                    list1 = self.get_adjacency_list(key)  # Get the list of adjacent nodes
                    for it1 in list1:  # Go through the list
                        g.add_edge(key, it1, 1)  # Add edge to the graph
                case 2:  # If the node belongs to the goal
                    list2 = self.get_adjacency_list(key)
                    for it2 in list2:
                        g.add_edge(key, it2, 1)
                case -1:  # If the node belongs to the start
                    list3 = self.get_adjacency_list(key)
                    for it3 in list3:
                        g.add_edge(key, it3, 1)
        return g  # Return the new graph
