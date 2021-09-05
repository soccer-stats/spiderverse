import os

BASE_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_PATH, "data")
DATE_UPDATE = "2021-05-25"

template_to_position_mapping = {
    "2021-2022": {
        "Forwards": {
            "filter": "FW",
            "default_player": "Romelu Lukaku | Chelsea",
            "default_compare_player": "Karim Benzema | Real Madrid"
        },
        "Midfielders": {
            "filter": "MF",
            "default_player": "Paul Pogba | Manchester Utd",
            "default_compare_player": "Rodri | Manchester City"
        },
        "Defenders": {
            "filter": "DF",
            "default_player": "Trent Alexander-Arnold | Liverpool",
            "default_compare_player": "Jordi Alba | Barcelona"
        },
    },
    "2020-2021": {
        "Forwards": {
            "filter": "FW",
            "default_player": "Lionel Messi | Barcelona",
            "default_compare_player": "Karim Benzema | Real Madrid"
        },
        "Midfielders": {
            "filter": "MF",
            "default_player": "Paul Pogba | Manchester Utd",
            "default_compare_player": "Kevin De Bruyne | Manchester City"
        },
        "Defenders": {
            "filter": "DF",
            "default_player": "Trent Alexander-Arnold | Liverpool",
            "default_compare_player": "Jordi Alba | Barcelona"
        },
    }
}


season_to_min_num_matches = {
    "2020-2021": 10,
    "2021-2022": 1  # increase it during the season
}