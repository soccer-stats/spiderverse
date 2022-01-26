import matplotlib.pyplot as plt
import pandas as pd
import math
from config import DATE_UPDATE
from config import season_to_min_num_matches
from template import template_service
from matplotlib.ticker import FixedFormatter
from matplotlib.ticker import FixedLocator
from fitter import Fitter
import matplotlib.patheffects as path_effects

season_to_label = {
    "2021-2022": "2021/22",
    "2020-2021": "2020/21",
    "2019-2020": "2019/20",
    "2018-2019": "2018/19",
    "2017-2018": "2017/18",
}


def draw_polar(df, player_name, template, season):
    csfont = {'fontname': 'DejaVu Sans'}

    p_absolute = df[['Player', '90s'] + template_service.get_columns(template)]

    metrics = template_service.get_metrics(template)

    values_df = pd.DataFrame()
    values_df['Player'] = p_absolute['Player']
    for metric in metrics:
        if "skip_p90" in metric and metric['skip_p90']:
            values_df[metric['label']] = p_absolute[metric['colname']]
        else:
            values_df[metric['label']] = (p_absolute[metric['colname']] / p_absolute['90s'])
    values_df = values_df.set_index("Player")

    ranked_df = pd.DataFrame()
    ranked_df['Player'] = p_absolute['Player']
    for metric in metrics:
        if metric["rank_type"] == "percentile":
            if "skip_p90" in metric and metric['skip_p90']:
                ranked_df[metric['label']] = (p_absolute[metric['colname']]).rank(pct=True) * 100
            else:
                ranked_df[metric['label']] = (p_absolute[metric['colname']] / p_absolute['90s']).rank(pct=True) * 100
        elif metric["rank_type"] == "beta":
            calculate_beta_rank(df, metric, ranked_df)
        else:
            raise Exception("Unsupported rank_type '{}'".format(metric["rank_type"]))
    ranked_df = ranked_df.set_index('Player')

    theta = list(map((lambda x: x * math.pi / len(metrics)), list(range(1, 2 * len(metrics) + 1, 2))))
    radii = list(ranked_df.loc[player_name])
    width = [math.pi / (len(metrics) / 2)] * len(radii)
    fig = plt.figure(figsize=(10, 10), facecolor='#000814')
    ax = fig.add_subplot(111, projection='polar')
    ax.set_facecolor('#000814')
    ax.grid(axis='y', color='#000814', alpha=0.1)
    ax.tick_params(axis='x', colors='xkcd:off white')
    ax.tick_params(axis='y', colors='xkcd:off white')
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.spines['polar'].set_color('#D7D7D7')
    ax.spines['polar'].set_linewidth(2)
    ax.set_rorigin(-30)
    ax.set_rlim(0, 100)
    colors = template_service.get_colors(template)
    ax.bar(theta, radii, width=width, color=colors, alpha=0.6, edgecolor='#2e353c', linewidth=1.5)
    tick_loc = list(map((lambda x: x * math.pi / len(metrics)), list(range(0, 2 * len(metrics), 2))))
    ax.xaxis.set_major_locator(FixedLocator(tick_loc))

    ax.tick_params(axis='x', which="minor", labelsize=16, colors='xkcd:off white', pad=40)
    ax.xaxis.set_minor_locator(FixedLocator(theta))
    labels = template_service.get_labels(template)
    ax.xaxis.set_minor_formatter(FixedFormatter(labels))

    fig.text(0.5, 0.97, player_name.split(" | ")[0], ha='center', va='top', color='w', size=44, **csfont, fontweight="bold")
    fig.text(0.5, 0.9, "vs Europe's Top 5 Leagues {}, {}".format(template.upper(), season_to_label[season]),
             ha='center', va='top', color='w', size='24', **csfont)
    fig.text(0.5, 0.86, "created by 'Roaming Playmaker' and 'Футбол в цифрах'",
             ha='center', va='top', color='w', size='16', **csfont, alpha=0.8)
    fig.text(0.5, 0.02,
             'stats per 90, played > {} mins, data Statsbomb via fbref.com, last update {}'.format(
                 season_to_min_num_matches[season] * 90, DATE_UPDATE),
             ha='center', color='#D7D7D7', style='italic', size='15', **csfont)

    for i in range(0, len(metrics)):
        plt.annotate(str(round(((list(values_df.loc[player_name]))[i]), 2)), (theta[i], radii[i]),
                     color='#000814', ha='center', size='16', **csfont,
                     fontweight="normal", bbox=dict(boxstyle="round", fc=colors[i]))

    fig.tight_layout(rect=[0, 0.07, 1, 0.83])
    return fig


