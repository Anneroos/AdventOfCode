import networkx as nx
G = nx.Graph()

with open("input25.txt") as f:
    lines = f.read().splitlines()


for line in lines:
    l = line.split(": ")
    node = l[0]
    connectedTo = l[1].split()
    print(node, connectedTo)
    G.add_node(node)
    for n in connectedTo:
        G.add_node(n)
        G.add_edge(node, n, capacity=1.0)
nredges = G.number_of_edges()
nrnodes = G.number_of_nodes()
print(nrnodes,nredges)

# G.minimum_cut()
cut_value, partition = nx.minimum_cut(G, "vnm", "bzg") # Trial and error of different nodes ;)
print(cut_value)
print(len(partition[0]), len(partition[1]))
print(len(partition[0])* len(partition[1]))