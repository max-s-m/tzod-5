import networkx as nx
import matplotlib.pyplot as plt

N = 100 # к-ть об'єктів (вузлів)
M = 2   # к-ть нових зв'язків для кожного об'єкта
G = nx.barabasi_albert_graph(N, M) #граф

degree_dict = dict(G.degree())
betweenness = nx.betweenness_centrality(G)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

pos = nx.spring_layout(G)
node_color = [betweenness[n] for n in G.nodes()]
node_size = [v * 100 for v in degree_dict.values()]

nx.draw_networkx_edges(G, pos, ax=ax1, alpha=0.15, edge_color='black')
nodes = nx.draw_networkx_nodes(G, pos, ax=ax1, node_size=node_size, node_color=node_color, cmap=plt.cm.viridis)
nx.draw_networkx_labels(G, pos, ax=ax1, font_size=7, font_color="white", font_weight="bold")

plt.colorbar(nodes, ax=ax1, label='Betweenness')
ax1.set_title(f"Graph\n(bigger = more connections)", fontsize=14)
ax1.axis('off')

degrees = [degree_dict[n] for n in G.nodes()]
ax2.hist(degrees, bins=range(min(degrees), max(degrees) + 2), alpha=0.7, color='royalblue', edgecolor='black', align='left')
ax2.set_xlabel('Connections of one node')
ax2.set_ylabel('Node amount')
ax2.set_title('Connection analyse', fontsize=14)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

print("Details:")
top_hubs = sorted(degree_dict.items(), key=lambda x: x[1], reverse=True)[:3]
print(f"Top hubs (most connections):")
for node, deg in top_hubs:
    print(f"Node #{node}: {deg} direct connections")

top_broker = max(betweenness.items(), key=lambda x: x[1])[0]
print(f"\nTop broker node: node #{top_broker} (controls most shortest paths)")
print(f"Avg density: {nx.density(G):.4f}")
print(f"Clustering: {nx.average_clustering(G):.4f}")