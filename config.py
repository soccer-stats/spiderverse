import os

BASE_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_PATH, "data")
DATE_UPDATE = "2021-05-20"

template_to_position_mapping = {
    "Forwards": {"filter": "FW", "default_player": "Lionel Messi", "default_compare_player": "Cristiano Ronaldo"},
    "Midfielders": {"filter": "MF", "default_player": "Kevin De Bruyne", "default_compare_player": "Thomas Muller"},
    "Defenders": {"filter": "DF", "default_player": "Juan Cuadrado", "default_compare_player": "Jesus Navas"},
}

