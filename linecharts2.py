import pandas as pd
import matplotlib.pyplot as plt
import csv 
df = pd.read_csv("stars.csv")
Gravity = df["Gravity"].to_list()
mass = df["Mass"].to_list()
mass.sort()
Gravity.sort()
plt.plot(Gravity,mass)
plt.title("Line Chart of Gravity & Mass of the Star")
plt.xlabel("Gravity")
plt.ylabel("Mass")
plt.show()
