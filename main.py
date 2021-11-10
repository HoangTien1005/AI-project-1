import os
from node import Node
from bfs import BFS
from dfs import DFS
from greedy import *
from a_star import A_Star
from utilities import *


bonus_points, maze = read_file('map6.txt')

graph, start, end, bonus_points = init(maze, bonus_points)



print('1. DFS (Depth First Search)')
print('2. BFS (Breadth First Search)')
print('3. A* (A Star)')
print('4. Greedy Best First Search')
print('Select algorithm: ')
selection = int(input())
if selection == 1:
    route, cost = DFS(start, end)
elif selection == 2:
    route, cost = BFS(start, end)
elif selection == 3:
    print('1. Manhattan Distance Heuristic')
    print('2. Euclidean Distance Heuristic')
    type = None
    while type != 1 and type != 2:
        type = int(input())
    tempbonus = bonus_points[:]
    route, cost = A_Star(start, end, tempbonus, type)
elif selection == 4:
    print('1. Manhattan Distance Heuristic')
    print('2. Euclidean Distance Heuristic')
    type = None
    while type != 1 and type != 2:
        type = int(input())
    route, cost = Greedy(start, end, bonus_points, type)
else: 
    exit()



visualize(maze, bonus_points, start, end, route, cost)
