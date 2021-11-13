from utilities import *


def A_Star_1(graph, start, end, type=1, bonus_points=[]):
    if len(bonus_points) == 0:
        openList = []
        resetList = []
        openList.append(start)

        while openList:
            increasing_sort(openList)
            node = openList.pop(0)

            if node.is_equal(end):
                reset(resetList)
                end.previous = node.previous
                route = get_route(start, end)
                return route, len(route)

            for neighbor in node.neighbors:
                temp_g = node.g + 1
                if temp_g < neighbor.g or neighbor.g == 0 and not neighbor.is_equal(start):
                    neighbor.previous = node
                    neighbor.g = temp_g
                    resetList.append(neighbor)
                    neighbor.h = heuristic(neighbor, end, type)
                    neighbor.f = neighbor.g + neighbor.h
                    if neighbor not in openList:
                        openList.append(neighbor)

    else:
        bonus_sort_1(bonus_points, start, type)
        route, cost = A_Star_1(graph, start, bonus_points[0], type)
        cost += bonus_points[0].reward

        for i in range(0, len(bonus_points) - 1):
            temp_route, route_length = A_Star_1(
                graph, bonus_points[i], bonus_points[i + 1], type)
            route = route + temp_route
            cost = cost + route_length - 1
            cost += bonus_points[i + 1].reward

        last_route, last_route_length = A_Star_1(
            graph, bonus_points[-1], end, type)
        route = route + last_route
        cost = cost + last_route_length - 1

        return route, cost