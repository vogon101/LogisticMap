#import sys
#sys.path.append(__file__)
from utils import *

for i in range(0,5):
    rates = np.linspace(i, i+0.9, 10)
    for j in range(0,10):
        #print(rates)

        maxy = 1 if i != 5 else 10
        miny = 0 if i != 5 else -10

        pops = simulateLogisticMap(num_gens=50,rates=rates, initial_pop=j/10)
        pops.applymap(lambda x: '{:03.3f}'.format(x))

        #print(pops)

        print(str(i) + "-" + str(j))

        genPlot(pops, str(i) + "-" + str(j), miny, maxy)