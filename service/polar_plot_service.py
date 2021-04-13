import matplotlib.pyplot as plt
import pandas as pd
import math


def draw_polar(df, player_name, template):
    csfont = {'fontname': 'Century Gothic'}

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

    ax.set_title(player_name + '\n\n', color='w', size=35, **csfont, fontweight="bold")
    fig.text(0.5, 1.1, "Attacking phase Ranks vs Europe's Top 5 Leagues (per90), 2020/21",
             horizontalalignment='center', verticalalignment='top', color='w', size='18',
             transform=ax.transAxes, **csfont, fontweight="bold")
    fig.text(1.1, -0.075, 'Players who have played > 300 min',
             horizontalalignment='right', verticalalignment='top', color='#D7D7D7',
             style='italic', transform=ax.transAxes, size='15', **csfont, fontweight="bold")
    fig.text(0.292, -0.075, 'Data: Statsbomb via fbref.com',
             horizontalalignment='right', verticalalignment='top', color='#D7D7D7',
             style='italic', transform=ax.transAxes, size='15', **csfont, fontweight="bold")
    fig.text(1.055, 0.71, l[0],
             horizontalalignment='center', verticalalignment='top', color='w',
             transform=ax.transAxes, size='15', **csfont, fontweight="bold")
    fig.text(0.73, 1.01, l[1],
             horizontalalignment='center', verticalalignment='center', color='w',
             transform=ax.transAxes, size='15', **csfont, fontweight="bold")
    fig.text(0.29, 1.01, l[2],
             horizontalalignment='center', verticalalignment='center', color='w',
             transform=ax.transAxes, size='15', **csfont, fontweight="bold")
    fig.text(-0.04, 0.68, l[3],
             horizontalalignment='center', verticalalignment='center', color='w',
             transform=ax.transAxes, size='15', **csfont, fontweight="bold")
    fig.text(-0.05, 0.32, l[4],
             horizontalalignment='center', verticalalignment='center', color='w',
             transform=ax.transAxes, size='15', **csfont, fontweight="bold")
    fig.text(0.29, 0, l[5],
             horizontalalignment='center', verticalalignment='center', color='w',
             transform=ax.transAxes, size='15', **csfont, fontweight="bold")
    fig.text(.73, 0.01, l[6],
             horizontalalignment='center', verticalalignment='center', color='w',
             transform=ax.transAxes, size='15', **csfont, fontweight="bold")
    fig.text(1.03, 0.32, l[7],
             horizontalalignment='center', verticalalignment='center', color='w',
             transform=ax.transAxes, size='15', **csfont, fontweight="bold")

    for i in [0, 1, 2, 3, 4, 5, 6, 7]:
        plt.annotate(str(round(((list(p_percentiles1.loc[player_name]))[i]), 2)), (theta[i], radii[i]),
                     color='#000814',
                     horizontalalignment='center', size='16', **csfont, fontweight="bold", bbox=dict(boxstyle="round",
                                                                                                     fc=color[i]))

    fig.tight_layout()
    return fig
