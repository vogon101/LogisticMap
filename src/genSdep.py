from utils import *

def gen(starts = np.linspace(0,1,11), folder="Sdep/", generations=50, min_r = 0, max_r = 5, rate_num = 51, hline_mode = LINE_NONE):

    print("Generating S-Dependant Graphs")

    rates = np.linspace(min_r, max_r, rate_num)
    print(rates)

    for r in rates:
        maxy = 1 if r <= 4 else 10
        miny = 0 if r <= 4 else -10

        pops = simulateLogisticMapSdep(num_gens=generations, rate=r, starts=starts)
        pops.applymap(lambda x: '{:03.3f}'.format(x))

        if hline_mode == LINE_RMO_OVER_R:
            hline = (r-1)/r
        else: hline = LINE_NONE

        #print(pops)

        print("Generated file "+folder+str(r*10))

        genPlotSdep(pops, folder+ str(r*10),r, miny, maxy, hline=hline)

if __name__ == "__main__":
    gen()