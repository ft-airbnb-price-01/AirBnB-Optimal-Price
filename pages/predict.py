"""Handles `Predictions` page where users input attributes of a listing and returns a predicted price of that listing"""

# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import datetime, date, timezone
import calendar
import numpy as np
import pytz

from .prediction import make_prediction
from dash.exceptions import PreventUpdate


# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

# app.layout = html.Div([

column1 = dbc.Col([
        html.Br(),
        dcc.Markdown(
            """
            ## Predictions
            Input data about your listing to get a predicted price per night.
            """
        ),

        dcc.DatePickerSingle(
            id='host_since',
            min_date_allowed=date(2008, 3, 1),
            max_date_allowed=date(2021, 5, 31),
            initial_visible_month=date(2021, 5, 31),
            placeholder="Host Since"
        ),

        html.Br(),
        html.Br(),
        html.Br(),
        dcc.Dropdown(
            id='host_identity_verified',
            options=[
                {'label': 'True', 'value': 1},
                {'label': 'False', 'value': 0}
            ],
            placeholder="Host Identity Verified"
        ),
        
        html.Br(),
        html.Br(),
        html.Br(),
        dcc.Dropdown(
        id='city',
        options=[
            {'label': 'Boston', 'value': 0},
            {'label': 'New York City', 'value': 4},
            {'label': 'Washington, DC', 'value': 2},
            {'label': 'Chicago', 'value': 1},
            {'label': 'Los Angeles', 'value': 3},
            {'label': 'San Francisco', 'value': 5}
        ],
        placeholder="City"
        ),
        
        html.Br(),
        html.Br(),
        html.Br(),
        dcc.Dropdown(
            id='zipcode',
            options=[
                {'label': '02101 (Boston)', 'value': 2101},
                {'label': '02126 (Boston-South)', 'value': 2126},
                {'label': '02127 (Boston-East)', 'value': 2127},
                {'label': '02129 (Boston-North)', 'value': 2129},
                {'label': '02215 (Boston-West)', 'value': 2215},

                {'label': '10001 (NYC-Manhattan)', 'value': 10001},
                {'label': '10302 (NYC-Staten Island)', 'value': 10302},
                {'label': '10453 (NYC-Bronx)', 'value': 10453},
                {'label': '11212 (NYC-Brooklyn)', 'value': 11212},
                {'label': '11361 (NYC-Queens)', 'value': 11361},

                {'label': '20001 (DC-Central)', 'value': 20001},
                {'label': '20003 (DC-South)', 'value': 20003},
                {'label': '20007 (DC-West)', 'value': 20007},
                {'label': '20011 (DC-North)', 'value': 20011},
                {'label': '20018 (DC-East)', 'value': 20018},

                {'label': '60601 (Chicago)', 'value': 60601},
                {'label': '60044 (Chicago-North)', 'value': 60044},
                {'label': '60185 (Chicago-West)', 'value': 60185},
                {'label': '60617 (Chicago-South)', 'value': 60617},

                {'label': '90001 (LA-South)', 'value': 90001},
                {'label': '90004 (LA-Central)', 'value': 90004},
                {'label': '90022 (LA-East)', 'value': 90022},
                {'label': '90024 (LA-West)', 'value': 90024},
                {'label': '90031 (LA-North)', 'value': 90031},

                {'label': '94015 (SF-South)', 'value': 94015},
                {'label': '94103 (SF-East)', 'value': 94103},
                {'label': '94104 (SF-Central)', 'value': 94104},
                {'label': '94111 (SF-North)', 'value': 94111},
                {'label': '94116 (SF-West)', 'value': 94116},


            ],
            placeholder="Zipcode"
        ),

        html.Br(),
        html.Br(),
        html.Br(),
        dcc.Dropdown(
            id="property_type",
            options=[
                {'label': 'Apartment', 'value': 0},
                {'label': 'House', 'value': 16},
                {'label': 'Condominium', 'value': 10},
                {'label': 'Townhouse', 'value': 25},
                {'label': 'Loft', 'value': 19},
                {'label': 'Guesthouse', 'value': 14},
                {'label': 'Bed & Breakfast', 'value': 1},
                {'label': 'Bungalow', 'value': 4},
                {'label': 'Villa', 'value': 29},
                {'label': 'Dorm', 'value': 11},
                {'label': 'Guest suite', 'value': 13},
                {'label': 'Camper/RV', 'value': 6},
                {'label': 'Timeshare', 'value': 23},
                {'label': 'Cabin', 'value': 5},
                {'label': 'In-law', 'value': 18},
                {'label': 'Hostel', 'value': 15},
                {'label': 'Boutique hotel', 'value': 3},
                {'label': 'Boat', 'value': 2},
                {'label': 'Serviced apartment', 'value': 21},
                {'label': 'Tent', 'value': 22},
                {'label': 'Castle', 'value': 7},
                {'label': 'Vacation home', 'value': 28},
                {'label': 'Yurt', 'value': 30},
                {'label': 'Hut', 'value': 17},
                {'label': 'Treehouse', 'value': 27},
                {'label': 'Chalet', 'value': 9},
                {'label': 'Earth House', 'value': 12},
                {'label': 'Tipi', 'value': 24},
                {'label': 'Train', 'value': 26},
                {'label': 'Cave', 'value': 8},
                # {'label': 'Island', 'value': 'NYC'},
                # {'label': 'Lighthouse', 'value': 'MTL'},
                # {'label': 'Parking Space', 'value': 'SF'},
                # {'label': 'Casa particular', 'value': 'NYC'},
                {'label': 'Other', 'value': 20}
            ],
            placeholder="Property Type"
        ),

        html.Br(),
        html.Br(),
        html.Br(),
        dcc.Dropdown(
            id='instant_bookable',
            options=[
                {'label': 'True', 'value': 1},
                {'label': 'False', 'value': 0}
            ],
            placeholder="Instantly Bookable"
        ),

        html.Br(),
        html.Br(),
        html.Br(),

        dcc.Dropdown(
            id='cleaning_fee',
            options=[
                {'label': 'Yes', 'value': 1},
                {'label': 'No', 'value': 0}
            ],
            placeholder="Cleaning Fee"
        ),

        html.Br(),
        html.Br(),
        html.Br(),

        dcc.Dropdown(
        id='cancellation_policy',
        options=[
            {'label': 'strict', 'value': 2},
            {'label': 'flexible', 'value': 0},
            {'label': 'moderate', 'value': 1},
            {'label': 'super_strict_30', 'value': 3},
            {'label': 'super_strict_60', 'value': 4}
        ],
        placeholder="Cancellation Policy"
        ),

        html.Br(),
        html.Br(),
        html.Br(),

        html.Div([
            dbc.Button(
                id="button",
                n_clicks=0,
                children="Submit",
                color="primary"
            )
        ]),


    ],
    md=4,
)

