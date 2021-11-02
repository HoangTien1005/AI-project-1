import matplotlib.pyplot as plt
from node import Node

# """
# Args:
#   1. maze: The maze read from the input file,
#   2. walls: The array of wall nodes,
#   3. bonus: The array of bonus nodes,
#   4. start, end: The starting and ending nodes,
#   5. route: The route from the starting node to the ending one


def visualize(maze, bonus, start, end, route = None ):
    print(f'The height of the maze: {len(maze)}')
    print(f'The width of the maze: {len(maze[0])}')    

    print(f'Starting point (x, y) = {start.x, start.y}')
    print(f'Ending point (x, y) = {end.x, end.y}')
    
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
    ax = plt.figure(dpi=100).add_subplot(111)

    for i in ['top', 'bottom', 'right', 'left']:
        ax.spines[i].set_visible(False)

    plt.scatter([i.y for i in walls], [-i.x for i in walls],
                marker='X', s=100, color='black')


    plt.scatter([i.y for i in bonus], [-i.x for i in bonus],
                marker='P', s=100, color='green')

    plt.scatter(start.y, -start.x, marker='*',
                s=100, color='gold')

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


