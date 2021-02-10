 
import azzinimunda.azzinimunda0 as am
import scf.initialization as init
import numpy as np
import time


om = np.array([
[0,7,6,6],
[3,0,4,4],
[4,6,0,2],
[4,6,8,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,8,6,8],
[2,0,4,4],
[4,6,0,7],
[2,6,3,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,8,4,8],
[2,0,2,4],
[6,8,0,6],
[2,6,4,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,4,4,8],
[6,0,8,9],
[6,2,0,6],
[2,1,4,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,7,7,6],
[3,0,6,7],
[3,4,0,6],
[4,3,4,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,3,4,4],
[7,0,6,4],
[6,4,0,4],
[6,6,6,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,4,2,4],
[6,0,4,7],
[8,6,0,6],
[6,3,4,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,4,3,2],
[6,0,3,4],
[7,7,0,6],
[8,6,4,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,3,3,3],
[7,0,4,3],
[7,6,0,4],
[7,7,6,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,6,4,7],
[4,0,3,3],
[6,7,0,7],
[3,7,3,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,5,5,6],
[5,0,5,6],
[5,5,0,5],
[4,4,5,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,5,5,3],
[5,0,4,5],
[5,6,0,5],
[7,5,5,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,8,6,5],
[2,0,4,3],
[4,6,0,5],
[5,7,5,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,8,5,5],
[2,0,4,5],
[5,6,0,8],
[5,5,2,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,5,6,5],
[5,0,4,6],
[4,6,0,5],
[5,4,5,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,7,5,5],
[3,0,4,2],
[5,6,0,4],
[5,8,6,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,7,5,5],
[3,0,2,3],
[5,8,0,5],
[5,7,5,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,7,5,5],
[3,0,4,5],
[5,6,0,5],
[5,5,5,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,5,7,6],
[5,0,3,6],
[3,7,0,5],
[4,4,5,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,3,3,4],
[7,0,4,5],
[7,6,0,5],
[6,5,5,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,7,6,7],
[3,0,5,6],
[4,5,0,3],
[3,4,7,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,5,4,4],
[5,0,3,4],
[6,7,0,7],
[6,6,3,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,4,5,2],
[6,0,8,8],
[5,2,0,4],
[8,2,6,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,5,5,4],
[5,0,5,3],
[5,5,0,3],
[6,7,7,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,5,5,4],
[5,0,4,3],
[5,6,0,4],
[6,7,6,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,8,7,8],
[2,0,3,6],
[3,7,0,4],
[2,4,6,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,2,5,4],
[8,0,7,7],
[5,3,0,5],
[6,3,5,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,2,4,5],
[8,0,4,7],
[6,6,0,9],
[5,3,1,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,7,9,7],
[3,0,5,5],
[1,5,0,3],
[3,5,7,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,3,5,3],
[7,0,6,4],
[5,4,0,4],
[7,6,6,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,4,4,5],
[6,0,5,9],
[6,5,0,7],
[5,1,3,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,5,7,6],
[5,0,4,5],
[3,6,0,7],
[4,5,3,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,5,6,5],
[5,0,5,4],
[4,5,0,3],
[5,6,7,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,5,7,5],
[5,0,7,8],
[3,3,0,5],
[5,2,5,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,6,4,7],
[4,0,5,5],
[6,5,0,7],
[3,5,3,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,4,3,4],
[6,0,5,5],
[7,5,0,4],
[6,5,6,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,4,6,6],
[6,0,7,5],
[4,3,0,6],
[4,5,4,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,5,5,5],
[5,0,3,6],
[5,7,0,6],
[5,4,4,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,3,3,4],
[7,0,7,4],
[7,3,0,5],
[6,6,5,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,3,4,5],
[7,0,6,4],
[6,4,0,7],
[5,6,3,0]])
  
algorithm = am.AzziniMunda0(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("kemeny/results4.txt", "a")
f.write("{0}
".format(exec_time))
f.close()
print(exec_time)
##############################################