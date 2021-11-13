class Node:
    def __init__(self, x, y, reward=0, f=0, g=0, h=0, neighbors=[], previous=None, isWall=False, isVisited=False):
        self.x = x
        self.y = y
        self.reward = reward
        self.f = f
        self.g = g
        self.h = h
        self.neighbors = neighbors[:]
        self.previous = previous
        self.isWall = isWall
        self.isVisited = isVisited

    def add_neighbors(self, graph):
        if self.isWall:
            return
            
        m = len(graph)
        n = len(graph[0])
        if self.x + 1 < m and not graph[self.x + 1][self.y].isWall:
            self.neighbors.append(graph[self.x + 1][self.y])

        if self.x - 1 > -1 and not graph[self.x - 1][self.y].isWall:
            self.neighbors.append(graph[self.x - 1][self.y])

        if self.y + 1 < n and not graph[self.x][self.y + 1].isWall:
            self.neighbors.append(graph[self.x][self.y + 1])

        if self.y - 1 > -1 and not graph[self.x][self.y - 1].isWall:
            self.neighbors.append(graph[self.x][self.y - 1])

    def show(self):
        print(f'(x, y) = {self.x, self.y}')
        for neighbor in self.neighbors:
            print(neighbor.x, neighbor.y)

    def is_equal(self, anotherNode):
        return self.x == anotherNode.x and self.y == anotherNode.y
