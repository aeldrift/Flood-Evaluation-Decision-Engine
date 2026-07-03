import pandas as pd

df = pd.read_csv("data/roads.csv")

print("Missing Values:\n")
print(df.isnull().sum())