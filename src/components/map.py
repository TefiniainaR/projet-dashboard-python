import plotly.express as px
import pandas as pd


# Chargement des données
file_path = 'data/cleaned/cleaned_data.csv'
df = pd.read_csv(file_path)

# Carte géospatiale : Répartition géographique de la dépression
fig_map = px.scatter_geo(df, lat='latitude', lon='longitude', hover_name='city', color='depression', 
                         size='age', title="Répartition Géospatiale de la Dépression chez les Étudiants", 
                         color_continuous_scale='Viridis', size_max=20)

# Limiter la carte à l'Asie ( car les données se limitent à l'Inde)
fig_map.update_geos(
    projection_type="natural earth",  # Utilisation de la projection naturelle
    scope="asia",  # Limiter la carte à l'Asie 
)

fig_map.update_layout(title="Répartition Géospatiale de la Dépression")