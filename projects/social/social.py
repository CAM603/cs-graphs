from util import Queue
import random


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}  # Nodes
        self.friendships = {}  # Edges
        count = 0

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        # Create friendships
        possible_friendships = []

        # Don't add duplicate combinations by ensuring the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        # Shuffle them
        random.shuffle(possible_friendships)

        # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            # Set up those friendships
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
            count += 1
        return count

    def bfs(self, starting_friend, destination_friend):
        q = Queue()
        q.enqueue([starting_friend])

        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            if path[-1] not in visited:
                if path[-1] == destination_friend:
                    return path
                visited.add(path[-1])
                for friend in self.friendships[path[-1]]:
                    new_path = list(path)
                    new_path.append(friend)
                    q.enqueue(new_path)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        for user in self.users:
            # for every user
            # find a path from the user_id to the user
            # if there is a path, add to the visited
            path = self.bfs(user_id, user)
            if path:
                visited[user] = path

        return visited


# if __name__ == '__main__':
#     sg = SocialGraph()
#     sg.populate_graph(1000, 5)
#     print(sg.friendships)
#     connections = sg.get_all_social_paths(1)
#     print(connections)

sg = SocialGraph()
sg.populate_graph(1000, 5)
# print(sg.friendships)
connections = sg.get_all_social_paths(1)

# calculate percentage of other users in a particular user's extended social network


def calc_network_percentage(graph, user_connections, num_users):
    count = 0
    for user in graph.users:
        if user in user_connections.keys():
            count += 1
    percentage = (count / num_users) * 100
    return percentage


print(calc_network_percentage(sg, connections, 1000))  # 99.1


def calc_avg_degree_separtation(graph, user_connections):
    degrees = 0
    friend_count = 0
    # length of users path to another user is the degree of separation
    for user in user_connections:
        # add degree of separation
        degrees += len(user_connections[user])
        # add to firend count
        count += 1
    # divide total degrees of separation by the number of user connections
    average = degrees / friend_count
    return average


print(calc_avg_degree_separtation(sg, connections))
