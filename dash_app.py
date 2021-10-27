import dash
from dash import dcc
from dash import html
import plotly.express as px

import seaborn as sns
import pandas as pd

diabetes_untouched = pd.read_csv("data/diabetes.csv")









def launch():
    app = dash.Dash()
    app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure= trace
    )
])

    if __name__ == '__main__':
        app.run_server(debug=True)
    return app.layout
