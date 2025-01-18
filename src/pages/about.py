import dash
from dash import html

about_layout = html.Div([
    html.H1("À propos de ce projet"),
    
    html.H2("Contexte du projet"),
    html.P("Ce projet est un tableau de bord interactif qui permet d'analyser la dépression chez les étudiants en Inde. Il explore l'impact de plusieurs facteurs tels que l'âge, le sexe, les habitudes de vie, le stress académique, et d'autres éléments sur le bien-être mental des étudiants."),
    
    html.H3("Objectifs du tableau de bord :"),
    html.Div([
        html.P("Analyser la répartition des niveaux de dépression chez les étudiants."),
        html.P("Explorer les relations entre différents facteurs tels que l'âge, la ville, le sexe, et la pression académique."),
        html.P("Visualiser l'impact des habitudes de vie et du stress sur la santé mentale des étudiants."),
        html.P("Offrir des perspectives sur la situation de la dépression chez les jeunes adultes."),
    ], style={'padding-left': '20px', 'list-style-type': 'disc'}),  # Vous pouvez personnaliser davantage le style si besoin
    
    html.H3("Les Données :"),
    html.P("Les données utilisées proviennent d'une enquête menée auprès des étudiants en Inde. Elles comprennent des informations sur l'âge, le sexe, le stress financier, les habitudes de sommeil, l'alimentation, le stress académique, et d'autres facteurs psychologiques. Ces données ont été analysées pour en tirer des conclusions sur la santé mentale des étudiants."),
    
    html.H3("Méthodologie :"),
    html.P("Les graphiques et cartes géospatiales sont générés à l'aide des bibliothèques Dash et Plotly. Ces outils permettent de créer des visualisations interactives qui facilitent l'exploration des données et offrent des analyses intuitives. Le tableau de bord permet de filtrer les données selon différents critères pour observer les tendances et patterns associés à la dépression."),
    
    html.H3("Conclusion :"),
    html.P("Ce tableau de bord vise à sensibiliser et à mieux comprendre la dépression chez les étudiants. Les visualisations interactives permettent de mieux appréhender l'impact des facteurs de risque sur la santé mentale des jeunes adultes et de promouvoir des actions de soutien adaptées."),
    
], style={
    'padding': '20px',
    'font-family': 'Arial, sans-serif',
    'background-color': '#f9f9f9',
    'border-radius': '8px',
    'box-shadow': '0 2px 4px rgba(0, 0, 0, 0.1)',
    'max-width': '800px',
    'margin': 'auto'
})
