import os
from node import Node
from visualize import visualize


def read_file(file_name: str = 'maze.txt'):
    f = open(file_name, 'r')
    n_bonus_points = int(next(f)[:-1])
    bonus_points = []
    for i in range(n_bonus_points):
        x, y, reward = map(int, next(f)[:-1].split(' '))
        bonus_points.append(Node(x, y, reward))

    text = f.read()
    maze = [list(i) for i in text.splitlines()]
    f.close()

    return bonus_points, maze

bonus_points, maze = read_file('maze_map.txt')

graph = []
for i in range(len(maze)):
    row = []
    for j in range(len(maze[0])):
        row.append(Node(i, j))

        if(maze[i][j] == 'x'):
            row[j].isWall = True

        elif maze[i][j] == 'S':
            start = row[j]

        elif maze[i][j] == ' ':
            if (i == 0) or (i == len(maze)-1) or (j == 0) or (j == len(maze[0])-1):
                end = row[j]

        elif maze[i][j] == '+':
            for point in bonus_points:
                if row[j].isEqual(point):
                    row[j].reward = point.reward

    graph.append(row)


visualize(maze, bonus_points, start, end)

