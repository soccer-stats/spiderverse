import matplotlib.pyplot as plt
import pandas as pd
import math
from config import DATE_UPDATE
from template import template_service
from matplotlib.ticker import FixedFormatter
from matplotlib.ticker import FixedLocator
import matplotlib.patheffects as path_effects
from adjustText import adjust_text

def draw_polar(df, player_name, template):
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

    percentiles_df = pd.DataFrame()
    percentiles_df['Player'] = p_absolute['Player']
    for metric in metrics:
        if "skip_p90" in metric and metric['skip_p90']:
            percentiles_df[metric['label']] = (p_absolute[metric['colname']]).rank(pct=True) * 100
        else:
            percentiles_df[metric['label']] = (p_absolute[metric['colname']] / p_absolute['90s']).rank(pct=True) * 100
    percentiles_df = percentiles_df.set_index('Player')

    theta = list(map((lambda x: x * math.pi / len(metrics)), list(range(1, 2 * len(metrics) + 1, 2))))
    radii = list(percentiles_df.loc[player_name])
    width = [math.pi / (len(metrics) / 2)] * len(radii)
    fig = plt.figure(figsize=(10, 10), facecolor='#000814')
    ax = fig.add_subplot(111, projection='polar')
    ax.set_facecolor('#000814')
    ax.grid(axis='y', color='#E8F3FF')
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

    fig.text(0.5, 0.97, player_name, ha='center', va='top', color='w', size=44, **csfont, fontweight="bold")
    fig.text(0.5, 0.9, "vs Europe's Top 5 Leagues {}, 2020/21".format(template.upper()),
             ha='center', va='top', color='w', size='24', **csfont)
    fig.text(0.5, 0.86, "created by 'Roaming Playmaker' and 'Футбол в цифрах'",
             ha='center', va='top', color='w', size='16', **csfont, alpha=0.8)
    fig.text(0.5, 0.02,
             'stats per 90, played > 270 mins, data Statsbomb via fbref.com, last update {}'.format(DATE_UPDATE),
             ha='center', color='#D7D7D7', style='italic', size='15', **csfont)

    for i in range(0, len(metrics)):
        plt.annotate(str(round(((list(values_df.loc[player_name]))[i]), 2)), (theta[i], radii[i]),
                     color='#000814', ha='center', size='16', **csfont,
                     fontweight="normal", bbox=dict(boxstyle="round", fc=colors[i]))

    fig.tight_layout(rect=[0, 0.07, 1, 0.83])
    return fig

def draw_polar2(df, player_name, player_name2, template):
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

    percentiles_df = pd.DataFrame()
    percentiles_df['Player'] = p_absolute['Player']
    for metric in metrics:
        if "skip_p90" in metric and metric['skip_p90']:
            percentiles_df[metric['label']] = (p_absolute[metric['colname']]).rank(pct=True) * 100
        else:
            percentiles_df[metric['label']] = (p_absolute[metric['colname']] / p_absolute['90s']).rank(pct=True) * 100
    percentiles_df = percentiles_df.set_index('Player')

    theta = list(map((lambda x: x * math.pi / len(metrics)), list(range(1, 2 * len(metrics) + 1, 2))))
    radii = list(percentiles_df.loc[player_name])
    radii2 = list(percentiles_df.loc[player_name2])
    width = [math.pi / (len(metrics) / 2)] * len(radii)
    width2 = [math.pi / (len(metrics) / 2)] * len(radii2)
    fig = plt.figure(figsize=(10, 10), facecolor='#000814')
    ax = fig.add_subplot(111, projection='polar')
    ax.set_facecolor('#000814')
    ax.grid(axis='y', color='#E8F3FF')
    ax.tick_params(axis='x', colors='xkcd:off white')
    ax.tick_params(axis='y', colors='xkcd:off white')
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.spines['polar'].set_color('#D7D7D7')
    ax.spines['polar'].set_linewidth(2)
    ax.set_rorigin(-30)
    ax.set_rlim(0, 100)
    colors = template_service.get_colors(template)
    ax.bar(theta, radii, width=width, color=colors, alpha=0.8, linewidth=4)
    ax.bar(theta,radii2,width=width2,color='#000814',alpha=0.4,edgecolor=colors,linewidth=4,hatch='xxx')
    tick_loc = list(map((lambda x: x * math.pi / len(metrics)), list(range(0, 2 * len(metrics), 2))))
    ax.xaxis.set_major_locator(FixedLocator(tick_loc))

    ax.tick_params(axis='x', which="minor", labelsize=16, colors='xkcd:off white', pad=40)
    ax.xaxis.set_minor_locator(FixedLocator(theta))
    labels = template_service.get_labels(template)
    ax.xaxis.set_minor_formatter(FixedFormatter(labels))

    fig.text(0.45, 0.97, player_name, ha='left', va='top', color='w', size=44, **csfont, fontweight="bold")
    fig.text(0.5, 0.97, s='vs', ha='center', va='top', fontweight='bold', **csfont, color='w', size=44)
    s=fig.text(0.55,0.97,player_name2,ha='right',va='top',color='w',size=44,**csfont,fontweight="bold")
    s.set_path_effects([path_effects.PathPatchEffect(hatch='xx',edgecolor='#000814',facecolor='w')])
    fig.text(0.5, 0.9, "vs Europe's Top 5 Leagues {}, 2020/21".format(template.upper()),
             ha='center', va='top', color='w', size='24', **csfont)
    fig.text(0.5, 0.86, "created by 'Roaming Playmaker' and 'Футбол в цифрах'",
             ha='center', va='top', color='w', size='16', **csfont, alpha=0.8)
    fig.text(0.5, 0.02,
             'stats per 90, played > 270 mins, data Statsbomb via fbref.com, last update {}'.format(DATE_UPDATE),
             ha='center', color='#D7D7D7', style='italic', size='15', **csfont)
    texts = []
    for i in range(0, len(metrics)):
        text =(str(round(((list(values_df.loc[player_name]))[i]), 2)))
        a = ax.text(theta[i],radii[i],text,color='w', ha='center', size='16', **csfont,
                    fontweight="bold", bbox=dict(boxstyle="round", fc=colors[i],mutation_aspect=0.2))
        text2 = (str(round(((list(values_df.loc[player_name2]))[i]),2)))
        b = ax.text(theta[i],radii2[i],text2,color='w', ha='center', size='16', **csfont,
                    fontweight="bold", bbox=dict(boxstyle="round", fc=colors[i],hatch='xxx',
                                                 color='#000814',mutation_aspect=0.2))
        a.set_path_effects([path_effects.withStroke(linewidth=1,foreground="black")])
        b.set_path_effects([path_effects.withStroke(linewidth=1,foreground="black")])
        texts.append(a)
        texts.append(b)
    adjust_text(texts)

    fig.tight_layout(rect=[0, 0.07, 1, 0.83])
    return fig
