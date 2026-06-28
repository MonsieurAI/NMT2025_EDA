import pandas as pd
from pathlib import Path

def load_raw_nmt2025(filename="nmt2025_raw_data.csv"):
    data_path = Path(__file__).parent.parent / 'data' / filename
    return pd.read_csv(data_path,sep=';',low_memory=False)

def load_cleaned_nmt2025(filename="nmt2025_cleaned.csv"):
    data_path = Path(__file__).parent.parent / 'data' / filename
    return pd.read_csv(data_path,low_memory=False)

def load_geo_nmt2025(filename="nmt2025_geo.csv"):
    data_path = Path(__file__).parent.parent / 'data' / filename
    return pd.read_csv(data_path,low_memory=False)

def load_without_not_passed_nmt2025(filename="nmt2025_without_not_passed.csv"):
    data_path = Path(__file__).parent.parent / 'data' / filename
    return pd.read_csv(data_path,low_memory=False)