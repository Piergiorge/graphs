import networkx as nx
import matplotlib.pyplot as plt

# Create a new graph
G = nx.Graph()

# Add nodes to the graph
G.add_node("Human")
G.add_node("Chimpanzee")
G.add_node("Gorilla")
G.add_node("Orangutan")

# Add edges to the graph
G.add_edge("Human", "Chimpanzee")
G.add_edge("Human", "Gorilla")
G.add_edge("Human", "Orangutan")
G.add_edge("Chimpanzee", "Gorilla")
G.add_edge("Chimpanzee", "Orangutan")
G.add_edge("Gorilla", "Orangutan")

# Draw the graph using the spring layout
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)

# Display the graph
plt.show()
