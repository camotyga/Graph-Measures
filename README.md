Graph Algorithms Simulation
This repository contains Python code for simulating graph algorithms, specifically random walks and shortest paths, on a given graph. The simulation utilizes the NetworkX library for graph-related operations and random module for generating random walks and target nodes.

Introduction
Graphs are fundamental data structures used to model relationships between objects. Graph algorithms play a crucial role in various fields, including computer science, social network analysis, and transportation systems.

This project focuses on simulating two common graph algorithms:

Random Walk: A stochastic process where an agent moves from one node to another randomly among its neighbors.
Shortest Path: Finding the shortest path between two nodes in a graph, typically using algorithms like Dijkstra's algorithm or breadth-first search.

Implementation
Graph Representation
The graph is represented using custom Python classes:
Node: Represents a node in the graph.
Edge: Represents an edge connecting two nodes.
Graph: Represents the entire graph and provides methods to add nodes and edges.

Graph Metrics
The GraphMetrics class computes centrality metrics for nodes in the graph, including:
Degree Centrality
Closeness Centrality
Betweenness Centrality

Agent
The Agent class operates on the graph and performs simulations of random walks and shortest paths.
It utilizes NetworkX for computing shortest paths between all pairs of nodes in the graph.

Simulation
Simulations are performed for both random walks and shortest paths with a specified number of iterations.
Random start and target nodes are chosen for each simulation.

Usage
To run the simulations:
Clone this repository to your local machine.
Install the required dependencies by running pip install -r requirements.txt.
Execute the Python script graph_simulation.py.

Dependencies
Python 3.x
NetworkX

Contributors
Oghenetega Emagha

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Special thanks to the contributors and the creators of NetworkX for their valuable libraries and resources.





