class Node:
    def __init__(self, parent, position):
        self.parent = parent
        self.position = position

        # g is the distance from the starting node
        # h is the estimated distance to the target node
        # f is the sum of g and h
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position