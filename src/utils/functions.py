from pynamical_functions import *
from constants import *

def logistic_map(pop, rate):
    return pop * rate * (1 - pop)

def simulateLogisticMapRdep(rates, num_gens=20, initial_pop=0.5):
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

def simulateLogisticMapSdep(starts, rate, num_gens = 20):

    pops = []

    for start in starts:
        pop = start

        for _ in range(num_gens):
            pops.append([start,pop])
            pop = logistic_map(pop, rate)

    #print(pops)

    df = pd.DataFrame(data=pops, columns=["start", "pop"])
    df.index = pd.MultiIndex.from_arrays([len(starts) * list(range(num_gens)), df['start'].values])

    #print(df)

    return df.drop(labels='start', axis=1).unstack()['pop']

def genPlotRdep(pops, name, start, miny =0, maxy=1):

    #print(pops)

    color_list = get_colors('gist_rainbow', n=len(pops.columns), start=0., stop=1)


    max_rate =0
    min_rate =1000

    for color, rate in reversed(list(zip(color_list, pops.columns))):
        #print(rate)
        if rate>max_rate:
            max_rate = rate
        if rate<min_rate:
            min_rate = rate
        ax = pops[rate].plot(kind='line', figsize=[10, 6], linewidth='2.5', alpha=0.95, c=color)

    max_rate = str(max_rate)
    min_rate = str(min_rate)
    #print("HELLO")
    ax.grid(True)
    ax.set_ylim([miny, maxy])
    ax.legend(title='Growth Rate', loc=3, bbox_to_anchor=(1, 0.0))
    ax.set_title('Logistic Model Results by Growth Rate Between ' + min_rate + ' and ' + max_rate + '\nStarting Population: ' + str(start), fontproperties=title_font)
    ax.set_xlabel('Generation', fontproperties=label_font)
    ax.set_ylabel('Population', fontproperties=label_font)

    save_fig(name)

    plt.clf()

def genPlotSdep(pops, name, rate, miny =0, maxy=1, hline = -1):

    #print(pops)

    color_list = get_colors('gist_rainbow', n=len(pops.columns), start=0., stop=1)


    for color, s_val in reversed(list(zip(color_list, pops.columns))):
        #print(rate)
        ax = pops[s_val].plot(kind='line', figsize=[10, 6], linewidth='2.5', alpha=0.95, c=color)
    #print("HELLO")
    ax.grid(True)
    ax.set_ylim([miny, maxy])
    ax.legend(title='Starting Population', loc=3, bbox_to_anchor=(1, 0.0))
    ax.set_title('Logistic Model Results by Starting Value - Rate: ' + str(rate), fontproperties=title_font)
    ax.set_xlabel('Generation', fontproperties=label_font)
    ax.set_ylabel('Population', fontproperties=label_font)

    if hline != LINE_NONE:
        print(hline)
        plt.hlines(hline, 0,1000)

    save_fig(name)

    plt.clf()
