#import scf
#import numpy as np

#def benchmark():
#    print("hehe bench")

#am.hello()
#scf.initialize()


import azzinimunda.azzinimunda0 as am
import scf.initialization as init
import numpy as np
import time

n = 11
np.random.seed(123)
om = init.create_random_om(n, 10)
algorithm = am.AzziniMunda0(om)
print("Executing...")
start_time = time.time()
sol = algorithm.execute()
print("Execution time for n = {} -> {}s".format(n, time.time() - start_time))
print(sol)
