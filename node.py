class Node:
    def __init__(self, x, y, reward = 0, f = 0, g = 0, h = 0, neighbors = [], previous = None, isWall = False):
        self.x = x
        self.y = y
        self.reward = reward
        self.f = f
        self.g = g
        self.h = h
        self.neighbors = neighbors
        self.previous = previous
        self.isWall = isWall

    def show(self):
        print(f'(x, y) = {self.x, self.y}')
    
    def isEqual(self, anotherNode):
        return self.x == anotherNode.x and self.y == anotherNode.y


