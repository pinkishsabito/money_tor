# %%
import requests
import pandas as pd
import dash
from dash import dcc, html
# %%
url = 'https://3a84-195-200-74-170.ngrok-free.app'
expense = requests.get(
    f'{url}/get_expense_related_data?banking_account_id=001ba43a-9bd0-4f14-8079-5e9e6c985628')
income = requests.get(
    f'{url}/get_income_related_data?banking_account_id=001ba43a-9bd0-4f14-8079-5e9e6c985628')

expense = expense.json()
income = income.json()
# %%
expense = pd.DataFrame(expense['expense'])
income = pd.DataFrame(income['income'])
# %%
expense = expense[['created_at', 'amount', 'to_id', 'category_id']]

# %%
income = income[['created_at', 'amount', 'from_id', 'category_id']]

# %%
expense['created_at'] = expense['created_at'].apply(lambda x: x.split('T')[0])
expense['created_at'] = pd.to_datetime(expense['created_at'])
# %%
income['created_at'] = income['created_at'].apply(lambda x: x.split('T')[0])
income['created_at'] = pd.to_datetime(income['created_at'])
# %%

# %%
# %%
top5_contacts = expense['to_id'].value_counts().reset_index().iloc[:5]

# %%
# %%
anual_outcome_by_category = expense[['category_id', 'amount']].groupby('category_id').aggregate(
    ['min', 'mean', 'median', 'max', 'sum']).reset_index()
# %%
expense['month'] = expense['created_at'].dt.month
# %%
anual_outcome_by_month = expense[['month', 'amount']].groupby('month').aggregate(
    ['min', 'mean', 'median', 'max', 'sum']).reset_index()

# %%
anual_outcome_by_catmonth_for_year = expense[['category_id', 'month', 'amount']].groupby(
    ['category_id', 'month']).aggregate(['min', 'mean', 'median', 'max', 'sum'])
# %%
income = income[['created_at', 'amount']]
# %%
total_expense = expense['amount'].sum()
# %%

# %%
total_income = income['amount'].sum()
# %%

# %%income.head()
# %%
income['month'] = income['created_at'].dt.month
# %%
# %%
income_by_month_for_year = income[['month', 'amount']].groupby('month').agg(
    ['min', 'mean', 'median', 'max', 'sum']).reset_index()
# %%
# %%

import plotly.express as px

# %%
difference = income_by_month_for_year['amount']['sum'] - anual_outcome_by_month['amount']['sum']
# Determine the color based on the difference
color_list = ['red' if diff < 0 else 'green' for diff in difference.values]
# %%

# %%
# Initialize the Dash app
app = dash.Dash(__name__)
# print(top5_contacts)
# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='My Dashboard'),

    # Pie chart using df1
    dcc.Graph(
        id='pie-chart',
        figure={
            'data': [
                {
                    'labels': ['Expense', 'Marzha'],
                    'values': [round(total_expense / total_income, 2) * 100,
                               round((total_income - total_expense) / total_income, 2) * 100],
                    'type': 'pie',
                    'hoverinfo': 'label+percent',
                    'textinfo': 'value',
                },
            ],
            'layout': {
                'title': 'Category Distribution (DataFrame 1)',
            }
        }
    ),

    # First chart
    dcc.Graph(
        id='graph1',
        figure={
            'data': [
                {'x': top5_contacts['to_id'], 'y': top5_contacts['count'], 'type': 'bar', 'name': 'Amount'},
            ],
            'layout': {
                'title': 'TOP 5 contacts'
            }
        }
    ),

    # Second chart
    dcc.Graph(
        id='graph2',
        figure={
            'data': [
                {'x': anual_outcome_by_category['category_id'].values, 'y': anual_outcome_by_category['amount']['sum'],
                 'type': 'bar', 'name': 'Amount'},
            ],
            'layout': {
                'title': 'Total expenses by category for year'
            }
        }
    ),
    # Third chart
    dcc.Graph(
        id='graph3',
        figure={
            'data': [
                {'x': anual_outcome_by_month['month'].values, 'y': anual_outcome_by_month['amount']['sum'],
                 'type': 'line', 'name': 'Expense'},
                {'x': income_by_month_for_year['month'].values, 'y': income_by_month_for_year['amount']['sum'],
                 'type': 'line', 'name': 'Income'},
            ],
            'layout': {
                'title': 'Total expenses by month for year'

            }
        }
    ),

    # Graph showing the difference between income and outcome
    dcc.Graph(
        id='difference-bar-chart',
        figure={
            'data': [
                {'x': income_by_month_for_year['month'], 'y': difference, 'type': 'bar', 'name': 'Difference',
                 'marker': {'color': color_list}},
            ],
            'layout': {
                'title': 'Monthly Difference between Income and Outcome',
                'xaxis': {'title': 'Month'},
                'yaxis': {'title': 'Difference'},
            }
        }
    )

])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
# %%
