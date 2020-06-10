from util import Queue, Stack

'''
          10
        /
       1   2   4  11
        \ /   / \ /
         3   5   8
          \ / \   \
           6   7   9
   '''


def get_neighbors(node, matrix):
    neighbors = []

    for i in range(len(matrix)):
        #
        if matrix[i][1] == node:
            neighbors.append(matrix[i][0])

    return neighbors


# def earliest_ancestor(ancestors, starting_node):
#     # initialize set to store visited vertices
#     visited = set()

#     # initilize a list to represent the longest path
#     longest_path = []

#     # initialize stack
#     s = Stack()

#     # add starting node to stack
#     s.push([starting_node])

#     # while there are paths in the stack
#     while s.size() > 0:

#         # get the next path in line
#         path = s.pop()

#         # check to see if there is a new longest path
#         if len(path) > len(longest_path):
#             longest_path = list(path)  # reassign longest path

#         # if there is a tie in length
#         elif len(path) == len(longest_path):

#             # longest path will be the one whose earliest ancestor has the lowest numeric ID
#             if path[-1] < longest_path[-1]:
#                 longest_path = list(path)

#         # get last node in the path
#         cur_node = path[-1]

#         if cur_node not in visited:

#             # add to visited
#             visited.add(cur_node)

#             for neighbor in get_neighbors(cur_node, ancestors):
#                 path_copy = list(path)
#                 path_copy.append(neighbor)
#                 s.push(path_copy)

#     if len(longest_path) == 1:
#         return -1
#     else:
#         return longest_path[-1]


def earliest_ancestor(ancestors, starting_node, longest_path=None, visited=None, path=None):
    if longest_path is None:
        longest_path = list()
    if visited is None:
        visited = set()
    if path is None:
        path = list()

    visited.add(starting_node)
    new_path = path + [starting_node]

    # check to see if there is a new longest path
    if len(new_path) > len(longest_path):
        longest_path = list(new_path)  # reassign longest path

        # if there is a tie in length
    elif len(new_path) == len(longest_path):

        # longest path will be the one whose earliest ancestor has the lowest numeric ID
        if new_path[-1] < longest_path[-1]:
            longest_path = list(new_path)

    for neighbor in get_neighbors(starting_node, ancestors):
        if neighbor not in visited:
            neighbor_path = earliest_ancestor(
                ancestors, neighbor, longest_path, visited, new_path)
            if neighbor_path:
                return neighbor_path

    if len(longest_path) == 1:
        return -1
    else:
        return longest_path[-1]


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# print(earliest_ancestor(ancestors, 6))
