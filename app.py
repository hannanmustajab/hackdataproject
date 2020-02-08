from flask import Flask, render_template
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly
import json
app = Flask(__name__)


def create_plot():
    df = pd.read_csv('data_set.csv')
    df = df.drop('context', axis=1)
    df = df[df['value'] > 0]
    data = [
        go.Scatter(
            x=df['human_readable_date'], # assign x as the dataframe column 'x'
            y=df['value']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON



@app.route('/')
def index():
    graph = create_plot()
    return render_template('index.html',graph=graph)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')