from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


visited_graph = {}
traversal_path = []
opposites = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}


def initialize_room(room):  # initializes room
    visited_graph[room.id] = {}
    for next_room in room.get_exits():
        visited_graph[room.id][next_room] = "?"


def search(paths):  # finds unexplored rooms
    directions = []
    for path in paths:
        if paths[path] == "?":
            directions.append(path)
    return directions  # example: ['n', 'e']


def bfs(explored_graph):  # returns a path to the closest unexplored path
    q = Queue()
    # enqueue current room id as first path
    q.enqueue([player.current_room.id])
    visited = set()

    while q.size() > 0:
        path = q.dequeue()
        cur_room = path[-1]

        if cur_room not in visited:
            visited.add(cur_room)
            # checks for unexplored path
            for direction in explored_graph[cur_room]:
                # return path to an unexplored room
                if explored_graph[cur_room][direction] == '?':
                    return path
                # keep looking, but don't go backwards
                elif explored_graph[cur_room][direction] not in visited:
                    new_path = list(path)
                    new_path.append(explored_graph[cur_room][direction])
                    q.enqueue(new_path)
    return path


while len(visited_graph) < len(room_graph):
    # initialize room if it has not been visited
    if player.current_room.id not in visited_graph:
        initialize_room(player.current_room)
    # get all possible directions
    directions = search(visited_graph[player.current_room.id])

    # If there are no unexplored paths
    if len(directions) == 0:
        # BDS to find the closest unexplored path
        # takes in the explored graph
        path = bfs(visited_graph)
        # record the path taken
        # for every room_id in the path
        for room_id in path:
            # grab the players current room id
            cur_room_id = player.current_room.id
            # for every direction in the player's current room
            for direction in visited_graph[cur_room_id]:
                # if the room id value for the direction is the same as the room id in the path
                # AND if the player is not already at the room in the path
                if visited_graph[cur_room_id][direction] == room_id and cur_room_id != room_id:
                    # record the direction
                    traversal_path.append(direction)
                    # gets the room where the player is headed next
                    next_room = player.current_room.get_room_in_direction(
                        direction)
                    # update the visited graph key value pair
                    visited_graph[cur_room_id][direction] = next_room.id
                    # if it is a room we have not visited in before
                    if next_room.id not in visited_graph:
                        # initialize the room as usual
                        initialize_room(next_room)
                    # get the opposite direction from the players traveled direction
                    opposite_dir = opposites[direction]
                    # record the path where the player came from
                    visited_graph[next_room.id][opposite_dir] = cur_room_id
                    # move player to the next room
                    player.travel(direction)
    else:
        # choose a random direction to travel from our options
        next_direction = random.choice(directions)
        # record the direction
        traversal_path.append(next_direction)
        # grab the next room for this direction
        next_room = player.current_room.get_room_in_direction(next_direction)
        # record the rooms direction value to the next room id
        visited_graph[player.current_room.id][next_direction] = next_room.id
        # if the next room has not been explored yet
        if next_room.id not in visited_graph:
            # initialize the room
            initialize_room(next_room)
        # get the opposite direction from the players traveled direction
        opposite_dir = opposites[next_direction]
        # record the path where the player came from
        visited_graph[next_room.id][opposite_dir] = player.current_room.id
        # move the player to the next room
        player.travel(next_direction)

# def bfs(start):
#     q = Queue()
#     q.enqueue([start])
#     # visited = set()

#     while q.size() > 0:
#         path = q.dequeue()
#         # if path[-1] not in visited:
#         #     visited.add(path[-1])
#         if search(graph[path[-1]]):
#             for i in range(len(path) - 1):
#                 for direction, num in graph[path[i]].items():
#                     if path[i + 1] == num:
#                         traversal_path.append(direction)
#             return path
#         for room in player.current_room.get_exits():
#             new_path = list(path)
#             player.travel(room)
#             new_path.append(player.current_room.id)
#             q.enqueue(new_path)


# while len(graph) < 17:
#     # players current room
#     cur_room = player.current_room.id
#     # players next move
#     next_direction = search(graph[player.current_room.id])
#     if next_direction:
#         player.travel(next_direction)
#         traversal_path.append(next_direction)
#         initialize_room(player.current_room.id)
#         graph[cur_room][next_direction] = player.current_room.id
#         graph[player.current_room.id][opposites[next_direction]] = cur_room
#     else:
#         bfs(player.current_room.id)


print(visited_graph)
print(traversal_path)
print(f'Current room: {player.current_room.id}')

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
