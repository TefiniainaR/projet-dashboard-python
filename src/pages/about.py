import dash
from dash import html

# Créer l'application Dash
app = dash.Dash(__name__)

# Mise en page de la page "À propos"
app.layout = html.Div([
    html.H1("À propos de ce projet"),
    html.P("Ce projet est un tableau de bord interactif permettant de visualiser des données géospatiales et statistiques."),
    html.P("Les données sont analysées et présentées sous forme de graphiques interactifs et de cartes géospatiales."),
])

# Exécution du serveur
if __name__ == "__main__":
    app.run_server(debug=True)