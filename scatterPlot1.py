import pandas as pd
import plotly.express as px
import csv 
df = pd.read_csv("stars.csv")
radius = df["Radius"].to_list()
mass = df["Mass"].to_list()
mass.sort()
radius.sort()
fig = px.line(x = mass,y=radius,title="Sctter Plot of Mass & Radius of Stars")
fig.show()