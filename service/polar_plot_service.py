import matplotlib.pyplot as plt
import pandas as pd
import math
from config import DATE_UPDATE


def draw_polar(df, player_name, template):
    csfont = {'fontname': 'DejaVu Sans'}

    p_features = ['Player', 'Succ', 'CPA', 'Prog', 'PPA', 'KP', 'Ast', 'Gls', 'Sh', '90s']
    p_absolute = df[p_features]

    p_percentiles1 = pd.DataFrame()
    p_percentiles1['Player'] = p_absolute['Player']
    p_percentiles1['Dribbles\nNumber'] = (p_absolute['Succ'] / p_absolute['90s'])
    p_percentiles1['Penbox\nCarries'] = (p_absolute['CPA'] / p_absolute['90s'])
    p_percentiles1['Progressive\nPass'] = (p_absolute['Prog'] / p_absolute['90s'])
    p_percentiles1['Penbox\nPass'] = (p_absolute['PPA'] / p_absolute['90s'])
    p_percentiles1['Key Pass'] = (p_absolute['KP'] / p_absolute['90s'])
    p_percentiles1['Assist'] = (p_absolute['Ast'] / p_absolute['90s'])
    p_percentiles1['Goal'] = (p_absolute['Gls'] / p_absolute['90s'])
    p_percentiles1['Shot'] = (p_absolute['Sh'] / p_absolute['90s'])
    p_percentiles1 = p_percentiles1.set_index("Player")

    p_percentiles = pd.DataFrame()
    p_percentiles['Player'] = p_absolute['Player']
    p_percentiles['Dribbles\nNumber'] = (p_absolute['Succ'] / p_absolute['90s']).rank(pct=True) * 100
    p_percentiles['Penbox\nCarries'] = (p_absolute['CPA'] / p_absolute['90s']).rank(pct=True) * 100
    p_percentiles['Progressive\nPass'] = (p_absolute['Prog'] / p_absolute['90s']).rank(pct=True) * 100
    p_percentiles['Penbox\nPass'] = (p_absolute['PPA'] / p_absolute['90s']).rank(pct=True) * 100
    p_percentiles['Key Pass'] = (p_absolute['KP'] / p_absolute['90s']).rank(pct=True) * 100
    p_percentiles['Assist'] = (p_absolute['Ast'] / p_absolute['90s']).rank(pct=True) * 100
    p_percentiles['Goal'] = (p_absolute['Gls'] / p_absolute['90s']).rank(pct=True) * 100
    p_percentiles['Shot'] = (p_absolute['Sh'] / p_absolute['90s']).rank(pct=True) * 100
    p_percentiles = p_percentiles.set_index('Player')

    theta = list(map((lambda x: x * math.pi / 8), list(range(1, 17, 2))))
    radii = list(p_percentiles.loc[player_name])
    width = [math.pi / 4] * len(radii)
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
    color = ['#2ec4b6', '#2ec4b6', '#ff9f1c', '#ff9f1c', '#ff9f1c', '#ff9f1c', '#e71d36', '#e71d36']
    ax.bar(theta, radii, width=width, color=color,
           alpha=0.6, edgecolor='#2e353c', linewidth=1.5)

    l = list(p_percentiles)

    fig.text(0.5, 0.97, player_name, ha='center', va='top', color='w', size=44, **csfont, fontweight="bold")
    fig.text(0.5, 0.9, "vs Europe's Top 5 Leagues {}, 2020/21".format(template.upper()),
             ha='center', va='top', color='w', size='24', **csfont)
    fig.text(0.5, 0.86, "created by 'Roaming Playmaker' and 'Футбол в цифрах'",
             ha='center', va='top', color='w', size='16', **csfont, alpha=0.8)
    fig.text(0.5, 0.02,
             'stats per 90, played > 270 mins, data Statsbomb via fbref.com, last update {}'.format(DATE_UPDATE),
             ha='center', color='#D7D7D7', style='italic', size='15', **csfont)

    text_size = '18'
    fontweight = "normal"
    fig.text(1.085, 0.77, l[0],
             horizontalalignment='center', verticalalignment='top', color='w',
             transform=ax.transAxes, size=text_size, **csfont, fontweight=fontweight)
    fig.text(0.72, 1.025, l[1],
             horizontalalignment='center', verticalalignment='center', color='w',
             transform=ax.transAxes, size=text_size, **csfont, fontweight=fontweight)
    fig.text(0.29, 1.03, l[2],
             horizontalalignment='center', verticalalignment='center', color='w',
             transform=ax.transAxes, size=text_size, **csfont, fontweight=fontweight)
    fig.text(-0.06, 0.75, l[3],
             horizontalalignment='center', verticalalignment='center', color='w',
             transform=ax.transAxes, size=text_size, **csfont, fontweight=fontweight)
    fig.text(-0.06, 0.31, l[4],
             horizontalalignment='center', verticalalignment='center', color='w',
             transform=ax.transAxes, size=text_size, **csfont, fontweight=fontweight)
    fig.text(0.28, -0.01, l[5],
             horizontalalignment='center', verticalalignment='center', color='w',
             transform=ax.transAxes, size=text_size, **csfont, fontweight=fontweight)
    fig.text(0.74, 0, l[6],
             horizontalalignment='center', verticalalignment='center', color='w',
             transform=ax.transAxes, size=text_size, **csfont, fontweight=fontweight)
    fig.text(1.055, 0.31, l[7],
             horizontalalignment='center', verticalalignment='center', color='w',
             transform=ax.transAxes, size=text_size, **csfont, fontweight=fontweight)

    for i in [0, 1, 2, 3, 4, 5, 6, 7]:
        plt.annotate(str(round(((list(p_percentiles1.loc[player_name]))[i]), 2)), (theta[i], radii[i]),
                     color='#000814',
                     horizontalalignment='center', size='16', **csfont, fontweight=fontweight, bbox=dict(boxstyle="round",
                                                                                                   fc=color[i]))

    fig.tight_layout(rect=[0, 0.07, 1, 0.78])
    return fig
