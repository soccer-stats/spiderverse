templates = {
    "Forwards": {
        "metrics": [
            {"label": "Dribbles\nNumber", "colname": "Succ", "color": "#2ec4b6"},
            {"label": "Penbox\nCarries", "colname": "CPA", "color": "#2ec4b6"},
            {"label": "Progressive\nPass", "colname": "Prog", "color": "#ff9f1c"},
            {"label": "Penbox\nPass", "colname": "PPA", "color": "#ff9f1c"},
            {"label": "Key Pass", "colname": "KP", "color": "#ff9f1c"},
            {"label": "Assist", "colname": "Ast", "color": "#ff9f1c"},
            {"label": "Goal", "colname": "Gls", "color": "#e71d36"},
            {"label": "Shot", "colname": "Sh", "color": "#e71d36"},
        ]
    },
    "Midfielders": {
        "metrics": [
            {"label": "Dribbles\nNumber", "colname": "Succ", "color": "#2ec4b6"},
            {"label": "Penbox\nCarries", "colname": "CPA", "color": "#2ec4b6"},
            {"label": "Progressive\nPass", "colname": "Prog", "color": "#ff9f1c"},
            {"label": "Penbox\nPass", "colname": "PPA", "color": "#ff9f1c"},
            {"label": "Key Pass", "colname": "KP", "color": "#ff9f1c"},
            {"label": "Assist", "colname": "Ast", "color": "#ff9f1c"},
            {"label": "Goal", "colname": "Gls", "color": "#e71d36"},
            {"label": "Shot", "colname": "Sh", "color": "#e71d36"},
        ]
    },
    "Defenders": {
        "metrics": [
            {"label": "Dribbles\nNumber", "colname": "Succ", "color": "#2ec4b6"},
            {"label": "Penbox\nCarries", "colname": "CPA", "color": "#2ec4b6"},
            {"label": "Progressive\nPass", "colname": "Prog", "color": "#ff9f1c"},
            {"label": "Penbox\nPass", "colname": "PPA", "color": "#ff9f1c"},
            {"label": "Key Pass", "colname": "KP", "color": "#ff9f1c"},
            {"label": "Assist", "colname": "Ast", "color": "#ff9f1c"},
            {"label": "Goal", "colname": "Gls", "color": "#e71d36"},
            {"label": "Shot", "colname": "Sh", "color": "#e71d36"},
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
