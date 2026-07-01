import pandas as pd
from pathlib import Path

def load_data(filename,year):
    data_path = Path(__file__).parent.parent / 'data' / f'{year}' / f'nmt{year}_{filename}.csv'
    if filename == 'raw_data':
        data = pd.read_csv(data_path,sep=';',low_memory=False)
    else:
        data = pd.read_csv(data_path,low_memory=False)
    return data