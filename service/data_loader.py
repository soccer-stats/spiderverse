import pandas as pd
from config import DATA_PATH
import os


def load_data(pos=None, min_matches=3):
    path = os.path.join(DATA_PATH, "data.csv")
    df = pd.read_csv(path)
    if pos is not None:
        df = df[df['Pos'].str.contains(pos)].copy()
    df = df[df['90s'] >= min_matches]
    df['Player'] = df['Player'].str.split('\\', expand=True)[0]
    return df
