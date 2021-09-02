import os

BASE_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_PATH, "data")
DATE_UPDATE = "2021-05-25"

template_to_position_mapping = {
    "Forwards": {"filter": "FW",
                 "default_player": "Romelu Lukaku",
                 "default_compare_player": "Karim Benzema"},
    "Midfielders": {"filter": "MF",
                    "default_player": "Paul Pogba",
                    "default_compare_player": "Rodri"},
    "Defenders": {"filter": "DF",
                  "default_player": "Trent Alexander-Arnold",
                  "default_compare_player": "Jordi Alba"},
}


season_to_min_num_matches = {
    "2020-2021": 10,
    "2021-2022": 1  # increase it during the season
}