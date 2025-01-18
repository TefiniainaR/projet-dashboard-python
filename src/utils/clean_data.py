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
    Aucun argument car les données (fichier CSV) sont chargées dans la fonction.
        
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
        "mumbai": (19.0760, 72.8777),
        "delhi": (28.6139, 77.2090),
        "kolkata": (22.5726, 88.3639),
        "hyderabad": (17.3850, 78.4867),
        "lucknow": (26.8467, 80.9462),
        "kanpur": (26.4499, 80.3319),
        "bhopal": (23.2599, 77.4126),
        "patna": (25.5941, 85.1376),
        "coimbatore": (11.0168, 76.9558),
        "kochi": (9.9312, 76.2673),
        "surat": (21.1702, 72.8311),
        "amritsar": (31.6340, 74.8723),
        "gwalior": (26.2183, 78.1828),
        "rajkot": (22.3039, 70.8022),
        "indore": (22.7196, 75.8577),
        "agra": (27.1767, 78.0081),
        "vadodara": (22.3072, 73.1812),
        "meerut": (28.9845, 77.7064),
        "nashik": (19.9975, 73.7898),
        "jodhpur": (26.2389, 73.0243),
        "guwahati": (26.1445, 91.7362),
        "dehradun": (30.3165, 78.0322),
        "ranchi": (23.3441, 85.3096),
        "mysore": (12.2958, 76.6394),
        "aurangabad": (19.8762, 75.3433),
        "trivandrum": (8.5241, 76.9366),
        "madurai": (9.9252, 78.1198),
        "udaipur": (24.5854, 73.7125),
        "ajmer": (26.4499, 74.6399)
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
    
    # Sauvegarde du DataFrame nettoyé dans un fichier CSV cleaned_data
    output_csv = os.path.join(output_dir, "cleaned_data.csv")
    df.to_csv(output_csv, index=False, encoding='utf-8')
    print(f"Data saved to {output_csv}")

    return df

# Appel de la fonction 
cleaned_df = clean_data()
