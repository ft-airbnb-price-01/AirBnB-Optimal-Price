# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import date
import numpy as np


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
        ## UPDATE INSTANT BOOKABLE VALUES
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
            {'label': 'New York City', 'value': 4},
            {'label': 'Los Angeles', 'value': 3},
            {'label': 'San Francisco', 'value': 5},
            {'label': 'Washington, DC', 'value': 2},
            {'label': 'Chicago', 'value': 1},
            {'label': 'Boston', 'value': 0}
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

            {'label': '60601 (Chicago)', 'value': 60617},
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
        ### NEED TO UPDATE VALUES
        dcc.Dropdown(
            id="property_type",
            options=[
                {'label': 'Apartment', 'value': 'Apartment'},
                {'label': 'House', 'value': 'House'},
                {'label': 'Condominium', 'value': 'Condominium'},
                {'label': 'Townhouse', 'value': 'Townhouse'},
                {'label': 'Loft', 'value': 'Loft'},
                {'label': 'Guesthouse', 'value': 'Guesthouse'},
                {'label': 'Bed & Breakfast', 'value': 'Bed & Breakfast'},
                {'label': 'Bungalow', 'value': 'Bungalow'},
                {'label': 'Villa', 'value': 'Villa'},
                {'label': 'Dorm', 'value': 'Dorm'},
                {'label': 'Guest suite', 'value': 'Guest suite'},
                {'label': 'Camper/RV', 'value': 'SF'},
                {'label': 'Timeshare', 'value': 'NYC'},
                {'label': 'Cabin', 'value': 'MTL'},
                {'label': 'In-law', 'value': 'SF'},
                {'label': 'Hostel', 'value': 'NYC'},
                {'label': 'Boutique hotel', 'value': 'MTL'},
                {'label': 'Boat', 'value': 'SF'},
                {'label': 'Serviced apartment', 'value': 'NYC'},
                {'label': 'Tent', 'value': 'MTL'},
                {'label': 'Castle', 'value': 'SF'},
                {'label': 'Vacation home', 'value': 'NYC'},
                {'label': 'Yurt', 'value': 'MTL'},
                {'label': 'Hut', 'value': 'SF'},
                {'label': 'Treehouse', 'value': 'NYC'},
                {'label': 'Chalet', 'value': 'MTL'},
                {'label': 'Earth House', 'value': 'SF'},
                {'label': 'Tipi', 'value': 'NYC'},
                {'label': 'Train', 'value': 'MTL'},
                {'label': 'Cave', 'value': 'SF'},
                {'label': 'Island', 'value': 'NYC'},
                {'label': 'Lighthouse', 'value': 'MTL'},
                {'label': 'Parking Space', 'value': 'SF'},
                {'label': 'Casa particular', 'value': 'NYC'},
                {'label': 'Other', 'value': 'MTL'}
            ],
            placeholder="Property Type"
        ),

        html.Br(),
        html.Br(),
        html.Br(),
        ## UPDATE INSTANT BOOKABLE VALUES
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
            {'label': 'strict', 'value': 0},
            {'label': 'flexible', 'value': 1},
            {'label': 'moderate', 'value': 2},
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
# ])

column2 = dbc.Col(
    [   
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        ## UPDATE ROOM TYPE VALUES
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
        ## UPDATE BED TYPE VALUES
        dcc.Dropdown(
            id='bed_type',
            options=[
                {'label': 'Real bed', 'value': 0},
                {'label': 'Futon', 'value': 1},
                {'label': 'Pull-out Sofa', 'value': 2},
                {'label': 'Airbed', 'value': 3},
                {'label': 'Couch', 'value': 4},
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
    [Input('button', 'n_clicks')],
    [State('host_since', 'date'),
    State('property_type', 'value'),
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
    State('bedrooms', 'value'),
    State('beds', 'value'),
    State('zipcode', 'value')]
)

def create_observation(host_since, property_type, room_type, accommodates, bathrooms,
                       bed_type, cancellation_policy, cleaning_fee, city, host_identity_verified,
                       instant_bookable, review_scores_rating, bedrooms, beds, zipcode, n_clicks):

    # container = f"""Host since:{host_since} Property type:{property_type} Room type:{room_type} Accommodates:{accommodates}
    #                 Bathrooms:{bathrooms} Bed type:{bed_type} Cancellation policy:{cancellation_policy} Cleaning fee:{cleaning_fee}
    #                 City:{city} Host identity verified:{host_identity_verified} Instant bookable:{instant_bookable}
    #                 Review scores rating:{review_scores_rating} Bedrooms:{bedrooms} Beds:{beds} Zipcode:{zipcode}"""
    
    # 2d, numpy array exactly the same way as the DF the model trained on.
    # sklearn pipeline to format data automatically
    container = np.array([host_since, property_type, room_type, accommodates, bathrooms,
                       bed_type, cancellation_policy, cleaning_fee, city, host_identity_verified,
                       instant_bookable, review_scores_rating, bedrooms, beds, zipcode, n_clicks])

    return container


layout = dbc.Row([column1, column2])
