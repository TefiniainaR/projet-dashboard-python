import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

file_path = r'data\raw\rawdata.csv'
# Charger vos données (par exemple, depuis un CSV nettoyé)
df = pd.read_csv(file_path)

# Créer l'application Dash
app = dash.Dash(__name__)

# Exemple de graphique : Histogramme sur une variable
fig_histogram = px.histogram(df, x='variable_name', title="Histogramme")

# Exemple de graphique de tendance : graphique linéaire sur le temps
fig_trend = px.line(df, x='date_column', y='value_column', title="Tendance au fil du temps")

# Définir la mise en page de la page d'accueil
app.layout = html.Div([
    html.H1("DashBoard sur la Dépression chez les étudiants"),
    html.Div([
        dcc.Graph(figure=fig_histogram),
        dcc.Graph(figure=fig_trend),
    ]),
    html.Div([
        html.H3("Filtres interactifs"),
        dcc.Dropdown(
            id='region-dropdown',
            options=[{'label': region, 'value': region} for region in df['region'].unique()],
            value=df['region'].unique()[0],
            multi=False
        ),
        dcc.DatePickerRange(
            id='date-picker',
            start_date=df['date_column'].min(),
            end_date=df['date_column'].max(),
            display_format='YYYY-MM-DD'
        )
    ])
])

# Charger les données géospatiales
df_map = pd.read_csv(file_path)

# Créer une carte géospatiale
fig_map = px.scatter_geo(df_map, lat='latitude', lon='longitude', hover_name='city',
                         color='region', size='population', projection="natural earth")
fig_map.update_layout(title="Carte Géospatiale Interactif")

# Créer l'application Dash
app = dash.Dash(__name__)

# Mise en page avec la carte et les graphiques
app.layout = html.Div([
    html.H1("Page d'Accueil - Dashboard Interactif"),
    html.Div([
        dcc.Graph(figure=fig_map),  # Carte géospatiale
    ]),
])

# Exécution du serveur
if __name__ == "__main__":
    app.run_server(debug=True)


# Callbacks pour interactivité
@app.callback(
    Output('region-dropdown', 'value'),
    [Input('region-dropdown', 'value')]
)
def update_region(value):
    # Vous pouvez mettre à jour les graphiques ou d'autres éléments en fonction du filtre
    return value

# Exécution du serveur
if __name__ == "__main__":
    app.run_server(debug=True)



