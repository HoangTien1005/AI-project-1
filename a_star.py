import math

def getRoute(start, end):
    route = [end]
    while not route[-1].isEqual(start):
        route.append(route[-1].previous)
    route.reverse()
    return route


def swapArrElement(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]


def increasingSort(arr, end):
    for i in range(len(arr)):
        arr[i].h = math.sqrt((arr[i].x - end.x)**2 + (arr[i].y - end.y)**2)     # Heuristic (distance)
        arr[i].g = arr[i].previous.g + 1
        arr[i].f = arr[i].g + arr[i].h

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if j < len(arr):
                if arr[i].f > arr[j].f:
                    swapArrElement(arr,i,j)  


def A_Star(start, end, bonus_points = None):
    queue = []
    queue.append(start)

    while queue:
        node = queue.pop(0)
        node.isVisited = True
        if node.isEqual(end):
            return getRoute(start, end)

        for neighbor in node.neighbors:
            if neighbor not in queue and not neighbor.isVisited:
                neighbor.previous = node
                queue.append(neighbor)
        increasingSort(queue, end)         
           
    
