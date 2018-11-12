import math


def initialize_shortest_distances():
    shortest_distance_v1 = [0, 5, 2, 4, 8, 12, 10]
    shortest_distance_v2 = [5, 0, 3, 5, 9, 13, 11]
    shortest_distance_v3 = [2, 3, 0, 2, 6, 10, 8]
    shortest_distance_v4 = [4, 5, 2, 0, 4, 8, 6]
    shortest_distance_v5 = [8, 9, 6, 4, 0, 4, 2]
    shortest_distance_v6 = [12, 13, 10, 8, 4, 0, 3]
    shortest_distance_v7 = [10, 11, 8, 6, 2, 3, 0]

    shortest_distance_set = [shortest_distance_v1, shortest_distance_v2, shortest_distance_v3, shortest_distance_v4,
                             shortest_distance_v5, shortest_distance_v6, shortest_distance_v7]

    return shortest_distance_set


def node_importance():
    vertices = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7']
    # vertices = []
    importance = [None for _ in range(len(vertices))]
    # the importance of each vertex is set to zero.
    for i in range(0, len(vertices)):
        importance[i] = 0

    shortest_distance_set = initialize_shortest_distances()

    for i in range(0, len(vertices)):
        shortest_distance_set[i].sort(reverse=True)  # the list will be sorted in descending order
        summation = 0
        index = len(vertices) - 1
        prev_distance = -1
        prev_importance = -1
        while index > 0:
            temp = shortest_distance_set[i][index - 1]
            if shortest_distance_set[i][index - 1] == prev_distance:
                current_importance = prev_importance
            else:
                current_importance = math.exp(-temp) / (index + 1) - summation

            importance[index - 1] = importance[index - 1] + current_importance
            summation += math.exp(-temp) / (index * (index + 1))

            prev_distance = temp
            prev_importance = current_importance
            index = index - 1

        importance[i] = importance[i] + 1 - summation  # since (math.exp(-0) = 1

    print("The importance of the nodes are listed below: ")
    for i in range(0, len(importance)):
        print('I(', i, ') = ', importance[i])

    print("The sum of importance = ", sum(importance))


node_importance()
