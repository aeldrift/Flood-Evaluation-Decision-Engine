import osmnx as ox

place = "Kurla, Mumbai, India"

G = ox.graph_from_place(place, network_type="drive")

nodes, edges = ox.graph_to_gdfs(G)

print(len(nodes))
print(len(edges))

edges.to_csv("kurla_roads.csv")


# conditions 
if rainfall > 50:
    road_status = "Flooded"