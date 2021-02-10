import azzinimunda.azzinimunda0 as am
import scf.initialization as init
import numpy as np
import time

om = np.array([
[0,4,0,3,0,4,3,3,7,4,0,7,3,0],
[6,0,3,6,0,7,6,6,3,10,6,7,3,0],
[10,7,0,10,4,7,10,10,7,10,10,7,10,4],
[7,4,0,0,4,4,0,3,7,4,7,4,4,0],
[10,10,6,6,0,7,6,6,7,10,10,10,10,0],
[6,3,3,6,3,0,6,6,3,6,6,7,3,3],
[7,4,0,10,4,4,0,6,7,4,7,4,4,0],
[7,4,0,7,4,4,4,0,7,4,7,4,4,4],
[3,7,3,3,3,7,3,3,0,7,3,7,3,3],
[6,0,0,6,0,4,6,6,3,0,6,7,3,0],
[10,4,0,3,0,4,3,3,7,4,0,7,7,0],
[3,3,3,6,0,3,6,6,3,3,3,0,6,0],
[7,7,0,6,0,7,6,6,7,7,3,4,0,0],
[10,10,6,10,10,7,10,6,7,10,10,10,10,0]])
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
