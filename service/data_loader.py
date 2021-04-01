import pandas as pd
from config import DATA_PATH
import os


def load_data():
    # TODO when we have more files we'd need to concatenate/merge them
    # For MVP it is fine having just one file
    path = os.path.join(DATA_PATH, "players_gca.csv")
    return pd.read_csv(path)
