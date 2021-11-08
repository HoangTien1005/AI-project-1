import os
from node import Node
from bfs import BFS
from dfs import DFS
from greedy import *
from a_star import A_Star
from utilities import *


bonus_points, maze = read_file('map5.txt')

graph, start, end = init(maze, bonus_points)



print('1. DFS (Depth First Search)')
print('2. BFS (Breadth First Search)')
print('3. A* (A Star)')
print('4. Greedy Best First Search')
print('Select algorithm: ')
selection = int(input())
if selection == 1:
    route = DFS(start, end)
elif selection == 2:
    route = BFS(start, end)
elif selection == 3:
    print('1. Manhattan Distance Heuristic')
    print('2. Euclidean Distance Heuristic')
    type = None
    while type != 1 and type != 2:
        type = int(input())
    route = A_Star(start, end, type)
elif selection == 4:
    print('1. Manhattan Distance Heuristic')
    print('2. Euclidean Distance Heuristic')
    type = None
    while type != 1 and type != 2:
        type = int(input())
    route = Greedy(start, end, type)
else: 
    exit()



visualize(maze, bonus_points, start, end, route)