def draw_polar2(df, player_name1, player_name2, template, season1, season2):
    csfont = {'fontname': 'DejaVu Sans'}

    p_absolute = df[['Player', '90s', 'season'] + template_service.get_columns(template)]
    metrics = template_service.get_metrics(template)

    values_df = pd.DataFrame()
    values_df['Player'] = p_absolute['Player']
    values_df['season'] = p_absolute['season']
    for metric in metrics:
        if "skip_p90" in metric and metric['skip_p90']:
            values_df[metric['label']] = p_absolute[metric['colname']]
        else:
            values_df[metric['label']] = (p_absolute[metric['colname']] / p_absolute['90s'])
    values_df = values_df.set_index(["Player", "season"])

    ranked_df = pd.DataFrame()
    ranked_df['Player'] = p_absolute['Player']
    ranked_df['season'] = p_absolute['season']
    for metric in metrics:
        if metric["rank_type"] == "percentile":
            if "skip_p90" in metric and metric['skip_p90']:
                ranked_df[metric['label']] = (p_absolute[metric['colname']]).rank(pct=True) * 100
            else:
                ranked_df[metric['label']] = (p_absolute[metric['colname']] / p_absolute['90s']).rank(pct=True) * 100
        elif metric["rank_type"] == "beta":
            calculate_beta_rank(df, metric, ranked_df)
        else:
            raise Exception("Unsupported rank_type '{}'".format(metric["rank_type"]))
    ranked_df = ranked_df.set_index(["Player", "season"])

    theta = list(map((lambda x: x * math.pi / len(metrics)), list(range(1, 2 * len(metrics) + 1, 2))))
    radii1 = ranked_df.loc[player_name1, season1].values.tolist()
    radii2 = ranked_df.loc[player_name2, season2].values.tolist()
    width = [math.pi / (len(metrics) / 2)] * len(radii1)
    width2 = [math.pi / (len(metrics) / 2)] * len(radii2)
    fig = plt.figure(figsize=(10, 11), facecolor='#000814')
    ax = fig.add_subplot(111, projection='polar')
    ax.set_facecolor('#000814')
    ax.grid(axis='y', color='#000814', alpha=0)
    ax.tick_params(axis='x', colors='xkcd:off white')
    ax.tick_params(axis='y', colors='xkcd:off white')
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.spines['polar'].set_color('#D7D7D7')
    ax.spines['polar'].set_linewidth(2)
    ax.set_rorigin(-30)
    ax.set_rlim(0, 100)
    colors = template_service.get_colors(template)
    ax.bar(theta, radii1, width=width, color=colors, alpha=0.8, linewidth=1)
    ax.bar(theta, radii2, width=width2, color='#000814', alpha=0.4, edgecolor=colors, linewidth=1, hatch='xxx')
    tick_loc = list(map((lambda x: x * math.pi / len(metrics)), list(range(0, 2 * len(metrics), 2))))
    ax.xaxis.set_major_locator(FixedLocator(tick_loc))

    ax.tick_params(axis='x', which="minor", labelsize=16, colors='xkcd:off white', pad=42)
    ax.xaxis.set_minor_locator(FixedLocator(theta))
    labels = template_service.get_labels(template)
    ax.xaxis.set_minor_formatter(FixedFormatter(labels))

    fontsize = 28
    title1 = build_title_from_player_name_and_season(player_name1, season1)
    title2 = build_title_from_player_name_and_season(player_name2, season2)
    fig.text(0.25, 0.96, title1,
             ha='center', va='top', color='w', size=fontsize, **csfont, fontweight="bold",
             bbox=dict(boxstyle="round", alpha=0.8, fc='#000814', mutation_aspect=0.5,
                       edgecolor='#ff9f1c', linewidth=2))
    s = fig.text(0.75, 0.96, title2, ha='center', va='top', color='w',
                 size=fontsize, **csfont, fontweight="bold",
                 bbox=dict(boxstyle="round", alpha=0.8, fc='#000814', hatch='xxx', edgecolor='#ff9f1c',
                           linewidth=2, mutation_aspect=0.5))
    #    s.set_path_effects([path_effects.PathPatchEffect(hatch='xx', edgecolor='#000814', facecolor='w')])
    fig.text(0.5, 0.86, "vs Europe's Top 5 Leagues {}, {}".format(template.upper(), calculate_period(season1, season2)),
             ha='center', va='top', color='w', size='24', **csfont)
    fig.text(0.5, 0.82, "created by 'Roaming Playmaker' and 'Футбол в цифрах'",
             ha='center', va='top', color='w', size='16', **csfont, alpha=0.8)
    fig.text(0.5, 0.02,
             'stats per 90, enough minutes played, data Statsbomb via fbref.com, last update {}'.format(DATE_UPDATE),
             ha='center', color='#D7D7D7', style='italic', size='15', **csfont)
    values1 = values_df.loc[player_name1, season1].values.tolist()
    values2 = values_df.loc[player_name2, season2].values.tolist()
    for i in range(0, len(metrics)):
        text = str(round(values1[i], 2))
        text2 = str(round(values2[i], 2))
        if radii1[i] > radii2[i]:
            if i < len(metrics) / 2:
                va1 = 'bottom'
                va2 = 'top'
            else:
                va1 = 'top'
                va2 = 'bottom'
        else:
            if i < len(metrics) / 2:
                va2 = 'bottom'
                va1 = 'top'
            else:
                va2 = 'top'
                va1 = 'bottom'
        a = ax.text(theta[i], radii1[i], text, color='w', ha="right", va=va1, size='16', **csfont,
                    fontweight="bold", bbox=dict(boxstyle="round", fc='#000814', mutation_aspect=0.5,alpha=0.8,
                                                 edgecolor=colors[i],linewidth=2))
        b = ax.text(theta[i], radii2[i], text2, color='w', ha="left", va=va2, size='16', **csfont,
                    fontweight="bold", bbox=dict(boxstyle="round", fc='#000814', hatch='xxxx',alpha=0.8,
                                                 mutation_aspect=0.5,edgecolor=colors[i],linewidth=2))
        a.set_path_effects([path_effects.withStroke(linewidth=1, foreground="black")])
        b.set_path_effects([path_effects.withStroke(linewidth=1, foreground="black")])

    fig.tight_layout(rect=[0, 0.08, 1, 0.77])
    return fig


def calculate_beta_rank(df, metric, ranked_df):
    # m - the number of attempts made by the 80th percentile player
    # IMDb uses constant "minimum votes required to be listed in the Top 250 (currently 25,000)"
    # we cannot use a constant as it varies from metric to metric
    m = df[metric['att_colname']].quantile(0.80)
    C = df[metric['colname']].mean()
    v = df[metric['att_colname']]
    R = df[metric['colname']]
    df[metric['colname'] + '_bayes_rank'] = (R * v + C * m) / (v + m)
    ranked_df[metric['label']] = (df[metric['colname'] + '_bayes_rank']).rank(pct=True) * 100


def build_title_from_player_name_and_season(player_name_with_squad, season):
    player_name = player_name_with_squad.split(" | ")[0]
    return player_name.split(' ')[0][0] + '. ' + player_name.split(' ')[-1] + "\n" + season


def calculate_period(season1, season2):
    season1_from = int(season1.split("-")[0])
    season1_to = int(season1.split("-")[1])
    season2_from = int(season2.split("-")[0])
    season2_to = int(season2.split("-")[1])
    return "{}-{}".format(min(season1_from, season2_from), max(season1_to, season2_to))
