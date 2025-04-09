from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from line_chart import line_chart_dropdown
from bar_chart import bar_gender_checklist
from scartter_chart import scatter_geo

# Variable that defines the meta tag for the viewport
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Initialize the app using Bootstrap CSS
external_stylesheets = [dbc.themes.BOOTSTRAP]
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

row_one = dbc.Row([
    dbc.Col([
        html.H1("Paralympics Data Analytics"),
        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent congue luctus elit nec gravida.")
    ]),
])

row_two = dbc.Row([
    dbc.Col(children=[
        dcc.Dropdown(
            id='line-chart-dropdown',  # Ensure this id matches the callback
            options=[
                {"label": "Events", "value": "events"},
                {"label": "Sports", "value": "sports"},
                {"label": "Countries", "value": "countries"},
                {"label": "Athletes", "value": "participants"},
            ],
            placeholder="Select an option"
        )
    ], width=4),
    dbc.Col(children=[
        dcc.Checklist(
            id='bar-chart-checklist',
            options=[
                {'label': 'Winter', 'value': 'winter'},
                {'label': 'Summer', 'value': 'summer'}
            ],
            value=[]
        )
    ], width={"size": 4, "offset": 2}),
])

row_three = dbc.Row([
    dbc.Col(children=[
        dcc.Graph(id='line-chart')  # 折线图
    ], width=6),
    dbc.Col(children=[
        dcc.Graph(id='bar-chart')  # 条形图 ✅ 确保它存在
    ], width=6),
])


row_four = dbc.Card([
    dbc.CardImg(src=app.get_asset_url("logos/2022_Beijing.jpg"), top=True),
    dbc.CardBody([
        html.H4("Beijing 2022", className="card-title"),
        html.P("Number of athletes: XX", className="card-text"),
        html.P("Number of events: XX", className="card-text"),
        html.P("Number of countries: XX", className="card-text"),
        html.P("Number of sports: XX", className="card-text"),
    ]),
],
    style={"width": "18rem"},
)

# Add an HTML layout to the Dash app
app.layout = dbc.Container([
    row_one,
    row_two,
    row_three,
    row_four
])

# Define the callback function
@app.callback(
    Output('line-chart', 'figure'),
    Input('line-chart-dropdown', 'value')
)
def update_line_chart(selected_option):
    if selected_option:
        # Generate the line chart based on the selected option
        fig = line_chart_dropdown(selected_option)
    else:
        # If no option is selected, return an empty figure
        fig = px.line(title='No data selected')
    return fig

# Define the callback function
@app.callback(
    Output('bar-chart', 'figure'),
    Input('bar-chart-checklist', 'value')
)
def update_line_chart(selected_option):
    if selected_option:
        # Generate the line chart based on the selected option
        fig = bar_gender_checklist(selected_option)
    else:
        # If no option is selected, return an empty figure
        fig = px.line(title='No data selected')
    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5050)
