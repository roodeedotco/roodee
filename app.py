# Ref : https://www.youtube.com/watch?v=acFOhdo_bxw
# Ref : https://plotly.com/python-api-reference/plotly.express.html
# Ref : https://plotly.com/python/pie-charts/

# https://hackerthemes.com/bootstrap-cheatsheet/
# https://www.youtube.com/watch?v=USTqY4gH_VM&t=7s
# https://plotlydash.com/responsive-covid-19-dashboard-in-python-by-plotly-dash/
# https://www.youtube.com/watch?v=bDXypNBH1uw
# https://www.youtube.com/results?search_query=dash+plotly+google+sheet
# https://towardsdatascience.com/building-a-plotly-dash-app-from-google-sheets-part-1-d37dc41ece10
# https://towardsdatascience.com/how-to-create-your-first-web-app-using-python-plotly-dash-and-google-sheets-api-7a2fe3f5d256
# https://beanthemes.com/how-to-basic-cloudflare/


import numpy as np
import pandas as pd
import datetime

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table
from dash.dependencies import Output, Input
import plotly.express as px
import plotly.graph_objects as go


#----- Data Exploration & Preparation with Pandas -----#

df = pd.read_csv('kkk2.csv')
df = df.sort_values(by='Reporting Starts') 

#df['ReportingStarts'] = pd.to_datetime(df['Reporting Starts'], format='%Y%m%d')

#df['Profit'] = df['On-Facebook Purchase Conversion Value']-df['Amount Spent (THB)']
#df['ROAS'] = df['Profit']-df['Amount Spent (THB)']
#df['Margin'] = df['Amount Spent (THB)']/df['On-Facebook Purchase Conversion Value']

print(df.columns)

df2 = df[['Reporting Starts','Impressions','Amount Spent (THB)','Objective','Age','On-Facebook Purchase Conversion Value']].groupby('Age')


fig = go.Figure(go.Funnel(
    x = ["Impressions", "Link Clicks", "On-Facebook Purchases"],
    y = [df['Impressions'].sum(), df['Link Clicks'].sum(), df['On-Facebook Purchases'].sum(),],
    orientation = 'v',
    textposition = 'outside',
    )
)

# Data Visualization with Pandas
# ------------------------------- #

# PIE CHART #
# fig_pie = px.pie(data_frame=df, names='Reporting Starts', values='Impressions')
# fig_pie.show()

# BAR CHART #
# fig_bar = px.bar(data_frame=df, x='Reporting Starts', y='Impressions')
# fig_bar.show()

# HISTOGRAM CHART #
# fig_hist = px.histogram(data_frame=df, x='Reporting Starts', y='Impressions')
# fig_hist.show()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

# App layout

app.layout = dbc.Container([

    # Title
    dbc.Row([
        dbc.Col(html.H1('Hello from Seedsauce',
                        className='text-center text-primary',
            ))
    ]),

    # Header
    dbc.Row([
        dbc.Col(html.H2('Facebook Investment'))
    ]),

    # Data 
    dbc.Row([
        dbc.Col([
            html.H5('Impressions'),
            html.P(f"{sum(df['Impressions']):,.0f}",)
        ], width={'size':4}),
        dbc.Col([
            html.H5('Reach'),
            html.P(f"{sum(df['Impressions']):,.0f}",)
        ], width={'size':4}),
        dbc.Col([
            html.H5('Reach'),
            html.P(f"{sum(df['Impressions']):,.0f}",)
        ], width={'size':4})
    ]),

    # Data2
    dbc.Row([
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardHeader('Card Header1'),
                    dbc.CardBody([
                        html.P(f"{sum(df['Impressions']):,.0f}",)
                    ])
                ]
            )
        ], xs=12, sm=4, md=4, lg=4, xl=4),
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardHeader('Card Header1'),
                    dbc.CardBody([
                        html.P(f"{sum(df['Impressions']):,.0f}",)
                    ])
                ]
            )
        ], xs=12, sm=4, md=4, lg=4, xl=4),
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardHeader('Card Header1'),
                    dbc.CardBody([
                        html.P(f"{sum(df['Impressions']):,.0f}",)
                    ])
                ]
            )
        ], xs=12, sm=4, md=4, lg=4, xl=4),
    ]),

    # Header
    dbc.Row([
        dbc.Col(html.H2('Facebook Investment Graph'))
    ]),

    # Investment hist graph
    dcc.Graph(id='business-graph', figure=px.histogram(
                                        data_frame=df, 
                                        x='Reporting Starts', 
                                        y='Amount Spent (THB)', 
                                        color='Age'
                                    )),

    # Header Funnel
    dbc.Row([
        dbc.Col(html.H2('Funnel'))
    ]),

     # Data 
    dbc.Row([
        dbc.Col([
            html.H5('Impressions'),
            html.P(f"{sum(df['Impressions']):,.0f}",)
        ], width={'size':4}),
        dbc.Col([
            html.H5('Link Clicks'),
            html.P(f"{sum(df['Link Clicks']):,.0f}",)
        ], width={'size':4}),
        dbc.Col([
            html.H5('On-Facebook Purchases'),
            html.P(f"{sum(df['On-Facebook Purchases']):,.0f}",)
        ], width={'size':4})
    ]),

    # Funnel hist graph
    dcc.Graph(id='funnel-graph', figure=fig), 

    ############## SESSION 3 : Create Table ####################
    # Header Funnel
    dbc.Row([
        dbc.Col(html.H2('Ad Performance'))
    ]),

    # Table
    dbc.Row([
        dbc.Col(dash_table.DataTable(
                    id='table',
                    data=df2.head().to_dict('records'),
                    columns=[
                        {"name": 'Age', 'id': 'Age'},
                        {"name": 'Impressions', 'id': 'Impressions'},
                        {"name": 'Amount Spent (THB)', 'id': 'Amount Spent (THB)'},
                    ],
                    sort_action='native',
        ))
    ]),





    # Ad performance hist graph
    dcc.Graph(id='scatter-graph', figure=px.scatter(
                                    data_frame=df, 
                                    x='Amount Spent (THB)', 
                                    y='On-Facebook Purchase Conversion Value',
                                    #symbol='Age',
                                    color='Age'
                                    )),

], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)