column2 = dbc.Col(
    [   
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        dcc.Dropdown(
            id='room_type',
            options=[
                {'label': 'Entire home/apt', 'value': 0},
                {'label': 'Private room', 'value': 1},
                {'label': 'Shared room', 'value': 2}
            ],
            placeholder="Room Type"
        ),


        html.Br(),
        html.Br(),
        dcc.Dropdown(
            id='bed_type',
            options=[
                {'label': 'Real bed', 'value': 4},
                {'label': 'Futon', 'value': 2},
                {'label': 'Pull-out Sofa', 'value': 3},
                {'label': 'Airbed', 'value': 0},
                {'label': 'Couch', 'value': 1},
            ],
            placeholder="Bed Type"
        ),


        html.Br(),
        html.Br(),
        html.Br(),
        dcc.Input(
            id = "accommodates",
            placeholder = "# Accommodates",
            type = "number"
        ),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

        dcc.Input(
            id = "bedrooms",
            placeholder = "# Bedrooms",
            type = "number"
        ),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        

        dcc.Input(
            id = "beds",
            placeholder = "# Beds",
            type = "number"
        ),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

        dcc.Input(
            id = "bathrooms",
            placeholder = "# Bathrooms",
            type = "number"
        ),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

        dcc.Input(
            id = "review_scores_rating",
            placeholder = "Review Score Rating (0-100)",
            type = "number"
        ),

        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),

        html.Div(id="output_container")

    ],
    md=4,
)

@app.callback(
    Output("output_container", 'children'),
    [Input('host_since', 'date'),
     Input('button', 'n_clicks')],
    [State('property_type', 'value'),
    State('room_type', 'value'),
    State('accommodates', 'value'),
    State('bathrooms', 'value'),
    State('bed_type', 'value'),
    State('cancellation_policy', 'value'),
    State('cleaning_fee', 'value'),
    State('city', 'value'),
    State('host_identity_verified', 'value'),
    State('instant_bookable', 'value'),
    State('review_scores_rating', 'value'),
    State('zipcode', 'value'),
    State('bedrooms', 'value'),
    State('beds', 'value')]
)

def create_observation(host_since, property_type, room_type, accommodates, bathrooms,
                       bed_type, cancellation_policy, cleaning_fee, city, host_identity_verified,
                       instant_bookable, review_scores_rating, zipcode, bedrooms, beds, n_clicks):
    
    # 2d, numpy array exactly the same way as the DF the model trained on.
    # sklearn pipeline to format data automatically

    if host_since is not None:
        datetime_obj = datetime.strptime(host_since, "%Y-%m-%d")
        # timestamp = calendar.timegm(datetime_obj.timetuple())
        # dt = datetime.utcfromtimestamp(timestamp)
        utc_timestamp_seconds = datetime_obj.replace(tzinfo=timezone.utc).timestamp()
        utc_timestamp_days = utc_timestamp_seconds / 86400
    
    if n_clicks is None:
        raise PreventUpdate
    else:
        # container = np.array([[utc_timestamp_days]])
        # container_2 = np.array([[property_type, room_type, accommodates, bathrooms,
        #                 bed_type, cancellation_policy, cleaning_fee, city, host_identity_verified,
        #                 instant_bookable, review_scores_rating, zipcode, bedrooms, beds]]).astype(np.int)
        # final_container = np.concatenate(container, container_2)
        # prediction = make_prediction(final_container)

        final_container = np.array([[utc_timestamp_days, property_type, room_type, accommodates, bathrooms,
                        bed_type, cancellation_policy, cleaning_fee, city, host_identity_verified,
                        instant_bookable, review_scores_rating, zipcode, bedrooms, beds]]).astype(np.int)

        prediction = make_prediction(final_container)

    return prediction

    # print(prediction)

layout = dbc.Row([column1, column2])
