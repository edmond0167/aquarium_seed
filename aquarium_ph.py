import plotly
import plotly.graph_objs as go
import pandas as pd
from plotly.graph_objs import Scatter, Layout
df = pd.read_csv("/var/www/html/aquarium/aquarium.csv")
data = [go.Scatter(
          x=df.Date,
          y=df['pH'])]
layout = go.Layout(
        title='Aquarium pH',
        xaxis=dict(
            title='Time',
            titlefont=dict(
                family='Courier New, monospace',
                size=30,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title='pH',
            titlefont=dict(
                family='Courier New, monospace',
                size=30,
                color='#7f7f7f'
            )
        )
    )
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig,
                    filename='/var/www/html/aquarium/aquarium_ph.html',
                    auto_open=False)
print("Aquarium pH plotted")
