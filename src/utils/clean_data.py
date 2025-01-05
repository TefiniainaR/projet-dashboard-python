
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
    df_defined = get_data_from_csv(file_path)
    
    # Suppression des valeurs manquantes
    df_defined.dropna(inplace=True)  # Suppression des lignes avec des valeurs manquantes
    
    # Conversion des types de données
    print(df_defined.columns)
    df_defined.columns = df_defined.columns.str.strip()
    df_defined.columns = df_defined.columns.str.lower()
    city_column = df_defined.get('city')
    if 'city' in df_defined.columns:
        df_defined['city'] = df_defined['city'].str.strip().str.lower()  # Supprimer les espaces et mettre en minuscule
        df_defined['city'] = df_defined['city'].str.normalize('NFD').str.encode('ascii', errors='ignore').str.decode('utf-8')  # Supprimer les accents
    else:
        print("La colonne 'city' est absente.")
    
    # Suppression des doublons
    df_defined.drop_duplicates(inplace=True)
    
    # Réindexation après suppression des lignes
    df_defined.reset_index(drop=True, inplace=True)
    
    return df_defined
