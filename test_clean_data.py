import pandas as pd
from get_data import get_data_from_csv
from clean_data import clean_data

file_path = r'U:\Lina-Tefiniaina-Dashboard-Python\projet-dashboard-python\data\raw\rawdata.csv'

def test_clean_data():
    df_cleaned= clean_data(get_data_from_csv(file_path))
    print(df_cleaned)

    assert df_cleaned.isnull().sum().sum()==0, "Il reste des valeurs manquantes"
    assert len(df_cleaned)== 3, " Le nombre de lignes après suppresion des doublons"
    print("test passé avec succés")

test_clean_data()