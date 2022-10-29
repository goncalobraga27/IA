#############################################
# Author:                                   #
# Created date:                             #
# Last update:                              #
#############################################
class Node:
    # Constructor of a node given the coordinates
    def __init__(self, n):
        self.coord = n

    # Returns the string representation of the node to be read 'friendly'
    def __str__(self):
        return str(self.coord)

    # Returns 'official' representation of the object
    def __repr__(self):
        return "Node " + str(self.coord)

    # Get the coordinates of a node
    def get_coord(self):
        return self.coord

    # Update node coordinates
    def set_coord(self, n):
        self.coord = n

    # Method used to compare two nodes, in this case two nodes are equal if they have the same coordinates
    def __eq__(self, other):
        return (self.coord[0] == other.coord[0]) and (self.coord[1] == other.coord[1])

    # Returns the hash of a node
    def __hash__(self):
        return hash(self.coord)
