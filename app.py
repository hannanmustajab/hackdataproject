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
    data = go.Figure([go.Scatter(x=df['human_readable_date'], y=df['value'], name="AAPL High",
                line_color='deepskyblue',
                opacity=0.8)])
    data.update_layout(title_text='Temperature Values with Reading',
                  xaxis_rangeslider_visible=True)



    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON



@app.route('/')
def index():
    graph = create_plot()
    return render_template('index.html',graph=graph)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')