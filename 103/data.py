


import pandas as pd

data = [1,2,3,4,5]

df = pd.DataFrame(data)

print(df)





import plotly.express as px

#reading data from csv files
df = pd.read_csv("103/data.csv")
fig = px.bar(df, x='Country', y='InternetUsers')
fig.show()

df = pd.read_csv("line_chart.cvs")
fig = px.line(df, x='Country', y='Year')
fig.show()


