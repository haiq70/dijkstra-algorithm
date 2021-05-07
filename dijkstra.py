# Dijkstra's shortest path algorithm - visualisation
# // haiq70

# defining infinity
INF = float('inf')

# intialising adjacency matrix
# weighted paths between vertices
vertices = [[0, 1, 2, 0],   # A
            [1, 0, 4, 0],   # B
            [2, 4, 0, 3],   # C
            [0, 0, 3, 0]]   # D

# get the number of vertices
num_vertices = len(vertices)

# initialise variable to keep track of visited nodes and distances between them
# first 0/1 - univisited/visited
# second - distance from the source vertex
nodes = [[0, 0]]

# append all of the nodes except the source, assign infinity as the distance
for node in range(num_vertices-1):
    nodes.append([0, INF])
    #[[0, 0], [0, inf], [0, inf], [0, inf]]

# function to get the path with the smallest weight and the node corresponding to it
# CHANGE 
def next_node():
    next = -1
    for path in range(num_vertices-1):
        if nodes[path][0] == 0 and (next<0 or nodes[path][1] <= nodes[next][1]):
            next = path
    return next


print(next_node())
