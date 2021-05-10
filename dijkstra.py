# Dijkstra's shortest path algorithm - visualisation
# // haiq70

# defining infinity
INF = float('inf')

# intialising adjacency matrix
# weighted paths between vertices
vertices = [[0, 3, 0, 2, 0, 0, 6],
            [3, 0, 6, 2, 1, 0, 0],
            [0, 6, 0, 0, 0, 1, 0],
            [2, 2, 0, 0, 3, 0, 0],
            [0, 1, 0, 3, 0, 4, 0],
            [0, 0, 1, 0, 4, 0, 2],
            [6, 0, 0, 0, 0, 2, 0]]

# initialise variable to keep track of visited nodes and distances between them
# first 0/1 - univisited/visited
# second - distance from the source vertex
nodes = [[0, 0]]

# get the number of vertices
num_vertices = len(vertices)

# append all of the nodes except the source, assign infinity as the distance
for node in range(0, num_vertices-1):
    nodes.append([0, INF])
    #[[0, 0], [0, inf], [0, inf], [0, inf]]

# function to mark a node as visited - clears up the code
def mark_visited(node):
    nodes[node][0] = 1

# function to get the path with the smallest weight and the node corresponding to it
def next_node():
    isFound = False
    next = 0
    for vertex in range(0, num_vertices):
        # if univisited and the value of the current node is smaller or eq to the next node's
        if nodes[vertex][0] == 0 and (not isFound or nodes[vertex][1] <= nodes[next][1]):
            isFound = True
            next = vertex
    return next

alg_path = []   # storing concurrent vertices the algorithm visits

# main algorithm
def dijkstra():
    for vertex in range(num_vertices):
        next_vertex = next_node()   # find next vertex to visit
        alg_path.append(chr(next_vertex + 65))    # visualise the path taken by the algorithm (conversion to ascii)
        for i in range(num_vertices):
            # if connection between nodes exists and node is unvisited
            if vertices[next_vertex][i] > 0 and nodes[i][0] == 0:
                # distance = current distance to the vertex + value of the path saved in the matrix
                distance = nodes[next_vertex][1] + vertices[next_vertex][i]
                # if current distance is greater than the calculated -> reset
                if nodes[i][1] > distance:
                    nodes[i][1] = distance
        mark_visited(next_vertex)

dijkstra()
print(alg_path)

counter = 0
print("Distance from source to: ")
for node in nodes:
    print("{} = {:1.2f}".format(chr(ord('A') + counter), node[1]))
    counter += 1
