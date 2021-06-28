# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app, server
from pages import index, predict, insights, process

# Navbar docs: https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar
navbar = dbc.NavbarSimple(
    brand='Airbnb Price Predictor',
    brand_href='/', 
    children=[
        dbc.NavItem(dcc.Link('Predictions', href='/predictions', className='nav-link')), 
        # dbc.NavItem(dcc.Link('Insights', href='/insights', className='nav-link')), 
        # dbc.NavItem(dcc.Link('Process', href='/process', className='nav-link')), 
    ],
    sticky='top',
    color='#FF5A60', 
    light=True, 
    dark=True
)

# Footer docs:
# dbc.Container, dbc.Row, dbc.Col: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# html.P: https://dash.plot.ly/dash-html-components
# fa (font awesome) : https://fontawesome.com/icons/github-square?style=brands
# mr (margin right) : https://getbootstrap.com/docs/4.3/utilities/spacing/
# className='lead' : https://getbootstrap.com/docs/4.3/content/typography/#lead
footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('FT-Airbnb-Price-01', className='mr-1'), 
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/ft-airbnb-price-01/AirBnB-Optimal-Price'),
                    
                    html.Span('Joshua Elamin', className='mr-1'),
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/JAaron93'),
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/joshua-elamin-2b2ba9209/'),

                    html.Span('Andrew Lee', className='mr-1'),
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/andrewlee977'),
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/andrewlee97/'),

                    html.Span('Ian Knight', className='mr-1'),
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/iknight7000'),
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/ianknight480/'),
                ], 
                className='lead'
            )
        )
    )
)

# Layout docs:
# html.Div: https://dash.plot.ly/getting-started
# dcc.Location: https://dash.plot.ly/dash-core-components/location
# dbc.Container: https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    navbar, 
    dbc.Container(id='page-content', className='mt-4'), 
    html.Hr(), 
    footer
])


# URL Routing for Multi-Page Apps: https://dash.plot.ly/urls
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/predictions':
        return predict.layout
    # elif pathname == '/insights':
    #     return insights.layout
    # elif pathname == '/process':
    #     return process.layout
    else:
        return dcc.Markdown('## Page not found')

# Run app server: https://dash.plot.ly/getting-started
if __name__ == '__main__':
    app.run_server(debug=True)