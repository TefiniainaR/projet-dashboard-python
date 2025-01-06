import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import datetime

# Charger les données (assurez-vous que votre fichier CSV est bien accessible)
file_path = 'data/cleaned/cleaned_data.csv'
df = pd.read_csv(file_path)

# Histogramme : Distribution des niveaux de dépression
fig_histogram = px.histogram(df, x='depression', title="Distribution des Niveaux de Dépression chez les Étudiants", 
                              labels={'depression': 'Dépression (0 = Non, 1 = Oui)'}, color='gender',  
                              category_orders={'depression': [0, 1]})  # Catégoriser les valeurs de dépression

fig_histogram.update_layout(bargap=0.2) 