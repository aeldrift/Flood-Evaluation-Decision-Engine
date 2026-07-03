import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/flooded_roads.csv")

# Graph 1: Open vs Flooded
counts = df["status"].value_counts()

plt.figure(figsize=(6,4))
counts.plot(kind="bar")
plt.title("Road Status")
plt.ylabel("Number of Roads")
plt.tight_layout()
plt.savefig("graphs/flood_risk_by_area.png")
plt.close()

# Graph 2: Route Comparison (sample demo values)
routes = pd.DataFrame({
    "Scenario": ["Normal Route", "Flood Route"],
    "Distance (km)": [3.2, 5.1]
})

plt.figure(figsize=(6,4))
plt.bar(routes["Scenario"], routes["Distance (km)"])
plt.title("Evacuation Route Comparison")
plt.ylabel("Distance (km)")
plt.tight_layout()
plt.savefig("graphs/route_comparison.png")
plt.close()

# Graph 3: GPU vs CPU (demo values)
perf = pd.DataFrame({
    "Method": ["CPU", "GPU"],
    "Time (ms)": [120, 18]
})

plt.figure(figsize=(6,4))
plt.bar(perf["Method"], perf["Time (ms)"])
plt.title("Route Recalculation Time")
plt.ylabel("Time (ms)")
plt.tight_layout()
plt.savefig("graphs/gpu_vs_cpu.png")
plt.close()

print("All graphs generated successfully!")