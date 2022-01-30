import pandas as pd
import matplotlib.pyplot as plt
import csv 
df = pd.read_csv("stars.csv")
radius = df["Radius"].to_list()
mass = df["Mass"].to_list()
mass.sort()
radius.sort()
plt.plot(radius,mass)
plt.title("Line Chart of Radius & Mass of the Star")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()
