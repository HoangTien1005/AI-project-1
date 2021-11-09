def getRoute(start, end):
    route = [end]
    while not route[-1].isEqual(start):
        route.append(route[-1].previous)
    route.reverse()
    return route

def DFS(start, end, bonus_points = None):
    stack = []
    stack.append(start)
    while stack:
        node = stack.pop()
        node.isVisited = True
        if node.isEqual(end):
            route = getRoute(start, end)
            return route, len(route)
        for neighbor in node.neighbors:
            if neighbor not in stack and not neighbor.isVisited:
                neighbor.previous = node
                stack.append(neighbor)