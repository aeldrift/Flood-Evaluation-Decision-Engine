import pandas as pd

df = pd.read_csv("data/flooded_roads.csv")

total_roads = len(df)
flooded_roads = len(df[df["status"]=="Flooded"])
open_roads = len(df[df["status"]=="Open"])

total_length = df["length"].sum()/1000
flooded_length = df[df["status"]=="Flooded"]["length"].sum()/1000