import os
from node import Node
from Algorithms.bfs import BFS
from Algorithms.dfs import DFS
from Algorithms.greedy import Greedy
from Algorithms.a_star import A_Star
from Algorithms.a_star_2 import A_Star_2
from utilities import *

print('1. Map 1')
print('2. Map 2')
print('3. Map 3')
print('4. Map 4')
print('5. Map 5')
print('6. Map 6 (contains 2 bonus point, for A* only)')
print('7. Map 7 (contains 5 bonus point, for A* only)')
print('8. Map 8 (contains 10 bonus point, for A* only)')
print('Choose map:')

map = int(input())
if map >= 1 and map <= 8:
    file = "./Maps/map" + str(map) + ".txt"
else: 
    exit()

bonus_points, maze = read_file(file)

graph, start, end, bonus_points = init(maze, bonus_points)


if map >=1 and map <= 5:
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

else:
    print("1. Get all bonus points before get to Exit")
    print("2. Get bonus points only if it costs better Heuristic")
    print('Choose A* method:')
    selection = int(input())
    if selection == 1:
        print('1. Manhattan Distance Heuristic')
        print('2. Euclidean Distance Heuristic')
        type = None
        while type != 1 and type != 2:
            type = int(input())
        tempbonus = bonus_points[:]
        route, cost = A_Star(start, end, tempbonus, type)
    elif selection == 2:
        print('1. Manhattan Distance Heuristic')
        print('2. Euclidean Distance Heuristic')
        type = None
        while type != 1 and type != 2:
            type = int(input())
        tempbonus = bonus_points[:]
        route, cost = A_Star_2(start, end, tempbonus, type)
    else:
        exit()


visualize(maze, bonus_points, start, end, route, cost)
