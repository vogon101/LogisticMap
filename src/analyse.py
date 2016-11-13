def logistic(pop, r): return r * pop * (1- pop)

did_stab = []

def analyse(pop_i,r):
    global did_stab

    pop = pop_i
    seq = []
    did_stabilize = False

    for i in range(0, 10000):
        if pop in seq:
            did_stabilize = True
            #print("Logistic map with r=" + str(r) + " and x0="+str(pop_i) + " stabilized at "+ str(pop) + " after gen "+ str(i))
            did_stab.append(r)
            break
        seq.append(pop)
        pop = logistic(pop, r)

    if not did_stabilize:
        print("Logistic map with r=" + str(r) + " and x0="+str(pop_i) + " did not stabilize")


for i in range(399, 411):
    analyse(0.5, i/100)

for i in did_stab:
    print(str(i))