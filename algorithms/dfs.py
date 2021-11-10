from utilities import get_route

def DFS(start, end, bonus_points = None):
    stack = []
    stack.append(start)
    while stack:
        node = stack.pop()
        node.isVisited = True
        if node.is_equal(end):
            route = get_route(start, end)
            return route, len(route)
        for neighbor in node.neighbors:
            if not neighbor.isVisited:
                neighbor.previous = node
                stack.append(neighbor)