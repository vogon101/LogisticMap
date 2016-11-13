from utils import *

starts = np.linspace(0,1,11)
for i in range(0,5):
    #print(rates)
    rates = np.linspace(i, i+0.9, 10)

    maxy = 1 if i != 5 else 10
    miny = 0 if i != 5 else -10

    for r in rates:
        print(r)
        pops = simulateLogisticMapSdep(num_gens=50, rate=r, starts=starts)
        pops.applymap(lambda x: '{:03.3f}'.format(x))

        #print(pops)

        print(str(r*10))

        genPlotSdep(pops, "Sdep/" + str(r*10),r, miny, maxy)