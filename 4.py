import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
import math
from collections import defaultdict

def uniform_random():
    return random.random()


def choose_node(G):
    nodes = list(G.nodes())
    return random.choice(nodes)

# RSRG (Random Scale-Free Recursive Graph) model
def generate_rsr_graph(num_nodes, p):
    G = nx.Graph()
    G.add_node(1)
    for i in range(2, num_nodes+1):
        u = i
        v = nx.utils
        v = choose_node(G)
        while v == u:
            v = nx.utils
            v = choose_node(G)
        G.add_edge(u, v)
        for node in G.neighbors(v):
            if node != u and uniform_random() < p:
                G.add_edge(u, node)
    return G

# RSRBG (Random Scale-Free Recursive Bipartite Graph) model
def generate_rsr_bipartite_graph(num_left_nodes, num_right_nodes, p):
    G = nx.Graph()
    G.add_nodes_from(range(1, num_left_nodes+1), bipartite=0)
    G.add_nodes_from(range(num_left_nodes+1, num_left_nodes+num_right_nodes+1), bipartite=1)
    for i in range(1, num_left_nodes+1):
        u = i
        v = nx.utils
        v = choose_node(G)
        while v == u or G.nodes[v]['bipartite'] != 1:
            v = nx.utils
            v = choose_node(G)
        G.add_edge(u, v)
        for node in G.neighbors(v):
            if G.nodes[node]['bipartite'] != 0 and nx.utils.uniform_random() < p:
                G.add_edge(u, node)
    return G

# WS (Watts-Strogatz) model
def generate_ws_graph(num_nodes, k, p):
    return nx.watts_strogatz_graph(num_nodes, k, p)

# SF (Scale-Free) model
def generate_sf_graph(num_nodes, m):
    return nx.barabasi_albert_graph(num_nodes, m)

# ER (Erdos-Renyi) model
def generate_er_graph(num_nodes, p):
    return nx.erdos_renyi_graph(num_nodes, p)

# Draw the graph using NetworkX and Matplotlib
def draw_graph(G, title):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=200, font_size=8)
    plt.title(title)
    plt.show()

# Example usage
num_nodes = 50
p = 0.3
k = 4
m = 2

rsrg_graph = generate_rsr_graph(num_nodes, p)
draw_graph(rsrg_graph, "RSRG Model")

rsrbg_graph = generate_rsr_bipartite_graph(num_nodes, num_nodes, p)
draw_graph(rsrbg_graph, "RSRBG Model")

ws_graph = generate_ws_graph(num_nodes, k, p)
draw_graph(ws_graph, "WS Model")

sf_graph = generate_sf_graph(num_nodes, m)
draw_graph(sf_graph, "SF Model")

er_graph = generate_er_graph(num_nodes, p)
draw_graph(er_graph, "ER Model")


# RSRG (Random Scale-Free Recursive Graph) model
def generate_rsr_graph(num_nodes, p):
    G = nx.path_graph(num_nodes)
    for i in range(2, num_nodes+1):
        u = i
        v = choose_node(G)
        while v == u:
            v = choose_node(G)
        G.add_edge(u, v)
        for node in G.neighbors(v):
            if node != u and uniform_random() < p:
                G.add_edge(u, node)
    return G

# RSRBG (Random Scale-Free Recursive Bipartite Graph) model
def generate_rsr_bipartite_graph(num_left_nodes, num_right_nodes, p):
    G = nx.Graph()
    G.add_nodes_from(range(1, num_left_nodes+1), bipartite=0)
    G.add_nodes_from(range(num_left_nodes+1, num_left_nodes+num_right_nodes+1), bipartite=1)
    for i in range(1, num_left_nodes+1):
        u = i
        v = choose_node(G)
        while v == u or G.nodes[v]['bipartite'] != 1:
            v = choose_node(G)
        G.add_edge(u, v)
        for node in G.neighbors(v):
            if G.nodes[node]['bipartite'] != 0 and nx.utils.uniform_random() < p:
                G.add_edge(u, node)
    return G

# WS (Watts-Strogatz) model
def generate_ws_graph(num_nodes, k, p):
    return nx.random_graphs.random_regular_graph(k, num_nodes, p)

# SF (Scale-Free) model
def generate_sf_graph(num_nodes, m):
    return nx.random_graphs.barabasi_albert_graph(num_nodes, m)

# ER (Erdos-Renyi) model
def generate_er_graph(num_nodes, p):
    return nx.random_graphs.erdos_renyi_graph(num_nodes, p)

# Draw the graph using NetworkX and Matplotlib
def draw_graph(G, title):
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_size=200, font_size=8, node_color='lightblue', edge_color='gray')
    plt.title(title)
    plt.show()

