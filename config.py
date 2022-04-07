import os
BASE_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_PATH, "data")
DATE_UPDATE = "2022-04-07"

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
            "default_compare_player": "Renato Sanches | Lille"
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
            "default_compare_player": "Erling Haaland | Dortmund"
        },
        "Midfielders": {
            "filter": "MF",
            "default_player": "Ruslan Malinovskyi | Atalanta",
            "default_compare_player": "Jack Grealish | Aston Villa"
        },
        "Defenders": {
            "filter": "DF",
            "default_player": "Andrew Robertson | Liverpool",
            "default_compare_player": "Theo Hernandez | Milan"
        },
    },
    "2019-2020": {
        "Forwards": {
            "filter": "FW",
            "default_player": "Robert Lewandowski | Bayern Munich",
            "default_compare_player": "Cristiano Ronaldo | Juventus"
        },
        "Midfielders": {
            "filter": "MF",
            "default_player": "Toni Kroos | Real Madrid",
            "default_compare_player": "Luis Alberto | Lazio"
        },
        "Defenders": {
            "filter": "DF",
            "default_player": "Lucas Digne | Everton",
            "default_compare_player": "Jesus Navas | Sevilla"
        },
    },
    "2018-2019": {
        "Forwards": {
            "filter": "FW",
            "default_player": "Paco Alcacer | Dortmund",
            "default_compare_player": "Kylian Mbappe | Paris S-G"
        },
        "Midfielders": {
            "filter": "MF",
            "default_player": "Denis Cheryshev | Valencia",
            "default_compare_player": "Angel Di Maria | Paris S-G"
        },
        "Defenders": {
            "filter": "DF",
            "default_player": "Trent Alexander-Arnold | Liverpool",
            "default_compare_player": "Jordi Alba | Barcelona"
        },
    },
    "2017-2018": {
        "Forwards": {
            "filter": "FW",
            "default_player": "Edinson Cavani | Paris S-G",
            "default_compare_player": "Mohamed Salah | Liverpool"
        },
        "Midfielders": {
            "filter": "MF",
            "default_player": "Dimitri Payet | Marseille",
            "default_compare_player": "Cesc Fabregas | Chelsea"
        },
        "Defenders": {
            "filter": "DF",
            "default_player": "Aleksandar Kolarov | Roma",
            "default_compare_player": "Leo Dubois | Nantes"
        },
    }
}


season_to_min_num_matches = {
    "2017-2018": 5,
    "2018-2019": 5,
    "2019-2020": 5,
    "2020-2021": 5,
    "2021-2022": 3  # increase it during the season
}
