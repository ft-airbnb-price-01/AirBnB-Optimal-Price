# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import date


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
        dcc.Input(
            id = "accommodates",
            placeholder = "# Accommodates",
            type = "number"
        ),

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

        dcc.Input(
            id = "beds",
            placeholder = "# Beds",
            type = "number"
        ),

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

        dcc.Input(
            id = "review_scores_rating",
            placeholder = "Review Score Rating",
            type = "number"
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
        html.Br(),
        ## UPDATE BED TYPE VALUES
        dcc.Dropdown(
            id='bed_type',
            options=[
                {'label': 'Read bed', 'value': 0},
                {'label': 'Futon', 'value': 1},
                {'label': 'Pull-out Sofa', 'value': 2},
                {'label': 'Airbed', 'value': 3},
                {'label': 'Couch', 'value': 4},
            ],
            placeholder="Bed Type"
        )



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
        ## UPDATE INSTANT BOOKABLE VALUES
        dcc.Dropdown(
            id='instant_bookable',
            options=[
                {'label': 'True', 'value': 0},
                {'label': 'False', 'value': 1}
            ],
            placeholder="Instantly Bookable"
        ),

        html.Br(),
        html.Br(),
        html.Br(),
        ## UPDATE INSTANT BOOKABLE VALUES
        dcc.Dropdown(
            id='host_identity_verified',
            options=[
                {'label': 'True', 'value': 0},
                {'label': 'False', 'value': 1}
            ],
            placeholder="Host Identity Verified"
        ),
        html.Br(),
        html.Br(),
        html.Br(),

        html.Div([
            dbc.Button(
                id="button",
                n_clicks=0,
                children="Submit"
            )
        ]),

        html.Div(id="output_container")



    ],
    md=4,
)

@app.callback(
    Output("output_container", 'children'),
    [Input('button', 'n_clicks')],
    [State('accommodates', 'value'),
    State('bedrooms', 'value'),
    State('beds', 'value'),
    State('bathrooms', 'value'),
    State('review_scores_rating', 'value'),
    State('cleaning_fee', 'value'),
    State('property_type', 'value'),
    State('room_type', 'value'),
    State('bed_type', 'value'),
    State('host_since', 'date'),
    State('cancellation_policy', 'value'),
    State('instant_bookable', 'value'),
    State('host_identity_verified', 'value')]
)

def create_observation(accommodates, bedrooms, beds, bathrooms, review_scores_rating, cleaning_fee,
                       property_type, room_type, bed_type, host_since, cancellation_policy, instant_bookable,
                       host_identity_verified, n_clicks):

    # 2d, numpy array exactly the same way as the DF the model trained on.
    # sklearn pipeline to format data automatically
    container = f"""{accommodates}{bedrooms}{beds}{bathrooms}{review_scores_rating}{cleaning_fee}
                    {property_type}{room_type}{bed_type}{host_since}{cancellation_policy}
                    {instant_bookable}{host_identity_verified}"""
    
    return container


layout = dbc.Row([column1, column2])


