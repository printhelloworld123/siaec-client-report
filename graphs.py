import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.express as px
from geopy.distance import geodesic

df = pd.read_csv('all_siaec_waypoints_cleaned_onemap_address_extracted_200721.csv')

# Preparing the dataframe for plotting the overall trend in mismatches #

df_overall_trend = pd.DataFrame(df.groupby('date').match.apply(pd.value_counts))

df_overall_trend['date_final'] = list(map(lambda x: x[0], list(df_overall_trend.index)))

df_overall_trend_plot = pd.DataFrame(columns=['Date', 'Mismatch(%)'])
dates = set(df_overall_trend['date_final'])
for date in dates:
    overall_stat = df_overall_trend.loc[date,'match']
    mismatch_percent = round(overall_stat[False] / (overall_stat[False] + overall_stat[True]) * 100, 2)
    index = len(df_overall_trend_plot)
    df_overall_trend_plot.loc[index,'Date'] = date
    df_overall_trend_plot.loc[index,'Mismatch(%)'] = mismatch_percent
    
df_overall_trend_plot = df_overall_trend_plot.sort_values(by=['Date'])
df_overall_trend_plot = df_overall_trend_plot.reset_index()
df_overall_trend_plot = df_overall_trend_plot.drop(columns=['index'])



# Preparing the dataframe for plotting the distance deviation between matches & mismatches #

df_adjusted = df[df['date'] > '2021-05-31']

requested_coords = np.array(df_adjusted[['requested_lat','requested_lon']])
offer_coords = np.array(df_adjusted[['offer_lat','offer_lon']])

df_adjusted['distance_deviation(m) b/w req & offer'] = list(map(lambda req, offer: 
                                                                             geodesic(req, offer).m,
                                                                             requested_coords, offer_coords))


df_adjusted['match'] = list(map(lambda x: 'Match' if x == True else 'Mismatch', list(df_adjusted['match'])))

# Plotting the graph of overall trend in mismatches #

fig_overall_trend = px.line(df_overall_trend_plot, 
                            x='Date', 
                            y='Mismatch(%)', 
                            title='Total Mismatch in requested and offered bookings per day (%)')

fig_overall_trend.update_layout(xaxis_tickformat = '%d %B %Y',
                                yaxis_title="% of Mismatch")

fig_overall_trend.add_vline(x='2021-05-17', 
                            line_width=2, 
                            line_dash="dash", 
                            line_color="red")

fig_overall_trend.add_vline(x='2021-05-31', 
                            line_width=2, 
                            line_dash="dash", 
                            line_color="red")

# Plotting the graph of distances between requested and offered waypoints #

fig_dist_dev = px.histogram(df_adjusted, 
                            x="distance_deviation(m) b/w req & offer", 
                            color="match",
                            marginal="box",
                            histnorm='percent',
                            nbins=40,
                            color_discrete_map = {'Match':'#3CB371','Mismatch':'#F08080'},
                            title = "Distances (geodesic) between requested and offered waypoints for all bookings (31 May - 19 July)")

fig_dist_dev.update_layout(barmode='overlay',
                           xaxis_title="Distances (geodesic) between requested and offered waypoints (m)", 
                           yaxis_title="% of waypoints")

fig_dist_dev.update_layout(legend=dict(orientation="h",
                                       yanchor="bottom",
                                       x=1,
                                       y=1.02,
                                       xanchor="right"))

fig_dist_dev.update_layout(legend_title_text='')
fig_dist_dev.update_traces(opacity=0.6)
fig_dist_dev.update_traces(marker_line_width=1,marker_line_color="black")