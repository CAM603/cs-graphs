"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print('Vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    # def bft(self, starting_vertex):
    #     """
    #     Print each vertex in breadth-first order
    #     beginning from starting_vertex.
    #     """
    #     # initialize queue
    #     q = Queue()
    #     # create set to store visited vertices
    #     visited = set()
    #     # add starting_vertex to queue
    #     q.enqueue(starting_vertex)
    #     # while queue is not empty
    #     while q.size() > 0:
    #         # dequeu starting_vertex
    #         v = q.dequeue()
    #         # if the vertex has not been visited
    #         if v not in visited:
    #             # visit it
    #             print(v)
    #             # mark as visited
    #             visited.add(v)
    #             # add neighbors to queue
    #             for next_vert in self.get_neighbors(v):
    #                 q.enqueue(next_vert)

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue and enqueue starting_vertex
        q = Queue()
        q.enqueue([starting_vertex])
        # create set to store visited vertices
        visited = set()
        # while queue is not empty
        while q.size() > 0:
            # dequeu/pop starting_vertex
            path = q.dequeue()
            print(f'Old {path}')
            print(path[-1])
            # if not visited
            if path[-1] not in visited:
                # DO THE THING
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    # makes a copy
                    new_path = list(path)
                    new_path.append(next_vert)
                    print(f'New {new_path}')
                    q.enqueue(new_path)

    # def dft(self, starting_vertex):
    #     """
    #     Print each vertex in depth-first order
    #     beginning from starting_vertex.
    #     """
    #     # initialize stack
    #     s = Stack()
    #     # create set to store visited vertices
    #     visited = set()
    #     # add starting_vertex to stack
    #     s.push(starting_vertex)
    #     # while stack is not empty
    #     while s.size() > 0:
    #         # pop starting_vertex
    #         v = s.pop()
    #         # if the vertex has not been visited
    #         if v not in visited:
    #             # visit it
    #             print(v)
    #             # mark as visited
    #             visited.add(v)
    #             # add neighbors to stack
    #             for next_vert in self.get_neighbors(v):
    #                 s.push(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # initialize stack
        s = Stack()
        # add starting_vertex to stack
        s.push([starting_vertex])
        # create set to store visited vertices
        visited = set()
        # while stack is not empty
        while s.size() > 0:
            # pop starting_vertex
            path = s.pop()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    # makes a copy
                    new_path = list(path)
                    new_path.append(next_vert)
                    s.push(new_path)

    # def dft_recursive(self, starting_vertex):
    #     """
    #     Print each vertex in depth-first order
    #     beginning from starting_vertex.

    #     This should be done using recursion.
    #     """
    #     # create set to store visited vertices
    #     visited = set()
    #     # create helper function that accepts a vertex

    #     def dft(vertex):
    #         # base case if there is no vertex
    #         if vertex is None:
    #             return
    #         else:
    #             visited.add(vertex)
    #             print(vertex)
    #             for neighbor in self.get_neighbors(vertex):
    #                 if neighbor not in visited:
    #                     dft(neighbor)
    #     dft(starting_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Initial case
        if visited is None:
            visited = set()
        # Base case: when we have no more neighbors (see below)

        # track visited nodes
        visited.add(starting_vertex)
        print(starting_vertex)

        # call the function recursively - on unvisited neighbors
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
                # If a node has no unvisited neighbors, do nothing
                # aka: the base case

    # def bfs(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing the shortest path from
    #     starting_vertex to destination_vertex in
    #     breath-first order.
    #     """
    #     # Create an empty queue and enqueue A PATH TO the starting vertex ID
    #     q = Queue()
    #     q.enqueue([starting_vertex])
    #     # Create a Set to store visited vertices
    #     visited = set()
    #     # While the queue is not empty...
    #     while q.size() > 0:
    #         # Dequeue the first PATH
    #         path = q.dequeue()
    #         # get last node in the path
    #         vertex = path[-1]
    #         # checks if we reached the end
    #         if vertex == destination_vertex:
    #             return path
    #         elif vertex not in visited:
    #             # loop over all neighbors
    #             for neighbor in self.get_neighbors(vertex):
    #                 # create a new path
    #                 new_path = list(path)
    #                 new_path.append(neighbor)
    #                 # add to queue
    #                 q.enqueue(new_path)
    #             # mark it as visited
    #             visited.add(vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING
                if path[-1] == destination_vertex:
                    return path
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for neighbor in self.get_neighbors(path[-1]):
                    # create a new path
                    new_path = list(path)
                    new_path.append(neighbor)
                    # add to queue
                    q.enqueue(new_path)
        # Path not found
        return None

    # def dfs(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.
    #     """
    #     # Create an empty queue and enqueue A PATH TO the starting vertex ID
    #     s = Stack()
    #     s.push([starting_vertex])
    #     # Create a Set to store visited vertices
    #     visited = set()
    #     # While the queue is not empty...
    #     while s.size() > 0:
    #         # Dequeue the first PATH
    #         path = s.pop()
    #         # get last node in the path
    #         vertex = path[-1]
    #         # checks if we reached the end
    #         if vertex == destination_vertex:
    #             return path
    #         elif vertex not in visited:
    #             # loop over all neighbors
    #             for neighbor in self.get_neighbors(vertex):
    #                 # create a new path
    #                 new_path = list(path)
    #                 new_path.append(neighbor)
    #                 # add to queue
    #                 s.push(new_path)
    #             # mark it as visited
    #             visited.add(vertex)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # initialize stack
        s = Stack()
        # add starting_vertex to stack
        s.push([starting_vertex])
        # create set to store visited vertices
        visited = set()
        # while stack is not empty
        while s.size() > 0:
            # pop starting_vertex
            path = s.pop()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING
                if path[-1] == destination_vertex:
                    return path
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    # makes a copy
                    new_path = list(path)
                    new_path.append(next_vert)
                    s.push(new_path)

    # def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.

    #     This should be done using recursion.
    #     """
    #     # if being called for the first time, initialize visited and path
    #     if visited is None:
    #         visited = set()
    #     if path is None:
    #         path = []
    #     # Track the visited vertices
    #     visited.add(starting_vertex)
    #     # Add to path
    #     path = path + [starting_vertex]
    #     # If destination is found, return path
    #     if starting_vertex == destination_vertex:
    #         return path
    #     # otherwise, call function on neighbors
    #     for neighbor in self.get_neighbors(starting_vertex):
    #         if neighbor not in visited:
    #             # checks for a path
    #             neighbor_path = self.dfs_recursive(
    #                 neighbor, destination_vertex, visited, path)
    #             # only return if there is a path
    #             if neighbor_path:
    #                 return neighbor_path

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # if being called for the first time, initialize visited and path
        # Initial case
        if visited is None:
            visited = set()
        if path is None:
            path = list()
        # Base case: when we have no more neighbors (see below)

        # track visited nodes
        visited.add(starting_vertex)
        new_path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return new_path

        # call the function recursively - on unvisited neighbors
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                neighbor_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, new_path)
                # only return if we have a path
                if neighbor_path:
                    return neighbor_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
