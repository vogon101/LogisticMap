from utils import *

for i in range(0,5):
    rates = np.linspace(i, i+0.9, 10)
    for j in range(0,11):
        #print(rates)

        maxy = 1 if i != 5 else 10
        miny = 0 if i != 5 else -10

        pops = simulateLogisticMapRdep(num_gens=50, rates=rates, initial_pop=j / 10)
        pops.applymap(lambda x: '{:03.3f}'.format(x))

        #print(pops)

        print(str(i) + "-" + str(j))

        genPlotRdep(pops, "Rdep/" + str(i) + "-" + str(j), j/10, miny, maxy)