# Example usage
num_nodes = 50
p = 0.3
q = 1
k = 4
m = 2

rsrg_graph = generate_rsr_graph(num_nodes, p)
draw_graph(rsrg_graph, "RSRG Model (Linear)")

rsrbg_graph = generate_rsr_bipartite_graph(num_nodes, num_nodes, p)
draw_graph(rsrbg_graph, "RSRBG Model (Linear)")

ws_graph = generate_ws_graph(num_nodes, k, q)
draw_graph(ws_graph, "WS Model (Linear)")

sf_graph = generate_sf_graph(num_nodes, m)
draw_graph(sf_graph, "SF Model (Linear)")

er_graph = generate_er_graph(num_nodes, p)
draw_graph(er_graph, "ER Model (Linear)")

# Function to plot the degree distribution PDF
def plot_degree_distribution_pdf(graph_type, graph, title):
    degrees = [degree for node, degree in graph.degree()]
    degree_count = np.bincount(degrees)
    pdf = degree_count / len(degrees)

    plt.bar(range(len(pdf)), pdf, width=0.8, color='b')
    plt.title(title)
    plt.xlabel('Degree')
    plt.ylabel('Probability Density')
    plt.xticks(np.arange(0, max(degrees)+1, 1))
    plt.xlim([-0.5, max(degrees)+0.5])
    plt.show()

# Generate RSRG graph
n = 1000  # Number of nodes
p = 0.05  # Probability of adding an edge between two nodes
rsrg_graph = nx.random_regular_graph(int(np.log(n)), n)
plot_degree_distribution_pdf("RSRG", rsrg_graph, "RSRG Degree Distribution PDF")

# Generate RSRBG graph
m1 = 500  # Number of nodes in set A
m2 = 500  # Number of nodes in set B
p_in = 0.1   # Probability of adding an edge between nodes in the same set
p_out = 0.01   # Probability of adding an edge between nodes in different sets
rsrbg_graph = nx.random_partition_graph([m1, m2], p_in, p_out)
plot_degree_distribution_pdf("RSRBG", rsrbg_graph, "RSRBG Degree Distribution PDF")

# Generate Watts-Strogatz graph
n = 1000  # Number of nodes
k = 10    # Each node is connected to k nearest neighbors
p = 0.1   # Probability of rewiring each edge
ws_graph = nx.watts_strogatz_graph(n, k, p)
plot_degree_distribution_pdf("WS", ws_graph, "WS Degree Distribution PDF")

# Generate Scale-Free graph
n = 1000  # Number of nodes
m = 10    # Number of edges to attach from a new node to existing nodes
sf_graph = nx.barabasi_albert_graph(n, m)
plot_degree_distribution_pdf("SF", sf_graph, "SF Degree Distribution PDF")

# Generate Erdős-Rényi graph
n = 1000  # Number of nodes
p = 0.01  # Probability of adding an edge between two nodes
er_graph = nx.erdos_renyi_graph(n, p)
plot_degree_distribution_pdf("ER", er_graph, "ER Degree Distribution PDF")

# Custom function to generate a random recursive tree
def generate_random_recursive_tree(n, m):
    if n <= 0:
        return nx.Graph()

    root = 0
    tree = nx.Graph()
    tree.add_node(root)

    def add_recursive_edges(node, remaining):
        if remaining <= 0:
            return

        children = np.random.choice(remaining, size=min(remaining, m), replace=False)
        for child in children:
            tree.add_edge(node, root + child + 1)
            add_recursive_edges(root + child + 1, remaining - child - 1)

    add_recursive_edges(root, n - 1)
    return tree
####

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Function to plot the degree distribution PDF
def plot_degree_distribution_pdf(graph_type, graph, title, ax):
    degrees = [degree for node, degree in graph.degree()]
    degree_count = np.bincount(degrees)
    pdf = degree_count / len(degrees)

    ax.bar(range(len(pdf)), pdf, width=0.8, alpha=0.7, label=graph_type)
    ax.set_title(title)
    ax.set_xlabel('Degree')
    ax.set_ylabel('Probability Density')
    ax.set_xticks(np.arange(0, max(degrees)+1, 1))
    ax.set_xlim([-0.5, max(degrees)+0.5])

# Generate RSRG graph
n = 1000  # Number of nodes
p = 0.05  # Probability of adding an edge between two nodes
rsrg_graph = nx.random_regular_graph(int(np.log(n)), n)

# Generate RSRBG graph
m1 = 500  # Number of nodes in set A
m2 = 500  # Number of nodes in set B
p_in = 0.1   # Probability of adding an edge between nodes in the same set
p_out = 0.01   # Probability of adding an edge between nodes in different sets
rsrbg_graph = nx.random_partition_graph([m1, m2], p_in, p_out)

