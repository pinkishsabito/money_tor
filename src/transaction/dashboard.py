# transaction/dashboard.py
from dash import Dash, dcc, html

def init_dashboard():
    print('ok')
    dash_app = Dash(__name__)
    dash_app.layout = html.Div(
        [
            dcc.Graph(
                id="example-graph",
                figure={
                    "data": [{"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "SF"}],
                    "layout": {"title": "Dash Data Visualization"},
                },
            )
        ]
    )
    return dash_app
