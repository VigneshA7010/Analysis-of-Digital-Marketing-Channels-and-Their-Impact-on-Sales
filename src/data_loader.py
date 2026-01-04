import pandas as pd
from pathlib import Path

def load_data():
    data_path = Path("data/raw/Marketing.csv")
    df = pd.read_csv(data_path)
    print(df.head())
    print(df.info())
    return df
