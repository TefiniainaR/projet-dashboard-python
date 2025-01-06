import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import datetime

# Charger les données (assurez-vous que votre fichier CSV est bien accessible)
file_path = 'data/cleaned/cleaned_data.csv'
df = pd.read_csv(file_path)

# Carte géospatiale : Répartition géographique de la dépression
fig_map = px.scatter_geo(df, lat='latitude', lon='longitude', hover_name='city', color='depression', 
                         size='age', title="Répartition Géospatiale de la Dépression chez les Étudiants", 
                         color_continuous_scale='Viridis', size_max=20)

# Limiter la carte à l'Inde et configurer les options de projection
fig_map.update_geos(
    projection_type="natural earth",  # Utilisation de la projection naturelle
    scope="asia",  # Limiter la carte à l'Asie (ou spécifiquement à l'Inde si vous le souhaitez)
)

fig_map.update_layout(title="Carte Géospatiale des Étudiants en Fonction de la Dépression")