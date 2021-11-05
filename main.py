import os
from node import Node
from bfs import BFS
from dfs import DFS
from utilities import *


bonus_points, maze = read_file('map3.txt')

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
# elif selection == 3:
#     route = A_Star(start, end)
# elif selection == 4:
#     route = greedy(start, end)
else: 
    exit()



visualize(maze, bonus_points, start, end, route)
