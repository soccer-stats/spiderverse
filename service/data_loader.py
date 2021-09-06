import pandas as pd
from config import DATA_PATH
import os

season_to_file = {
    "2021-2022": "data21.csv",
    "2020-2021": "data20.csv",
    "2019-2020": "data19.csv",
    "2018-2019": "data18.csv",
    "2017-2018": "data17.csv",
}


def load_data(pos=None, min_matches=3, season="2020-2021"):
    path = os.path.join(DATA_PATH, season_to_file[season])
    df = pd.read_csv(path)
    if pos is not None:
        df = df.dropna(subset=["Pos"]).copy()
        df = df[df['Pos'].str.contains(pos)].copy()
    df = df[df['90s'] >= min_matches]
    df['Player'] = df['Player'].str.split('\\', expand=True)[0]
    df['Player'] = df['Player'] + " | " + df['Squad']
    df['season'] = season
    return df
