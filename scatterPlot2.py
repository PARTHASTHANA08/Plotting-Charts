import pandas as pd 
import matplotlib.pyplot as plt
import csv 
df = df = pd.read_csv("stars.csv")
gravity = df["Gravity"].to_list()
mass = df["Mass"].to_list()
mass.sort()
gravity.sort()
plt.scatter(gravity,mass)
plt.title("Scatter Plot of Gravity & Mass of the Star")
plt.xlabel("Gravity")
plt.ylabel("Mass")
plt.show()
