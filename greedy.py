import math

def getRoute(start, end):
    route = [end]
    while not route[-1].isEqual(start):
        route.append(route[-1].previous.pop())
    route.reverse()
    return route


def swapArrElement(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]


def Manhattan(node, end):
    h = abs(node.x - end.x) + abs(node.y - end.y)
    return h 


def Euclidean(node, end):
    h = math.sqrt((node.x - end.x)**2 + (node.y - end.y)**2)
    return h

def Heuristic(node, end, type = 1):
    if type == 1:
        node.h = Manhattan(node, end)
    elif type == 2:
        node.h = Euclidean(node, end)

def increasingSort(arr, end, type = 1): # Calculate the distance from each node to END point
                                        # Rearrange nodes due to it
    for i in range(len(arr)):
        Heuristic(arr[i], end, type)
        arr[i].f = arr[i].g + arr[i].h

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if j < len(arr):
                if arr[i].f > arr[j].f:
                    swapArrElement(arr,i,j)


def Greedy(start, end, type = 1, bonus_points = []):
    PriorityQueue = []
    PriorityQueue.append(start)
    while PriorityQueue:
        node = PriorityQueue.pop(0)
        node.isVisited = True
        if node.isEqual(end):
            route = getRoute(start, end)
            return route, len(route)
        
        increasingSort(node.neighbors, end, type)

        for neighbor in node.neighbors:
            if neighbor not in PriorityQueue and not neighbor.isVisited:
                neighbor.previous.append(node)
                PriorityQueue.append(neighbor)



# def Greedy2(start, end, bonus_points = None):
#     PriorityQueue = []
#     PriorityQueue.append(start)
#     while PriorityQueue:
#         increasingSort(PriorityQueue, end)
#         node = PriorityQueue.pop(0)
#         node.isVisited = True
#         if node.isEqual(end):
#             return getRoute(start, end)
        

#         for neighbor in node.neighbors:
#             if neighbor not in PriorityQueue and not neighbor.isVisited:
#                 neighbor.previous = node
#                 PriorityQueue.append(neighbor)
           
    
