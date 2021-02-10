 
import azzinimunda.azzinimunda0 as am
import scf.initialization as init
import numpy as np
import time


om = np.array([
[0,4,4,3],
[6,0,6,6],
[6,4,0,6],
[7,4,4,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,8,6,7],
[2,0,4,6],
[4,6,0,7],
[3,4,3,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,7,6,7],
[3,0,4,3],
[4,6,0,4],
[3,7,6,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,6,4,3],
[4,0,3,3],
[6,7,0,2],
[7,7,8,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,1,1,2],
[9,0,7,6],
[9,3,0,6],
[8,4,4,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,7,6,9],
[3,0,7,9],
[4,3,0,6],
[1,1,4,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,4,3,3],
[6,0,7,7],
[7,3,0,4],
[7,3,6,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,3,6,4],
[7,0,6,6],
[4,4,0,4],
[6,4,6,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,6,6,7],
[4,0,8,8],
[4,2,0,6],
[3,2,4,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,4,4,3],
[6,0,6,3],
[6,4,0,4],
[7,7,6,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,6,5,6],
[4,0,3,6],
[5,7,0,4],
[4,4,6,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,6,5,6],
[4,0,3,4],
[5,7,0,4],
[4,6,6,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,4,4,4],
[6,0,5,7],
[6,5,0,3],
[6,3,7,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,4,4,2],
[6,0,3,2],
[6,7,0,5],
[8,8,5,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,9,3,4],
[1,0,2,2],
[7,8,0,5],
[6,8,5,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,5,6,4],
[5,0,5,5],
[4,5,0,5],
[6,5,5,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,4,5,5],
[6,0,5,6],
[5,5,0,6],
[5,4,4,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,7,5,5],
[3,0,5,7],
[5,5,0,6],
[5,3,4,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,4,4,3],
[6,0,4,4],
[6,6,0,5],
[7,6,5,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,6,7,5],
[4,0,6,5],
[3,4,0,4],
[5,5,6,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,4,5,6],
[6,0,7,8],
[5,3,0,5],
[4,2,5,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,5,4,5],
[5,0,3,6],
[6,7,0,8],
[5,4,2,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,7,8,7],
[3,0,5,3],
[2,5,0,4],
[3,7,6,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,4,5,3],
[6,0,6,4],
[5,4,0,4],
[7,6,6,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,3,8,7],
[7,0,8,7],
[2,2,0,5],
[3,3,5,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,7,6,9],
[3,0,3,5],
[4,7,0,7],
[1,5,3,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,5,2,8],
[5,0,3,6],
[8,7,0,8],
[2,4,2,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,5,3,7],
[5,0,4,8],
[7,6,0,7],
[3,2,3,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,6,5,3],
[4,0,5,4],
[5,5,0,4],
[7,6,6,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,5,3,4],
[5,0,2,3],
[7,8,0,7],
[6,7,3,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,3,4,5],
[7,0,7,5],
[6,3,0,6],
[5,5,4,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,7,5,7],
[3,0,4,5],
[5,6,0,7],
[3,5,3,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,4,3,3],
[6,0,5,5],
[7,5,0,6],
[7,5,4,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,5,5,6],
[5,0,6,6],
[5,4,0,6],
[4,4,4,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,4,5,5],
[6,0,5,5],
[5,5,0,4],
[5,5,6,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,7,5,6],
[3,0,2,4],
[5,8,0,2],
[4,6,8,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,7,4,7],
[3,0,4,6],
[6,6,0,8],
[3,4,2,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,6,3,3],
[4,0,7,5],
[7,3,0,5],
[7,5,5,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,3,5,6],
[7,0,6,8],
[5,4,0,6],
[4,2,4,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################
om = np.array([
[0,4,2,2],
[6,0,3,4],
[8,7,0,8],
[8,6,2,0]])
  
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("results4A1.txt", "a")
f.write("{}\n".format(exec_time))
f.close()
print(exec_time)
##############################################