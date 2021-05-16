# Dijkstra's shortest path algorithm - visualisation
# // haiq70

import networkx as nx
import matplotlib.pyplot as plot
import tkinter as tk
from tkinter import messagebox

# intialising adjacency matrix
# weighted paths between vertices
vertices = [[0, 3, 0, 2, 0, 0, 6],  # A # 0
            [3, 0, 6, 2, 1, 0, 0],  # B # 1
            [0, 6, 0, 0, 0, 1, 0],  # C # 2
            [2, 2, 0, 0, 3, 0, 0],  # D # 3
            [0, 1, 0, 3, 0, 4, 0],  # E # 4
            [0, 0, 1, 0, 4, 0, 2],  # F # 5
            [6, 0, 0, 0, 0, 2, 0]]  # G # 6

# adjacency list - matrix converted manually
edge_list = [('A', 'B', 3),
             ('A', 'D', 2),
             ('A', 'G', 6),
             ('B', 'C', 6),
             ('B', 'D', 2),
             ('B', 'E', 1),
             ('C', 'F', 1),
             ('D', 'E', 3),
             ('E', 'F', 4),
             ('F', 'G', 2)]

# initialise variable to keep track of visited nodes and distances between them
# first 0/1 - univisited/visited
# second - distance from the source vertex
nodes = [[0, 0]]
num_vertices = len(vertices) # get the number of vertices
alg_path = []                # storing concurrent vertices the algorithm visits
INF = float('inf')           # defining infinity

# append all of the nodes except the source, assign infinity as the distance
def append_nodes():
    for node in range(0, num_vertices-1):
        nodes.append([0, INF])

# function to mark a node as visited - clears up the code
def mark_visited(node):
    nodes[node][0] = 1

# function to get the path with the smallest weight and the node corresponding to it
def next_node():
    isFound = False
    next = 0
    for vertex in range(0, num_vertices):
        # if univisited and the value of the current node is smaller or eq to the next node
        if nodes[vertex][0] == 0 and (not isFound or nodes[vertex][1] <= nodes[next][1]):
            isFound = True
            next = vertex
    return next

# main algorithm
def dijkstra():
    append_nodes()
    for vertex in range(num_vertices):
        next_vertex = next_node()                 # find next vertex to visit
        alg_path.append(chr(next_vertex + 65))    # visualise the path taken by the algorithm (conversion to ASCII)
        for i in range(num_vertices):
            # if connection between nodes exists and node is unvisited
            if vertices[next_vertex][i] > 0 and nodes[i][0] == 0:
                # distance = current distance to the vertex + value of the path saved in the matrix
                distance = nodes[next_vertex][1] + vertices[next_vertex][i]
                # if current distance is greater than the calculated -> reset
                if nodes[i][1] > distance:
                    nodes[i][1] = distance
        mark_visited(next_vertex)

def print_result():
    counter = 0
    print("Distance from source [A] to: ")
    for node in nodes:
        print("{} = {:1.2f}".format(chr(ord('A') + counter), node[1]))
        counter += 1

# networkx + matplotlib visualisation
def visualise():

    start_node = start_entry.get().upper()
    end_node = end_entry.get().upper()
    if start_node not in alg_path:
        message = tk.Tk()
        message.withdraw()
        tk.messagebox.showwarning("Warning", "The specified start node doesn't exist.")

    elif end_node not in alg_path:
        message = tk.Tk()
        message.withdraw()
        tk.messagebox.showwarning("Warning", "The specified end node doesn't exist.")

    else:
        G = nx.Graph()


        G.add_weighted_edges_from(edge_list)

        layout = nx.spring_layout(G, k=1)
        nx.draw_networkx_nodes(G, layout, node_size=700, node_color='red')
        nx.draw_networkx_labels(G, layout, font_size=10, font_family='sans-serif')
        nx.draw_networkx_edges(G, layout, edgelist=edge_list, width=1)

        path = nx.shortest_path(G, source=start_node, target=end_node)
        path_edges = set(zip(path, path[1:]))

        for node in alg_path:
            if node == end_node:
                nx.draw_networkx_nodes(G, layout, node_size=700, node_color='green', nodelist=node)
                break
            else:
                nx.draw_networkx_nodes(G, layout, node_size=700, node_color='green', nodelist=node)

        nx.draw_networkx_edges(G, layout, width=5, edgelist=path_edges, edge_color='green')
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G, layout, edge_labels=labels)

        plot.axis('off')
        title = "Dijkstra's algorithm ({} -> {})".format(start_node, end_node)
        plot.title(title)
        plot.show()


def init_window():
    # initialise root
    global root, start_entry, end_entry
    root = tk.Tk()
    root.title("Input data")
    root.geometry("250x200")

    # labels
    start_label = tk.Label(root, text="Enter start node: ")
    start_label.grid(row=1, column=1)
    end_label = tk.Label(root, text="Enter end node: ")
    end_label.grid(row=2, column=1)

    # entry fields
    start_entry = tk.Entry(root)
    start_entry.grid(row=1, column=2)
    end_entry = tk.Entry(root)
    end_entry.grid(row=2, column=2)

    # visualise button
    btn = tk.Button(root, text="Visualise", command=visualise)
    btn.grid(row=3, column=1)


# main loop
if __name__ == "__main__":
    init_window()
    dijkstra()
    print(alg_path)
    print_result()

    root.mainloop()
