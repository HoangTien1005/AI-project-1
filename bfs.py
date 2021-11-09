def getRoute(start, end):
    route = [end]
    while not route[-1].isEqual(start):
        route.append(route[-1].previous)
    route.reverse()
    return route


def BFS(start, end, bonus_points = None):
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop(0)
        node.isVisited = True
        if node.isEqual(end):
            route = getRoute(start, end)
            return route, len(route)
        for neighbor in node.neighbors:
            if neighbor not in queue and not neighbor.isVisited:
                neighbor.previous = node
                queue.append(neighbor)
    