# Generate Watts-Strogatz graph
n = 1000  # Number of nodes
k = 10    # Each node is connected to k nearest neighbors
p = 0.1   # Probability of rewiring each edge
ws_graph = nx.watts_strogatz_graph(n, k, p)

# Generate Scale-Free graph
n = 1000  # Number of nodes
m = 10    # Number of edges to attach from a new node to existing nodes
sf_graph = nx.barabasi_albert_graph(n, m)

# Generate Erdős-Rényi graph
n = 1000  # Number of nodes
p = 0.01  # Probability of adding an edge between two nodes
er_graph = nx.erdos_renyi_graph(n, p)

# Generate Random Recursive Tree
rrt_graph = generate_random_recursive_tree(n, m)

# Create subplots
fig, ax = plt.subplots()

# Plotting degree distribution PDFs for all graphs
plot_degree_distribution_pdf("RSRG", rsrg_graph, "RSRG Degree Distribution PDF", ax)
plot_degree_distribution_pdf("RSRBG", rsrbg_graph, "RSRBG Degree Distribution PDF", ax)
plot_degree_distribution_pdf("WS", ws_graph, "WS Degree Distribution PDF", ax)
plot_degree_distribution_pdf("SF", sf_graph, "SF Degree Distribution PDF", ax)
plot_degree_distribution_pdf("ER", er_graph, "ER Degree Distribution PDF", ax)
plot_degree_distribution_pdf("RRT", rrt_graph, "Random Recursive Tree Degree Distribution PDF", ax)

# Set plot properties
ax.legend()
ax.grid(True)

# Display the plot
plt.show()


import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
import math
from collections import defaultdict


# Function to plot the degree distribution PDF
def plot_degree_distribution_pdf(graph_type, degrees, title):
    degree_count = np.bincount(degrees)
    pdf = degree_count / len(degrees)

    plt.bar(range(len(pdf)), pdf, width=0.8, color='b')
    plt.title(title)
    plt.xlabel('Degree')
    plt.ylabel('Probability Density')
    plt.xticks(np.arange(0, max(degrees)+1, 1))
    plt.xlim([-0.5, max(degrees)+0.5])
    plt.show()

# Random Scale-Free Recursive Graph (RSRG)
def plot_rsr_graph():
    graph = nx.barabasi_albert_graph(100, 3, seed=42)
    degrees = [degree for _, degree in graph.degree()]
    degree_hist = np.histogram(degrees, bins=range(max(degrees) + 2))[0]
    degree_pdf = degree_hist / sum(degree_hist)
    plt.plot(range(len(degree_pdf)), degree_pdf, label='RSRG')

# Random Scale-Free Recursive Bipartite Graph (RSRBG)
def plot_rsr_bipartite_graph():
    graph = nx.bipartite.random_graph(10, 5, 0.5, seed=42)
    projection = nx.bipartite.projected_graph(graph, list(range(10)))
    degrees = [degree for _, degree in projection.degree()]
    degree_hist = np.histogram(degrees, bins=range(max(degrees) + 2))[0]
    degree_pdf = degree_hist / sum(degree_hist)
    plt.plot(range(len(degree_pdf)), degree_pdf, label='RSRBG')

# Watts-Strogatz (WS)
def plot_ws_graph():
    graph = nx.watts_strogatz_graph(100, 4, 0.3, seed=42)
    degrees = [degree for _, degree in graph.degree()]
    degree_hist = np.histogram(degrees, bins=range(max(degrees) + 2))[0]
    degree_pdf = degree_hist / sum(degree_hist)
    plt.plot(range(len(degree_pdf)), degree_pdf, label='WS')

# Scale-Free (SF)
def plot_sf_graph():
    graph = nx.scale_free_graph(100, seed=42)
    degrees = [degree for _, degree in graph.degree()]
    degree_hist = np.histogram(degrees, bins=range(max(degrees) + 2))[0]
    degree_pdf = degree_hist / sum(degree_hist)
    plt.plot(range(len(degree_pdf)), degree_pdf, label='SF')

# Erdos-Renyi (ER)
def plot_er_graph():
    graph = nx.erdos_renyi_graph(100, 0.15, seed=42)
    degrees = [degree for _, degree in graph.degree()]
    degree_hist = np.histogram(degrees, bins=range(max(degrees) + 2))[0]
    degree_pdf = degree_hist / sum(degree_hist)
    plt.plot(range(len(degree_pdf)), degree_pdf, label='ER')

# Plotting all graphs
plot_rsr_graph()
plot_rsr_bipartite_graph()
plot_ws_graph()
plot_sf_graph()
plot_er_graph()

# Setting plot properties
plt.xlabel('Degree')
plt.ylabel('Probability Density')
plt.title('Degree Distribution PDF')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()


