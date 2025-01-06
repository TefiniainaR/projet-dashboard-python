
import pandas as pd
from src.utils.get_data import get_data_from_csv

file_path = 'data/raw/rawdata.csv'

def clean_data(df_defined):
    """
    Fonction de nettoyage des données : gestion des valeurs manquantes, 
    conversion des types de données et suppression des doublons.
    
    Arguments:
    df : pandas.DataFrame
        Le DataFrame contenant les données à nettoyer.
        
    Retourne:
    df : pandas.DataFrame
        Le DataFrame nettoyé.
    """
    #output_dir = 'data\cleaned'
    #os.makedirs(output_dir, exist_ok=True)

    df_defined = get_data_from_csv(file_path)
    
    # Suppression des valeurs manquantes
    df_defined.dropna(inplace=True)  # Suppression des lignes avec des valeurs manquantes
    
     # Conversion des types de données
    print(df.columns)
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.lower()
    
    # Nettoyage de la colonne 'city'
    if 'city' in df.columns:
        df['city'] = df['city'].astype(str).str.strip().str.lower()
        df['city'] = df['city'].str.normalize('NFD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    else:
        print("La colonne 'city' est absente.")
    
    # Ajout des coordonnées géographiques (latitude et longitude) en fonction des villes
    city_coords = {
        "Visakhapatnam": (17.6868, 83.2185),
        "Bangalore": (12.9716, 77.5946),
        "Srinagar": (34.0837, 74.7973),
        "Varanasi": (25.3216, 82.9876),
        "Jaipur": (26.9124, 75.7873),
        "Pune": (18.5204, 73.8567),
        "Thane": (19.2183, 72.9784),
        "Chennai": (13.0827, 80.2707),
        "Nagpur": (21.1458, 79.0882),
        "Ahmedabad": (23.0225, 72.5714),
        # Ajoutez d'autres villes ici...
    }
    
    # Ajouter les colonnes de latitude et longitude
    df['latitude'] = df['city'].map(lambda city: city_coords.get(city, (None, None))[0])
    df['longitude'] = df['city'].map(lambda city: city_coords.get(city, (None, None))[1])

    # Filtrer les données pour enlever les villes sans coordonnées
    df = df.dropna(subset=['latitude', 'longitude'])

    # Suppression des doublons
    df.drop_duplicates(inplace=True)
    
    # Réindexation après suppression des lignes
    df.reset_index(drop=True, inplace=True)
    
    #output_csv = os.path.join(output_dir, "cleaned_data.csv")
    #df.to_csv(output_csv, index=False, encoding='utf-8')
    #print(f"La data frame nettoyée et souvegardée sous '{output_csv}'.")
    return df