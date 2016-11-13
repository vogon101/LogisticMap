import genSdep,genRdep
from utils import *

starts = np.linspace(0,1,11)
print(starts)

#genSdep.gen(starts, folder="Custom/post4/",generations=200, min_r=4, max_r=5,rate_num=11)
genRdep.gen("Custom/post4/", get_rates=lambda i:np.linspace(4.1, 5, 10), rate_gen_max=1, num_gens=50)