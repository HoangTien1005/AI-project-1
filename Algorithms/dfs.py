from utilities import getRoute

def DFS(start, end, bonus_points = None):
    stack = []
    stack.append(start)
    while stack:
        node = stack.pop()
        node.isVisited = True
        if node.isEqual(end):
            route = getRoute(start, node)
            return route, len(route)
        for neighbor in node.neighbors:
            if not neighbor.isVisited:
                neighbor.previous = node
                stack.append(neighbor)