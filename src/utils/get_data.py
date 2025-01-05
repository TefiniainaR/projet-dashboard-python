import pandas as pd

file_path = 'data/raw/rawdata.csv' #relative path

def get_data_from_csv(file_path):
    # Charger le fichier CSV dans un DataFrame pandas
    df = pd.read_csv(file_path, sep=',', encoding='utf-8')
    
    # Retourner le DataFrame pour utilisation dans d'autres parties de votre code
    return df
    

