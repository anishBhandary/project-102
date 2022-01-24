import pandas as pd
import plotly.express as px

df = pd.read_csv("Data.csv")
fig = px.scatter(df, x = "Population" , y = "Per capita",color = "Country",size = "Percentage")
fig.show()