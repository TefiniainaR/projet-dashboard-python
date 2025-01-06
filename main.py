
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import datetime

# Charger les données (assurez-vous que votre fichier CSV est bien accessible)
file_path = 'data/raw/rawdata.csv'
df = pd.read_csv(file_path)

# Coordonnées géographiques pour chaque ville (exemple)
city_coords = {
    "Visakhapatnam": (17.6868, 83.2185),
    "Bangalore": (12.9716, 77.5946),
    "Srinagar": (34.0837, 74.7973),
    "Varanasi": (25.3216, 82.9876),
    "Jaipur": (26.9124, 75.7873),
    "Pune": (18.5204, 73.8567),
    "Thane": (19.2183, 72.9784),
    "Chennai": (13.0827, 80.2707),
    "Nagpur": (21.1458, 79.0882),
    "Ahmedabad": (23.0225, 72.5714),
    # Ajoutez d'autres villes ici...
}

# Ajouter les colonnes de latitude et longitude
df['latitude'] = df['City'].map(lambda city: city_coords.get(city, (None, None))[0])
df['longitude'] = df['City'].map(lambda city: city_coords.get(city, (None, None))[1])

# Filtrer les données pour enlever les villes sans coordonnées
df_geo = df.dropna(subset=['latitude', 'longitude'])

# Créer l'application Dash
app = dash.Dash(__name__)

# Histogramme : Distribution des niveaux de dépression
fig_histogram = px.histogram(df, x='Depression', title="Distribution des Niveaux de Dépression chez les Étudiants", labels={'Depression': 'Dépression (0 = Non, 1 = Oui)'}, color='Gender',  category_orders={'Depression': [0, 1]})  # Catégoriser les valeurs de dépression

fig_histogram.update_layout(bargap=0.2) 

# Carte géospatiale : Répartition géographique de la dépression
fig_map = px.scatter_geo(df_geo, lat='latitude', lon='longitude', hover_name='City',color='Depression', size='Age', title="Répartition Géospatiale de la Dépression chez les Étudiants",color_continuous_scale='Viridis', size_max=20)


# Limiter la carte à l'Inde et configurer les options de projection
fig_map.update_geos(
    projection_type="natural earth",  # Utilisation de la projection naturelle
    scope="asia",  # Limiter la carte à l'Asie (ou spécifiquement à l'Inde si vous le souhaitez)
)

fig_map.update_layout(title="Carte Géospatiale des Étudiants en Fonction de la Dépression")

# Conversion des valeurs "Yes" et "No" en 1 et 0
df['Have you ever had suicidal thoughts ?'] = df['Have you ever had suicidal thoughts ?'].map({'Yes': 1, 'No': 0})

# Graphique en secteur : Proportion de personnes ayant des pensées suicidaires
fig_pie = px.pie(df, names='Have you ever had suicidal thoughts ?', title="Proportion de Personnes Ayant des Pensées Suicidaires",color='Have you ever had suicidal thoughts ?', color_discrete_map={0: 'lightgreen', 1: 'red'}, labels={'Have you ever had suicidal thoughts ?': 'Pensées Suicidaires (0 = Non, 1 = Oui)'})

# Nuage de points : 
fig_nuage = px.scatter(df, x='Financial Stress', y='CGPA',color='Depression', size='Age',title="Stress Financier vs CGPA",labels={'Financial Stress': 'Stress Financier', 'CGPA': 'CGPA'})
# Correction d'erreur: DatePickerRange 

# Trouver le min et le max dans la colomne 'Age' : 
min_age = df['Age'].min()
max_age = df['Age'].max()

# Convertir la valeur numérique en chaîne de caractères : 

current_year = datetime.datetime.now().year    # Définir l'année actuelle

# Créer les bonnes valeurs de départ et de fin (remplacer les ages par des années de naissance)
start_year = current_year - max_age  
end_year = current_year - min_age    

# Format 'YYYY-MM-DD' 
start_date = f"{start_year}-01-01"
end_date = f"{end_year}-12-31"

# Ensure start_date and end_date are in the correct string format
start_date = str(start_date)  # Ensure it's a string
end_date = str(end_date)      # Ensure it's a string

# Définition la mise en page de l'application Dash
app.layout = html.Div([
    html.H1("Dashboard sur la Dépression chez les Étudiants"),
    
    # Histogramme de dépression
    html.Div([dcc.Graph(figure=fig_histogram)]),
    
    # Carte géospatiale
    html.Div([dcc.Graph(figure=fig_map)]),
    
    # Pie chart
    html.Div([dcc.Graph(figure=fig_pie)]),

    # Nuage de points 
    html.Div([dcc.Graph(figure=fig_nuage)]),

    # Filtres interactifs
    html.Div([
        html.H3("Filtres interactifs"),
        dcc.Dropdown(
            id='region-dropdown',
            options=[{'label': region, 'value': region} for region in df['City'].unique()],
            value=df['City'].unique()[0],
            multi=False
        ),
        dcc.Dropdown(
            id='age-dropdown',
            options=[{'label': age, 'value': age} for age in df['Age'].unique()],
            value=df['Age'].unique()[0],
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