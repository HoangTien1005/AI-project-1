from utilities import *
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.greedy import Greedy
from algorithms.a_star_1 import A_Star_1
from algorithms.a_star_2 import A_Star_2


print('Select your maze:  (1 -> 5: no bonus  ;  6 -> 8: bonus)')
mazes_number = int(input())

bonus_points, maze = read_file(f'./mazes/{mazes_number}.txt')
graph, start, end, temp_bonus_points = init(maze, bonus_points)



if(mazes_number in range(1, 6)):
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
        route, cost = A_Star_1(graph, start, end, type, temp_bonus_points)

    elif selection == 4:
        print('1. Manhattan Distance Heuristic')
        print('2. Euclidean Distance Heuristic')
        type = None
        while type != 1 and type != 2:
            type = int(input())
        route, cost = Greedy(start, end, bonus_points, type)


elif (mazes_number in range(6, 9)):
    print('We will be using A* for the bonus maps')
    print('1. Manhattan Distance Heuristic')
    print('2. Euclidean Distance Heuristic')
    type = None
    while type != 1 and type != 2:
        type = int(input())

    print('1. Brute Force (get all bonus points on map)')
    print('2. Nearly optimal (get bonus points with conditions)')
    selection = int(input())

    if selection == 1:
        route, cost = A_Star_1(graph, start, end, type, temp_bonus_points)

    elif selection == 2:
        route, cost = A_Star_2(graph, start, end, type, temp_bonus_points)

visualize(maze, bonus_points, start, end, route, cost)
