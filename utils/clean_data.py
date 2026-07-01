import pandas as pd
import numpy as np
from utils.load_data import load_data
from pathlib import Path

YEAR = 2025

# Clean data file
def clean_data(data,subjects):
    # Needed columns
    columns_ball_100 = [f'{subj}BlockBall100' for subj in subjects]
    columns_ball_standard = [f'{subj}BlockBall' for subj in subjects]
    columns_name = [f'{subj}Block' for subj in subjects]

    # Drop unnecessary columns
    data.drop(['outid','Test'],axis=1,inplace=True)
    data.drop([col for col in columns_name],axis=1,inplace=True)

    # Convert to int_16 and replace NaN with -1 for 100-200 scale
    def convert_int16_100(data):
        for column in columns_ball_100:
            data[column] = data[column].str.replace(',0', '').fillna(-1).astype(np.int16)

    # Convert to int_16 and replace NaN with -1 for standard scale
    def convert_int16_standard(data):
        for column in columns_ball_standard:
            data[column] = data[column].fillna(-1).astype(np.int16)

    # Cleaning
    convert_int16_100(data)
    convert_int16_standard(data)

    return data

# Geo data file
def geo_data(data):
    translit_map = {
        'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b',
        'В': 'V', 'в': 'v', 'Г': 'H', 'г': 'h',
        'Ґ': 'G', 'ґ': 'g', 'Д': 'D', 'д': 'd',
        'Е': 'E', 'е': 'e', 'Є': 'Ye', 'є': 'ie',
        'Ж': 'Zh', 'ж': 'zh', 'З': 'Z', 'з': 'z',
        'И': 'Y', 'и': 'y', 'І': 'I', 'і': 'i',
        'Ї': 'Yi', 'ї': 'i', 'Й': 'Y', 'й': 'i',
        'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l',
        'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n',
        'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p',
        'Р': 'R', 'р': 'r', 'С': 'S', 'с': 's',
        'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u',
        'Ф': 'F', 'ф': 'f', 'Х': 'Kh', 'х': 'kh',
        'Ц': 'Ts', 'ц': 'ts', 'Ч': 'Ch', 'ч': 'ch',
        'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Shch', 'щ': 'shch',
        'Ю': 'Yu', 'ю': 'iu', 'Я': 'Ya', 'я': 'ia',
        'Ь': '', 'ь': '', 'Ъ': '', 'ъ': '', "'": ""
    }

    # Transliterate area names
    def transliterate_ukrainian(name: str) -> str:
        original = name.strip()

        # Remove "район"
        if original.endswith("район"):
            base = original.replace("район", "").strip()
            translit = "".join(translit_map.get(ch, ch) for ch in base)
            return translit

        # Remove "м."
        if original.startswith("м."):
            base = original[2:].strip()
            translit = "".join(translit_map.get(ch, ch) for ch in base)
            return translit

        # Default: transliterate the whole string
        return "".join(translit_map.get(ch, ch) for ch in original)

    # Apply
    data['AreaName'] = data['AreaName'].apply(transliterate_ukrainian)

    return data

# Without absent file
def without_absent_data(data,subjects):
    mask = ~(data[[f'{subj}BlockStatus' for subj in subjects]] == 'Не з’явився(лася)').any(axis=1)
    data_without_absent = data[mask]

    return data_without_absent

# Save files
def save(data,filename):
    DATA_PATH = Path(__file__).parent.parent / 'data' / f'{YEAR}' / f'nmt{YEAR}_{filename}.csv'
    data.to_csv(DATA_PATH,index=False,encoding='utf-8-sig')

if __name__ == '__main__':
    # Load raw data
    data=load_data('raw_data',YEAR)

    # Subjects list (100-200 and standard scales)
    subjects = [col.replace('BlockBall100','') for col in data.columns if 'BlockBall100' in col]

    # Clean file
    data_cleaned = clean_data(data.copy(),subjects)

    # Cleaned file with transliterated area names (suitable for maps)
    data_geo = geo_data(data_cleaned.copy())

    # Cleaned file without failed participants
    data_without_not_passed = without_absent_data(data_cleaned.copy(),subjects)

    # Saving
    save(data_cleaned,'cleaned')
    save(data_geo,'geo')
    save(data_without_not_passed,'without_absent')