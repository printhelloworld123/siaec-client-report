import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.express as px
from geopy.distance import geodesic
import graphs
import markdown
from graphs import *
from markdown import *

app = dash.Dash(__name__, external_stylesheets=['https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lux/bootstrap.min.css'])
server = app.server
app.layout = html.Div(
    [
        # Title #
        dbc.Row(dbc.Col(html.H2("SIAEC Waypoints Issue Analysis"),
                        style = {"padding-top":"5%",
                                 "padding-left":"8%"})),
        
        # Section 1 Header #
        dbc.Row(dbc.Col(html.H4("1. Overview"),
                        style = {"padding-top":"3%",
                                 "padding-left":"8%"})),
        
        # Section 1 Graph - Overall Trend in Mismatches #
        dbc.Row([dbc.Col(dcc.Graph(id='example-graph',
                                   figure=fig_overall_trend,
                                   style={"height": "500px",
                                          "padding-left":"5%",
                                          "padding-right":"17%"}))]),
        
        # Section 1 Analysis #
        dbc.Row(dbc.Col(children=markdown_text_section_1,
                        style={"padding-left":"8%",
                               "padding-right":"23%",
                               "text-align":"justify",
                               "font-size": "16px"})),
        
        # Section 2 Header #
        dbc.Row(dbc.Col(html.H4("2. Mismatch Analysis"),
                        style = {"padding-top" : "3%",
                                 "padding-left":"8%"})),
        
        # Section 2 Histogram #
        dbc.Row([dbc.Col(dcc.Graph(id='example-graph-1',
                                   figure=fig_dist_dev,
                                   style={"height": "550px",
                                          "padding-left":"5%",
                                          "padding-right":"17%"}))]),
        
        
        # Section 2 Map Visualization #     
        dbc.Row([html.Iframe(src="https://studio.unfolded.ai/public/10c60ffe-5f2e-458b-856e-8e633165d59c/embed",
                            style={"height": "550px",
                                   "width": "1390px",
                                   "overflow":"auto",
                                   "border":"0",
                                   "padding-left":"8%",
                                   "padding-right":"17%",
                                   "padding-bottom":"2%"})]),
        
        
        # Section 2 Analysis #
        dbc.Row([dbc.Col(children=markdown_text_section_2_1,
                        style={"padding-left":"8%",
                               "padding-right":"23%",
                               "padding-bottom":"5%",
                               "text-align":"justify",
                               "font-size": "16px"})])
    ]
)
        
                  
if __name__ == "__main__":
    app.run_server(debug=True)