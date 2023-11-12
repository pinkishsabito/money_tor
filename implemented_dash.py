import dash
import pandas as pd
import plotly.express as px
import requests
from dash import dcc, html

URL = "https://3a84-195-200-74-170.ngrok-free.app"
PARAMS = "banking_account_id=001ba43a-9bd0-4f14-8079-5e9e6c985628"

expense_response = requests.get(f"{URL}/get_expense_related_data?{PARAMS}")
income_response = requests.get(f"{URL}/get_income_related_data?{PARAMS}")

expense_data = pd.DataFrame(expense_response.json()['expense'])
income_data = pd.DataFrame(income_response.json()['income'])

expense_data['created_at'] = pd.to_datetime(expense_data['created_at'].apply(lambda x: x.split('T')[0]))
income_data['created_at'] = pd.to_datetime(income_data['created_at'].apply(lambda x: x.split('T')[0]))

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Expense and Income Dashboard'),

    dcc.Graph(
        id='expense-vs-income',
        figure=px.scatter(expense_data, x='created_at', y='amount', color='category_id', title='Expense vs. Income')
    ),

    dcc.Graph(
        id='expense-by-category',
        figure=px.bar(expense_data, x='category_id', y='amount', title='Expense by Category')
    ),

    dcc.Graph(
        id='income-over-time',
        figure=px.line(income_data, x='created_at', y='amount', title='Income Over Time')
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
