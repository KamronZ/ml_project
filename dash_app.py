import dash
from dash import html

dash_app = dash.Dash(__name__,requests_pathname_prefix='/dash_app.py')
dash_app.layout = html.Div("Dash app")