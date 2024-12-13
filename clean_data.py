import pandas as pd

def clean_data(df):
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
    
    # Suppression des valeurs manquantes
    df.dropna(inplace=True)  # Suppression des lignes avec des valeurs manquantes
    
    # Conversion des types de données
    print(df.columns)
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.lower()
    city_column = df.get('City')
    if 'city' in df.columns:
        df['City'] = df['City'].str.strip().str.lower()  # Supprimer les espaces et mettre en minuscule
        df['City'] = df['City'].str.normalize('NFD').str.encode('ascii', errors='ignore').str.decode('utf-8')  # Supprimer les accents
    else:
        print("La colonne 'City' est absente.")
    
    # Suppression des doublons
    df.drop_duplicates(inplace=True)
    
    # Réindexation après suppression des lignes
    df.reset_index(drop=True, inplace=True)
    
    return df
