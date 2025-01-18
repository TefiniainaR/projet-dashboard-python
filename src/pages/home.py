import dash
from dash import html

# Définition de la mise en page « Accueil »

home_layout = html.Div([
    html.H1("Bienvenue sur notre DashBoard"),
    html.H2("Étude sur la dépression chez les étudiants en Inde"),
    html.P("Ce tableau de bord permet d'analyser la répartition des niveaux de dépression parmi les étudiants en fonction de facteurs tels que l'âge, le sexe, les habitudes de vie, le stress académique et financier."),
    
    html.H3("Objectifs du Dashboard :"),
    html.Ul([
        html.Li("Analyser la répartition de la dépression parmi les étudiants."),
        html.Li("Explorer les tendances selon l'âge, la ville, le sexe, etc."),
        html.Li("Visualiser l'impact des habitudes de vie et du stress sur la santé mentale."),
        html.Li("Comprendre l'étendue de la dépression chez les jeunes.")
    ]),
    
    html.H3("Instructions pour l'utilisateur :"),
    html.P("Sélectionnez une tranche d'âge et une ou plusieurs villes pour ajuster les graphiques interactifs."),
    html.P("Les graphiques permettent d'explorer la répartition des niveaux de dépression, les pensées suicidaires, le stress financier, et plus encore.")
], style={
    'padding': '20px',
    'font-family': 'Arial, sans-serif',
    'background-color': '#f9f9f9',
    'border-radius': '8px',
    'box-shadow': '0 2px 4px rgba(0, 0, 0, 0.1)',
    'max-width': '800px',
    'margin': 'auto'
})

