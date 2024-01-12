import plotly_express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go 
from plotly.subplots import make_subplots
from dateutil.parser import parse

def parse_date(date_str):
    try:
        return parse(date_str)
    except (ValueError, TypeError):
        return pd.NaT

def line(data, selection='Total'): 

    # Utilisation de parse_date pour convertir 'date_added' en datetime
    data['date_added'] = data['date_added'].apply(parse_date)

    # Extraire l'année et créer une nouvelle colonne 'year_added'
    data['year_added'] = data['date_added'].dt.year

    # Filtrage des données pour les films et les séries télévisées
    movies_data = data[data['type'] == 'Movie']
    tv_shows_data = data[data['type'] == 'TV Show']

    # Comptage des émissions uniques par année pour chaque catégorie
    unique_movies_per_year = movies_data.groupby('year_added')['show_id'].nunique()
    unique_tv_shows_per_year = tv_shows_data.groupby('year_added')['show_id'].nunique()
    unique_total_per_year = data.groupby('year_added')['show_id'].nunique()

    # Création d'une figure Plotly
    fig = go.Figure()
    if selection == 'Total' or selection == 'Movies':
        fig.add_trace(go.Scatter(x=unique_movies_per_year.index, y=unique_movies_per_year, mode='lines', name='Movies'))

    if selection == 'Total' or selection == 'TV Shows':
        fig.add_trace(go.Scatter(x=unique_tv_shows_per_year.index, y=unique_tv_shows_per_year, mode='lines', name='TV Shows'))

    if selection == 'Total':
        fig.add_trace(go.Scatter(x=unique_total_per_year.index, y=unique_total_per_year, mode='lines', name='Total'))

    fig.update_layout(title='Number of Unique Shows Added to Netflix Each Year',
                      xaxis_title='Year',
                      yaxis_title='Number of Shows',
                      plot_bgcolor='rgba(0,0,0,0)',
                      paper_bgcolor='rgba(0,0,0,0)')

    return fig

    
def pie(data):#graph camembert

    # Comptage du nombre de films et séries TV uniques
    unique_movies = data[data['type'] == 'Movie']['title'].nunique()
    unique_tv_shows = data[data['type'] == 'TV Show']['title'].nunique()

    # Données pour le graphique en secteurs
    labels = ['Movies', 'TV Shows']
    sizes = [unique_movies, unique_tv_shows]
    colors = ['red', 'black']  # Vous pouvez personnaliser les couleurs ici

    # Création du graphique en secteurs avec Plotly
    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, marker_colors=colors)])
    fig.update_traces(textinfo='percent+label', pull=[0.1, 0])  
    fig.update_layout(title='Distribution of Movies and TV Shows on Netflix',
                      legend=dict(x=0.1, y=1.1),
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      paper_bgcolor='rgba(0, 0, 0, 0)',
                      showlegend=True)

    return fig

def pie2(data):#graph camembert

    # Comptage des occurrences de chaque genre
    genre_counts = data['listed_in'].value_counts()

    # Sélection des 10 genres les plus populaires
    top_genres = genre_counts.head(10)

    # Définition d'une palette de couleurs personnalisée
    netflix_colors = ['#E50914',  # Netflix Red
                      '#221f1f',  # Nearly Black
                      '#f5f5f1',  # Off White

                     ]

    # Création du graphique en secteurs avec Plotly
    fig = go.Figure(data=[go.Pie(labels=top_genres.index, 
                                 values=top_genres, 
                                 marker_colors=netflix_colors)])
    fig.update_traces(textinfo='percent+label', pull=[0.1] * len(top_genres))  
    fig.update_layout(title='Top 10 Popular Genres on Netflix',
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      paper_bgcolor='rgba(0, 0, 0, 0)',
                      showlegend=True)

    return fig



def map(df, selected_type):
    # Filtrez les données en fonction du type de contenu sélectionné
    if selected_type != 'All':
        filtered_data = df[df['type'] == selected_type]
    else:
        filtered_data = df

    # Préparez les données pour la carte
    filtered_data['country'] = filtered_data['country'].astype(str)
    data_expanded = filtered_data.assign(country=filtered_data['country'].str.split(',')).explode('country')
    data_expanded['country'] = data_expanded['country'].str.strip()
    data_clean = data_expanded[data_expanded['country'].str.len() > 0]
    country_count = data_clean['country'].value_counts().reset_index()
    country_count.columns = ['country', 'content_count']

    # Créez la carte choroplèthe avec les données filtrées
    map_fig = px.choropleth(country_count,
                            locations="country",
                            color="content_count",
                            color_continuous_scale=px.colors.sequential.Redor,
                            locationmode="country names",
                            projection="natural earth",
                            title=f'Distribution of Netflix {selected_type} Content by Country')
    map_fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return map_fig


def colonne(data):
    data['rating'].nunique()
    sub_data = data['rating'].value_counts().head(10)

    # Création du graphique en barres avec Plotly Express
    fig = px.bar(sub_data, x=sub_data.index, y=sub_data.values, color=sub_data.values,
                 color_continuous_scale='greens', title="Top 10 Ratings")

    # Mise à jour du layout si nécessaire
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',
                      paper_bgcolor='rgba(0,0,0,0)',
                      yaxis_title="Count")

    return fig




def main(data):

    app = dash.Dash(__name__)


    app.layout = html.Div( children=[

    dcc.Tabs([
        dcc.Tab(
            label='Line Chart',
            children=[
                html.Div([
                    dcc.Graph(figure=line(data))
                ])
            ]
        ),
        dcc.Tab(
            label='Pie Chart Movies/Series',
            children=[
                html.Div([
                    dcc.Graph(figure=pie(data))
                ])
            ]
        ),
        dcc.Tab(
            label='Pie Chart Genres ',
            children=[
                html.Div([
                    dcc.Graph(figure=pie2(data))
                ])
            ]
        ),
        dcc.Tab(
            label='Ratings',
            children=[
                html.Div([
                    dcc.Graph(figure=colonne(data))
                ])
            ]
        ),
        dcc.Tab(
            label='Content posted by countries',
            children=[
                html.Div([
                    dcc.RadioItems(
                        id='content-type-selector',
                        options=[
                            {'label': 'All', 'value': 'All'},
                            {'label': 'Series', 'value': 'TV Show'},
                            {'label': 'Movies', 'value': 'Movie'}
                        ],
                        labelStyle={'display': 'block', 'margin': '10px', 'font-size': '20px'},
                        style={'textAlign': 'center', 'color': '#E50914', 'padding': '20px'}
                    ),
                    dcc.Graph(id='map-chart')
                ])
            ]
        )

    ]),
    ])
    
    @app.callback(
        Output('map-chart', 'figure'),
        [Input('content-type-selector', 'value')]
    )
    def update_map(selected_type):
        return map(data, selected_type)


    app.run_server(debug=True, port=80)







