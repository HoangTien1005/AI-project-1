import math

def getRoute(start, end):
    route = [end]
    while not route[-1].isEqual(start):
        route.append(route[-1].previous.pop())
    route.reverse()
    return route

def wayPaving(route):
    for node in route:
        node.isVisited = False


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

def bonus_iSort(arr, end, type = 1):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if j < len(arr):
                if type == 1:
                    if Manhattan(arr[i], end) > Manhattan(arr[j], end):
                        swapArrElement(arr,i,j) 
                elif type == 2:
                    if Euclidean(arr[i], end) > Euclidean(arr[j], end):
                       swapArrElement(arr,i,j)   

def A_Star(start, end, bonus_points = [], type=1):
    if len(bonus_points) == 0:
        openList = []
        closedList = []
        openList.append(start)

        while openList:
            node = openList.pop(0)
            node.isVisited = True
            closedList.append(node)
            if node.isEqual(end):
                route = getRoute(start, end)
                return route, len(route)

            for neighbor in node.neighbors:
                if neighbor in closedList:
                    continue
                if type == 1:              
                    tempf = node.g + 1 + Manhattan(neighbor, end)
                elif type == 2:
                    tempf = node.g + 1 + Euclidean(neighbor, end)
                if neighbor in openList and tempf >= openList[openList.index(neighbor)].f:
                    continue
                openList.append(neighbor)
                neighbor.previous.append(node)

        increasingSort(openList, end, type)

    else:
        cost = 0
        for node in bonus_points:
            cost += node.reward
        bonus_iSort(bonus_points, start, type)
        node = bonus_points.pop(0)
        
        wayPaving(A_Star(start, node, [], type)[0])
        A_Star(node, end, bonus_points, type)
        route = getRoute(start, end)
        return route, len(route) + cost    
           
    
