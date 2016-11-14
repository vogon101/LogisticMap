import pandas as pd, numpy as np, matplotlib.pyplot as plt, matplotlib.cm as cm, matplotlib.font_manager as fm

# CODE FROM https://github.com/gboeing/pynamical to reduce dependancies
def save_fig(filename='image', folder='images', dpi=300, bbox_inches='tight', pad=0.1):
    plt.savefig('{}/{}.png'.format(folder, filename), dpi=dpi, bbox_inches=bbox_inches, pad_inches=pad)

_font_family = ['Helvetica', 'Arial', 'sans-serif']
title_font = fm.FontProperties(family=_font_family, style='normal', size=20, weight='normal', stretch='normal')
label_font = fm.FontProperties(family=_font_family, style='normal', size=16, weight='normal', stretch='normal')

def get_colors(cMap, n, start=0., stop=1., alpha=1., reverse=False):
    colors = [cm.get_cmap(cMap)(x) for x in np.linspace(start, stop, n)]
    colors = [(r, g, b, alpha) for r, g, b, _ in colors]
    return list(reversed(colors)) if reverse else colors