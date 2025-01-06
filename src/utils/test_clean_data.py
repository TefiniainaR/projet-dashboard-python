# a enlever

import sys
import os
from get_data import get_data_from_csv
from clean_data import clean_data
file_path='data/raw/rawdata.csv'
def test_clean_data():
    df_tested = get_data_from_csv(file_path)
    df_cleaned= clean_data(df_tested)
    print(df_cleaned)

    assert df_cleaned.isnull().sum().sum()==0, "Il reste des valeurs manquantes"
    assert len(df_cleaned)==1999," Le nombre de lignes après suppresion des doublons"
    print("test passé avec succés")

test_clean_data()