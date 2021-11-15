from utilities import *

def increasingSort(arr, end, type = 1): # Calculate the distance from each node to END point
    for i in range(len(arr)):           # Rearrange nodes due to it
        Heuristic(arr[i], end, type)
        arr[i].f = arr[i].g + arr[i].h

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if j < len(arr):
                if arr[i].f > arr[j].f:
                    swapArrElement(arr,i,j)

def Greedy(start, end, bonus_points = None, type = 1):
    PriorityQueue = []
    PriorityQueue.append(start)

    while PriorityQueue:
        increasingSort(PriorityQueue, end, type)
        node = PriorityQueue.pop(0)
        node.isVisited = True
        if node.isEqual(end):
            route = getRoute(start,node)
            return route, len(route)
        
        for neighbor in node.neighbors:
            if neighbor not in PriorityQueue and not neighbor.isVisited:
                neighbor.previous = node
                PriorityQueue.append(neighbor)
           
    
