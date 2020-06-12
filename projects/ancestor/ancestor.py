from util import Queue, Stack


def get_neighbors(node, matrix):
    neighbors = []

    for i in range(len(matrix)):
        if matrix[i][1] == node:
            neighbors.append(matrix[i][0])

    return neighbors


def earliest_ancestor(ancestors, starting_node):
    # initilize a list to represent the longest path
    longest_path = 1
    earliest_ancestor = -1

    # initialize stack
    # add starting node to stack
    s = Stack()
    s.push([starting_node])

    # while there are paths in the stack
    while s.size() > 0:

        # get the next path in line
        path = s.pop()
        # get last node in the path
        cur_node = path[-1]

        # check to see if there is a new longest path
        if len(path) >= longest_path and cur_node < earliest_ancestor or len(path) > longest_path:
            longest_path = len(path)  # reassign longest path
            earliest_ancestor = cur_node

        for neighbor in get_neighbors(cur_node, ancestors):
            path_copy = list(path)
            path_copy.append(neighbor)
            s.push(path_copy)

    return earliest_ancestor


# def earliest_ancestor(ancestors, starting_node, longest_path=1, path=None, earliest=-1):
#     if path is None:
#         path = list()

#     new_path = path + [starting_node]

#     if len(new_path) >= longest_path and starting_node < earliest or len(new_path) > longest_path:
#         longest_path = len(new_path)  # reassign longest path
#         earliest = starting_node

#     for neighbor in get_neighbors(starting_node, ancestors):

#         neighbor_path = earliest_ancestor(
#             ancestors, neighbor, longest_path, new_path, earliest)
#         if neighbor_path:
#             return neighbor_path

#     return earliest


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(ancestors, 6))
