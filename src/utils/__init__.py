from pynamical import simulate, bifurcation_plot, save_fig, title_font, label_font
import pandas as pd, numpy as np, IPython.display as display, matplotlib.pyplot as plt, matplotlib.cm as cm

def logistic_map(pop, rate):
    return pop * rate * (1 - pop)

def simulateLogisticMap(rates, num_gens=20, initial_pop=0.5):
    pops = []
    #rates = np.array(rates)

    for rate in rates:
        pop = initial_pop

        for _ in range(num_gens):
            pops.append([rate, pop])
            pop = logistic_map(pop, rate)

    df = pd.DataFrame(data=pops, columns=["rate", "pop"])
    df.index = pd.MultiIndex.from_arrays([len(rates) * list(range(num_gens)), df['rate'].values])
    return df.drop(labels='rate', axis=1).unstack()['pop']


def get_colors(cMap, n, start=0., stop=1., alpha=1., reverse=False):
    colors = [cm.get_cmap(cMap)(x) for x in np.linspace(start, stop, n)]
    colors = [(r, g, b, alpha) for r, g, b, _ in colors]
    return list(reversed(colors)) if reverse else colors


def genPlot(pops, name,miny =0,maxy=1):

    #print(pops)

    color_list = get_colors('gist_rainbow', n=len(pops.columns), start=0., stop=1)


    for color, rate in reversed(list(zip(color_list, pops.columns))):
        #print(rate)
        ax = pops[rate].plot(kind='line', figsize=[10, 6], linewidth='2.5', alpha=0.95, c=color)
    #print("HELLO")
    ax.grid(True)
    ax.set_ylim([miny, maxy])
    ax.legend(title='Growth Rate', loc=3, bbox_to_anchor=(1, 0.525))
    ax.set_title('Logistic Model Results by Growth Rate', fontproperties=title_font)
    ax.set_xlabel('Generation', fontproperties=label_font)
    ax.set_ylabel('Population', fontproperties=label_font)

    save_fig(name)
    plt.clf()


