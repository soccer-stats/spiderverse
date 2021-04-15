templates = {
    "Forwards": {
        "metrics": [
            {"label": "Win ball\n(tackle+int)", "colname": "Tkl+Int", "color": "#2ec4b6"},
            {"label": "Penbox\nCarries", "colname": "CarriesPenbox", "color": "#ff9f1c"},
            {"label": "Dribbles\nSucc", "colname": "Succ", "color": "#ff9f1c"},
            {"label": "Penbox\nTouch", "colname": "AttPen", "color": "#ff9f1c"},
            {"label": "Aerial\nWon", "colname": "AerialWon", "color": "#e71d36"},
            {"label": "xA", "colname": "xA", "color": "#e71d36"},
            {"label": "npxG", "colname": "npxG", "color": "#e71d36"},
            {"label": "Shot-Creating\nActions", "colname": "SCA", "color": "#e71d36"},
            {"label": "Shot", "colname": "Sh", "color": "#e71d36"},
            {"label": "Goal", "colname": "Gls", "color": "#e71d36"}
        ]
    },
    "Midfielders": {
        "metrics": [
            {"label": "Win ball\n(tackle+int)", "colname": "Tkl+Int", "color": "#2ec4b6"},
            {"label": "Progressive\n(pass+carries)", "colname": "Prog", "color": "#ff9f1c"},
            {"label": "Pass\ncompetiton %", "colname": "Cmp%", "color": "#ff9f1c", "skip_p90": True},
            {"label": "Penbox\nPass", "colname": "PassPenbox", "color": "#ff9f1c"},
            {"label": "Dribbles\nSucc", "colname": "Succ", "color": "#ff9f1c"},
            {"label": "xA", "colname": "xA", "color": "#e71d36"},
            {"label": "npxG", "colname": "npxG", "color": "#e71d36"},
            {"label": "Shot-Creating\nActions", "colname": "SCA", "color": "#e71d36"},
            {"label": "Shot", "colname": "Sh", "color": "#e71d36"},
            {"label": "Goal", "colname": "Gls", "color": "#e71d36"}
        ]
    },
    "Defenders": {
        "metrics": [
            {"label": "Tackles\nWon", "colname": "TklW", "color": "#2ec4b6"},
            {"label": "Interception", "colname": "Int", "color": "#2ec4b6"},
            {"label": "Blocked\n(pass+shot)", "colname": "Blocked", "color": "#2ec4b6"},
            {"label": "Aerial\nWon", "colname": "AerialWon", "color": "#2ec4b6"},
            {"label": "Pass\nInto\nFinal third", "colname": "PassFinThird", "color": "#ff9f1c"},
            {"label": "Pass\ncompetiton%", "colname": "Cmp%", "color": "#ff9f1c", "skip_p90": True},
            {"label": "Progressive\n(pass+carry)", "colname": "Prog", "color": "#ff9f1c"},
            {"label": "Shot-Creating\nActions", "colname": "SCA", "color": "#e71d36"},
            {"label": "xA", "colname": "xA", "color": "#e71d36"},
            {"label": "Shot", "colname": "Sh", "color": "#e71d36"}
        ]
    }
}


def get_metrics(template):
    if template in templates:
        return templates[template]["metrics"]
    else:
        raise Exception("template with name {} not supported".format(template))


def get_columns(template):
    return get_list_of(template, "colname")


def get_labels(template):
    return get_list_of(template, "label")


def get_colors(template):
    return get_list_of(template, "color")


def get_list_of(template, param_name):
    if template in templates:
        res = []
        for metric in templates[template]["metrics"]:
            res.append(metric[param_name])
        return res
    else:
        raise Exception("template with name {} not supported".format(template))
