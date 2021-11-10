from utilities import get_route

def BFS(start, end, bonus_points = None):
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop(0)
        node.isVisited = True
        if node.is_equal(end):
            route = get_route(start, end)
            return route, len(route)
        for neighbor in node.neighbors:
            if neighbor not in queue and not neighbor.isVisited:
                neighbor.previous = node
                queue.append(neighbor)
    
