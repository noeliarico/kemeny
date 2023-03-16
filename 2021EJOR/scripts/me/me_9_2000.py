
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,967,969,1034,951,988,980,941,922],
[1033,0,980,1026,1040,955,1012,932,945],
[1031,1020,0,1051,1003,964,1014,972,1011],
[966,974,949,0,954,902,967,921,902],
[1049,960,997,1046,0,899,1052,944,975],
[1012,1045,1036,1098,1101,0,1078,1036,998],
[1020,988,986,1033,948,922,0,913,950],
[1059,1068,1028,1079,1056,964,1087,0,1015],
[1078,1055,989,1098,1025,1002,1050,985,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 1, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,1002,1004,1042,1013,986,1033,1059],
[995,0,968,992,1022,1001,976,981,1055],
[998,1032,0,1017,1073,1023,1031,1047,1044],
[996,1008,983,0,1016,976,966,1005,1033],
[958,978,927,984,0,946,940,992,1006],
[987,999,977,1024,1054,0,1000,1013,1039],
[1014,1024,969,1034,1060,1000,0,1050,1028],
[967,1019,953,995,1008,987,950,0,985],
[941,945,956,967,994,961,972,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 2, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,976,949,944,978,1008,999,989],
[1016,0,965,991,885,995,991,1005,943],
[1024,1035,0,955,962,1012,998,1028,994],
[1051,1009,1045,0,972,1024,1043,1087,1013],
[1056,1115,1038,1028,0,973,1051,1049,1044],
[1022,1005,988,976,1027,0,995,1033,993],
[992,1009,1002,957,949,1005,0,990,1002],
[1001,995,972,913,951,967,1010,0,933],
[1011,1057,1006,987,956,1007,998,1067,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 3, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1022,977,977,961,1013,995,976,976],
[978,0,987,975,1018,972,984,993,991],
[1023,1013,0,1003,990,973,1024,966,1001],
[1023,1025,997,0,984,1019,1020,948,1028],
[1039,982,1010,1016,0,999,1014,1004,1005],
[987,1028,1027,981,1001,0,1055,985,1022],
[1005,1016,976,980,986,945,0,997,1005],
[1024,1007,1034,1052,996,1015,1003,0,999],
[1024,1009,999,972,995,978,995,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 4, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,972,956,964,1027,1013,985,1011],
[993,0,1019,970,965,997,985,996,1030],
[1028,981,0,993,973,1007,1008,1021,1019],
[1044,1030,1007,0,1000,1044,1018,1005,998],
[1036,1035,1027,1000,0,1030,1006,1050,1044],
[973,1003,993,956,970,0,1018,1008,1019],
[987,1015,992,982,994,982,0,980,1015],
[1015,1004,979,995,950,992,1020,0,996],
[989,970,981,1002,956,981,985,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 5, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,985,992,980,989,970,999,1015],
[999,0,966,997,981,979,1011,977,994],
[1015,1034,0,975,981,1019,996,1001,1014],
[1008,1003,1025,0,966,994,1002,978,1009],
[1020,1019,1019,1034,0,988,1035,1038,1019],
[1011,1021,981,1006,1012,0,1023,1015,1024],
[1030,989,1004,998,965,977,0,1003,985],
[1001,1023,999,1022,962,985,997,0,1001],
[985,1006,986,991,981,976,1015,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 6, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,984,999,1042,1005,1000,1024,975],
[1007,0,985,988,996,1008,993,1031,1006],
[1016,1015,0,1038,1038,1039,992,1030,1040],
[1001,1012,962,0,1016,1017,1002,1059,999],
[958,1004,962,984,0,1015,965,1023,998],
[995,992,961,983,985,0,1015,985,931],
[1000,1007,1008,998,1035,985,0,1039,1025],
[976,969,970,941,977,1015,961,0,951],
[1025,994,960,1001,1002,1069,975,1049,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 7, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,985,1020,1027,1078,999,1084,1016],
[986,0,998,1044,980,1073,983,1026,1000],
[1015,1002,0,979,1003,1017,1016,1050,1000],
[980,956,1021,0,992,1042,989,1021,1007],
[973,1020,997,1008,0,1026,967,1048,1003],
[922,927,983,958,974,0,981,990,963],
[1001,1017,984,1011,1033,1019,0,1039,954],
[916,974,950,979,952,1010,961,0,978],
[984,1000,1000,993,997,1037,1046,1022,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 8, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,1033,1035,1042,1043,1072,997,1079],
[1016,0,1002,1069,979,1041,1026,972,1111],
[967,998,0,1020,993,1036,1010,964,1098],
[965,931,980,0,963,1024,1006,939,1066],
[958,1021,1007,1037,0,1037,1034,1009,1039],
[957,959,964,976,963,0,1001,952,1061],
[928,974,990,994,966,999,0,972,1062],
[1003,1028,1036,1061,991,1048,1028,0,1090],
[921,889,902,934,961,939,938,910,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 9, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,1019,993,1011,1007,998,1012,1020],
[1001,0,991,979,1044,1040,1008,1021,994],
[981,1009,0,1000,1026,1027,1007,1020,995],
[1007,1021,1000,0,1013,1016,1019,996,1007],
[989,956,974,987,0,996,994,966,991],
[993,960,973,984,1004,0,998,980,993],
[1002,992,993,981,1006,1002,0,998,1004],
[988,979,980,1004,1034,1020,1002,0,1017],
[980,1006,1005,993,1009,1007,996,983,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 10, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1059,986,1047,1029,1044,1048,1046,1017],
[941,0,939,1024,936,991,1034,989,964],
[1014,1061,0,998,1023,1011,1042,1012,968],
[953,976,1002,0,993,1001,1028,1028,1008],
[971,1064,977,1007,0,995,1031,1015,1038],
[956,1009,989,999,1005,0,1049,1008,951],
[952,966,958,972,969,951,0,978,978],
[954,1011,988,972,985,992,1022,0,951],
[983,1036,1032,992,962,1049,1022,1049,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 11, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,892,932,933,1037,1017,996,1005,965],
[1108,0,1048,993,1044,1134,1114,1098,1001],
[1068,952,0,1032,1091,1113,1088,1076,1040],
[1067,1007,968,0,1066,1049,1013,1023,1002],
[963,956,909,934,0,1047,1016,1010,970],
[983,866,887,951,953,0,973,994,969],
[1004,886,912,987,984,1027,0,962,1003],
[995,902,924,977,990,1006,1038,0,999],
[1035,999,960,998,1030,1031,997,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 12, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,1005,983,972,945,981,982,973],
[980,0,1021,1003,1007,978,1003,956,983],
[995,979,0,994,993,987,1001,997,988],
[1017,997,1006,0,1001,1016,998,1002,1005],
[1028,993,1007,999,0,956,1009,988,963],
[1055,1022,1013,984,1044,0,1049,1000,1034],
[1019,997,999,1002,991,951,0,984,979],
[1018,1044,1003,998,1012,1000,1016,0,994],
[1027,1017,1012,995,1037,966,1021,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 13, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1068,1072,1055,992,1002,1012,1055,1017],
[932,0,984,1047,994,934,932,989,986],
[928,1016,0,1001,987,917,950,895,967],
[945,953,999,0,962,944,1005,958,964],
[1008,1006,1013,1038,0,1051,999,979,1018],
[998,1066,1083,1056,949,0,1007,1060,1037],
[988,1068,1050,995,1001,993,0,1058,1029],
[945,1011,1105,1042,1021,940,942,0,1006],
[983,1014,1033,1036,982,963,971,994,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 14, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,937,1029,998,1005,1077,1042,970,1055],
[1063,0,1028,1053,1070,1173,1063,987,1070],
[971,972,0,943,908,981,1024,999,965],
[1002,947,1057,0,1059,1012,1065,918,1043],
[995,930,1092,941,0,983,999,1018,924],
[923,827,1019,988,1017,0,1012,910,973],
[958,937,976,935,1001,988,0,925,944],
[1030,1013,1001,1082,982,1090,1075,0,1039],
[945,930,1035,957,1076,1027,1056,961,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 15, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,1056,1029,1030,1010,973,1010,1038],
[987,0,1054,1000,1025,1011,969,998,1017],
[944,946,0,993,979,954,940,975,984],
[971,1000,1007,0,1008,981,950,926,984],
[970,975,1021,992,0,987,985,952,981],
[990,989,1046,1019,1013,0,1014,1027,1027],
[1027,1031,1060,1050,1015,986,0,1000,1047],
[990,1002,1025,1074,1048,973,1000,0,1032],
[962,983,1016,1016,1019,973,953,968,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 16, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1054,1011,1007,977,1040,1039,1051,1031],
[946,0,1005,944,960,991,960,971,1003],
[989,995,0,982,1036,1049,1018,1025,1017],
[993,1056,1018,0,1001,1085,995,1060,1015],
[1023,1040,964,999,0,1026,1033,1058,1036],
[960,1009,951,915,974,0,967,989,949],
[961,1040,982,1005,967,1033,0,1057,995],
[949,1029,975,940,942,1011,943,0,969],
[969,997,983,985,964,1051,1005,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 17, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,976,995,1007,970,949,1029,1012,972],
[1024,0,1058,1020,1014,1019,1013,983,1004],
[1005,942,0,999,979,1013,995,1023,966],
[993,980,1001,0,938,984,988,1031,995],
[1030,986,1021,1062,0,996,1049,1005,1004],
[1051,981,987,1016,1004,0,1013,995,1016],
[971,987,1005,1012,951,987,0,1035,944],
[988,1017,977,969,995,1005,965,0,1011],
[1028,996,1034,1005,996,984,1056,989,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 18, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,995,1024,989,991,1008,1037,994],
[1012,0,994,1013,987,1009,1032,1039,1039],
[1005,1006,0,1032,971,1017,1024,1040,1046],
[976,987,968,0,985,990,988,1025,1021],
[1011,1013,1029,1015,0,1020,1044,1000,1020],
[1009,991,983,1010,980,0,1039,1007,1029],
[992,968,976,1012,956,961,0,995,1001],
[963,961,960,975,1000,993,1005,0,998],
[1006,961,954,979,980,971,999,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 19, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,1017,989,998,1054,1029,1012,1035],
[985,0,986,1016,1002,993,1004,1016,993],
[983,1014,0,978,1029,983,1006,935,1027],
[1011,984,1022,0,1032,1027,1055,964,1027],
[1002,998,971,968,0,973,1023,930,1041],
[946,1007,1017,973,1027,0,1048,971,995],
[971,996,994,945,977,952,0,940,951],
[988,984,1065,1036,1070,1029,1060,0,1055],
[965,1007,973,973,959,1005,1049,945,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 20, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,1005,948,996,1032,966,983,1022],
[1004,0,1015,957,1019,1033,987,937,992],
[995,985,0,969,972,980,1000,967,994],
[1052,1043,1031,0,998,992,986,985,985],
[1004,981,1028,1002,0,949,985,995,990],
[968,967,1020,1008,1051,0,1014,991,1011],
[1034,1013,1000,1014,1015,986,0,1012,1029],
[1017,1063,1033,1015,1005,1009,988,0,1027],
[978,1008,1006,1015,1010,989,971,973,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 21, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,985,997,1000,1004,1064,1002,999,1038],
[1015,0,989,1042,1024,1042,999,1031,1046],
[1003,1011,0,1042,1003,1066,942,1016,1033],
[1000,958,958,0,1016,1012,985,1013,1013],
[996,976,997,984,0,1065,959,996,1046],
[936,958,934,988,935,0,894,956,966],
[998,1001,1058,1015,1041,1106,0,1028,1038],
[1001,969,984,987,1004,1044,972,0,1004],
[962,954,967,987,954,1034,962,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 22, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1070,988,1087,1097,1061,1035,1002,1041],
[930,0,975,1007,973,953,981,925,928],
[1012,1025,0,1054,1021,952,1068,984,959],
[913,993,946,0,959,958,960,917,973],
[903,1027,979,1041,0,965,932,984,973],
[939,1047,1048,1042,1035,0,983,996,1031],
[965,1019,932,1040,1068,1017,0,997,1047],
[998,1075,1016,1083,1016,1004,1003,0,1027],
[959,1072,1041,1027,1027,969,953,973,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 23, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,1020,1055,990,963,999,970,1007],
[989,0,976,1001,958,962,950,973,1001],
[980,1024,0,996,1015,961,1012,984,1026],
[945,999,1004,0,1006,956,959,964,1032],
[1010,1042,985,994,0,1000,955,1004,1018],
[1037,1038,1039,1044,1000,0,1004,1012,1033],
[1001,1050,988,1041,1045,996,0,969,1045],
[1030,1027,1016,1036,996,988,1031,0,1030],
[993,999,974,968,982,967,955,970,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 24, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,978,1029,970,1014,991,972,1008,995],
[1022,0,1011,989,1000,979,1013,1001,974],
[971,989,0,998,1005,954,989,1005,979],
[1030,1011,1002,0,983,1009,1033,1033,1028],
[986,1000,995,1017,0,989,1022,1026,1011],
[1009,1021,1046,991,1011,0,1021,1046,1020],
[1028,987,1011,967,978,979,0,1014,1003],
[992,999,995,967,974,954,986,0,1008],
[1005,1026,1021,972,989,980,997,992,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 25, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,897,1024,980,933,931,925,952,972],
[1103,0,1057,1073,955,945,1051,980,1075],
[976,943,0,1011,963,953,1054,1042,1017],
[1020,927,989,0,944,955,960,980,1014],
[1067,1045,1037,1056,0,1014,1070,924,1024],
[1069,1055,1047,1045,986,0,1057,1020,978],
[1075,949,946,1040,930,943,0,966,980],
[1048,1020,958,1020,1076,980,1034,0,1082],
[1028,925,983,986,976,1022,1020,918,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 26, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,1019,994,1022,1034,945,1021,1006],
[985,0,1031,932,921,990,977,979,1001],
[981,969,0,925,958,999,960,998,1009],
[1006,1068,1075,0,994,1060,1058,1062,1034],
[978,1079,1042,1006,0,1068,1003,1037,1066],
[966,1010,1001,940,932,0,971,941,993],
[1055,1023,1040,942,997,1029,0,988,1023],
[979,1021,1002,938,963,1059,1012,0,966],
[994,999,991,966,934,1007,977,1034,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 27, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1070,1048,1054,1067,1002,1042,1065,977],
[930,0,1004,1019,1014,965,961,995,963],
[952,996,0,950,964,960,952,1019,951],
[946,981,1050,0,998,997,996,1031,945],
[933,986,1036,1002,0,980,988,1031,971],
[998,1035,1040,1003,1020,0,996,1069,1013],
[958,1039,1048,1004,1012,1004,0,994,1028],
[935,1005,981,969,969,931,1006,0,961],
[1023,1037,1049,1055,1029,987,972,1039,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 28, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,959,988,1003,968,986,982,1017,1011],
[1041,0,1046,1058,1021,991,1008,969,1021],
[1012,954,0,988,964,998,993,1035,1014],
[997,942,1012,0,927,954,954,953,993],
[1032,979,1036,1073,0,1022,1024,1062,1045],
[1014,1009,1002,1046,978,0,987,948,981],
[1018,992,1007,1046,976,1013,0,1013,1018],
[983,1031,965,1047,938,1052,987,0,997],
[989,979,986,1007,955,1019,982,1003,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 29, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1058,981,912,1033,985,947,977,925],
[942,0,943,922,920,947,933,993,885],
[1019,1057,0,1018,1026,964,948,987,990],
[1088,1078,982,0,1095,1068,1006,1069,955],
[967,1080,974,905,0,991,959,1062,957],
[1015,1053,1036,932,1009,0,1075,1040,1006],
[1053,1067,1052,994,1041,925,0,1024,992],
[1023,1007,1013,931,938,960,976,0,973],
[1075,1115,1010,1045,1043,994,1008,1027,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 30, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1059,955,1056,966,948,1013,965,1018],
[941,0,971,971,921,966,936,935,955],
[1045,1029,0,998,1043,1010,1058,1015,1001],
[944,1029,1002,0,969,966,960,980,1022],
[1034,1079,957,1031,0,957,987,991,997],
[1052,1034,990,1034,1043,0,1012,1022,1047],
[987,1064,942,1040,1013,988,0,1001,1026],
[1035,1065,985,1020,1009,978,999,0,986],
[982,1045,999,978,1003,953,974,1014,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 31, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,942,956,978,995,976,1022,979],
[988,0,973,979,959,996,958,1017,990],
[1058,1027,0,999,1005,1024,965,1005,1028],
[1044,1021,1001,0,1038,1043,977,1035,1043],
[1022,1041,995,962,0,1022,985,1017,1013],
[1005,1004,976,957,978,0,1002,1014,1018],
[1024,1042,1035,1023,1015,998,0,1045,1030],
[978,983,995,965,983,986,955,0,992],
[1021,1010,972,957,987,982,970,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 32, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1036,1034,1076,962,1060,1032,969,1137],
[964,0,914,942,988,1043,826,885,1040],
[966,1086,0,1144,896,1057,1163,1100,1013],
[924,1058,856,0,1007,1064,891,879,908],
[1038,1012,1104,993,0,1049,1008,930,891],
[940,957,943,936,951,0,946,894,974],
[968,1174,837,1109,992,1054,0,993,1026],
[1031,1115,900,1121,1070,1106,1007,0,1065],
[863,960,987,1092,1109,1026,974,935,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 33, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,1094,1002,1039,977,967,1038,1009],
[1004,0,1018,955,936,1049,912,1041,940],
[906,982,0,930,933,957,942,1003,977],
[998,1045,1070,0,989,964,955,1046,987],
[961,1064,1067,1011,0,999,976,1077,1020],
[1023,951,1043,1036,1001,0,994,1031,1014],
[1033,1088,1058,1045,1024,1006,0,1031,954],
[962,959,997,954,923,969,969,0,945],
[991,1060,1023,1013,980,986,1046,1055,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 34, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1077,985,991,1103,957,1023,980,1113],
[923,0,938,928,973,940,873,885,1012],
[1015,1062,0,931,1012,949,955,1011,1092],
[1009,1072,1069,0,1045,991,983,1000,1108],
[897,1027,988,955,0,954,954,935,1014],
[1043,1060,1051,1009,1046,0,970,1021,1062],
[977,1127,1045,1017,1046,1030,0,1006,1086],
[1020,1115,989,1000,1065,979,994,0,1066],
[887,988,908,892,986,938,914,934,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 35, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,994,962,1025,964,981,958,972],
[1006,0,988,1002,973,975,989,1001,1024],
[1006,1012,0,1035,1020,997,968,989,974],
[1038,998,965,0,1015,968,949,938,1041],
[975,1027,980,985,0,959,991,988,1018],
[1036,1025,1003,1032,1041,0,998,1042,1048],
[1019,1011,1032,1051,1009,1002,0,952,1029],
[1042,999,1011,1062,1012,958,1048,0,992],
[1028,976,1026,959,982,952,971,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 36, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,977,971,972,1025,1000,1008,1029],
[987,0,972,1004,966,1040,948,978,1036],
[1023,1028,0,993,1022,1043,982,1016,1025],
[1029,996,1007,0,1022,1054,1031,1025,1032],
[1028,1034,978,978,0,1024,995,981,1003],
[975,960,957,946,976,0,977,961,1015],
[1000,1052,1018,969,1005,1023,0,998,1026],
[992,1022,984,975,1019,1039,1002,0,1024],
[971,964,975,968,997,985,974,976,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 37, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1000,993,991,1003,1006,990,997,1003],
[1000,0,976,1008,990,1010,980,1008,1015],
[1007,1024,0,1021,1008,1028,966,1021,1017],
[1009,992,979,0,969,1024,1011,1031,1005],
[997,1010,992,1031,0,1022,1000,1026,1047],
[994,990,972,976,978,0,956,1004,984],
[1010,1020,1034,989,1000,1044,0,1028,1031],
[1003,992,979,969,974,996,972,0,1010],
[997,985,983,995,953,1016,969,990,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 38, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,1048,1041,959,1031,923,1010,1043],
[997,0,1072,881,907,1041,988,943,1001],
[952,928,0,927,991,941,937,933,954],
[959,1119,1073,0,1015,1078,988,1025,1011],
[1041,1093,1009,985,0,1026,1023,949,1030],
[969,959,1059,922,974,0,943,936,986],
[1077,1012,1063,1012,977,1057,0,1019,1022],
[990,1057,1067,975,1051,1064,981,0,994],
[957,999,1046,989,970,1014,978,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 39, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1027,990,1008,1026,1048,1020,1056,1024],
[973,0,1005,932,993,1024,1013,1001,963],
[1010,995,0,926,947,953,971,934,943],
[992,1068,1074,0,1030,1078,1070,1078,1028],
[974,1007,1053,970,0,1057,975,1000,997],
[952,976,1047,922,943,0,977,1001,949],
[980,987,1029,930,1025,1023,0,994,1039],
[944,999,1066,922,1000,999,1006,0,985],
[976,1037,1057,972,1003,1051,961,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 40, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,971,1026,1018,997,987,990,1021,990],
[1029,0,1012,1037,1001,1011,994,1031,1022],
[974,988,0,994,952,957,942,986,951],
[982,963,1006,0,978,993,988,990,958],
[1003,999,1048,1022,0,1024,1006,1021,996],
[1013,989,1043,1007,976,0,972,1046,998],
[1010,1006,1058,1012,994,1028,0,1039,991],
[979,969,1014,1010,979,954,961,0,953],
[1010,978,1049,1042,1004,1002,1009,1047,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 41, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,986,1003,1035,1029,987,998,1024,1048],
[1014,0,1022,1068,993,1044,1017,1038,1064],
[997,978,0,966,1024,1007,1015,1025,1061],
[965,932,1034,0,954,957,965,967,980],
[971,1007,976,1046,0,1017,1029,1035,1010],
[1013,956,993,1043,983,0,996,1013,1048],
[1002,983,985,1035,971,1004,0,1023,1025],
[976,962,975,1033,965,987,977,0,1025],
[952,936,939,1020,990,952,975,975,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 42, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1074,980,1126,1033,980,1148,1089,1079],
[926,0,1024,1062,912,1040,990,1077,970],
[1020,976,0,1185,885,966,1124,1149,999],
[874,938,815,0,718,976,992,1022,946],
[967,1088,1115,1282,0,1126,1207,1107,1140],
[1020,960,1034,1024,874,0,923,990,969],
[852,1010,876,1008,793,1077,0,1064,953],
[911,923,851,978,893,1010,936,0,818],
[921,1030,1001,1054,860,1031,1047,1182,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 43, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,943,937,975,954,923,991,925,985],
[1057,0,1006,1059,1007,1003,1072,985,1087],
[1063,994,0,1050,1002,975,1029,1044,1073],
[1025,941,950,0,971,957,990,966,1019],
[1046,993,998,1029,0,983,1037,1025,1066],
[1077,997,1025,1043,1017,0,1084,998,1114],
[1009,928,971,1010,963,916,0,920,998],
[1075,1015,956,1034,975,1002,1080,0,1044],
[1015,913,927,981,934,886,1002,956,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 44, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,982,976,992,976,1011,1002,1036,943],
[1018,0,971,1046,995,930,1065,961,935],
[1024,1029,0,978,977,1008,1070,994,1048],
[1008,954,1022,0,969,1031,1017,953,952],
[1024,1005,1023,1031,0,1038,1133,977,1027],
[989,1070,992,969,962,0,1018,979,1002],
[998,935,930,983,867,982,0,991,951],
[964,1039,1006,1047,1023,1021,1009,0,972],
[1057,1065,952,1048,973,998,1049,1028,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 45, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,986,969,991,987,984,979,1026],
[987,0,910,983,1041,986,999,1069,998],
[1014,1090,0,984,1080,987,1051,1032,1076],
[1031,1017,1016,0,1051,947,1061,996,1035],
[1009,959,920,949,0,944,978,965,1016],
[1013,1014,1013,1053,1056,0,1007,967,1070],
[1016,1001,949,939,1022,993,0,1032,1005],
[1021,931,968,1004,1035,1033,968,0,1011],
[974,1002,924,965,984,930,995,989,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 46, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,996,1013,1010,998,1035,1033,1016],
[994,0,1017,999,1054,1015,1065,993,1045],
[1004,983,0,1009,990,976,1004,983,1013],
[987,1001,991,0,1015,989,1000,984,1009],
[990,946,1010,985,0,971,988,996,984],
[1002,985,1024,1011,1029,0,1014,1012,1032],
[965,935,996,1000,1012,986,0,949,1001],
[967,1007,1017,1016,1004,988,1051,0,1038],
[984,955,987,991,1016,968,999,962,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 47, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,973,992,964,992,957,976,970,967],
[1027,0,1027,1055,1049,1008,984,1006,1026],
[1008,973,0,994,1013,976,992,961,971],
[1036,945,1006,0,1037,1000,1000,979,1018],
[1008,951,987,963,0,958,1003,979,974],
[1043,992,1024,1000,1042,0,1005,981,1017],
[1024,1016,1008,1000,997,995,0,990,1005],
[1030,994,1039,1021,1021,1019,1010,0,1033],
[1033,974,1029,982,1026,983,995,967,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 48, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1044,1022,1028,992,983,1017,988,1040],
[956,0,1008,973,926,979,1008,987,981],
[978,992,0,978,992,957,932,944,986],
[972,1027,1022,0,974,960,989,934,1035],
[1008,1074,1008,1026,0,1047,1004,991,1019],
[1017,1021,1043,1040,953,0,998,1016,1067],
[983,992,1068,1011,996,1002,0,957,1038],
[1012,1013,1056,1066,1009,984,1043,0,1080],
[960,1019,1014,965,981,933,962,920,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 49, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,909,1108,890,1021,1032,982,1023,1059],
[1091,0,1040,856,972,993,1014,947,969],
[892,960,0,855,938,1069,970,980,902],
[1110,1144,1145,0,1053,1125,1079,1104,974],
[979,1028,1062,947,0,1093,1015,1030,1043],
[968,1007,931,875,907,0,900,976,963],
[1018,986,1030,921,985,1100,0,919,1044],
[977,1053,1020,896,970,1024,1081,0,1045],
[941,1031,1098,1026,957,1037,956,955,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 50, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,983,994,982,998,981,992,1001,983],
[1017,0,966,1025,976,996,979,976,968],
[1006,1034,0,1007,1011,1019,1019,1004,957],
[1018,975,993,0,976,978,975,967,947],
[1002,1024,989,1024,0,1030,1018,1011,1040],
[1019,1004,981,1022,970,0,1000,981,935],
[1008,1021,981,1025,982,1000,0,1023,1002],
[999,1024,996,1033,989,1019,977,0,987],
[1017,1032,1043,1053,960,1065,998,1013,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 51, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,959,932,936,1008,978,1006,1083,970],
[1041,0,1022,987,999,960,980,1077,977],
[1068,978,0,1031,981,942,1012,1092,1004],
[1064,1013,969,0,1000,1003,1027,1107,966],
[992,1001,1019,1000,0,948,1001,1093,991],
[1022,1040,1058,997,1052,0,1042,1143,1052],
[994,1020,988,973,999,958,0,1051,1004],
[917,923,908,893,907,857,949,0,900],
[1030,1023,996,1034,1009,948,996,1100,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 52, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,980,966,1006,988,1019,1010,974],
[993,0,942,961,1009,999,1008,957,964],
[1020,1058,0,1021,1031,1051,1045,995,1006],
[1034,1039,979,0,1020,1023,1036,987,977],
[994,991,969,980,0,983,1027,998,967],
[1012,1001,949,977,1017,0,1026,970,960],
[981,992,955,964,973,974,0,976,979],
[990,1043,1005,1013,1002,1030,1024,0,988],
[1026,1036,994,1023,1033,1040,1021,1012,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 53, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,968,1024,987,1067,1021,1095,979,1034],
[1032,0,1028,959,1049,941,1029,947,991],
[976,972,0,917,1030,938,1024,967,983],
[1013,1041,1083,0,1103,990,1090,1030,1047],
[933,951,970,897,0,1037,1036,998,957],
[979,1059,1062,1010,963,0,1020,934,1094],
[905,971,976,910,964,980,0,847,945],
[1021,1053,1033,970,1002,1066,1153,0,1060],
[966,1009,1017,953,1043,906,1055,940,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 54, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,971,989,970,952,960,944,999,956],
[1029,0,1022,1028,993,1008,1027,1040,1029],
[1011,978,0,1009,997,992,952,1009,1013],
[1030,972,991,0,1020,987,987,1025,994],
[1048,1007,1003,980,0,983,980,1026,990],
[1040,992,1008,1013,1017,0,972,1014,1002],
[1056,973,1048,1013,1020,1028,0,1020,1012],
[1001,960,991,975,974,986,980,0,976],
[1044,971,987,1006,1010,998,988,1024,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 55, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,1011,997,1027,997,995,990,1005],
[998,0,1021,986,1005,994,996,996,980],
[989,979,0,975,993,970,1012,1005,964],
[1003,1014,1025,0,993,1009,1019,1013,1002],
[973,995,1007,1007,0,1004,1012,988,941],
[1003,1006,1030,991,996,0,1029,1060,1003],
[1005,1004,988,981,988,971,0,984,950],
[1010,1004,995,987,1012,940,1016,0,1012],
[995,1020,1036,998,1059,997,1050,988,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 56, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1094,980,1027,1048,1016,988,1002,1064],
[906,0,939,928,943,943,936,936,998],
[1020,1061,0,1014,1030,1031,1054,982,1075],
[973,1072,986,0,963,962,945,968,1016],
[952,1057,970,1037,0,997,974,1048,1029],
[984,1057,969,1038,1003,0,1071,1033,1041],
[1012,1064,946,1055,1026,929,0,1028,1011],
[998,1064,1018,1032,952,967,972,0,1071],
[936,1002,925,984,971,959,989,929,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 57, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,970,1038,1027,1041,1009,1013,1027,977],
[1030,0,1094,1000,1008,1081,1058,1052,1023],
[962,906,0,994,939,981,950,961,924],
[973,1000,1006,0,1042,1045,988,1009,972],
[959,992,1061,958,0,988,973,980,992],
[991,919,1019,955,1012,0,937,1008,993],
[987,942,1050,1012,1027,1063,0,992,1006],
[973,948,1039,991,1020,992,1008,0,950],
[1023,977,1076,1028,1008,1007,994,1050,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 58, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,951,1012,973,960,1021,950,990,1000],
[1049,0,1034,999,1010,1016,946,1041,1079],
[988,966,0,994,1001,976,959,979,1019],
[1027,1001,1006,0,1032,1023,1000,983,1064],
[1040,990,999,968,0,1010,1024,980,1027],
[979,984,1024,977,990,0,944,998,1077],
[1050,1054,1041,1000,976,1056,0,1007,1066],
[1010,959,1021,1017,1020,1002,993,0,996],
[1000,921,981,936,973,923,934,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 59, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1010,916,890,945,1005,933,994,973],
[990,0,890,907,980,1006,936,986,929],
[1084,1110,0,1028,1002,1109,987,1013,1083],
[1110,1093,972,0,1001,1080,1064,1019,990],
[1055,1020,998,999,0,1082,1045,1075,991],
[995,994,891,920,918,0,926,982,987],
[1067,1064,1013,936,955,1074,0,1097,990],
[1006,1014,987,981,925,1018,903,0,985],
[1027,1071,917,1010,1009,1013,1010,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 60, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1039,963,976,1058,947,988,954,930],
[961,0,1028,1002,1057,1005,1049,1046,928],
[1037,972,0,1030,1018,1005,951,955,915],
[1024,998,970,0,987,966,918,949,1017],
[942,943,982,1013,0,963,990,918,917],
[1053,995,995,1034,1037,0,1027,1015,974],
[1012,951,1049,1082,1010,973,0,1018,950],
[1046,954,1045,1051,1082,985,982,0,903],
[1070,1072,1085,983,1083,1026,1050,1097,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 61, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,997,1074,1043,1029,995,990,1026,1007],
[1003,0,1075,1027,1041,1004,1029,1023,995],
[926,925,0,978,962,986,962,970,997],
[957,973,1022,0,998,982,945,984,1022],
[971,959,1038,1002,0,985,933,1028,982],
[1005,996,1014,1018,1015,0,983,976,1038],
[1010,971,1038,1055,1067,1017,0,1002,1016],
[974,977,1030,1016,972,1024,998,0,1053],
[993,1005,1003,978,1018,962,984,947,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 62, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,1024,1039,1019,1048,1028,992,1033],
[991,0,1026,988,963,1028,1066,985,974],
[976,974,0,973,971,1008,986,994,980],
[961,1012,1027,0,983,1039,1023,999,977],
[981,1037,1029,1017,0,1009,1040,988,1022],
[952,972,992,961,991,0,1006,971,955],
[972,934,1014,977,960,994,0,993,952],
[1008,1015,1006,1001,1012,1029,1007,0,995],
[967,1026,1020,1023,978,1045,1048,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 63, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,977,1026,1008,979,1004,1050,965],
[1004,0,990,1021,996,973,1001,1002,968],
[1023,1010,0,1025,990,1003,1046,1023,1048],
[974,979,975,0,1014,997,968,1006,946],
[992,1004,1010,986,0,990,1016,1043,1008],
[1021,1027,997,1003,1010,0,1010,1068,1009],
[996,999,954,1032,984,990,0,1018,1000],
[950,998,977,994,957,932,982,0,967],
[1035,1032,952,1054,992,991,1000,1033,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 64, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1038,1039,1020,1000,1006,998,1004,1020],
[962,0,1003,1014,977,938,962,953,959],
[961,997,0,999,931,972,967,998,981],
[980,986,1001,0,985,985,997,1000,990],
[1000,1023,1069,1015,0,1019,993,999,1020],
[994,1062,1028,1015,981,0,1000,1014,1013],
[1002,1038,1033,1003,1007,1000,0,1018,1044],
[996,1047,1002,1000,1001,986,982,0,1000],
[980,1041,1019,1010,980,987,956,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 65, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,934,914,1008,1146,1014,778,1054,861],
[1066,0,1169,1024,1161,1176,1011,1036,954],
[1086,831,0,1014,947,1124,871,1045,676],
[992,976,986,0,1167,1135,919,1232,954],
[854,839,1053,833,0,1026,788,846,974],
[986,824,876,865,974,0,855,986,880],
[1222,989,1129,1081,1212,1145,0,1022,1065],
[946,964,955,768,1154,1014,978,0,853],
[1139,1046,1324,1046,1026,1120,935,1147,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 66, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,983,994,993,1003,984,994,996,1023],
[1017,0,1031,991,1027,1020,1040,1036,1013],
[1006,969,0,976,989,992,996,975,1018],
[1007,1009,1024,0,993,1007,993,960,1002],
[997,973,1011,1007,0,1014,1015,999,975],
[1016,980,1008,993,986,0,984,966,991],
[1006,960,1004,1007,985,1016,0,966,979],
[1004,964,1025,1040,1001,1034,1034,0,1009],
[977,987,982,998,1025,1009,1021,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 67, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,906,874,1122,1080,1033,1172,893,1048],
[1094,0,1135,1110,1103,1101,921,888,1089],
[1126,865,0,991,838,983,792,799,1039],
[878,890,1009,0,831,1038,770,783,1042],
[920,897,1162,1169,0,1163,852,929,1116],
[967,899,1017,962,837,0,874,862,1031],
[828,1079,1208,1230,1148,1126,0,1024,996],
[1107,1112,1201,1217,1071,1138,976,0,1160],
[952,911,961,958,884,969,1004,840,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 68, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,982,916,1013,951,962,955,952,970],
[1018,0,940,1088,964,970,1009,1031,1058],
[1084,1060,0,1071,997,1002,993,1022,1092],
[987,912,929,0,909,939,922,959,1007],
[1049,1036,1003,1091,0,993,979,1006,1037],
[1038,1030,998,1061,1007,0,971,1034,1049],
[1045,991,1007,1078,1021,1029,0,1021,1066],
[1048,969,978,1041,994,966,979,0,1014],
[1030,942,908,993,963,951,934,986,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 69, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1051,990,1071,890,927,1014,937,923],
[949,0,948,983,902,856,983,932,914],
[1010,1052,0,1086,957,937,1033,929,985],
[929,1017,914,0,886,938,1000,894,912],
[1110,1098,1043,1114,0,1004,1025,996,1039],
[1073,1144,1063,1062,996,0,1016,1015,978],
[986,1017,967,1000,975,984,0,960,969],
[1063,1068,1071,1106,1004,985,1040,0,1069],
[1077,1086,1015,1088,961,1022,1031,931,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 70, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,1044,1041,1068,1091,1061,1033,1007],
[1013,0,1002,993,1004,1023,1044,1041,1003],
[956,998,0,984,1001,1011,1033,1031,965],
[959,1007,1016,0,1036,1081,995,1040,991],
[932,996,999,964,0,1050,983,1004,1007],
[909,977,989,919,950,0,937,917,948],
[939,956,967,1005,1017,1063,0,989,1013],
[967,959,969,960,996,1083,1011,0,974],
[993,997,1035,1009,993,1052,987,1026,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 71, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1008,1040,993,1004,991,999,1021,995],
[992,0,1004,989,1001,1018,1002,1021,968],
[960,996,0,974,1016,990,978,1020,987],
[1007,1011,1026,0,987,1014,998,1027,1022],
[996,999,984,1013,0,996,987,1013,1000],
[1009,982,1010,986,1004,0,998,992,968],
[1001,998,1022,1002,1013,1002,0,1020,970],
[979,979,980,973,987,1008,980,0,1007],
[1005,1032,1013,978,1000,1032,1030,993,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 72, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,959,998,1029,1017,979,969,1032,992],
[1041,0,1031,1041,1027,989,992,1017,999],
[1002,969,0,1006,1009,1012,989,1012,959],
[971,959,994,0,954,976,930,1047,972],
[983,973,991,1046,0,997,961,1005,989],
[1021,1011,988,1024,1003,0,1025,1080,965],
[1031,1008,1011,1070,1039,975,0,1044,1005],
[968,983,988,953,995,920,956,0,995],
[1008,1001,1041,1028,1011,1035,995,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 73, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,964,978,995,980,951,996,970,956],
[1036,0,1012,1018,1003,1030,1010,979,978],
[1022,988,0,1007,972,977,998,994,981],
[1005,982,993,0,961,984,1016,953,1017],
[1020,997,1028,1039,0,998,1028,979,1009],
[1049,970,1023,1016,1002,0,997,993,989],
[1004,990,1002,984,972,1003,0,965,1011],
[1030,1021,1006,1047,1021,1007,1035,0,994],
[1044,1022,1019,983,991,1011,989,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 74, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1120,1268,988,976,833,1000,1166,1009],
[880,0,1076,922,1007,1024,794,1130,1034],
[732,924,0,1012,887,857,1062,1232,906],
[1012,1078,988,0,1013,1057,993,1089,974],
[1024,993,1113,987,0,990,941,1294,1082],
[1167,976,1143,943,1010,0,965,1145,962],
[1000,1206,938,1007,1059,1035,0,1196,987],
[834,870,768,911,706,855,804,0,855],
[991,966,1094,1026,918,1038,1013,1145,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 75, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,1005,1034,961,938,996,972,962],
[976,0,1105,1084,935,990,1046,990,998],
[995,895,0,982,948,954,1017,955,897],
[966,916,1018,0,924,924,969,946,918],
[1039,1065,1052,1076,0,1025,1054,985,1082],
[1062,1010,1046,1076,975,0,1091,1036,1017],
[1004,954,983,1031,946,909,0,1000,948],
[1028,1010,1045,1054,1015,964,1000,0,1081],
[1038,1002,1103,1082,918,983,1052,919,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 76, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,981,938,923,966,1015,999,932,987],
[1019,0,968,974,976,1048,1033,989,1034],
[1062,1032,0,961,1018,1039,1035,982,1007],
[1077,1026,1039,0,993,1054,1053,974,1021],
[1034,1024,982,1007,0,1052,1024,956,1026],
[985,952,961,946,948,0,996,947,991],
[1001,967,965,947,976,1004,0,962,974],
[1068,1011,1018,1026,1044,1053,1038,0,998],
[1013,966,993,979,974,1009,1026,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 77, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,1004,1022,1003,1036,1013,986,1028],
[976,0,969,982,964,990,997,968,982],
[996,1031,0,1032,968,1003,972,972,998],
[978,1018,968,0,962,990,1000,985,1005],
[997,1036,1032,1038,0,1020,1011,1002,1037],
[964,1010,997,1010,980,0,971,945,1015],
[987,1003,1028,1000,989,1029,0,1005,1012],
[1014,1032,1028,1015,998,1055,995,0,1040],
[972,1018,1002,995,963,985,988,960,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 78, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1031,1084,981,1017,1012,1028,1026,1046],
[969,0,1041,1004,1043,1029,1019,1019,995],
[916,959,0,945,1012,958,981,961,903],
[1019,996,1055,0,1036,1029,979,997,986],
[983,957,988,964,0,992,962,975,965],
[988,971,1042,971,1008,0,970,985,1003],
[972,981,1019,1021,1038,1030,0,1021,1003],
[974,981,1039,1003,1025,1015,979,0,1029],
[954,1005,1097,1014,1035,997,997,971,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 79, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,832,1123,780,891,693,995,906,1048],
[1168,0,992,1073,1247,1140,1279,1024,1316],
[877,1008,0,964,929,759,1125,1127,1099],
[1220,927,1036,0,1033,733,1072,1020,1332],
[1109,753,1071,967,0,919,1222,1047,1267],
[1307,860,1241,1267,1081,0,1352,1083,1210],
[1005,721,875,928,778,648,0,890,1096],
[1094,976,873,980,953,917,1110,0,1245],
[952,684,901,668,733,790,904,755,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 80, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,953,1058,976,1035,1058,1028,982,980],
[1047,0,1115,1022,1054,1070,1021,959,950],
[942,885,0,896,931,930,954,967,885],
[1024,978,1104,0,1054,988,973,963,971],
[965,946,1069,946,0,959,992,930,991],
[942,930,1070,1012,1041,0,977,979,977],
[972,979,1046,1027,1008,1023,0,917,1019],
[1018,1041,1033,1037,1070,1021,1083,0,945],
[1020,1050,1115,1029,1009,1023,981,1055,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 81, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,1013,998,1031,973,942,1021,1059],
[986,0,1035,1001,1030,941,900,1019,1051],
[987,965,0,998,1025,935,1001,1030,1032],
[1002,999,1002,0,963,910,944,997,1050],
[969,970,975,1037,0,940,942,979,1008],
[1027,1059,1065,1090,1060,0,1049,988,1082],
[1058,1100,999,1056,1058,951,0,1056,1050],
[979,981,970,1003,1021,1012,944,0,1034],
[941,949,968,950,992,918,950,966,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 82, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1027,1103,1016,965,1032,1002,1068,1022],
[973,0,1031,1019,953,1040,973,1032,949],
[897,969,0,949,904,1003,899,1031,923],
[984,981,1051,0,1003,1035,960,1056,976],
[1035,1047,1096,997,0,1092,1009,1022,1011],
[968,960,997,965,908,0,974,1017,945],
[998,1027,1101,1040,991,1026,0,1118,1025],
[932,968,969,944,978,983,882,0,876],
[978,1051,1077,1024,989,1055,975,1124,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 83, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,963,1023,962,992,986,1012,919,988],
[1037,0,1003,970,905,973,977,943,948],
[977,997,0,977,957,960,1055,962,990],
[1038,1030,1023,0,932,1004,999,928,931],
[1008,1095,1043,1068,0,982,1011,1006,962],
[1014,1027,1040,996,1018,0,969,907,931],
[988,1023,945,1001,989,1031,0,928,970],
[1081,1057,1038,1072,994,1093,1072,0,1122],
[1012,1052,1010,1069,1038,1069,1030,878,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 84, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,1011,1015,998,1039,1020,997,995],
[1002,0,1018,988,1012,1026,1056,975,1007],
[989,982,0,971,962,1015,1013,990,970],
[985,1012,1029,0,999,1035,1025,1015,995],
[1002,988,1038,1001,0,1040,1031,1020,1001],
[961,974,985,965,960,0,1005,990,974],
[980,944,987,975,969,995,0,962,954],
[1003,1025,1010,985,980,1010,1038,0,987],
[1005,993,1030,1005,999,1026,1046,1013,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 85, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1081,1016,1041,1009,1054,1016,1030,981],
[919,0,1012,938,1011,1023,949,1015,956],
[984,988,0,1029,1076,1085,1026,1017,985],
[959,1062,971,0,1007,1012,913,1000,1011],
[991,989,924,993,0,1028,1012,982,995],
[946,977,915,988,972,0,916,994,942],
[984,1051,974,1087,988,1084,0,1085,1000],
[970,985,983,1000,1018,1006,915,0,907],
[1019,1044,1015,989,1005,1058,1000,1093,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 86, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,1013,993,1092,1000,984,1037,1014],
[987,0,997,1020,1062,991,1031,1052,1033],
[987,1003,0,1006,1053,1005,992,1028,981],
[1007,980,994,0,1046,1021,1013,1026,1011],
[908,938,947,954,0,983,988,1028,974],
[1000,1009,995,979,1017,0,1046,995,990],
[1016,969,1008,987,1012,954,0,1008,968],
[963,948,972,974,972,1005,992,0,960],
[986,967,1019,989,1026,1010,1032,1040,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 87, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1031,1014,1009,1030,1010,991,1051,1034],
[969,0,993,983,987,1018,977,1013,1044],
[986,1007,0,1023,1024,1011,1010,1061,1056],
[991,1017,977,0,1011,1005,977,1053,1025],
[970,1013,976,989,0,1018,965,1039,1061],
[990,982,989,995,982,0,955,1032,993],
[1009,1023,990,1023,1035,1045,0,1046,1073],
[949,987,939,947,961,968,954,0,1034],
[966,956,944,975,939,1007,927,966,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 88, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,1031,1033,1001,1012,975,1026,1029],
[987,0,1004,1016,1001,993,979,1014,997],
[969,996,0,1004,989,986,991,1025,1034],
[967,984,996,0,973,957,983,986,1014],
[999,999,1011,1027,0,990,999,1011,1026],
[988,1007,1014,1043,1010,0,1003,1013,1028],
[1025,1021,1009,1017,1001,997,0,1019,1051],
[974,986,975,1014,989,987,981,0,985],
[971,1003,966,986,974,972,949,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 89, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,981,1029,964,950,931,1002,889,1042],
[1019,0,955,913,905,924,1026,953,1004],
[971,1045,0,990,961,1046,1047,951,990],
[1036,1087,1010,0,981,1006,1051,1038,1028],
[1050,1095,1039,1019,0,1049,1033,996,1016],
[1069,1076,954,994,951,0,942,954,996],
[998,974,953,949,967,1058,0,935,958],
[1111,1047,1049,962,1004,1046,1065,0,1003],
[958,996,1010,972,984,1004,1042,997,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 90, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,911,896,874,633,849,744,826,625],
[1089,0,1211,900,944,908,768,1039,1027],
[1104,789,0,1193,1180,1103,733,921,1265],
[1126,1100,807,0,749,838,813,997,862],
[1367,1056,820,1251,0,1372,928,1044,1061],
[1151,1092,897,1162,628,0,845,898,754],
[1256,1232,1267,1187,1072,1155,0,997,1040],
[1174,961,1079,1003,956,1102,1003,0,1271],
[1375,973,735,1138,939,1246,960,729,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 91, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,965,996,1043,978,1021,993,950,1019],
[1035,0,1057,1064,1015,1013,1020,954,1023],
[1004,943,0,1020,954,999,900,1005,1023],
[957,936,980,0,986,1017,905,972,979],
[1022,985,1046,1014,0,991,968,949,1014],
[979,987,1001,983,1009,0,965,985,1007],
[1007,980,1100,1095,1032,1035,0,998,1065],
[1050,1046,995,1028,1051,1015,1002,0,1016],
[981,977,977,1021,986,993,935,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 92, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1033,1035,1025,1023,1001,961,1006,1024],
[967,0,1006,1014,968,1020,996,1009,1002],
[965,994,0,976,999,995,979,994,995],
[975,986,1024,0,991,1014,992,1012,996],
[977,1032,1001,1009,0,1029,993,1010,1010],
[999,980,1005,986,971,0,964,975,1014],
[1039,1004,1021,1008,1007,1036,0,992,1067],
[994,991,1006,988,990,1025,1008,0,991],
[976,998,1005,1004,990,986,933,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 93, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,959,984,1006,995,955,1006,982,1026],
[1041,0,1025,1018,1005,1004,1000,1017,1003],
[1016,975,0,1022,998,1005,1007,998,1043],
[994,982,978,0,982,982,959,974,981],
[1005,995,1002,1018,0,986,976,982,991],
[1045,996,995,1018,1014,0,1016,999,997],
[994,1000,993,1041,1024,984,0,1005,1006],
[1018,983,1002,1026,1018,1001,995,0,1005],
[974,997,957,1019,1009,1003,994,995,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 94, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1025,1027,986,1029,1013,999,983,986],
[975,0,980,973,999,973,977,980,957],
[973,1020,0,982,1029,983,977,975,986],
[1014,1027,1018,0,1025,993,992,988,983],
[971,1001,971,975,0,991,956,959,948],
[987,1027,1017,1007,1009,0,995,971,957],
[1001,1023,1023,1008,1044,1005,0,1005,986],
[1017,1020,1025,1012,1041,1029,995,0,1009],
[1014,1043,1014,1017,1052,1043,1014,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 95, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,940,1003,972,1009,941,987,971,984],
[1060,0,1023,1005,1046,1004,988,1048,1004],
[997,977,0,976,988,957,964,998,986],
[1028,995,1024,0,1047,999,1003,1001,1014],
[991,954,1012,953,0,963,969,969,979],
[1059,996,1043,1001,1037,0,1043,1070,1056],
[1013,1012,1036,997,1031,957,0,1022,1059],
[1029,952,1002,999,1031,930,978,0,1045],
[1016,996,1014,986,1021,944,941,955,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 96, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,1054,979,1020,1032,978,998,999],
[1008,0,1025,998,1064,1050,1008,1060,951],
[946,975,0,985,1006,997,970,984,967],
[1021,1002,1015,0,1035,998,992,981,994],
[980,936,994,965,0,1049,972,1014,970],
[968,950,1003,1002,951,0,957,1017,938],
[1022,992,1030,1008,1028,1043,0,1011,1023],
[1002,940,1016,1019,986,983,989,0,968],
[1001,1049,1033,1006,1030,1062,977,1032,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 97, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1000,1067,1051,985,1076,1032,1010,1042],
[1000,0,1058,1072,995,1067,1011,989,1029],
[933,942,0,994,971,1009,938,964,940],
[949,928,1006,0,982,1018,1007,975,986],
[1015,1005,1029,1018,0,1026,997,1001,997],
[924,933,991,982,974,0,985,965,984],
[968,989,1062,993,1003,1015,0,989,1028],
[990,1011,1036,1025,999,1035,1011,0,1014],
[958,971,1060,1014,1003,1016,972,986,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 98, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,973,1002,1058,992,981,1002,1045,1007],
[1027,0,1022,1063,1035,991,1006,1037,1007],
[998,978,0,1045,986,1004,1010,1033,1016],
[942,937,955,0,951,932,950,986,953],
[1008,965,1014,1049,0,961,999,1028,1027],
[1019,1009,996,1068,1039,0,974,1034,1033],
[998,994,990,1050,1001,1026,0,1001,1020],
[955,963,967,1014,972,966,999,0,999],
[993,993,984,1047,973,967,980,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 99, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,969,962,968,998,940,966,943,957],
[1031,0,978,1033,1006,1014,962,991,989],
[1038,1022,0,1032,1005,1005,971,1002,996],
[1032,967,968,0,983,1002,977,944,980],
[1002,994,995,1017,0,1018,981,953,979],
[1060,986,995,998,982,0,963,984,966],
[1034,1038,1029,1023,1019,1037,0,987,1023],
[1057,1009,998,1056,1047,1016,1013,0,1023],
[1043,1011,1004,1020,1021,1034,977,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 100, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,959,981,982,969,1016,915,997,1019],
[1041,0,1049,1002,973,1037,1022,1075,1052],
[1019,951,0,1001,1002,989,953,1018,1027],
[1018,998,999,0,991,1013,975,1042,1015],
[1031,1027,998,1009,0,1031,989,1044,1029],
[984,963,1011,987,969,0,940,1016,1017],
[1085,978,1047,1025,1011,1060,0,1087,1068],
[1003,925,982,958,956,984,913,0,998],
[981,948,973,985,971,983,932,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 101, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,1023,961,1030,967,997,1008,964],
[997,0,1021,995,985,981,1028,1044,959],
[977,979,0,975,974,948,1015,984,930],
[1039,1005,1025,0,1050,988,1032,1036,972],
[970,1015,1026,950,0,1018,992,1006,1003],
[1033,1019,1052,1012,982,0,1053,1057,968],
[1003,972,985,968,1008,947,0,1010,961],
[992,956,1016,964,994,943,990,0,968],
[1036,1041,1070,1028,997,1032,1039,1032,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 102, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,948,961,957,992,941,995,993,974],
[1052,0,973,1024,1010,1010,1076,1045,1015],
[1039,1027,0,1008,985,1023,1025,1041,980],
[1043,976,992,0,1040,971,1029,1027,1023],
[1008,990,1015,960,0,975,995,1018,1022],
[1059,990,977,1029,1025,0,1025,1000,1000],
[1005,924,975,971,1005,975,0,998,974],
[1007,955,959,973,982,1000,1002,0,982],
[1026,985,1020,977,978,1000,1026,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 103, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1116,1123,1004,1107,993,1050,1129,994],
[884,0,1025,838,976,925,947,1022,1002],
[877,975,0,855,937,1026,973,932,1008],
[996,1162,1145,0,1030,1123,1116,1103,1113],
[893,1024,1063,970,0,1006,992,1018,1031],
[1007,1075,974,877,994,0,1004,1029,1033],
[950,1053,1027,884,1008,996,0,934,1064],
[871,978,1068,897,982,971,1066,0,1006],
[1006,998,992,887,969,967,936,994,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 104, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,930,1034,1012,1042,1038,1068,1036,985],
[1070,0,1038,1067,1131,1089,1158,996,1092],
[966,962,0,966,978,976,1015,1048,1016],
[988,933,1034,0,1019,972,1063,1065,1046],
[958,869,1022,981,0,968,1052,1014,1001],
[962,911,1024,1028,1032,0,1110,983,1065],
[932,842,985,937,948,890,0,893,990],
[964,1004,952,935,986,1017,1107,0,1044],
[1015,908,984,954,999,935,1010,956,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 105, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,953,881,1004,987,985,1008,933,982],
[1047,0,936,1018,1001,1003,987,960,1003],
[1119,1064,0,1008,1081,989,1049,1045,1068],
[996,982,992,0,997,986,1032,964,989],
[1013,999,919,1003,0,948,986,990,947],
[1015,997,1011,1014,1052,0,1078,996,985],
[992,1013,951,968,1014,922,0,898,960],
[1067,1040,955,1036,1010,1004,1102,0,988],
[1018,997,932,1011,1053,1015,1040,1012,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 106, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1033,1033,1003,998,1065,986,1014,1006],
[967,0,996,972,969,986,960,1004,1005],
[967,1004,0,964,1001,1017,990,976,938],
[997,1028,1036,0,1003,1012,999,1006,1011],
[1002,1031,999,997,0,1019,996,1029,1027],
[935,1014,983,988,981,0,959,1014,942],
[1014,1040,1010,1001,1004,1041,0,1028,980],
[986,996,1024,994,971,986,972,0,976],
[994,995,1062,989,973,1058,1020,1024,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 107, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,1037,1037,1072,1038,1002,979,1090],
[976,0,1023,1023,1077,1045,1041,964,1049],
[963,977,0,971,1023,935,962,958,1051],
[963,977,1029,0,1087,1097,1070,1033,1043],
[928,923,977,913,0,955,969,926,985],
[962,955,1065,903,1045,0,1048,959,998],
[998,959,1038,930,1031,952,0,931,992],
[1021,1036,1042,967,1074,1041,1069,0,1021],
[910,951,949,957,1015,1002,1008,979,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 108, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,964,1011,977,976,972,955,1009,998],
[1036,0,995,998,1028,991,981,997,977],
[989,1005,0,1004,1013,1015,976,1018,999],
[1023,1002,996,0,1019,974,1001,1000,982],
[1024,972,987,981,0,999,960,1005,980],
[1028,1009,985,1026,1001,0,992,1009,981],
[1045,1019,1024,999,1040,1008,0,996,1023],
[991,1003,982,1000,995,991,1004,0,1002],
[1002,1023,1001,1018,1020,1019,977,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 109, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,933,971,997,960,919,1027,945],
[1021,0,935,1011,968,988,972,1091,1037],
[1067,1065,0,1087,996,1090,1063,1120,1025],
[1029,989,913,0,979,1016,941,1035,973],
[1003,1032,1004,1021,0,1084,973,1049,1050],
[1040,1012,910,984,916,0,930,1009,968],
[1081,1028,937,1059,1027,1070,0,1095,1030],
[973,909,880,965,951,991,905,0,954],
[1055,963,975,1027,950,1032,970,1046,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 110, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,1040,1018,1039,1036,1076,1007,988],
[1002,0,909,890,1031,966,1013,958,948],
[960,1091,0,1017,1026,1062,1044,1037,993],
[982,1110,983,0,1047,1050,1069,1003,971],
[961,969,974,953,0,935,969,952,969],
[964,1034,938,950,1065,0,1044,991,1001],
[924,987,956,931,1031,956,0,949,955],
[993,1042,963,997,1048,1009,1051,0,940],
[1012,1052,1007,1029,1031,999,1045,1060,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 111, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1039,1043,1003,1024,981,1008,1005,1015],
[961,0,1034,970,1032,976,977,992,977],
[957,966,0,971,982,981,978,1016,985],
[997,1030,1029,0,1042,997,1021,1029,997],
[976,968,1018,958,0,940,956,994,945],
[1019,1024,1019,1003,1060,0,979,1038,987],
[992,1023,1022,979,1044,1021,0,1030,1036],
[995,1008,984,971,1006,962,970,0,998],
[985,1023,1015,1003,1055,1013,964,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 112, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,998,994,977,986,1007,1009,978],
[987,0,986,984,987,981,996,991,977],
[1002,1014,0,1000,1034,1014,1032,1037,1030],
[1006,1016,1000,0,993,1010,989,1023,1018],
[1023,1013,966,1007,0,1018,1008,999,1023],
[1014,1019,986,990,982,0,1023,1003,1031],
[993,1004,968,1011,992,977,0,1038,999],
[991,1009,963,977,1001,997,962,0,986],
[1022,1023,970,982,977,969,1001,1014,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 113, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,1036,956,999,1005,991,965,976],
[994,0,1040,1016,1027,1019,985,968,1057],
[964,960,0,943,981,971,1004,938,1021],
[1044,984,1057,0,1061,1012,1018,1018,1098],
[1001,973,1019,939,0,1007,1007,960,1006],
[995,981,1029,988,993,0,1008,994,997],
[1009,1015,996,982,993,992,0,953,1005],
[1035,1032,1062,982,1040,1006,1047,0,1040],
[1024,943,979,902,994,1003,995,960,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 114, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1008,1031,1026,1001,982,1013,991,1016],
[992,0,998,977,966,956,941,988,972],
[969,1002,0,963,974,986,1007,1001,977],
[974,1023,1037,0,978,963,961,976,1000],
[999,1034,1026,1022,0,1013,976,1017,998],
[1018,1044,1014,1037,987,0,1015,1010,1042],
[987,1059,993,1039,1024,985,0,1022,1014],
[1009,1012,999,1024,983,990,978,0,1000],
[984,1028,1023,1000,1002,958,986,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 115, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,992,1003,974,996,984,1038,988],
[1012,0,997,1027,996,1018,1002,1041,1003],
[1008,1003,0,1015,996,1012,969,1037,990],
[997,973,985,0,986,1015,965,1012,977],
[1026,1004,1004,1014,0,999,985,1066,1010],
[1004,982,988,985,1001,0,993,1017,1010],
[1016,998,1031,1035,1015,1007,0,1061,1021],
[962,959,963,988,934,983,939,0,936],
[1012,997,1010,1023,990,990,979,1064,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 116, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,902,1024,934,963,935,934,934,937],
[1098,0,1019,1021,1000,1006,1039,1005,950],
[976,981,0,1002,947,932,967,990,913],
[1066,979,998,0,1041,971,1031,987,957],
[1037,1000,1053,959,0,988,1007,1000,1000],
[1065,994,1068,1029,1012,0,1038,1041,955],
[1066,961,1033,969,993,962,0,925,971],
[1066,995,1010,1013,1000,959,1075,0,981],
[1063,1050,1087,1043,1000,1045,1029,1019,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 117, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,995,1067,1000,1018,1076,1058,1007,1044],
[1005,0,1044,1004,994,1030,1012,1006,1032],
[933,956,0,957,979,1038,969,982,1002],
[1000,996,1043,0,1033,1093,1025,991,1033],
[982,1006,1021,967,0,1056,1027,979,983],
[924,970,962,907,944,0,962,939,987],
[942,988,1031,975,973,1038,0,937,1015],
[993,994,1018,1009,1021,1061,1063,0,1002],
[956,968,998,967,1017,1013,985,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 118, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,970,911,958,890,948,1006,852,951],
[1030,0,979,1037,1005,984,1023,992,1001],
[1089,1021,0,1008,1025,975,1080,982,983],
[1042,963,992,0,959,891,991,935,952],
[1110,995,975,1041,0,1061,1037,993,1054],
[1052,1016,1025,1109,939,0,1081,1014,969],
[994,977,920,1009,963,919,0,928,985],
[1148,1008,1018,1065,1007,986,1072,0,1047],
[1049,999,1017,1048,946,1031,1015,953,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 119, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,978,990,989,992,990,1010,1033,978],
[1022,0,1008,993,1022,1018,998,1015,1014],
[1010,992,0,989,1020,1027,1032,1001,1023],
[1011,1007,1011,0,1020,991,1033,1036,1020],
[1008,978,980,980,0,988,1022,1028,1000],
[1010,982,973,1009,1012,0,1023,1019,1021],
[990,1002,968,967,978,977,0,991,998],
[967,985,999,964,972,981,1009,0,978],
[1022,986,977,980,1000,979,1002,1022,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 120, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,962,991,1016,992,984,1013,993],
[1007,0,988,1017,1023,1008,985,1021,971],
[1038,1012,0,1015,1022,980,967,996,967],
[1009,983,985,0,991,975,956,988,981],
[984,977,978,1009,0,971,980,965,968],
[1008,992,1020,1025,1029,0,976,1007,979],
[1016,1015,1033,1044,1020,1024,0,982,981],
[987,979,1004,1012,1035,993,1018,0,1007],
[1007,1029,1033,1019,1032,1021,1019,993,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 121, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1030,1039,1049,996,1045,1032,1037,1013],
[970,0,1047,1038,1008,1026,994,1007,1004],
[961,953,0,1019,948,983,987,949,989],
[951,962,981,0,983,1003,1010,940,956],
[1004,992,1052,1017,0,1037,1052,1009,1017],
[955,974,1017,997,963,0,993,993,998],
[968,1006,1013,990,948,1007,0,1005,979],
[963,993,1051,1060,991,1007,995,0,956],
[987,996,1011,1044,983,1002,1021,1044,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 122, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1093,1029,1038,1157,1027,1031,879,1077],
[907,0,876,816,962,835,955,765,947],
[971,1124,0,1022,1015,944,935,827,1099],
[962,1184,978,0,1031,857,958,915,1149],
[843,1038,985,969,0,752,872,858,1016],
[973,1165,1056,1143,1248,0,1023,1022,1324],
[969,1045,1065,1042,1128,977,0,811,1024],
[1121,1235,1173,1085,1142,978,1189,0,1198],
[923,1053,901,851,984,676,976,802,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 123, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,944,1146,1325,950,893,1050,1238],
[988,0,1075,1088,986,979,1043,1064,1358],
[1056,925,0,1265,1481,968,1127,1449,1325],
[854,912,735,0,1244,726,801,943,985],
[675,1014,519,756,0,567,584,604,841],
[1050,1021,1032,1274,1433,0,908,989,1353],
[1107,957,873,1199,1416,1092,0,1109,1091],
[950,936,551,1057,1396,1011,891,0,1054],
[762,642,675,1015,1159,647,909,946,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 124, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,983,972,982,991,972,966,1003,992],
[1017,0,996,982,1008,994,993,1019,998],
[1028,1004,0,996,1004,1006,1019,1003,987],
[1018,1018,1004,0,1000,1009,990,981,979],
[1009,992,996,1000,0,985,995,976,1010],
[1028,1006,994,991,1015,0,1003,1007,960],
[1034,1007,981,1010,1005,997,0,978,968],
[997,981,997,1019,1024,993,1022,0,984],
[1008,1002,1013,1021,990,1040,1032,1016,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 125, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,967,1013,927,973,946,1001,1015,954],
[1033,0,1035,1030,1054,1070,1010,1109,941],
[987,965,0,1018,990,1026,966,1048,955],
[1073,970,982,0,1005,1014,946,979,922],
[1027,946,1010,995,0,999,998,1073,989],
[1054,930,974,986,1001,0,992,1025,948],
[999,990,1034,1054,1002,1008,0,1029,1021],
[985,891,952,1021,927,975,971,0,883],
[1046,1059,1045,1078,1011,1052,979,1117,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 126, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,1032,999,1043,1025,1023,1018,1014],
[1004,0,1026,1018,1012,987,995,942,971],
[968,974,0,974,990,995,1001,941,1004],
[1001,982,1026,0,1032,1004,977,995,988],
[957,988,1010,968,0,943,920,965,959],
[975,1013,1005,996,1057,0,990,950,989],
[977,1005,999,1023,1080,1010,0,1004,987],
[982,1058,1059,1005,1035,1050,996,0,1012],
[986,1029,996,1012,1041,1011,1013,988,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 127, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,995,1008,1002,988,1025,980,1056,1021],
[1005,0,988,1010,975,979,1008,989,1015],
[992,1012,0,1040,1032,990,998,1033,1032],
[998,990,960,0,991,969,988,996,1017],
[1012,1025,968,1009,0,983,998,967,1030],
[975,1021,1010,1031,1017,0,1018,1011,1019],
[1020,992,1002,1012,1002,982,0,990,1002],
[944,1011,967,1004,1033,989,1010,0,1002],
[979,985,968,983,970,981,998,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 128, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1077,1013,1009,989,1009,976,970,997],
[923,0,893,1017,979,930,931,883,950],
[987,1107,0,1005,1035,1015,1029,1001,1053],
[991,983,995,0,997,972,997,951,965],
[1011,1021,965,1003,0,977,968,948,1006],
[991,1070,985,1028,1023,0,981,1001,999],
[1024,1069,971,1003,1032,1019,0,972,1024],
[1030,1117,999,1049,1052,999,1028,0,1099],
[1003,1050,947,1035,994,1001,976,901,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 129, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,960,1031,943,1037,1024,1022,984],
[993,0,980,1066,954,1045,1014,1000,1021],
[1040,1020,0,1041,1000,1041,1049,1046,1042],
[969,934,959,0,966,924,994,1022,992],
[1057,1046,1000,1034,0,1024,1038,1025,1020],
[963,955,959,1076,976,0,1038,1066,1006],
[976,986,951,1006,962,962,0,1050,959],
[978,1000,954,978,975,934,950,0,982],
[1016,979,958,1008,980,994,1041,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 130, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,1016,1019,1019,988,995,999,974],
[976,0,997,962,989,952,956,965,950],
[984,1003,0,1012,1014,1009,1000,1049,959],
[981,1038,988,0,1053,996,997,1024,975],
[981,1011,986,947,0,958,970,971,954],
[1012,1048,991,1004,1042,0,1021,1082,1009],
[1005,1044,1000,1003,1030,979,0,1038,967],
[1001,1035,951,976,1029,918,962,0,935],
[1026,1050,1041,1025,1046,991,1033,1065,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 131, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1025,1004,1016,1030,1022,1018,1023,962],
[975,0,1019,1016,990,1004,1048,1013,1000],
[996,981,0,1024,1024,1028,1033,1005,993],
[984,984,976,0,1019,971,1005,1033,941],
[970,1010,976,981,0,970,1045,1005,970],
[978,996,972,1029,1030,0,1050,1044,1014],
[982,952,967,995,955,950,0,958,968],
[977,987,995,967,995,956,1042,0,962],
[1038,1000,1007,1059,1030,986,1032,1038,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 132, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,997,1050,1032,993,1045,1042,935,1012],
[1003,0,1040,988,1034,971,988,979,1059],
[950,960,0,950,979,970,1018,948,984],
[968,1012,1050,0,969,1033,1036,989,986],
[1007,966,1021,1031,0,986,991,1010,1028],
[955,1029,1030,967,1014,0,997,926,1054],
[958,1012,982,964,1009,1003,0,944,1039],
[1065,1021,1052,1011,990,1074,1056,0,1054],
[988,941,1016,1014,972,946,961,946,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 133, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,1013,1002,978,992,988,1003,1019],
[993,0,991,1007,922,1033,1034,1006,982],
[987,1009,0,1029,1046,1017,1032,1059,1013],
[998,993,971,0,960,985,1014,1005,947],
[1022,1078,954,1040,0,1004,1027,1030,984],
[1008,967,983,1015,996,0,985,995,957],
[1012,966,968,986,973,1015,0,1030,964],
[997,994,941,995,970,1005,970,0,990],
[981,1018,987,1053,1016,1043,1036,1010,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 134, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1032,1009,981,986,1018,989,991,1060],
[968,0,963,967,1075,1079,1033,1012,1138],
[991,1037,0,977,989,1054,1011,1022,1016],
[1019,1033,1023,0,995,961,964,1069,1025],
[1014,925,1011,1005,0,1079,1028,978,980],
[982,921,946,1039,921,0,983,892,964],
[1011,967,989,1036,972,1017,0,1014,1021],
[1009,988,978,931,1022,1108,986,0,1026],
[940,862,984,975,1020,1036,979,974,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 135, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1051,1027,1003,1028,915,943,1064,960],
[949,0,1019,1004,1007,912,1003,954,989],
[973,981,0,965,952,948,949,946,939],
[997,996,1035,0,1040,985,1031,1009,945],
[972,993,1048,960,0,969,936,1023,964],
[1085,1088,1052,1015,1031,0,971,1024,957],
[1057,997,1051,969,1064,1029,0,1055,1013],
[936,1046,1054,991,977,976,945,0,964],
[1040,1011,1061,1055,1036,1043,987,1036,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 136, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,1013,1018,1040,1018,1005,1037,1030],
[1006,0,1006,971,1021,987,997,1018,971],
[987,994,0,999,1040,971,983,1007,1022],
[982,1029,1001,0,1046,975,996,1000,1029],
[960,979,960,954,0,950,984,966,982],
[982,1013,1029,1025,1050,0,1034,1018,1011],
[995,1003,1017,1004,1016,966,0,999,1014],
[963,982,993,1000,1034,982,1001,0,990],
[970,1029,978,971,1018,989,986,1010,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 137, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1131,1022,907,1052,1185,935,1100,982],
[869,0,951,856,949,1060,987,1042,1043],
[978,1049,0,1011,1012,1057,952,1137,1037],
[1093,1144,989,0,977,1117,960,1076,1043],
[948,1051,988,1023,0,1097,1040,1146,1104],
[815,940,943,883,903,0,974,1007,903],
[1065,1013,1048,1040,960,1026,0,1132,1010],
[900,958,863,924,854,993,868,0,954],
[1018,957,963,957,896,1097,990,1046,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 138, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,967,1035,985,1024,1004,1000,955,978],
[1033,0,1039,1000,1029,1036,1040,986,1043],
[965,961,0,983,984,985,968,980,1014],
[1015,1000,1017,0,1033,1003,1005,1014,1036],
[976,971,1016,967,0,969,994,1013,1009],
[996,964,1015,997,1031,0,1002,998,1024],
[1000,960,1032,995,1006,998,0,983,999],
[1045,1014,1020,986,987,1002,1017,0,1021],
[1022,957,986,964,991,976,1001,979,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 139, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1113,1002,1010,976,1086,1098,1002,1043],
[887,0,983,926,970,974,940,983,966],
[998,1017,0,971,1028,1030,985,1040,1057],
[990,1074,1029,0,1028,1036,1072,1039,1068],
[1024,1030,972,972,0,1012,977,1020,910],
[914,1026,970,964,988,0,989,934,990],
[902,1060,1015,928,1023,1011,0,974,992],
[998,1017,960,961,980,1066,1026,0,1041],
[957,1034,943,932,1090,1010,1008,959,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 140, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,995,1001,994,983,1019,1013,1010],
[989,0,994,952,991,982,1006,952,982],
[1005,1006,0,994,1023,984,1038,984,1018],
[999,1048,1006,0,995,999,1028,1022,968],
[1006,1009,977,1005,0,1008,1022,1006,970],
[1017,1018,1016,1001,992,0,1049,1019,981],
[981,994,962,972,978,951,0,994,966],
[987,1048,1016,978,994,981,1006,0,991],
[990,1018,982,1032,1030,1019,1034,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 141, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1026,976,1056,1012,1017,995,1040,978],
[974,0,1006,1011,1006,1023,1038,1005,1006],
[1024,994,0,999,1025,1053,1041,1030,1004],
[944,989,1001,0,994,980,959,947,927],
[988,994,975,1006,0,961,1003,984,957],
[983,977,947,1020,1039,0,994,991,951],
[1005,962,959,1041,997,1006,0,983,956],
[960,995,970,1053,1016,1009,1017,0,980],
[1022,994,996,1073,1043,1049,1044,1020,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 142, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1021,995,1004,991,1006,994,1046,1003],
[979,0,965,1001,1005,995,999,1024,970],
[1005,1035,0,987,1000,1001,976,1013,975],
[996,999,1013,0,992,1024,990,1055,984],
[1009,995,1000,1008,0,1019,1051,1037,1002],
[994,1005,999,976,981,0,970,1010,951],
[1006,1001,1024,1010,949,1030,0,1046,990],
[954,976,987,945,963,990,954,0,912],
[997,1030,1025,1016,998,1049,1010,1088,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 143, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,951,963,970,988,959,982,993],
[1021,0,971,981,974,994,967,983,1013],
[1049,1029,0,1065,1031,1022,990,1004,1000],
[1037,1019,935,0,952,948,987,1026,975],
[1030,1026,969,1048,0,1009,1014,1006,977],
[1012,1006,978,1052,991,0,988,983,996],
[1041,1033,1010,1013,986,1012,0,986,994],
[1018,1017,996,974,994,1017,1014,0,1010],
[1007,987,1000,1025,1023,1004,1006,990,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 144, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,965,981,1063,1070,1017,1066,1112,1002],
[1035,0,1034,1104,1031,1003,1127,1007,972],
[1019,966,0,968,1028,986,1131,1009,977],
[937,896,1032,0,909,1019,1031,956,922],
[930,969,972,1091,0,1037,1056,1012,1011],
[983,997,1014,981,963,0,1021,1069,928],
[934,873,869,969,944,979,0,915,967],
[888,993,991,1044,988,931,1085,0,1005],
[998,1028,1023,1078,989,1072,1033,995,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 145, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,945,958,966,987,979,990,946,983],
[1055,0,995,1000,1021,992,988,978,1015],
[1042,1005,0,997,1083,1027,1030,1027,1006],
[1034,1000,1003,0,1031,1035,994,1027,1017],
[1013,979,917,969,0,992,984,975,967],
[1021,1008,973,965,1008,0,997,974,1002],
[1010,1012,970,1006,1016,1003,0,937,1012],
[1054,1022,973,973,1025,1026,1063,0,1019],
[1017,985,994,983,1033,998,988,981,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 146, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1035,984,1019,1051,1062,1032,1032,1027],
[965,0,1025,982,1029,1039,1017,1074,1025],
[1016,975,0,1008,981,1047,1057,1060,977],
[981,1018,992,0,1048,1037,1030,1096,991],
[949,971,1019,952,0,1027,997,1055,981],
[938,961,953,963,973,0,949,994,946],
[968,983,943,970,1003,1051,0,1021,986],
[968,926,940,904,945,1006,979,0,958],
[973,975,1023,1009,1019,1054,1014,1042,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 147, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,966,975,1016,1014,976,1014,966,992],
[1034,0,1019,1036,1023,1034,1038,1000,1005],
[1025,981,0,992,1001,987,1039,1006,1009],
[984,964,1008,0,972,978,1019,973,1007],
[986,977,999,1028,0,1015,996,1000,987],
[1024,966,1013,1022,985,0,985,985,977],
[986,962,961,981,1004,1015,0,976,993],
[1034,1000,994,1027,1000,1015,1024,0,1022],
[1008,995,991,993,1013,1023,1007,978,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 148, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,1039,1014,1064,978,1048,1023,1003],
[980,0,1006,1018,1039,985,1010,948,1032],
[961,994,0,1021,1040,987,1022,961,1022],
[986,982,979,0,1014,979,1008,960,1054],
[936,961,960,986,0,950,1016,925,1012],
[1022,1015,1013,1021,1050,0,1046,957,1023],
[952,990,978,992,984,954,0,933,987],
[977,1052,1039,1040,1075,1043,1067,0,1094],
[997,968,978,946,988,977,1013,906,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 149, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,975,965,964,970,1003,981,993,980],
[1025,0,1001,1011,971,1028,1010,1016,1008],
[1035,999,0,996,999,1026,1028,990,1000],
[1036,989,1004,0,1003,1040,991,1019,976],
[1030,1029,1001,997,0,1010,1013,1009,999],
[997,972,974,960,990,0,993,971,963],
[1019,990,972,1009,987,1007,0,995,1001],
[1007,984,1010,981,991,1029,1005,0,978],
[1020,992,1000,1024,1001,1037,999,1022,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 150, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,1021,981,1017,1003,980,1020,993],
[989,0,1029,1000,1016,991,984,1012,998],
[979,971,0,979,1003,1004,983,1008,1000],
[1019,1000,1021,0,1039,1009,1030,1021,1014],
[983,984,997,961,0,999,978,1014,970],
[997,1009,996,991,1001,0,998,1000,1001],
[1020,1016,1017,970,1022,1002,0,1060,1039],
[980,988,992,979,986,1000,940,0,1011],
[1007,1002,1000,986,1030,999,961,989,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 151, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,970,959,976,1010,988,998,1025],
[998,0,985,971,1005,1012,966,991,1031],
[1030,1015,0,983,1007,1048,962,1008,988],
[1041,1029,1017,0,1020,1069,986,1008,1049],
[1024,995,993,980,0,1016,992,1003,1048],
[990,988,952,931,984,0,959,979,992],
[1012,1034,1038,1014,1008,1041,0,982,1036],
[1002,1009,992,992,997,1021,1018,0,1024],
[975,969,1012,951,952,1008,964,976,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 152, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,969,999,940,978,968,998,976,996],
[1031,0,1015,988,974,994,993,1013,989],
[1001,985,0,974,956,961,964,966,981],
[1060,1012,1026,0,1052,1003,1020,993,1007],
[1022,1026,1044,948,0,1001,1059,1002,1008],
[1032,1006,1039,997,999,0,990,1005,1004],
[1002,1007,1036,980,941,1010,0,985,986],
[1024,987,1034,1007,998,995,1015,0,1003],
[1004,1011,1019,993,992,996,1014,997,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 153, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1055,993,995,996,1014,986,1027,1021],
[945,0,945,985,989,943,972,982,919],
[1007,1055,0,1013,1028,991,1019,1020,1003],
[1005,1015,987,0,1016,1010,997,1027,993],
[1004,1011,972,984,0,974,987,1015,942],
[986,1057,1009,990,1026,0,1023,1014,1004],
[1014,1028,981,1003,1013,977,0,987,1007],
[973,1018,980,973,985,986,1013,0,1005],
[979,1081,997,1007,1058,996,993,995,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 154, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,980,983,957,958,1005,994,983,981],
[1020,0,982,985,974,1004,988,980,991],
[1017,1018,0,1051,975,1009,979,991,983],
[1043,1015,949,0,974,994,971,972,978],
[1042,1026,1025,1026,0,1035,960,1016,1040],
[995,996,991,1006,965,0,972,967,985],
[1006,1012,1021,1029,1040,1028,0,1018,994],
[1017,1020,1009,1028,984,1033,982,0,979],
[1019,1009,1017,1022,960,1015,1006,1021,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 155, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,959,976,1006,966,1007,1006,997,974],
[1041,0,1000,1002,974,1044,1013,983,1018],
[1024,1000,0,1013,1004,1011,1009,996,1017],
[994,998,987,0,988,971,986,973,1021],
[1034,1026,996,1012,0,1009,1023,996,1016],
[993,956,989,1029,991,0,1008,1012,1000],
[994,987,991,1014,977,992,0,974,1000],
[1003,1017,1004,1027,1004,988,1026,0,1031],
[1026,982,983,979,984,1000,1000,969,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 156, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,905,1079,1011,1002,928,923,1140],
[986,0,953,1080,958,979,1056,851,1109],
[1095,1047,0,1101,987,1028,1059,1010,1157],
[921,920,899,0,843,972,955,934,1114],
[989,1042,1013,1157,0,1052,1013,1025,1155],
[998,1021,972,1028,948,0,981,893,1071],
[1072,944,941,1045,987,1019,0,988,1092],
[1077,1149,990,1066,975,1107,1012,0,1222],
[860,891,843,886,845,929,908,778,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 157, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1052,965,979,935,991,962,933,995],
[948,0,996,1038,961,1047,946,985,989],
[1035,1004,0,981,873,972,916,989,1011],
[1021,962,1019,0,1001,981,894,975,1027],
[1065,1039,1127,999,0,1035,1064,1086,1067],
[1009,953,1028,1019,965,0,967,1036,1020],
[1038,1054,1084,1106,936,1033,0,1073,1059],
[1067,1015,1011,1025,914,964,927,0,1062],
[1005,1011,989,973,933,980,941,938,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 158, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,1015,1013,1040,978,960,1015,999],
[993,0,1047,1009,1061,1003,1012,1030,1036],
[985,953,0,932,986,918,945,939,995],
[987,991,1068,0,1073,1069,985,1026,1023],
[960,939,1014,927,0,981,941,967,966],
[1022,997,1082,931,1019,0,962,978,1049],
[1040,988,1055,1015,1059,1038,0,1041,1014],
[985,970,1061,974,1033,1022,959,0,1025],
[1001,964,1005,977,1034,951,986,975,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 159, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,1024,1024,966,1003,1021,1012,975],
[1023,0,998,1027,1032,1016,1015,1000,1018],
[976,1002,0,1005,996,981,994,984,979],
[976,973,995,0,951,986,996,972,998],
[1034,968,1004,1049,0,1029,1016,1022,992],
[997,984,1019,1014,971,0,1036,1008,984],
[979,985,1006,1004,984,964,0,976,949],
[988,1000,1016,1028,978,992,1024,0,968],
[1025,982,1021,1002,1008,1016,1051,1032,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 160, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1077,997,990,1030,1020,1017,1025,1023],
[923,0,939,937,923,951,947,903,911],
[1003,1061,0,1026,1054,1004,978,974,1046],
[1010,1063,974,0,1012,1012,987,974,965],
[970,1077,946,988,0,980,986,951,990],
[980,1049,996,988,1020,0,1037,974,1013],
[983,1053,1022,1013,1014,963,0,968,1011],
[975,1097,1026,1026,1049,1026,1032,0,1042],
[977,1089,954,1035,1010,987,989,958,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 161, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,1057,975,1010,1042,1040,977,956],
[1016,0,1047,1040,1011,1014,1032,1015,975],
[943,953,0,969,981,1009,1007,926,942],
[1025,960,1031,0,1032,998,1025,987,1002],
[990,989,1019,968,0,980,1024,951,992],
[958,986,991,1002,1020,0,997,908,985],
[960,968,993,975,976,1003,0,898,979],
[1023,985,1074,1013,1049,1092,1102,0,1006],
[1044,1025,1058,998,1008,1015,1021,994,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 162, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,936,957,960,931,989,956,975,927],
[1064,0,1008,1002,971,1020,1029,996,972],
[1043,992,0,991,949,956,980,996,914],
[1040,998,1009,0,1012,1018,988,1007,956],
[1069,1029,1051,988,0,1019,1022,992,1004],
[1011,980,1044,982,981,0,1008,946,996],
[1044,971,1020,1012,978,992,0,976,990],
[1025,1004,1004,993,1008,1054,1024,0,992],
[1073,1028,1086,1044,996,1004,1010,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 163, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,928,1055,1000,999,1018,992,1002,978],
[1072,0,1074,1030,1000,1024,1011,1033,1026],
[945,926,0,976,996,969,957,1017,989],
[1000,970,1024,0,1033,996,1002,1007,1032],
[1001,1000,1004,967,0,989,1000,1028,952],
[982,976,1031,1004,1011,0,1025,999,1043],
[1008,989,1043,998,1000,975,0,1000,1056],
[998,967,983,993,972,1001,1000,0,964],
[1022,974,1011,968,1048,957,944,1036,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 164, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1037,1027,1008,1021,1005,965,1009,1036],
[963,0,1005,987,972,985,963,1002,980],
[973,995,0,987,973,990,946,982,976],
[992,1013,1013,0,990,1006,953,1003,1022],
[979,1028,1027,1010,0,1033,1029,1020,1021],
[995,1015,1010,994,967,0,998,1030,1024],
[1035,1037,1054,1047,971,1002,0,1041,1021],
[991,998,1018,997,980,970,959,0,998],
[964,1020,1024,978,979,976,979,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 165, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1025,1054,1042,992,1024,1019,1033,1029],
[975,0,1039,1015,996,1009,999,978,1003],
[946,961,0,986,954,991,1000,997,997],
[958,985,1014,0,981,1017,991,973,972],
[1008,1004,1046,1019,0,1036,1003,998,1021],
[976,991,1009,983,964,0,999,990,994],
[981,1001,1000,1009,997,1001,0,991,998],
[967,1022,1003,1027,1002,1010,1009,0,999],
[971,997,1003,1028,979,1006,1002,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 166, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,1162,916,1091,1041,1038,1039,1080],
[1013,0,1091,949,982,968,1004,994,1039],
[838,909,0,909,931,929,1034,970,951],
[1084,1051,1091,0,994,995,1153,1024,1048],
[909,1018,1069,1006,0,967,1039,1025,999],
[959,1032,1071,1005,1033,0,1118,1063,1064],
[962,996,966,847,961,882,0,966,1024],
[961,1006,1030,976,975,937,1034,0,980],
[920,961,1049,952,1001,936,976,1020,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 167, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,973,977,1039,1002,1010,967,979,997],
[1027,0,985,1005,1039,1036,1014,1005,981],
[1023,1015,0,1027,1040,1033,980,1002,995],
[961,995,973,0,982,1003,948,971,951],
[998,961,960,1018,0,978,943,970,951],
[990,964,967,997,1022,0,937,964,970],
[1033,986,1020,1052,1057,1063,0,1017,1030],
[1021,995,998,1029,1030,1036,983,0,998],
[1003,1019,1005,1049,1049,1030,970,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 168, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,1004,1028,975,977,1025,970,1035],
[1006,0,985,1052,947,941,980,1033,991],
[996,1015,0,1051,1007,1050,1050,1005,1011],
[972,948,949,0,969,954,998,988,937],
[1025,1053,993,1031,0,964,1004,1021,998],
[1023,1059,950,1046,1036,0,984,995,970],
[975,1020,950,1002,996,1016,0,1016,966],
[1030,967,995,1012,979,1005,984,0,951],
[965,1009,989,1063,1002,1030,1034,1049,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 169, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1038,1005,957,1031,943,983,950,939],
[962,0,958,970,978,923,943,944,921],
[995,1042,0,985,1033,923,995,1016,952],
[1043,1030,1015,0,1055,982,987,1029,989],
[969,1022,967,945,0,915,978,967,926],
[1057,1077,1077,1018,1085,0,1064,1025,999],
[1017,1057,1005,1013,1022,936,0,994,990],
[1050,1056,984,971,1033,975,1006,0,1008],
[1061,1079,1048,1011,1074,1001,1010,992,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 170, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1031,826,906,866,998,939,882,1009],
[969,0,924,927,902,912,932,992,1036],
[1174,1076,0,978,973,993,1062,999,1092],
[1094,1073,1022,0,961,974,1033,1035,1001],
[1134,1098,1027,1039,0,1058,964,979,1131],
[1002,1088,1007,1026,942,0,1017,881,984],
[1061,1068,938,967,1036,983,0,918,969],
[1118,1008,1001,965,1021,1119,1082,0,1096],
[991,964,908,999,869,1016,1031,904,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 171, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,1018,957,1047,1011,1051,990,976],
[1016,0,1005,984,1019,991,1064,1051,982],
[982,995,0,987,1036,1006,1047,1020,998],
[1043,1016,1013,0,1036,981,1037,1041,1011],
[953,981,964,964,0,954,982,980,960],
[989,1009,994,1019,1046,0,1002,1050,978],
[949,936,953,963,1018,998,0,1047,972],
[1010,949,980,959,1020,950,953,0,980],
[1024,1018,1002,989,1040,1022,1028,1020,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 172, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,975,935,1029,979,1060,1095,1001,998],
[1025,0,955,1044,1076,1023,1107,1051,1019],
[1065,1045,0,937,948,1052,1057,1041,934],
[971,956,1063,0,999,1031,1077,1007,1003],
[1021,924,1052,1001,0,1013,1019,980,920],
[940,977,948,969,987,0,974,921,977],
[905,893,943,923,981,1026,0,972,947],
[999,949,959,993,1020,1079,1028,0,993],
[1002,981,1066,997,1080,1023,1053,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 173, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1025,995,995,973,978,998,988,957],
[975,0,957,982,938,946,980,960,928],
[1005,1043,0,1012,975,988,1036,988,992],
[1005,1018,988,0,970,966,1053,980,960],
[1027,1062,1025,1030,0,1013,1033,1026,990],
[1022,1054,1012,1034,987,0,1062,967,1009],
[1002,1020,964,947,967,938,0,964,929],
[1012,1040,1012,1020,974,1033,1036,0,980],
[1043,1072,1008,1040,1010,991,1071,1020,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 174, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1054,1046,991,1039,1043,1063,1038,1058],
[946,0,1012,962,945,920,963,945,971],
[954,988,0,965,982,999,1010,996,1050],
[1009,1038,1035,0,996,1026,1039,1017,1030],
[961,1055,1018,1004,0,1014,1032,1033,1007],
[957,1080,1001,974,986,0,1022,950,1003],
[937,1037,990,961,968,978,0,973,1021],
[962,1055,1004,983,967,1050,1027,0,1061],
[942,1029,950,970,993,997,979,939,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 175, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,962,946,993,1036,1037,1024,1023,1009],
[1038,0,978,971,996,1034,977,993,978],
[1054,1022,0,1010,1010,1038,964,1001,999],
[1007,1029,990,0,1051,1043,992,1032,1034],
[964,1004,990,949,0,998,996,1009,967],
[963,966,962,957,1002,0,960,969,988],
[976,1023,1036,1008,1004,1040,0,987,1024],
[977,1007,999,968,991,1031,1013,0,996],
[991,1022,1001,966,1033,1012,976,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 176, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,972,1012,1001,934,984,1009,974,1055],
[1028,0,1031,1005,978,1004,1113,1004,1063],
[988,969,0,1011,1029,1013,1066,1036,1041],
[999,995,989,0,1025,983,1051,1033,1001],
[1066,1022,971,975,0,1019,1045,1021,1077],
[1016,996,987,1017,981,0,1032,1027,1010],
[991,887,934,949,955,968,0,1028,985],
[1026,996,964,967,979,973,972,0,968],
[945,937,959,999,923,990,1015,1032,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 177, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1050,968,1036,1002,1059,1015,1052,1025],
[950,0,970,1019,929,1007,979,1024,989],
[1032,1030,0,1010,1022,1042,974,1059,1011],
[964,981,990,0,951,975,969,938,961],
[998,1071,978,1049,0,990,1023,1000,1065],
[941,993,958,1025,1010,0,974,1013,990],
[985,1021,1026,1031,977,1026,0,1017,1019],
[948,976,941,1062,1000,987,983,0,987],
[975,1011,989,1039,935,1010,981,1013,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 178, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,984,985,1029,977,970,1016,969],
[987,0,985,1008,1000,989,973,1024,969],
[1016,1015,0,998,1004,1006,1008,1028,989],
[1015,992,1002,0,1013,1001,997,1037,1002],
[971,1000,996,987,0,1005,1002,1024,960],
[1023,1011,994,999,995,0,1007,1005,972],
[1030,1027,992,1003,998,993,0,1043,976],
[984,976,972,963,976,995,957,0,946],
[1031,1031,1011,998,1040,1028,1024,1054,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 179, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,956,986,1028,983,1018,1016,1008,1035],
[1044,0,1005,1016,960,1018,984,1013,1046],
[1014,995,0,1069,1036,1032,1057,988,1022],
[972,984,931,0,899,1029,997,932,978],
[1017,1040,964,1101,0,1020,1031,993,1063],
[982,982,968,971,980,0,1041,964,965],
[984,1016,943,1003,969,959,0,987,997],
[992,987,1012,1068,1007,1036,1013,0,1031],
[965,954,978,1022,937,1035,1003,969,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 180, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,845,1158,1260,1260,1169,1154,1095,1117],
[1155,0,1100,1165,1102,1103,1133,946,1056],
[842,900,0,1003,964,1065,1055,881,879],
[740,835,997,0,1009,965,1074,765,875],
[740,898,1036,991,0,1002,1130,987,897],
[831,897,935,1035,998,0,1087,829,1034],
[846,867,945,926,870,913,0,994,990],
[905,1054,1119,1235,1013,1171,1006,0,990],
[883,944,1121,1125,1103,966,1010,1010,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 181, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,1028,1022,987,1010,973,1013,967],
[999,0,1027,1010,1036,1002,977,1000,966],
[972,973,0,1009,976,1004,979,1009,968],
[978,990,991,0,1001,978,977,993,973],
[1013,964,1024,999,0,997,1015,997,990],
[990,998,996,1022,1003,0,989,985,967],
[1027,1023,1021,1023,985,1011,0,992,1004],
[987,1000,991,1007,1003,1015,1008,0,978],
[1033,1034,1032,1027,1010,1033,996,1022,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 182, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,921,906,962,950,917,988,947,989],
[1079,0,1026,997,963,957,949,969,1011],
[1094,974,0,1048,986,1018,1006,1030,1045],
[1038,1003,952,0,983,939,968,1023,993],
[1050,1037,1014,1017,0,1018,982,1053,1069],
[1083,1043,982,1061,982,0,988,1009,984],
[1012,1051,994,1032,1018,1012,0,992,960],
[1053,1031,970,977,947,991,1008,0,977],
[1011,989,955,1007,931,1016,1040,1023,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 183, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,890,958,983,1069,1014,995,900,959],
[1110,0,1143,1154,1041,990,987,1093,1100],
[1042,857,0,997,988,1125,1071,948,946],
[1017,846,1003,0,1066,1093,906,966,1127],
[931,959,1012,934,0,1084,863,999,913],
[986,1010,875,907,916,0,956,965,976],
[1005,1013,929,1094,1137,1044,0,981,995],
[1100,907,1052,1034,1001,1035,1019,0,1055],
[1041,900,1054,873,1087,1024,1005,945,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 184, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,1009,992,1037,1000,978,1015,991],
[980,0,992,990,984,1007,977,970,948],
[991,1008,0,1014,992,1014,993,992,952],
[1008,1010,986,0,1018,1014,993,991,971],
[963,1016,1008,982,0,1035,957,978,973],
[1000,993,986,986,965,0,969,960,984],
[1022,1023,1007,1007,1043,1031,0,1007,984],
[985,1030,1008,1009,1022,1040,993,0,1017],
[1009,1052,1048,1029,1027,1016,1016,983,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 185, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,967,1005,1011,981,993,1039,957,968],
[1033,0,977,929,1035,972,997,968,968],
[995,1023,0,1008,1038,1001,977,968,952],
[989,1071,992,0,1074,996,1007,954,980],
[1019,965,962,926,0,991,997,880,905],
[1007,1028,999,1004,1009,0,1039,970,1003],
[961,1003,1023,993,1003,961,0,924,1005],
[1043,1032,1032,1046,1120,1030,1076,0,928],
[1032,1032,1048,1020,1095,997,995,1072,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 186, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,993,961,976,953,990,1005,977],
[1010,0,1039,964,1041,1018,1038,1057,928],
[1007,961,0,967,948,933,993,968,887],
[1039,1036,1033,0,981,1007,1038,1074,1012],
[1024,959,1052,1019,0,946,1048,1010,967],
[1047,982,1067,993,1054,0,1097,1105,998],
[1010,962,1007,962,952,903,0,1014,956],
[995,943,1032,926,990,895,986,0,877],
[1023,1072,1113,988,1033,1002,1044,1123,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 187, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1136,937,968,1071,943,900,1134,1058],
[864,0,951,1076,860,935,1014,1190,1184],
[1063,1049,0,1067,1087,966,999,1167,1049],
[1032,924,933,0,958,1022,944,1076,1102],
[929,1140,913,1042,0,870,796,1043,1098],
[1057,1065,1034,978,1130,0,1040,1116,992],
[1100,986,1001,1056,1204,960,0,1221,1032],
[866,810,833,924,957,884,779,0,911],
[942,816,951,898,902,1008,968,1089,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 188, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,1004,1014,983,1009,988,1000,1080],
[1023,0,983,987,1004,1014,1005,979,1052],
[996,1017,0,1012,1040,989,1018,968,1053],
[986,1013,988,0,1046,1040,961,961,1075],
[1017,996,960,954,0,925,984,987,1091],
[991,986,1011,960,1075,0,1041,985,1079],
[1012,995,982,1039,1016,959,0,968,1106],
[1000,1021,1032,1039,1013,1015,1032,0,1093],
[920,948,947,925,909,921,894,907,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 189, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,992,998,992,973,957,959,995],
[984,0,984,964,989,975,983,977,969],
[1008,1016,0,988,995,985,986,985,982],
[1002,1036,1012,0,1005,1020,969,983,989],
[1008,1011,1005,995,0,986,975,979,1003],
[1027,1025,1015,980,1014,0,1016,974,1019],
[1043,1017,1014,1031,1025,984,0,1002,1019],
[1041,1023,1015,1017,1021,1026,998,0,1011],
[1005,1031,1018,1011,997,981,981,989,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 190, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,905,1004,944,930,956,982,1015,918],
[1095,0,1060,1040,1018,1020,1032,990,1004],
[996,940,0,926,932,995,1004,1016,926],
[1056,960,1074,0,1001,1040,1005,1027,978],
[1070,982,1068,999,0,1002,1009,1026,1009],
[1044,980,1005,960,998,0,1008,970,996],
[1018,968,996,995,991,992,0,1025,943],
[985,1010,984,973,974,1030,975,0,958],
[1082,996,1074,1022,991,1004,1057,1042,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 191, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,976,990,998,1013,1024,998,950],
[989,0,956,989,961,995,967,974,919],
[1024,1044,0,1011,1037,1050,977,993,1010],
[1010,1011,989,0,968,1046,1010,940,1000],
[1002,1039,963,1032,0,1045,1003,939,963],
[987,1005,950,954,955,0,946,984,951],
[976,1033,1023,990,997,1054,0,982,959],
[1002,1026,1007,1060,1061,1016,1018,0,996],
[1050,1081,990,1000,1037,1049,1041,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 192, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,795,947,878,907,862,887,953,1036],
[1205,0,1018,1008,1112,1075,997,1053,1101],
[1053,982,0,980,1061,940,979,1112,1101],
[1122,992,1020,0,1046,1061,955,1032,1117],
[1093,888,939,954,0,996,1047,976,1070],
[1138,925,1060,939,1004,0,1041,1072,1166],
[1113,1003,1021,1045,953,959,0,1060,1086],
[1047,947,888,968,1024,928,940,0,1043],
[964,899,899,883,930,834,914,957,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 193, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,982,1012,993,1017,1018,1039,1001,985],
[1018,0,1013,1018,1000,1010,1038,1001,1022],
[988,987,0,1008,1015,996,1032,1029,1030],
[1007,982,992,0,1006,959,1042,1002,1016],
[983,1000,985,994,0,961,1049,1026,997],
[982,990,1004,1041,1039,0,1035,1019,1037],
[961,962,968,958,951,965,0,981,954],
[999,999,971,998,974,981,1019,0,1024],
[1015,978,970,984,1003,963,1046,976,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 194, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1028,989,1043,1028,1049,1031,1017,1024],
[972,0,1021,1000,982,1016,977,962,1009],
[1011,979,0,1023,1010,1028,1004,1038,1028],
[957,1000,977,0,1003,1037,985,993,983],
[972,1018,990,997,0,1043,997,951,1028],
[951,984,972,963,957,0,982,965,991],
[969,1023,996,1015,1003,1018,0,969,1001],
[983,1038,962,1007,1049,1035,1031,0,1045],
[976,991,972,1017,972,1009,999,955,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 195, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,969,954,1009,972,964,988,950,941],
[1031,0,1016,964,1034,999,1028,1019,997],
[1046,984,0,984,993,974,963,1025,1045],
[991,1036,1016,0,1037,1047,977,1010,1032],
[1028,966,1007,963,0,989,1007,952,1022],
[1036,1001,1026,953,1011,0,1036,959,1060],
[1012,972,1037,1023,993,964,0,985,1050],
[1050,981,975,990,1048,1041,1015,0,1020],
[1059,1003,955,968,978,940,950,980,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 196, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,1024,998,1027,1017,1019,990,1009],
[985,0,989,962,984,967,998,999,984],
[976,1011,0,992,1043,998,1013,1010,1008],
[1002,1038,1008,0,1033,985,1010,1010,1008],
[973,1016,957,967,0,978,999,998,989],
[983,1033,1002,1015,1022,0,1022,996,981],
[981,1002,987,990,1001,978,0,1005,987],
[1010,1001,990,990,1002,1004,995,0,969],
[991,1016,992,992,1011,1019,1013,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 197, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,998,1031,1018,1057,983,1036,1018],
[987,0,962,943,968,1031,965,973,991],
[1002,1038,0,971,967,1048,998,1053,988],
[969,1057,1029,0,1001,1058,1021,1016,1038],
[982,1032,1033,999,0,1046,985,1060,1027],
[943,969,952,942,954,0,931,992,996],
[1017,1035,1002,979,1015,1069,0,1060,1008],
[964,1027,947,984,940,1008,940,0,999],
[982,1009,1012,962,973,1004,992,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 198, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,1037,992,993,982,1039,1055,1027],
[994,0,1031,993,1022,963,1019,1004,1061],
[963,969,0,982,1015,929,999,1013,946],
[1008,1007,1018,0,972,1009,1057,1101,1119],
[1007,978,985,1028,0,971,1061,1082,1012],
[1018,1037,1071,991,1029,0,1053,1067,1060],
[961,981,1001,943,939,947,0,985,1001],
[945,996,987,899,918,933,1015,0,960],
[973,939,1054,881,988,940,999,1040,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 199, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1028,950,989,984,982,995,966,973],
[972,0,940,941,959,903,985,958,932],
[1050,1060,0,1055,1011,1012,1014,994,1000],
[1011,1059,945,0,1015,975,1001,986,1030],
[1016,1041,989,985,0,964,1007,950,965],
[1018,1097,988,1025,1036,0,1035,999,1039],
[1005,1015,986,999,993,965,0,1031,997],
[1034,1042,1006,1014,1050,1001,969,0,970],
[1027,1068,1000,970,1035,961,1003,1030,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda1(om) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([9, 2000, 200, "ME", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/me/me_9_2000.csv", index=False, header=False)