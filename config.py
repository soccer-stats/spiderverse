import os

BASE_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_PATH, "data")
DATE_UPDATE = "2021-04-24"

template_to_position_mapping = {
    "Forwards": {"filter": "FW", "default_player": "Lionel Messi"},
    "Midfielders": {"filter": "MF", "default_player": "Kevin De Bruyne"},
    "Defenders": {"filter": "DF", "default_player": "Juan Cuadrado"},
}

