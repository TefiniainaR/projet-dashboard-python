import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import datetime
from src.components.histogramme import fig_histogram
from src.components.map import fig_map
from src.components.pie import fig_pie
from src.components.nuage import fig_nuage
from src.pages.home import home_layout
from src.pages.about import about_layout


file_path = 'data/cleaned/cleaned_data.csv'
df = pd.read_csv(file_path)
df.columns = df.columns.str.strip().str.lower()

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Accueil', href='/home'),
        html.Span(" | "),
        dcc.Link('Nos Graphes', href='/'),
        html.Span(" | "),
        dcc.Link('à Propos', href='/about'),
    ], style={
    'padding': '20px',
    'font-family': 'Arial, sans-serif',
    'background-color': '#f9f9f9',
    'border-radius': '8px',
    'box-shadow': '0 2px 4px rgba(0, 0, 0, 0.1)',
    'max-width': '800px',
    'margin': 'auto'
}),
    html.Hr(),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/about':
        return about_layout
    elif pathname == '/home':
        return home_layout
    else:
        return html.Div([
            html.H1("Dashboard sur la Dépression chez les Étudiants"),
            html.Div([
                html.H3("Sélectionner une plage d'âge"),
                dcc.RangeSlider(
                    id='age-range-slider',
                    min = int(df['age'].min()), 
                    max = int(df['age'].max()),  
                    step = 1,        
                    marks = {i : str(i) for i in range(int(df['age'].min()), int(df['age'].max()) + 1, 5)},  
                    value = [int(df['age'].min()), int(df['age'].max())],  
                ),
            ], style={'padding': '10px'}),
            html.Div([
                html.H3("Sélectionner une ville"),
                dcc.Dropdown(
                    id='region-dropdown',
                    options = [{'label': region, 'value': region} for region in df['city'].unique()],
                    value = df['city'].unique().tolist(),  
                    multi=True,
                ),
            ], style = {'padding': '10px'}),
            html.Div([
                html.H2("Histogramme"),
                dcc.Graph(id='histogramme-graph', figure = fig_histogram),
            ]),
            html.Div([
                html.H2("Carte géospatiale"),
                dcc.Graph(id='map-graph', figure = fig_map),
            ]),
            html.Div([
                html.H2("Graphique en secteurs"),
                dcc.Graph(id = 'pie-graph', figure = fig_pie)
            ]),
            html.Div([
                html.H2("Nuage de points"),
                dcc.Graph(id = 'nuage-graph', figure = fig_nuage)
            ]),
        ])

@app.callback(
    [Output('histogramme-graph', 'figure'),
     Output('pie-graph', 'figure'),
     Output('nuage-graph', 'figure'),
     Output('map-graph', 'figure')],
    [Input('region-dropdown', 'value'),
     Input('age-range-slider', 'value')]  
)
def update_graphs_by_region_and_age(regions, age_range):
    """Met à jour chaque graphique après un choix de ville ou une tranche d'âge"""

    # Si aucune ville n'est sélectionnée, on affiche toutes les villes
    if not regions:
        regions = df['city'].unique().tolist()  # Afficher toutes les villes si aucune n'est sélectionnée
    
    if age_range is None:
        age_range = [int(df['age'].min()), int(df['age'].max())]  

    filtered_df = df[(df['city'].isin(regions)) & 
                     (df['age'] >= age_range[0]) & 
                     (df['age'] <= age_range[1])]

    fig_histogram_filtered = px.histogram(
        filtered_df,
        x='depression', 
        title="Distribution des Niveaux de Dépression",
        labels={'depression': 'Dépression (0 = Non, 1 = Oui)'},
        color ='gender',
        category_orders={'depression': [0, 1]}
    )
    fig_histogram_filtered.update_layout(bargap = 0.2)

    fig_pie_filtered = px.pie(
        filtered_df,
        names='have you ever had suicidal thoughts ?',
        title="Proportion de Personnes Ayant des Pensées Suicidaires",
        color='have you ever had suicidal thoughts ?',
        color_discrete_map={0: 'lightgreen', 1: 'red'},
        labels={'have you ever had suicidal thoughts ?': 'Pensées Suicidaires (0 = Non, 1 = Oui)'}
    )

    fig_nuage_filtered = px.scatter(
        filtered_df,
        x='financial stress',
        y='cgpa',
        color='depression',
        size='age',
        title="Stress Financier vs CGPA",
        labels={'financial stress': 'Stress Financier', 'cgpa': 'CGPA'}
    )

    fig_map_filtered = px.scatter_geo(
        filtered_df,
        lat ='latitude',
        lon ='longitude',
        hover_name ='city',
        color ='depression',
        size ='age',
        title ="Répartition Géospatiale de la Dépression",
        color_continuous_scale ='Viridis',
        size_max=20
    )
    fig_map_filtered.update_geos(projection_type="natural earth", scope="asia")

    return fig_histogram_filtered, fig_pie_filtered, fig_nuage_filtered, fig_map_filtered



if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
