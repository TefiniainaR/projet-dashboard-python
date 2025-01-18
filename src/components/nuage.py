import plotly.express as px
import pandas as pd


# Chargement des données
file_path = 'data/cleaned/cleaned_data.csv'
df = pd.read_csv(file_path)

# Nuage de points : Stress Financier vs CGPA
fig_nuage = px.scatter(df, x='financial stress', y='cgpa', color='depression', size='age',
                       title="Stress Financier vs CGPA", labels={'financial stress': 'Stress Financier', 'cgpa': 'CGPA'})