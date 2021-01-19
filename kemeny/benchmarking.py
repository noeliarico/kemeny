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



n = 9
np.random.seed(123)
om = init.create_random_om(n, 10)
algorithm = am.AzziniMunda0(om)
print("Executing...")
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
print("Execution time for n = {} -> {}s".format(n, time.time() - start_time))

n = 9
np.random.seed(123)
om = init.create_random_om(n, 10)
algorithm = am.AzziniMunda0(om)
print("Executing...")
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
print("Execution time for n = {} -> {}s".format(n, time.time() - start_time))

n = 9
np.random.seed(123)
om = init.create_random_om(n, 10)
algorithm = am.AzziniMunda0(om)
print("Executing...")
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
print("Execution time for n = {} -> {}s".format(n, time.time() - start_time))
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
print("Execution time for n = {} -> {}s".format(n, time.time() - start_time))

#f = open("results.txt", "a")
#f.write(str(sol))
#f.close()

