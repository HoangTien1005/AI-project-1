import math

def getRoute(start, end):
    route = [end]
    while not route[-1].isEqual(start):
        route.append(route[-1].previous)
    route.reverse()
    return route

def wayPaving(graph):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            graph[i][j].g = 0


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
    return node.h


def increasingSort(arr, end, type = 1):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if j < len(arr):
                if arr[i].f > arr[j].f:
                    swapArrElement(arr,i,j)  

def bonus_iSort(arr, end, type = 1):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if j < len(arr):
                if Heuristic(arr[i], end, type) > Heuristic(arr[j], end, type):
                    swapArrElement(arr,i,j)   

def A_Star(graph, start, end, type=1, bonus_points = []):
    if len(bonus_points) == 0:
        openList = []

        openList.append(start)

        while openList:
            increasingSort(openList, end, type)
            node = openList.pop(0)
            
            if node.isEqual(end):
                end.previous = node.previous
                route = getRoute(start, end)
                return route, len(route)

            for neighbor in node.neighbors:
                temp_g = node.g + 1
                if temp_g < neighbor.g or neighbor.g == 0 and not neighbor.isEqual(start):
                    neighbor.previous = node
                    neighbor.g = temp_g
                    neighbor.f = neighbor.g + Heuristic(neighbor, end, type)
                    if neighbor not in openList:
                        openList.append(neighbor)

    else:
        bonus_iSort(bonus_points, start, type)
        route, cost = A_Star(graph, start, bonus_points[0], type)
        cost += bonus_points[0].reward
        wayPaving(graph)

        for i in range(0, len(bonus_points) -1):
            temp_route, route_length = A_Star(graph, bonus_points[i], bonus_points[i + 1], type)
            wayPaving(graph)
            route = route + temp_route
            cost = cost + route_length
            cost += bonus_points[i + 1].reward

        last_route, last_route_length = A_Star(graph, bonus_points[-1], end, type)
        route = route + last_route
        cost = cost + last_route_length

        return route, cost    
           
    
