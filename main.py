import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import datetime
from src.components.histogramme import fig_histogram
from src.components.map import fig_map
from src.components.pie import fig_pie
from src.components.nuage import fig_nuage

# Charger les données (assurez-vous que votre fichier CSV est bien accessible)
file_path = 'data/cleaned/cleaned_data.csv'
df = pd.read_csv(file_path)

# Nettoyer les noms de colonnes : retirer les espaces et convertir en minuscules
df.columns = df.columns.str.strip().str.lower()


# Vérifier si la colonne existe et convertir les valeurs "Yes" et "No" en 1 et 0
if 'have you ever had suicidal thoughts ?' in df.columns:
    df['have you ever had suicidal thoughts ?'] = df['have you ever had suicidal thoughts ?'].map({'Yes': 1, 'No': 0})
else:
    print("La colonne 'have you ever had suicidal thoughts ?' n'existe pas dans le DataFrame.")

# Créer l'application Dash
app = dash.Dash(__name__)

# Trouver le min et le max dans la colonne 'age' :
min_age = df['age'].min()
max_age = df['age'].max()

# Convertir la valeur numérique en chaîne de caractères : 
current_year = datetime.datetime.now().year  # Définir l'année actuelle

# Créer les bonnes valeurs de départ et de fin (remplacer les ages par des années de naissance)
start_year = current_year - max_age  
end_year = current_year - min_age    

# Format 'YYYY-MM-DD' 
start_date = f"{start_year}-01-01"
end_date = f"{end_year}-12-31"

# Définition de la mise en page de l'application Dash
app.layout = html.Div([
    html.H1("Dashboard sur la Dépression chez les Étudiants"),
    
    # Histogramme de dépression
    html.Div([dcc.Graph(figure=fig_histogram)]),
    
    # Carte géospatiale
    html.Div([dcc.Graph(figure=fig_map)]),
    
    # Graphique en secteur (Pie chart)
    html.Div([dcc.Graph(figure=fig_pie)]),

    # Nuage de points 
    html.Div([dcc.Graph(figure=fig_nuage)]),

    # Filtres interactifs
    html.Div([
        html.H3("Filtres interactifs"),
        dcc.Dropdown(
            id='region-dropdown',
            options=[{'label': region, 'value': region} for region in df['city'].unique()],
            value=df['city'].unique()[0],
            multi=False
        ),
        dcc.Dropdown(
            id='age-dropdown',
            options=[{'label': age, 'value': age} for age in df['age'].unique()],
            value=df['age'].unique()[0],
            multi=False
        ),
    ])
])

# Callbacks pour l'interactivité (si nécessaire, à adapter selon votre logique)
@app.callback(
    Output('region-dropdown', 'value'),
    [Input('region-dropdown', 'value')]
)
def update_region(value):
    # Logique pour filtrer ou mettre à jour des graphiques selon la sélection de la région
    return value

# Exécution du serveur Dash
if __name__ == "__main__":
    app.run_server(debug=True)
