from utils import *

def gen (folder = "Rdep/", get_rates=lambda i: np.linspace(i, i+0.9, 10), rate_gen_min = 0, rate_gen_max = 5, num_gens=50):

    print("Generating R-Dependant Graphs")

    for i in range(rate_gen_min,rate_gen_max):
        rates = get_rates(i)
        for j in range(0,11):
            #print(rates)

            maxy = 1 if max(rates) <= 4 else 10
            miny = 0 if max(rates) <= 4 else -10

            pops = simulateLogisticMapRdep(num_gens=num_gens, rates=rates, initial_pop=j / 10)
            pops.applymap(lambda x: '{:03.3f}'.format(x))

            #print(pops)

            print("Generated "+ folder + str(i) + "-" + str(j))

            genPlotRdep(pops, folder + str(i) + "-" + str(j), j/10, miny, maxy)


if __name__ == "__main__":
    gen()