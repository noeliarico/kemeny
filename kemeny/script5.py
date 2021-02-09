import azzinimunda.azzinimunda0 as am
import scf.initialization as init
import numpy as np
import time

om = np.array([
[0,7,7,6,6,4,7,6,9,7,8,9],
[3,0,6,4,5,4,5,4,6,7,6,7],
[3,4,0,4,5,3,4,6,5,2,4,7],
[4,6,6,0,5,4,5,8,7,6,5,7],
[4,5,5,5,0,4,6,6,8,5,5,7],
[6,6,7,6,6,0,5,8,9,8,8,8],
[3,5,6,5,4,5,0,6,5,4,5,6],
[4,6,4,2,4,2,4,0,7,4,5,8],
[1,4,5,3,2,1,5,3,0,5,5,8],
[3,3,8,4,5,2,6,6,5,0,4,8],
[2,4,6,5,5,2,5,5,5,6,0,8],
[1,3,3,3,3,2,4,2,2,2,2,0]])
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
