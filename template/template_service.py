templates = {
    "Forwards": {
        "metrics": [
            {"label": "Win ball\n(tackle+int)", "colname": "Tkl+Int", "color": "#2ec4b6", "rank_type": "percentile"},
            {"label": "Pass - xPass\ncompletion %", "colname": "diff_pass", "color": "#ff9f1c", "skip_p90": True, "add_sign": True, "rank_type": "percentile"},
            {"label": "Pass\ncompletion %", "colname": "Cmp%", "color": "#ff9f1c", "skip_p90": True, "rank_type": "percentile"},
            {
                "label": "Dribbles\nWon\nin duels",
                "colname": "Succ",
                "color": "#ff9f1c",
                "rank_type": "beta",
                "att_colname": "Att_pos"  # mandatory attribute for rank_type = 'beta'
            },
            {"label": "Penbox\nTouch", "colname": "Att Pen", "color": "#ff9f1c", "rank_type": "percentile"},
            {
                "label": "Aerial\nWon\nin duels",
                "colname": "Won",
                "color": "#e71d36",
                "rank_type": "beta",
                "att_colname": "Att_aer"  # mandatory attribute for rank_type = 'beta'
            },
            {"label": "xA", "colname": "xA", "color": "#e71d36", "rank_type": "percentile"},
            {"label": "npxG", "colname": "npxG", "color": "#e71d36", "rank_type": "percentile"},
            {"label": "Shot", "colname": "Sh", "color": "#e71d36", "rank_type": "percentile"},
            {"label": "Goal", "colname": "Gls", "color": "#e71d36", "rank_type": "percentile"}
        ]
    },
    "Midfielders": {
        "metrics": [
            {
                "label": "Tackles\nWon\nin duels",
                "colname": "TklW",
                "color": "#2ec4b6",
                "rank_type": "beta",
                "att_colname": "Att_def"  # mandatory attribute for rank_type = 'beta'
            },
            {"label": "Progressive\n(pass+carries)", "colname": "Prog+", "color": "#ff9f1c", "rank_type": "percentile"},
            {"label": "Pass - xPass\ncompletion %", "colname": "diff_pass", "color": "#ff9f1c", "skip_p90": True,
             "add_sign": True, "rank_type": "percentile"},
            {"label": "Pass\ncompletion %", "colname": "Cmp%", "color": "#ff9f1c", "skip_p90": True, "rank_type": "percentile"},
            {
                "label": "Dribbles\nWon\nin duels",
                "colname": "Succ",
                "color": "#ff9f1c",
                "rank_type": "beta",
                "att_colname": "Att_pos"  # mandatory attribute for rank_type = 'beta'
            },
            {"label": "xA", "colname": "xA", "color": "#e71d36", "rank_type": "percentile"},
            {"label": "npxG", "colname": "npxG", "color": "#e71d36", "rank_type": "percentile"},
            {"label": "Shot-Creating\nActions", "colname": "SCA", "color": "#e71d36", "rank_type": "percentile"},
            {"label": "Shot", "colname": "Sh", "color": "#e71d36", "rank_type": "percentile"},
            {"label": "Goal", "colname": "Gls", "color": "#e71d36", "rank_type": "percentile"}
        ]
    },
    "Defenders": {
        "metrics": [
            {
                "label": "Tackles\nWon\nin duels",
                "colname": "TklW",
                "color": "#2ec4b6",
                "rank_type": "beta",
                "att_colname": "Att_def"  # mandatory attribute for rank_type = 'beta'
            },
            {"label": "Interception", "colname": "Int", "color": "#2ec4b6", "rank_type": "percentile"},
            {"label": "Blocked\n(pass+shot)", "colname": "Blocks", "color": "#2ec4b6", "rank_type": "percentile"},
            {
                "label": "Aerial\nWon\nin duels",
                "colname": "Won",
                "color": "#2ec4b6",
                "rank_type": "beta",
                "att_colname": "Att_aer"  # mandatory attribute for rank_type = 'beta'
            },
            {"label": "Pass\nInto\nFinal third", "colname": "1/3_x", "color": "#ff9f1c", "rank_type": "percentile"},
            {"label": "Pass - xPass\ncompletion %", "colname": "diff_pass", "color": "#ff9f1c", "skip_p90": True,
             "add_sign": True, "rank_type": "percentile"},
            {"label": "Pass\ncompletion %", "colname": "Cmp%", "color": "#ff9f1c", "skip_p90": True, "rank_type": "percentile"},
            {"label": "Progressive\n(pass+carry)", "colname": "Prog+", "color": "#ff9f1c", "rank_type": "percentile"},
            {"label": "Shot-Creating\nActions", "colname": "SCA", "color": "#e71d36", "rank_type": "percentile"},
            {"label": "xA", "colname": "xA", "color": "#e71d36", "rank_type": "percentile"},
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
