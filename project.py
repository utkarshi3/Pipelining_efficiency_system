import heapq
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            # Union by rank
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1
            return True
        return False

def create_graph(edges):
    graph = defaultdict(list)
    for start, end, weight in edges:
        graph[start].append((weight, end))
        graph[end].append((weight, start))
    return graph

def prims_algorithm(start, edges):
    graph = create_graph(edges)
    frontier = []
    heapq.heappush(frontier, (0, start, None))  # None represents no prior vertex
    in_mst = set()
    total_cost = 0
    mst = []

    while frontier:
        weight, vertex, prev_vertex = heapq.heappop(frontier)
        if vertex in in_mst:
            continue
        in_mst.add(vertex)
        total_cost += weight
        if prev_vertex is not None:  # Only add edge if it connects to a previous vertex
            mst.append((prev_vertex, vertex))
        
        for next_cost, neighbor in graph[vertex]:
            if neighbor not in in_mst:
                heapq.heappush(frontier, (next_cost, neighbor, vertex))  # Pass current vertex as the new 'prev_vertex'
    
    return total_cost, mst

def kruskals_algorithm(nodes, edges):
    uf = UnionFind(len(nodes))
    mst = []
    total_cost = 0
    edges.sort(key=lambda x: x[2])  # Sort by weight

    for u, v, weight in edges:
        if uf.union(nodes.index(u), nodes.index(v)):
            mst.append((u, v))
            total_cost += weight

    return total_cost, mst

def draw_graph(graph, mst):
    G = nx.Graph()
    for node, edges in graph.items():
        for weight, neighbor in edges:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    all_edges = set(G.edges())
    mst_edges = set(mst)
    non_mst_edges = all_edges - mst_edges
    nx.draw_networkx_edges(G, pos, edgelist=non_mst_edges, style='dashed')
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, width=2)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    plt.axis('off')
    plt.show()

def main():
    print("Choose the algorithm for the MST:")
    print("1: Prim's Algorithm")
    print("2: Kruskal's Algorithm")
    choice = input("Enter choice (1 or 2): ")

    nodes = ['Extraction Site', 'Processing Plant', 'Storage Facility A', 'Storage Facility B']
    edges = [
        ('Extraction Site', 'Processing Plant', 5),
        ('Extraction Site', 'Storage Facility A', 10),
        ('Extraction Site', 'Storage Facility B', 7),
        ('Processing Plant', 'Storage Facility A', 15),
        ('Processing Plant', 'Storage Facility B', 6),
        ('Storage Facility A', 'Storage Facility B', 2)
    ]

    if choice == '1':
        start_facility = 'Extraction Site'
        cost, mst = prims_algorithm(start_facility, edges)
        print("Using Prim's Algorithm")
    elif choice == '2':
        cost, mst = kruskals_algorithm(nodes, edges)
        print("Using Kruskal's Algorithm")
    else:
        print("Invalid choice")
        return

    print("Total cost of MST:", cost)
    print("Edges in MST:", mst)
    draw_graph(create_graph(edges), mst)

if __name__ == '__main__':
    main()
