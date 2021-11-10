import matplotlib.pyplot as plt
from node import Node
import math


def visualize(maze, bonus, start, end, route=None, cost=None):
    print(f'The height of the maze: {len(maze)}')
    print(f'The width of the maze: {len(maze[0])}')

    print(f'Starting point (x, y) = {start.x, start.y}')
    print(f'Ending point (x, y) = {end.x, end.y}')

    if cost:
        print(f'Cost: {cost}')

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


def read_file(file_name: str = './mazes/1.txt'):
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


# initialize all the variables needed
def init(maze, bonus_points = None):
    graph = []
    temp_bonus_points = []
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
                    if node.is_equal(point):
                        node.reward = point.reward
                        temp_bonus_points.append(node)
            row.append(node)

        graph.append(row)

    for i in range(1, len(graph) - 1):
        for j in range(1, len(graph[0]) - 1):
            graph[i][j].add_neighbors(graph)
    return graph, start, end, temp_bonus_points


# get the path from start to end using backtracking
def get_route(start, end):
    route = [end]
    while not route[-1].is_equal(start):
        route.append(route[-1].previous)
    route.reverse()
    return route

# reset every node.g in graph
def wayPaving(graph):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            graph[i][j].g = 0
            
# reset every node.g in arr
def reset(arr):
    for node in arr:
           node.g = 0

def swap_arr_element(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]

# Manhattan heuristic
def manhattan(node, end):
    h = abs(node.x - end.x) + abs(node.y - end.y)
    return h 

# Euclidean heuristic
def euclidean(node, end):
    h = math.sqrt((node.x - end.x)**2 + (node.y - end.y)**2)
    return h

# return the heuristic based on type
def heuristic(node, end, type = 1):
    if type == 1:
        return manhattan(node, end)
    
    return euclidean(node, end)
    
# sorting based on node.f
def increasing_sort(arr, end, type = 1):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if j < len(arr):
                if arr[i].f > arr[j].f:
                    swap_arr_element(arr,i,j)  

#sorting the array of bonus points (A* brute-force strategy)
def bonus_sort_1(arr, end, type = 1):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if j < len(arr):
                if heuristic(arr[i], end, type) > heuristic(arr[j], end, type):
                    swap_arr_element(arr,i,j)   


#sorting the array of bonus points (A* nearly optimal strategy)
def bonus_sort_2(arr,start, end, type = 1):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if j < len(arr):
                score_i = heuristic(arr[i], start, type) + heuristic(arr[i], end, type) + arr[i].reward
                score_j = heuristic(arr[j], start, type) + heuristic(arr[j], end, type) + arr[j].reward
                if score_i > score_j:
                    swap_arr_element(arr,i,j)   
