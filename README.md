Minimum Spanning Tree Algorithms

This project implements two classic algorithms for finding the Minimum Spanning Tree (MST) of a graph: Prim's Algorithm and Kruskal's Algorithm. The code is designed to simulate a scenario involving a network of facilities, such as an extraction site, a processing plant, and storage facilities. The MST is used to determine the most cost-effective way to connect all facilities with the minimum total weight of edges (e.g., cost or distance).

Features
- Union-Find Data Structure: Efficiently manages and merges sets during Kruskal's Algorithm to prevent cycles and ensure that only the minimum edges are included in the MST.

- Prim's Algorithm: Starts from a specific node and grows the MST by adding the least costly edge connecting a vertex inside the MST to a vertex outside it.

- Kruskal's Algorithm: Sorts all edges by weight and adds them one by one to the MST, ensuring that no cycles are formed using the Union-Find data structure.

Graph Visualization: Utilizes matplotlib and networkx to visually represent the graph and highlight the edges that are part of the MST.

How to Use
1. Run the Program: Execute the script. You'll be prompted to choose between Prim's Algorithm and Kruskal's Algorithm.

2. Input: The graph is predefined with nodes representing facilities and edges representing the connections between them, along with their respective weights.

3. Output: The program will output:

   - The total cost of the MST.
   - The edges that are part of the MST.
   - A graphical representation of the graph, with the MST highlighted.
     
Code Structure
1. UnionFind Class:

   - __init__(size): Initializes the Union-Find data structure.
   - find(p): Finds the root of the element p, with path compression.
   - union(p, q): Merges the sets containing p and q using union by rank.
   - create_graph(edges): Converts a list of edges into a graph represented as an adjacency list.

2. prims_algorithm(start, edges): Implements Prim's Algorithm to compute the MST starting from the given start node.

3. kruskals_algorithm(nodes, edges): Implements Kruskal's Algorithm to compute the MST for the given nodes and edges.

4. draw_graph(graph, mst): Visualizes the graph and highlights the MST using matplotlib and networkx.

5. main(): The main function that handles user input, executes the selected algorithm, and displays the results.

Example
Upon running the program, you'll be prompted to choose between Prim's or Kruskal's Algorithm. For instance, if you choose Prim's Algorithm, the program will calculate the MST starting from the "Extraction Site" and display the resulting MST along with its total cost.

