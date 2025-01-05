import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.utils.get_data import get_data_from_csv
from src.utils.clean_data import clean_data
file_path='data/raw/rawdata.csv'
def test_clean_data():
    df_tested = get_data_from_csv(file_path)
    df_cleaned= clean_data(df_tested)
    print(df_cleaned)

    assert df_cleaned.isnull().sum().sum()==0, "Il reste des valeurs manquantes"
    assert len(df_cleaned)==1999," Le nombre de lignes après suppresion des doublons"
    print("test passé avec succés")

test_clean_data()