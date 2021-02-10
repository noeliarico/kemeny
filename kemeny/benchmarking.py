#import scf
#import numpy as np

#def benchmark():
#    print("hehe bench")

#am.hello()
#scf.initialize()


import azzinimunda.azzinimunda0 as am0
import scf.initialization as init
import numpy as np
import time
import azzinimunda.azzinimunda2 as am2
import azzinimunda.azzinimunda1 as am1

n = 5
#np.random.seed(123)
#om = init.create_random_om(n, 10)
om = np.array([0, 4, 3, 6, 1,
              6, 0, 5, 7, 8,
              7, 5, 0, 9, 6,
              4, 3, 1, 0, 3,
              9, 2, 4, 7, 0]).reshape(n,n)
print(om)
algorithm = am0.AzziniMunda0(om)
print(algorithm.execute())

# n = 9
# np.random.seed(123)
# om = init.create_random_om(n, 10)
# algorithm = am.AzziniMunda0(om)
# print("Executing AzziniMunda0...")
# start_time = time.time()
# sol = algorithm.execute()
# exec_time = time.time() - start_time
# print("Execution time for n = {} -> {}s".format(n, time.time() - start_time))
# 
# 
# n = 9
# np.random.seed(123)
# om = init.create_random_om(n, 10)
# algorithm = am.AzziniMunda1(om)
# print("Executing AzziniMunda1...")
# start_time = time.time()
# sol = algorithm.execute()
# exec_time = time.time() - start_time
# print("Execution time for n = {} -> {}s".format(n, time.time() - start_time))

#f = open("results.txt", "a")
#f.write(str(sol))
#f.close()

