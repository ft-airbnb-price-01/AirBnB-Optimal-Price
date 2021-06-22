# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predict the price of a listing
            The Problem: Hosts have limited information to properly price their listings. \n
            ✅ This app will return the optimal price for a listing based on certain characteristics of that listing. \n
            ✅ This app will show which features are most important in determining price (which features guests care about most).
            """
        ),
        dcc.Link(dbc.Button('Predict Price', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src="assets/airbnb_image.jpeg", width='725px', height='400px')
    ]
)

layout = dbc.Row([column1, column2])