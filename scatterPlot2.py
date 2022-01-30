import pandas as pd 
import plotly.express as px 
import csv 
df = df = pd.read_csv("stars.csv")
gravity = df["Gravity"].to_list()
mass = df["Mass"].to_list()
mass.sort()
gravity.sort()
fig = px.scatter(x = mass,y=gravity,title="Scatter Plot of Mass & Gravity of Stars")
fig.show()