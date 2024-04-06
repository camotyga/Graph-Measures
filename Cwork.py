import random
import networkx as nx

# Define a class to represent nodes in the graph
class Node:
    def __init__(self, id):
        # Each node has a unique identifier
        self.id = id
        # Set to store the identifiers of neighboring nodes
        self.neighbors = set()

    # Method to add a neighboring node
    def add_neighbor(self, neighbor_id):
        self.neighbors.add(neighbor_id)

# Define a class to represent edges in the graph
class Edge:
    def __init__(self, node1, node2):
        # Each edge connects two nodes
        self.node1 = node1
        self.node2 = node2

# Define a class to represent the entire graph
class Graph:
    def __init__(self):
        # Dictionary to store nodes with their identifiers as keys
        self.nodes = {}
        # List to store edges
        self.edges = []

    # Method to add a new node to the graph
    def add_node(self, id):
        # Create a new node object with the given identifier
        self.nodes[id] = Node(id)

    # Method to add a new edge between two nodes
    def add_edge(self, id1, id2):
        # If the nodes don't exist in the graph, create them
        if id1 not in self.nodes:
            self.add_node(id1)
        if id2 not in self.nodes:
            self.add_node(id2)
        # Add the neighboring relationship between the nodes
        self.nodes[id1].add_neighbor(id2)
        self.nodes[id2].add_neighbor(id1)
        # Create an edge object and add it to the list of edges
        self.edges.append(Edge(self.nodes[id1], self.nodes[id2]))

    # Method to get adjacency information compatible with NetworkX
    def adjacency(self):
        adjacency_dict = {}
        for node_id, node in self.nodes.items():
            adjacency_dict[node_id] = list(node.neighbors)
        return adjacency_dict

    # Method to iterate over nodes in the graph
    def __iter__(self):
        return iter(self.nodes.values())

# Create an instance of the graph
graph = Graph()

# Add nodes to the graph (7 vertices)
for i in range(1, 8):
    graph.add_node(i)

# Add edges to the graph (7 edges for an undirected graph)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(5, 6)
graph.add_edge(6, 7)
graph.add_edge(7, 1)

class GraphMetrics:
    def __init__(self, graph):
        self.graph = graph

    # Degree Centrality metric
    def degree_centrality(self, node_id):
        return len(self.graph.nodes[node_id].neighbors)

    # Closeness Centrality metric
    def closeness_centrality(self, node_id):
        total_distance = 0
        for node in self.graph.nodes.values():
            if node.id != node_id:
                total_distance += self.shortest_path_length(node_id, node.id)
        return 1 / total_distance

    # Betweenness Centrality metric
    def betweenness_centrality(self, node_id):
        total_paths = 0
        for source_node in self.graph.nodes.values():
            for target_node in self.graph.nodes.values():
                if source_node.id != node_id and target_node.id != node_id:
                    total_paths += self.shortest_path_count(source_node.id, target_node.id, node_id)
        return total_paths

    # Placeholder for computing shortest path length
    def shortest_path_length(self, start_id, end_id):
        # Implement shortest path algorithm here (e.g., Dijkstra's algorithm)
        pass

    # Placeholder for computing shortest path count
    def shortest_path_count(self, start_id, end_id, node_id):
        # Implement shortest path counting algorithm here
        pass


class Agent:
    def __init__(self, graph):
        """
        Initialize the Agent with the graph it operates on.

        Args:
            graph (Graph): The graph the agent operates on.
        """
        self.graph = graph
        # Compute and store shortest paths between each pair of nodes
        self.shortest_paths = nx.all_pairs_shortest_path_length(nx.Graph(graph.adjacency()))

    def random_walk(self, start_node_id, target_node_id):
        """
        Perform a random walk from the start node to the target node.

        Args:
            start_node_id (int): The ID of the start node.
            target_node_id (int): The ID of the target node.

        Returns:
            list: The IDs of the visited nodes.
        """
        current_node_id = start_node_id
        visited_nodes = [current_node_id]  # Store visited nodes
        while current_node_id != target_node_id:
            # Get the list of neighboring nodes
            neighbors = list(self.graph.nodes[current_node_id].neighbors)
            # Choose a random neighboring node to move to
            next_node_id = random.choice(neighbors)
            current_node_id = next_node_id
            visited_nodes.append(current_node_id)  # Store visited node
        return visited_nodes

    def shortest_path(self, start_node_id, target_node_id):
        """
        Find the shortest path from the start node to the target node.

        Args:
            start_node_id (int): The ID of the start node.
            target_node_id (int): The ID of the target node.

        Returns:
            list: The IDs of the nodes representing the shortest path.
        """
        # Retrieve the shortest path from the precomputed dictionary
        shortest_path = nx.shortest_path(nx.Graph(self.graph.adjacency()), source=start_node_id, target=target_node_id)
        return shortest_path

import random

# Define the number of simulations
num_simulations = 1000

# Initialize an instance of the Agent class with the graph
agent = Agent(graph)  # Assuming 'graph' is the instance of the Graph class you have defined

# Initialize variables to store results
random_walk_results = []
shortest_path_results = []

# Perform simulations for Random Walk
for _ in range(num_simulations):
    start_node_id = random.randint(1, 7)
    target_node_id = random.randint(1, 7)
    while start_node_id == target_node_id:
        target_node_id = random.randint(1, 7)
    visited_nodes = agent.random_walk(start_node_id, target_node_id)
    random_walk_results.append(len(visited_nodes))

# Perform simulations for Shortest Path
for _ in range(num_simulations):
    start_node_id = random.randint(1, 7)
    target_node_id = random.randint(1, 7)
    while start_node_id == target_node_id:
        target_node_id = random.randint(1, 7)
    visited_nodes = agent.shortest_path(start_node_id, target_node_id)
    shortest_path_results.append(len(visited_nodes))

# Print the average number of visited nodes for each movement
print("Average number of visited nodes for Random Walk:", sum(random_walk_results) / num_simulations)
print("Average number of visited nodes for Shortest Path:", sum(shortest_path_results) / num_simulations)
