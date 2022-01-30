import pandas as pd
import matplotlib.pyplot as plt
import csv 
df = pd.read_csv("stars.csv")
radius = df["Radius"].to_list()
mass = df["Mass"].to_list()
mass.sort()
radius.sort()
plt.scatter(radius,mass)
plt.title("Scatter Plot of Radius & Mass of the Star")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()
