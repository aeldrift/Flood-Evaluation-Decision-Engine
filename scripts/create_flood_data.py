import pandas as pd

df = pd.read_csv("kurla_roads.csv")

# Copy original data
df["status"] = "Open"

# Flood 10% of roads
flooded = df.sample(frac=0.10, random_state=42).index

df.loc[flooded, "status"] = "Flooded"

df.to_csv("kurla_flooded_roads.csv", index=False)

print(df["status"].value_counts())