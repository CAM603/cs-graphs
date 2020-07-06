from util import Stack
# Write a function that takes in a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. for example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) returns 4

# islands consist of - connected components
# connected - neighbors (edges)
# directions - NSEW (edges)
# 2D array - graph, more or less?
# returns (shape of solution) - number of islands

# How could we write a get neighbor function that uses this shape?
# Offset coordinates

# How can we find the extent of an island?
# Either of our traversals to find all of the nodes in an island

# How do I explore the larger set?
# Loop through and call a traversal if we find an unvisited 1


# def get_neighbors(matrix, node_x, node_y, size):
#     neighbors = []
#     if node_y > 0:
#         n_neighbor = (node_y - 1, node_x)
#         neighbors.append(n_neighbor)
#     if node_x > 0:
#         w_neighbor = (node_y, node_x - 1)
#         neighbors.append(w_neighbor)
#     if node_y < size - 1:
#         s_neighbor = (node_y + 1, node_x)
#         neighbors.append(s_neighbor)
#     if node_x < size - 1:
#         e_neighbor = (node_y, node_x + 1)
#         neighbors.append(e_neighbor)
#     return neighbors


# def dft_recursive(matrix, node_x, node_y, size, visited):
#     neighbors = get_neighbors(matrix, node_x, node_y, size)
#     for neighbor in neighbors:
#         if neighbor not in visited:
#             visited.add(neighbor)
#             neighbor_x = neighbor[0]
#             neighbor_y = neighbor[1]
#             if matrix[neighbor_x][neighbor_y] == 1:
#                 dft_recursive(matrix, neighbor_x, neighbor_y, size, visited)


# def findIslands(matrix):
#     size = len(matrix)
#     visited = set()
#     islands = 0
#     for i in range(size):
#         for j in range(size):
#             if (i, j) not in visited:
#                 visited.add((i, j))
#                 if matrix[i][j] == 1:
#                     dft_recursive(matrix, j, i, size, visited)
#                     islands += 1
#     return islands

def get_neighbors(x, y, matrix):
    neighbors = []
    # checks
    if x > 0 and matrix[y][x-1] == 1:
        neighbors.append((x - 1, y))
    if x < len(matrix[0]) - 1 and matrix[y][x + 1] == 1:
        neighbors.append((x + 1, y))
    if y > 0 and matrix[y - 1][x] == 1:
        neighbors.append((x, y - 1))
    if y < len(matrix) - 1 and matrix[y + 1][x] == 1:
        neighbors.append((x, y + 1))
    return neighbors


def dfs(x, y, matrix, visited):
    s = Stack()
    s.push((x, y))
    while s.size() > 0:
        # pop first vert
        v = s.pop()
        # If not visited, traverse
        if not visited[v[1]][v[0]]:
            # mark vert as visited
            visited[v[1]][v[0]] = True
            for neighbor in get_neighbors(v[0], v[1], matrix):
                s.push(neighbor)
    return visited


def island_counter(matrix):
    visited = []
    for _ in range(len(matrix)):  # length = 5
        visited.append([False] * len(matrix[0]))
        #   [False, False, False, False, False], [False, False, False, False, False],   [False, False, False, False, False], [False, False, False, False, False],   [False, False, False, False, False]]
    island_count = 0
    # Walk through all the nodes, elements in the input matrix
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            # If it is not visited
            if not visited[y][x]:
                # If the value in the matrix at this position is a 1
                if matrix[y][x] == 1:
                    # do a traversal and mark each as visited
                    visited = dfs(x, y, matrix, visited)
                    # increment island_count
                    island_count += 1
                else:
                    # we hit water (0)
                    visited[y][x] = True
    return island_count


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print(island_counter(islands))
