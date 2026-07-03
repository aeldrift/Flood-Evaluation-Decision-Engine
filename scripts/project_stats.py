import pandas as pd

df = pd.read_csv("data/flooded_roads.csv")

total_roads = len(df)
flooded_roads = len(df[df["status"]=="Flooded"])
open_roads = len(df[df["status"]=="Open"])

total_length = df["length"].sum()/1000
flooded_length = df[df["status"]=="Flooded"]["length"].sum()/1000

print(f"Total Road Segments: {total_roads}")
print(f"Open Roads: {open_roads}")
print(f"Flooded Roads: {flooded_roads}")
print(f"Total Network Length: {total_length:.2f} km")
print(f"Flooded Length: {flooded_length:.2f} km")