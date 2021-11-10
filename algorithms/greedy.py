from utilities import increasing_sort, get_route, heuristic


def Greedy(start, end, type=1, bonus_points=[]):
    priority_queue = []
    priority_queue.append(start)
    while priority_queue:
        increasing_sort(priority_queue, end, type)
        node = priority_queue.pop(0)
        node.isVisited = True
        if node.is_equal(end):
            route = get_route(start, end)
            return route, len(route)

        for neighbor in node.neighbors:
            neighbor.h = heuristic(neighbor, end, type)
            neighbor.f = neighbor.h
            if neighbor not in priority_queue and not neighbor.isVisited:
                neighbor.previous = node
                priority_queue.append(neighbor)
