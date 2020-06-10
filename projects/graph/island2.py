from util import Stack


def island_counter(matrix):
    # create a visited data structure
    visited = []

    for _ in range(len(matrix)):
        visited.append([False] * len(matrix[0]))

    island_count = 0
    # walk through all the nodes, elements in the input matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            # If it's not visited
            if not visited[row][col]:
                # If the value in the matrix at this position is a 1:
                if matrix[row][col] == 1:
                    # Do a traversal and mark each as visited
                    visited = dft(row, col, matrix, visited)
                    # increment island counter
                    island_count += 1
                else:
                    # we hit water (0)
                    visited[row][col] = True
    return island_count


def dft(row, col, matrix, visited):
    s = Stack()

    # push starting vert on the stack
    s.push((row, col))

    # while stack is not empty
    while s.size() > 0:

        # pop the first vert
        v = s.pop()
        # destructure
        row, col = v
        # if not visited, traverse!
        if not visited[row][col]:
            # Mark visited
            visited[row][col] = True

            for neighbor in get_neighbors(row, col, matrix):
                s.push(neighbor)
    return visited


def get_neighbors(row, col, matrix):
    neighbors = []
    # check north only if row is greater than 0
    # row - 1 checks up
    if row > 0 and matrix[row - 1][col] == 1:
        neighbors.append((row - 1, col))
    # check south only if row is less than length of matrix - 1
    # cant go south if you are at row == len(matrix)
    # row + 1 checks down
    if row < len(matrix) - 1 and matrix[row + 1][col] == 1:
        neighbors.append((row + 1, col))
    # check west
    # col - 1 checks west
    if col > 0 and matrix[row][col - 1] == 1:
        neighbors.append((row, col - 1))
    # check east
    # col < len(matrix[0]) - 1 makes sure we can go east
    # col + 1 checks east
    if col < len(matrix[0]) - 1 and matrix[row][col + 1] == 1:
        neighbors.append((row, col + 1))

    return neighbors


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
print(island_counter(islands))
