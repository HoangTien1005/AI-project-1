from utilities import *

def increasingSort(arr, end, type = 1):
    for i in range(len(arr)):
        Heuristic(arr[i], end, type)
        arr[i].g = arr[i].previous.g + 1
        arr[i].f = arr[i].g + arr[i].h

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if j < len(arr):
                if arr[i].f > arr[j].f:
                    swapArrElement(arr,i,j)

def bonus_iSort(arr, start, end, type = 1):
    i = len(arr) - 1
    while i >= 0:
        if (DistanceX(start, end, arr[i], type) >= 0):
            arr.remove(arr[i])
        i-= 1

    if len(arr) > 1:
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if j < len(arr):
                    if DistanceX(start, end, arr[i], type) > DistanceX(start, end, arr[j], type):
                        swapArrElement(arr, i, j)

def A_Star_2(start, end, bonus_points = [], type=1):
    if len(bonus_points) == 0:
        openList = []
        closedList = []
        openList.append(start)

        while openList:
            node = openList.pop(0)
            node.isVisited = True
            closedList.append(node)
            if node.isEqual(end):
                route = getRoute(start, node)
                return route, len(route)

            for neighbor in node.neighbors:
                if neighbor in closedList:
                    continue
                tempf = node.g + 1 + Distance(neighbor, end, type)
                if neighbor in openList and tempf >= openList[openList.index(neighbor)].f:
                    continue
                openList.append(neighbor)
                neighbor.previous = node

        increasingSort(openList, end, type)

    else:
        cost = 0
        bonus_iSort(bonus_points, start, end, type)
        if len(bonus_points) == 0:
            return A_Star_2(start, end, [], type)
        node = bonus_points.pop(0)
        cost += node.reward
        route = A_Star_2(start, node, [], type)[0]
        wayPaving(route)
        route.pop()
        route += A_Star_2(node, end, bonus_points, type)[0]
        return route, len(route) + cost    
           
    
