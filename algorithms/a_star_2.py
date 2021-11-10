from utilities import *


def A_Star_2(graph, start, end, type=1, bonus_points=[]):
    if len(bonus_points) == 0:
        open_list = []
        reset_list = []
        open_list.append(start)

        while open_list:
            increasing_sort(open_list, end, type)
            node = open_list.pop(0)

            if node.is_equal(end):
                reset(reset_list)
                end.previous = node.previous
                route = get_route(start, end)
                return route, len(route)

            for neighbor in node.neighbors:
                temp_g = node.g + 1
                if temp_g < neighbor.g or neighbor.g == 0 and not neighbor.is_equal(start):
                    neighbor.previous = node
                    neighbor.g = temp_g
                    reset_list.append(neighbor)
                    neighbor.h = heuristic(neighbor, end, type)
                    neighbor.f = neighbor.g + neighbor.h
                    if neighbor not in open_list:
                        open_list.append(neighbor)

    else:
        bonus_sort_2(bonus_points, start, end, type)

        temp = heuristic(start, bonus_points[0], type) + heuristic(
            bonus_points[0], end, type) + bonus_points[0].reward
        if temp < heuristic(start, end, type):
            route, cost = A_Star_2(graph, start, bonus_points[0], type)
            cost += bonus_points[0].reward

        else:
            return A_Star_2(graph, start, end, type)

        i = 0
        while i < len(bonus_points) - 1:
            temp_2 = heuristic(bonus_points[i], bonus_points[i + 1], type) + heuristic(
                bonus_points[i + 1], end, type) + bonus_points[i + 1].reward
            if temp_2 >= heuristic(bonus_points[i], end, type):
                bonus_points.remove(bonus_points[i+1])

            else:
                temp_route, route_length = A_Star_2(
                    graph, bonus_points[i], bonus_points[i + 1], type)
                route = route + temp_route
                cost = cost + route_length - 1
                cost += bonus_points[i + 1].reward
                i = i + 1

        last_route, last_route_length = A_Star_2(
            graph, bonus_points[-1], end, type)
        route = route + last_route
        cost = cost + last_route_length - 1

        return route, cost
