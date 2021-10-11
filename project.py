import pandas as pd
import plotly.express as px
import csv
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
print(mean)

graph = px.scatter(mean, x = "student_id" , y = "level", size="attempt", color="attempt",size_max=60)
graph.show()

