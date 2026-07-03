# import osmnx as ox

# place = "Kurla, Mumbai, India"

# G = ox.graph_from_place(place, network_type="drive")

# nodes, edges = ox.graph_to_gdfs(G)

# print(len(nodes))
# print(len(edges))

# edges.to_csv("kurla_roads.csv")

# # Condition

# if rainfall > 50:
#     road_status = "Flooded"

import osmnx as ox

# Kurla Station coordinates
center_point = (19.0728, 72.8826)

G = ox.graph_from_point(
    center_point,
    dist=2000,  # 2 km radius
    network_type="drive"
)

print(G)

nodes, edges = ox.graph_to_gdfs(G)

print("Nodes:", len(nodes))
print("Edges:", len(edges))

edges.to_csv("kurla_roads.csv")

print("CSV saved successfully!")