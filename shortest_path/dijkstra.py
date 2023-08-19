"""
 Dijkstra algorithm for finding all shortest paths from start.
 Source: Design of Heuristic Algorithms for hard optimization. Ch. 2, page 36
"""


def dijkstra(number_of_cities, distance_matrix, starting_city):
    # Cities ordered by increasing shortest path
    priority_queue = [i for i in range(number_of_cities)]

    # Immediate predecessor on a shortest path from start
    pred = [starting_city] * number_of_cities
    shortest_path_length = [float('inf')] * number_of_cities

    # Only shortest path to order[0]=start already known
    shortest_path_length[starting_city] = 0
    priority_queue[0], priority_queue[starting_city] = priority_queue[starting_city], priority_queue[0]

    for city in range(number_of_cities - 1):
        for neighbor_to_update in range(city+1, number_of_cities):
            current_path_length = shortest_path_length[priority_queue[city]]
            distance_to_neighbor = distance_matrix[priority_queue[city]][priority_queue[neighbor_to_update]]
            path_length_to_neigbor = shortest_path_length[priority_queue[neighbor_to_update]]
            if current_path_length + distance_to_neighbor < path_length_to_neigbor:
                shortest_path_length[neighbor_to_update] = current_path_length + distance_to_neighbor
                pred[priority_queue[neighbor_to_update]] = priority_queue[city]

            # update order if a better i+1th shortest path is identified
            if shortest_path_length[priority_queue[city+1]] > shortest_path_length[priority_queue[neighbor_to_update]]:
                priority_queue[city+1], priority_queue[neighbor_to_update] = priority_queue[neighbor_to_update], priority_queue[city+1]

    return shortest_path_length, pred


if __name__=="__main__":
    number_of_cities = 5
    inf = float('inf')
    distance_matrix = [
        [inf, 2, inf, inf, 3],     # a->b, a->e
        [2, inf, 3, inf, 4],       # b->a, b->c, b->e
        [inf, 3, inf, 5, inf],     # c->b, c->d
        [inf, inf, inf, 5, 3],     # c->d, d-> e
        [3, 4, inf, 3, inf],       # a->b, a->e
    ]
    starting_node = 0
    shortest_path_length, pred = dijkstra(number_of_cities, distance_matrix, starting_node)
    nodes_name = "A B C D E".split(" ")
    print(f"Caminho mínimo: {[(nodes_name[dest], dist) for dest, dist in enumerate(shortest_path_length)]}\n")
    print(f"Pais: {[(nodes_name[pai], nodes_name[filho]) for filho, pai in enumerate(pred)]}")