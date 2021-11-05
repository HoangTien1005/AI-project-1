import matplotlib.pyplot as plt
from node import Node


def visualize(maze, bonus, start, end, route=None):
    print(f'The height of the maze: {len(maze)}')
    print(f'The width of the maze: {len(maze[0])}')

    print(f'Starting point (x, y) = {start.x, start.y}')
    print(f'Ending point (x, y) = {end.x, end.y}')

    if route:
        print(f'Cost: {len(route)}')

    for _, point in enumerate(bonus):
        print(
            f'Bonus point at position (x, y) = {point.x, point.y} with point {point.reward}')

    walls = []
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'x':
                walls.append(Node(i, j))

    if route:
        direction = []
        for i in range(1, len(route)):
            if route[i].x-route[i-1].x > 0:
                direction.append('v')
            elif route[i].x-route[i-1].x < 0:
                direction.append('^')
            elif route[i].y-route[i-1].y > 0:
                direction.append('>')
            else:
                direction.append('<')

        direction.pop(0)

    # Drawing the map
    ax = plt.figure(figsize=(10, 5), dpi=100).add_subplot(111)

    for i in ['top', 'bottom', 'right', 'left']:
        ax.spines[i].set_visible(False)

    plt.scatter([i.y for i in walls], [-i.x for i in walls],
                marker='X', s=100, color='black')

    plt.scatter([i.y for i in bonus], [-i.x for i in bonus],
                marker='P', s=100, color='green')

    plt.scatter(start.y, -start.x, marker='*',
                s=150, color='gold')

    if route:
        for i in range(len(route)-2):
            plt.scatter(route[i+1].y, -route[i+1].x,
                        marker=direction[i], color='silver')

    plt.text(end.y, -end.x, 'EXIT', color='red',
             horizontalalignment='center',
             verticalalignment='center')

    plt.xticks([])
    plt.yticks([])
    plt.show()


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


def init(maze, bonus_points = None):
    graph = []
    for i in range(len(maze)):
        row = []
        for j in range(len(maze[0])):
            node = Node(i, j)

            if maze[i][j] == 'x':
                node.isWall = True

            elif maze[i][j] == 'S':
                start = node

            elif maze[i][j] == ' ':
                if (i == 0) or (i == len(maze)-1) or (j == 0) or (j == len(maze[0])-1):
                    end = node

            elif maze[i][j] == '+':
                for point in bonus_points:
                    if node.isEqual(point):
                        node.reward = point.reward
            row.append(node)

        graph.append(row)

    for i in range(1, len(graph) - 1):
        for j in range(1, len(graph[0]) - 1):
            graph[i][j].addNeighbors(graph)
    return graph, start, end
