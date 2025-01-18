import plotly.express as px
import pandas as pd


# Chargement des données
file_path = 'data/cleaned/cleaned_data.csv'
df = pd.read_csv(file_path)

# Graphique en secteur (camembert): Proportion de personnes ayant des pensées suicidaires
fig_pie = px.pie(df, names='have you ever had suicidal thoughts ?', title="Proportion de Personnes Ayant des Pensées Suicidaires",
                 color='have you ever had suicidal thoughts ?', color_discrete_map={0: 'lightgreen', 1: 'red'}, 
                 labels={'have you ever had suicidal thoughts ?': 'Pensées Suicidaires (0 = Non, 1 = Oui)'})