import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import datetime

# Chargement des données
file_path = 'data/cleaned/cleaned_data.csv'
df = pd.read_csv(file_path)

# Histogramme : Distribution des âges
fig_histogram = px.histogram(
    df, 
    x='age', 
    title="Distribution des Âges des Étudiants", 
    labels={'age': 'Âge'}, 
    color='gender', 
    nbins=10  # Définir le nombre de classes
)

# Personnalisation de la mise en page
fig_histogram.update_layout(bargap=0.2)


