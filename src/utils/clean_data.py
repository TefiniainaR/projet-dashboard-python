import os
import sys
import pandas as pd
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from get_data import get_data_from_csv

# Chemin du fichier brut
file_path = 'data/raw/rawdata.csv'

def clean_data():
    """
    Fonction de nettoyage des données : gestion des valeurs manquantes, 
    conversion des types de données et suppression des doublons.
    
    Arguments:
    Aucun argument n'est nécessaire, le fichier CSV est chargé directement dans la fonction.
        
    Retourne:
    df : pandas.DataFrame
        Le DataFrame nettoyé.
    """
    # Vérifier si le fichier existe
    if not os.path.exists(file_path):
        print(f"Le fichier '{file_path}' n'existe pas.")
        return None
    
    # Chargement des données
    df = get_data_from_csv(file_path)
    print(f"Data loaded: {df.head()}")  # Vérification des premières lignes

    # Création du répertoire de sortie s'il n'existe pas déjà
    output_dir = 'data/cleaned'
    os.makedirs(output_dir, exist_ok=True)
    print(f"Répertoire de sortie créé : {output_dir}")

    # Suppression des valeurs manquantes
    df.dropna(inplace=True)  # Suppression des lignes avec des valeurs manquantes
    print(f"Data after cleaning missing values: {df.head()}")

    # Conversion des noms de colonnes : suppression des espaces et conversion en minuscules
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.lower()

    # Nettoyage de la colonne 'city' si elle existe
    if 'city' in df.columns:
        df['city'] = df['city'].astype(str).str.strip().str.lower()
        df['city'] = df['city'].str.normalize('NFD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        print(f"Data after city normalization: {df.head()}")
    else:
        print("La colonne 'city' est absente.")
    
    # Dictionnaire des coordonnées géographiques des villes
    city_coords = {
        "visakhapatnam": (17.6868, 83.2185),
        "bangalore": (12.9716, 77.5946),
        "srinagar": (34.0837, 74.7973),
        "varanasi": (25.3216, 82.9876),
        "jaipur": (26.9124, 75.7873),
        "pune": (18.5204, 73.8567),
        "thane": (19.2183, 72.9784),
        "chennai": (13.0827, 80.2707),
        "nagpur": (21.1458, 79.0882),
        "ahmedabad": (23.0225, 72.5714),
        # Ajoutez d'autres villes ici...
    }

    # Ajouter les colonnes de latitude et longitude en fonction des villes
    df['latitude'] = df['city'].map(lambda city: city_coords.get(city, (None, None))[0])
    df['longitude'] = df['city'].map(lambda city: city_coords.get(city, (None, None))[1])

    # Filtrer les données pour enlever les villes sans coordonnées géographiques
    df = df.dropna(subset=['latitude', 'longitude'])
    print(f"Data after filtering cities without coordinates: {df.head()}")

    # Suppression des doublons
    df.drop_duplicates(inplace=True)
    
    # Réindexation après suppression des lignes
    df.reset_index(drop=True, inplace=True)

    # Vérifier si la colonne existe et convertir les valeurs "Yes" et "No" en 1 et 0
    if 'have you ever had suicidal thoughts ?' in df.columns:
        df['have you ever had suicidal thoughts ?'] = df['have you ever had suicidal thoughts ?'].map({'Yes': 1, 'No': 0})
    else:
        print("La colonne 'have you ever had suicidal thoughts ?' n'existe pas dans le DataFrame.")
    
    # Sauvegarde du DataFrame nettoyé dans un fichier CSV
    output_csv = os.path.join(output_dir, "cleaned_data.csv")
    df.to_csv(output_csv, index=False, encoding='utf-8')
    print(f"Data saved to {output_csv}")

    return df

# Appel de la fonction pour nettoyer les données
cleaned_df = clean_data()
