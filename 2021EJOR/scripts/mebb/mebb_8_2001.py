
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg

rep = 3
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,1006,965,883,1004,920,1012,963],
[995,0,1001,982,1028,960,932,979],
[1036,1000,0,924,978,987,1013,966],
[1118,1019,1077,0,1004,995,995,1025],
[997,973,1023,997,0,961,994,944],
[1081,1041,1014,1006,1040,0,1004,969],
[989,1069,988,1006,1007,997,0,992],
[1038,1022,1035,976,1057,1032,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 1, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,1019,1005,971,1046,999,1053],
[988,0,988,976,970,1014,973,987],
[982,1013,0,1002,1022,1035,978,1024],
[996,1025,999,0,1013,1014,964,1020],
[1030,1031,979,988,0,1059,1006,1019],
[955,987,966,987,942,0,940,1005],
[1002,1028,1023,1037,995,1061,0,1043],
[948,1014,977,981,982,996,958,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 2, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1053,1044,970,997,1036,1006,1007],
[948,0,1007,1031,950,994,970,957],
[957,994,0,976,943,971,963,978],
[1031,970,1025,0,957,991,939,1016],
[1004,1051,1058,1044,0,1023,991,975],
[965,1007,1030,1010,978,0,1025,967],
[995,1031,1038,1062,1010,976,0,1009],
[994,1044,1023,985,1026,1034,992,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 3, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,992,1011,1031,1027,1016,971],
[1008,0,1009,1048,1034,1027,1049,998],
[1009,992,0,1015,1019,988,990,998],
[990,953,986,0,1034,993,1005,967],
[970,967,982,967,0,978,952,952],
[974,974,1013,1008,1023,0,1025,971],
[985,952,1011,996,1049,976,0,1026],
[1030,1003,1003,1034,1049,1030,975,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 4, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,983,968,1027,1015,1024,1001],
[977,0,970,982,983,960,957,958],
[1018,1031,0,1009,1005,1001,1007,987],
[1033,1019,992,0,1036,1020,1014,976],
[974,1018,996,965,0,977,972,954],
[986,1041,1000,981,1024,0,987,962],
[977,1044,994,987,1029,1014,0,955],
[1000,1043,1014,1025,1047,1039,1046,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 5, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,994,1007,1003,1003,1036,999],
[985,0,994,969,1001,982,1016,1018],
[1007,1007,0,1000,1012,991,1065,1010],
[994,1032,1001,0,1006,979,1059,1012],
[998,1000,989,995,0,998,1025,1009],
[998,1019,1010,1022,1003,0,1030,1007],
[965,985,936,942,976,971,0,988],
[1002,983,991,989,992,994,1013,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 6, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,1018,1000,971,963,995,956],
[1011,0,1008,1011,999,974,966,985],
[983,993,0,979,965,959,997,965],
[1001,990,1022,0,1005,975,982,956],
[1030,1002,1036,996,0,1019,1020,1008],
[1038,1027,1042,1026,982,0,1017,993],
[1006,1035,1004,1019,981,984,0,955],
[1045,1016,1036,1045,993,1008,1046,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 7, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,1032,1034,972,1066,1028,987],
[1003,0,1017,981,1005,1013,1015,994],
[969,984,0,993,993,1053,1050,966],
[967,1020,1008,0,999,1095,1009,955],
[1029,996,1008,1002,0,1053,1011,1028],
[935,988,948,906,948,0,1005,952],
[973,986,951,992,990,996,0,980],
[1014,1007,1035,1046,973,1049,1021,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 8, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,970,1024,984,1029,989,1021,1029],
[1031,0,1025,1004,1016,1004,997,1023],
[977,976,0,985,1021,1014,1006,1016],
[1017,997,1016,0,1010,1027,1015,992],
[972,985,980,991,0,964,988,996],
[1012,997,987,974,1037,0,994,1006],
[980,1004,995,986,1013,1007,0,985],
[972,978,985,1009,1005,995,1016,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 9, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,999,982,941,1023,959,1002],
[1008,0,1083,968,976,1044,956,993],
[1002,918,0,950,981,1040,962,963],
[1019,1033,1051,0,1008,1028,985,997],
[1060,1025,1020,993,0,1051,1035,1033],
[978,957,961,973,950,0,960,941],
[1042,1045,1039,1016,966,1041,0,1010],
[999,1008,1038,1004,968,1060,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 10, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,920,960,973,930,1051,973,974],
[1081,0,1028,1017,1001,1081,984,1053],
[1041,973,0,972,969,1071,967,998],
[1028,984,1029,0,973,1069,1015,1021],
[1071,1000,1032,1028,0,1100,979,1048],
[950,920,930,932,901,0,910,958],
[1028,1017,1034,986,1022,1091,0,1039],
[1027,948,1003,980,953,1043,962,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 11, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1004,1040,986,994,964,1000,968],
[997,0,1086,1005,1008,967,1029,1031],
[961,915,0,957,977,927,933,933],
[1015,996,1044,0,997,948,976,975],
[1007,993,1024,1004,0,934,995,955],
[1037,1034,1074,1053,1067,0,1004,974],
[1001,972,1068,1025,1006,997,0,972],
[1033,970,1068,1026,1046,1027,1029,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 12, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,968,961,987,1008,1043,983,1029],
[1033,0,1043,1047,1023,1030,988,1058],
[1040,958,0,993,963,1005,912,1031],
[1014,954,1008,0,999,1035,956,1089],
[993,978,1038,1002,0,1033,1014,1055],
[958,971,996,966,968,0,918,1005],
[1018,1013,1089,1045,987,1083,0,1104],
[972,943,970,912,946,996,897,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 13, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1029,1030,1006,975,1037,983,1026],
[972,0,1004,981,947,985,990,994],
[971,997,0,981,978,1008,1004,1005],
[995,1020,1020,0,960,1013,999,987],
[1026,1054,1023,1041,0,1003,1022,986],
[964,1016,993,988,998,0,997,1006],
[1018,1011,997,1002,979,1004,0,1010],
[975,1007,996,1014,1015,995,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 14, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1017,1053,1062,1025,1019,981,1042],
[984,0,1030,1019,995,1001,975,999],
[948,971,0,1013,957,966,920,997],
[939,982,988,0,984,984,950,1033],
[976,1006,1044,1017,0,1001,1003,1037],
[982,1000,1035,1017,1000,0,1001,1043],
[1020,1026,1081,1051,998,1000,0,1068],
[959,1002,1004,968,964,958,933,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 15, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,957,1019,949,1003,975,957,982],
[1044,0,998,970,1004,973,982,983],
[982,1003,0,936,993,964,954,996],
[1052,1031,1065,0,1034,1019,988,1013],
[998,997,1008,967,0,974,1001,1017],
[1026,1028,1037,982,1027,0,1024,1029],
[1044,1019,1047,1013,1000,977,0,1024],
[1019,1018,1005,988,984,972,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 16, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,1021,993,1003,1004,990,980],
[1002,0,1030,1016,1036,1036,1001,985],
[980,971,0,998,994,986,991,988],
[1008,985,1003,0,983,1016,971,985],
[998,965,1007,1018,0,985,982,972],
[997,965,1015,985,1016,0,965,973],
[1011,1000,1010,1030,1019,1036,0,1001],
[1021,1016,1013,1016,1029,1028,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 17, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,968,989,993,925,918,934,876],
[1033,0,1019,987,982,985,1052,941],
[1012,982,0,1043,1011,987,1003,1002],
[1008,1014,958,0,1042,1055,974,963],
[1076,1019,990,959,0,990,1001,981],
[1083,1016,1014,946,1011,0,1065,952],
[1067,949,998,1027,1000,936,0,945],
[1125,1060,999,1038,1020,1049,1056,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 18, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,973,1003,928,947,985,984,908],
[1028,0,1088,1008,1088,1032,1022,980],
[998,913,0,933,985,992,949,948],
[1073,993,1068,0,1029,1054,1004,1019],
[1054,913,1016,972,0,979,957,941],
[1016,969,1009,947,1022,0,995,944],
[1017,979,1052,997,1044,1006,0,970],
[1093,1021,1053,982,1060,1057,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 19, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,991,1034,1009,1017,1012,974,1020],
[1010,0,1008,1037,1007,1041,1041,985],
[967,993,0,1008,1035,1037,991,967],
[992,964,993,0,1038,1006,993,1004],
[984,994,966,963,0,966,954,971],
[989,960,964,995,1035,0,955,988],
[1027,960,1010,1008,1047,1046,0,996],
[981,1016,1034,997,1030,1013,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 20, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1023,996,971,941,1005,1010,979],
[978,0,974,982,973,1006,969,1024],
[1005,1027,0,1020,956,1058,1055,1018],
[1030,1019,981,0,1024,1017,1009,1015],
[1060,1028,1045,977,0,1041,1004,1016],
[996,995,943,984,960,0,1005,964],
[991,1032,946,992,997,996,0,992],
[1022,977,983,986,985,1037,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 21, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,1031,1012,981,1039,1060,997],
[1005,0,1011,1028,1016,1007,1102,994],
[970,990,0,1001,974,1003,1046,953],
[989,973,1000,0,964,1019,1053,986],
[1020,985,1027,1037,0,1034,1055,1024],
[962,994,998,982,967,0,1029,943],
[941,899,955,948,946,972,0,920],
[1004,1007,1048,1015,977,1058,1081,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 22, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1036,996,1032,1017,1061,1037,1048],
[965,0,952,976,981,976,957,914],
[1005,1049,0,1029,1057,1011,978,988],
[969,1025,972,0,1034,1068,1036,944],
[984,1020,944,967,0,1010,1004,887],
[940,1025,990,933,991,0,1044,984],
[964,1044,1023,965,997,957,0,997],
[953,1087,1013,1057,1114,1017,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 23, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,1008,996,1050,1039,1018,1031],
[1007,0,1014,1017,976,1045,958,1015],
[993,987,0,983,982,1007,1015,1020],
[1005,984,1018,0,1019,1032,1000,1004],
[951,1025,1019,982,0,993,1010,984],
[962,956,994,969,1008,0,1001,1045],
[983,1043,986,1001,991,1000,0,993],
[970,986,981,997,1017,956,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 24, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,991,1040,1039,1013,1028,1006],
[1013,0,989,1017,1057,953,1028,1009],
[1010,1012,0,1018,1042,968,1004,1011],
[961,984,983,0,1008,935,1015,1001],
[962,944,959,993,0,959,955,993],
[988,1048,1033,1066,1042,0,1043,1045],
[973,973,997,986,1046,958,0,989],
[995,992,990,1000,1008,956,1012,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 25, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,960,998,996,978,969,991],
[1011,0,1011,996,1006,1018,986,986],
[1041,990,0,999,1047,1048,1001,1015],
[1003,1005,1002,0,1067,1046,992,1018],
[1005,995,954,934,0,965,994,966],
[1023,983,953,955,1036,0,989,978],
[1032,1015,1000,1009,1007,1012,0,1005],
[1010,1015,986,983,1035,1023,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 26, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,984,1022,1034,1002,1022,1031],
[1008,0,981,1015,1009,956,972,981],
[1017,1020,0,1052,1013,977,1015,1035],
[979,986,949,0,1032,944,968,1016],
[967,992,988,969,0,960,965,998],
[999,1045,1024,1057,1041,0,1000,1030],
[979,1029,986,1033,1036,1001,0,1017],
[970,1020,966,985,1003,971,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 27, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1008,1002,1020,952,1018,1016,1024],
[993,0,1055,1031,979,1003,1079,1085],
[999,946,0,1031,1021,1010,1038,1016],
[981,970,970,0,942,1016,1025,989],
[1049,1022,980,1059,0,1065,1091,1077],
[983,998,991,985,936,0,1022,1015],
[985,922,963,976,910,979,0,975],
[977,916,985,1012,924,986,1026,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 28, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,1015,1034,1012,1052,1016,1000],
[981,0,1028,970,1030,1026,970,940],
[986,973,0,917,1009,1006,931,934],
[967,1031,1084,0,1036,1012,1011,981],
[989,971,992,965,0,998,987,1004],
[949,975,995,989,1003,0,993,952],
[985,1031,1070,990,1014,1008,0,1000],
[1001,1061,1067,1020,997,1049,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 29, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,991,1000,1005,1016,1004,1001,1030],
[1010,0,1010,979,1050,1001,987,977],
[1001,991,0,966,1003,983,977,983],
[996,1022,1035,0,1027,1024,1005,1005],
[985,951,998,974,0,981,976,988],
[997,1000,1018,977,1020,0,992,1006],
[1000,1014,1024,996,1025,1009,0,1008],
[971,1024,1018,996,1013,995,993,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 30, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,956,977,1009,974,904,1032,925],
[1045,0,953,1023,1006,900,946,963],
[1024,1048,0,1045,1075,976,1024,962],
[992,978,956,0,1000,954,989,961],
[1027,995,926,1001,0,1005,1017,949],
[1097,1101,1025,1047,996,0,1011,1019],
[969,1055,977,1012,984,990,0,989],
[1076,1038,1039,1040,1052,982,1012,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 31, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1038,1047,1057,1021,1020,998,988],
[963,0,1021,1014,978,998,984,1014],
[954,980,0,983,984,981,987,994],
[944,987,1018,0,1015,981,1018,979],
[980,1023,1017,986,0,991,1028,1003],
[981,1003,1020,1020,1010,0,991,959],
[1003,1017,1014,983,973,1010,0,984],
[1013,987,1007,1022,998,1042,1017,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 32, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,996,997,991,1036,996,1022],
[995,0,983,1011,995,1045,998,1023],
[1005,1018,0,995,1004,1063,985,1040],
[1004,990,1006,0,998,1040,1012,993],
[1010,1006,997,1003,0,1057,993,1019],
[965,956,938,961,944,0,959,971],
[1005,1003,1016,989,1008,1042,0,1005],
[979,978,961,1008,982,1030,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 33, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,923,1051,1063,999,999,1086,1045],
[1078,0,1144,1141,981,1004,1126,1112],
[950,857,0,1000,884,941,1083,918],
[938,860,1001,0,974,975,1136,1004],
[1002,1020,1117,1027,0,926,1093,1079],
[1002,997,1060,1026,1075,0,1101,1011],
[915,875,918,865,908,900,0,946],
[956,889,1083,997,922,990,1055,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 34, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1042,1024,997,964,931,932,1027],
[959,0,986,959,936,940,925,998],
[977,1015,0,982,957,959,967,971],
[1004,1042,1019,0,984,953,1006,1035],
[1037,1065,1044,1017,0,1004,993,1031],
[1070,1061,1042,1048,997,0,1032,1088],
[1069,1076,1034,995,1008,969,0,1012],
[974,1003,1030,966,970,913,989,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 35, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1058,979,1075,986,961,1017,1048],
[943,0,949,967,958,953,971,982],
[1022,1052,0,1081,981,1022,974,1029],
[926,1034,920,0,945,942,915,929],
[1015,1043,1020,1056,0,966,1032,1015],
[1040,1048,979,1059,1035,0,1063,970],
[984,1030,1027,1086,969,938,0,1009],
[953,1019,972,1072,986,1031,992,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 36, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,986,950,949,978,984,1018,977],
[1015,0,943,957,1004,971,1014,996],
[1051,1058,0,1019,1041,1033,1062,998],
[1052,1044,982,0,1043,997,1061,1028],
[1023,997,960,958,0,947,979,937],
[1017,1030,968,1004,1054,0,1042,1016],
[983,987,939,940,1022,959,0,972],
[1024,1005,1003,973,1064,985,1029,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 37, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1008,1113,1077,989,1242,1097,1024],
[993,0,1026,911,892,1113,1081,1028],
[888,975,0,930,987,1233,987,1009],
[924,1090,1071,0,1064,1205,1123,965],
[1012,1109,1014,937,0,1099,1120,991],
[759,888,768,796,902,0,851,813],
[904,920,1014,878,881,1150,0,942],
[977,973,992,1036,1010,1188,1059,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 38, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,1062,962,1002,1015,953,1001],
[1008,0,992,982,966,1003,979,947],
[939,1009,0,935,997,912,970,935],
[1039,1019,1066,0,1026,995,964,941],
[999,1035,1004,975,0,949,914,932],
[986,998,1089,1006,1052,0,1010,1003],
[1048,1022,1031,1037,1087,991,0,980],
[1000,1054,1066,1060,1069,998,1021,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 39, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1039,1021,1020,1009,986,997,989],
[962,0,976,1019,978,990,951,976],
[980,1025,0,1026,1011,1006,1005,1003],
[981,982,975,0,990,1019,988,1003],
[992,1023,990,1011,0,1002,1009,1014],
[1015,1011,995,982,999,0,1020,1032],
[1004,1050,996,1013,992,981,0,1032],
[1012,1025,998,998,987,969,969,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 40, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,999,991,970,981,998,998],
[992,0,1008,995,971,1006,981,974],
[1002,993,0,1007,964,988,975,999],
[1010,1006,994,0,976,1012,1017,999],
[1031,1030,1037,1025,0,1016,1021,975],
[1020,995,1013,989,985,0,971,1008],
[1003,1020,1026,984,980,1030,0,952],
[1003,1027,1002,1002,1026,993,1049,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 41, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1017,1010,987,951,964,1007,936],
[984,0,971,962,984,980,1012,1003],
[991,1030,0,986,960,981,1021,982],
[1014,1039,1015,0,1012,987,981,996],
[1050,1017,1041,989,0,999,1001,999],
[1037,1021,1020,1014,1002,0,1013,995],
[994,989,980,1020,1000,988,0,985],
[1065,998,1019,1005,1002,1006,1016,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 42, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1004,1049,992,1023,980,1032,987],
[997,0,1085,1024,933,972,1007,1062],
[952,916,0,959,958,948,960,958],
[1009,977,1042,0,991,967,962,1014],
[978,1068,1043,1010,0,996,1012,1026],
[1021,1029,1053,1034,1005,0,1041,993],
[969,994,1041,1039,989,960,0,973],
[1014,939,1043,987,975,1008,1028,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 43, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,921,993,928,915,1022,922,958],
[1080,0,1014,1085,1014,1066,1020,981],
[1008,987,0,1009,1011,1059,975,947],
[1073,916,992,0,1012,1074,997,989],
[1086,987,990,989,0,1053,995,980],
[979,935,942,927,948,0,935,929],
[1079,981,1026,1004,1006,1066,0,1043],
[1043,1020,1054,1012,1021,1072,958,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 44, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,966,960,1018,984,1003,987,1016],
[1035,0,959,1001,987,1015,1048,1027],
[1041,1042,0,1025,999,1015,1036,1013],
[983,1000,976,0,961,973,998,1011],
[1017,1014,1002,1040,0,1002,997,1009],
[998,986,986,1028,999,0,1019,1006],
[1014,953,965,1003,1004,982,0,1010],
[985,974,988,990,992,995,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 45, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,1043,1021,1030,1023,991,1005],
[1003,0,1015,1011,1047,1013,1015,993],
[958,986,0,987,979,1007,987,995],
[980,990,1014,0,1000,995,966,969],
[971,954,1022,1001,0,1007,960,984],
[978,988,994,1006,994,0,969,996],
[1010,986,1014,1035,1041,1032,0,1015],
[996,1008,1006,1032,1017,1005,986,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 46, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,977,984,1000,989,978,1038],
[1013,0,1030,1009,996,995,1018,1045],
[1024,971,0,985,998,968,994,1018],
[1017,992,1016,0,981,982,1015,1022],
[1001,1005,1003,1020,0,1021,997,1027],
[1012,1006,1033,1019,980,0,1019,1038],
[1023,983,1007,986,1004,982,0,1041],
[963,956,983,979,974,963,960,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 47, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1067,975,938,992,1030,938,938],
[934,0,958,949,959,999,936,936],
[1026,1043,0,1009,993,1068,978,1026],
[1063,1052,992,0,1064,996,1032,1067],
[1009,1042,1008,937,0,1071,938,997],
[971,1002,933,1005,930,0,1027,966],
[1063,1065,1023,969,1063,974,0,1026],
[1063,1065,975,934,1004,1035,975,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 48, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,970,929,937,963,967,913],
[1022,0,1009,1062,988,966,994,1049],
[1031,992,0,1034,962,922,967,982],
[1072,939,967,0,935,871,982,931],
[1064,1013,1039,1066,0,975,997,935],
[1038,1035,1079,1130,1026,0,1021,915],
[1034,1007,1034,1019,1004,980,0,978],
[1088,952,1019,1070,1066,1086,1023,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 49, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,1010,982,1006,1008,962,1024],
[1009,0,1032,1024,979,1031,1013,988],
[991,969,0,983,969,981,995,996],
[1019,977,1018,0,960,1014,1001,983],
[995,1022,1032,1041,0,1030,1008,1049],
[993,970,1020,987,971,0,976,991],
[1039,988,1006,1000,993,1025,0,1031],
[977,1013,1005,1018,952,1010,970,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 50, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,741,653,999,877,1387,909,954],
[1260,0,1075,1314,828,1402,1358,1510],
[1348,926,0,1186,958,901,1235,1273],
[1002,687,815,0,857,1066,1128,1009],
[1124,1173,1043,1144,0,1112,819,884],
[614,599,1100,935,889,0,688,1137],
[1092,643,766,873,1182,1313,0,1096],
[1047,491,728,992,1117,864,905,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 51, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,958,1019,991,988,934,914,974],
[1043,0,1061,974,986,973,952,1015],
[982,940,0,993,916,934,948,980],
[1010,1027,1008,0,971,966,1032,935],
[1013,1015,1085,1030,0,1022,1048,990],
[1067,1028,1067,1035,979,0,1038,1038],
[1087,1049,1053,969,953,963,0,987],
[1027,986,1021,1066,1011,963,1014,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 52, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,951,949,989,1020,982,1022],
[1005,0,993,1002,978,1054,1018,1015],
[1050,1008,0,1031,998,1068,1000,1027],
[1052,999,970,0,1002,1014,1035,1041],
[1012,1023,1003,999,0,1042,1037,1035],
[981,947,933,987,959,0,928,984],
[1019,983,1001,966,964,1073,0,1022],
[979,986,974,960,966,1017,979,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 53, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1026,999,1019,1094,949,1026,942],
[975,0,1031,1019,1018,907,961,1051],
[1002,970,0,1071,1013,862,1068,1046],
[982,982,930,0,999,961,1054,963],
[907,983,988,1002,0,926,1003,993],
[1052,1094,1139,1040,1075,0,1081,981],
[975,1040,933,947,998,920,0,950],
[1059,950,955,1038,1008,1020,1051,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 54, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,990,1002,1007,1002,1019,1003],
[1008,0,997,1005,992,1025,1025,971],
[1011,1004,0,987,1012,1041,1042,984],
[999,996,1014,0,1005,1037,1011,1010],
[994,1009,989,996,0,1028,1011,995],
[999,976,960,964,973,0,1003,997],
[982,976,959,990,990,998,0,994],
[998,1030,1017,991,1006,1004,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 55, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,847,974,849,906,930,980,1014],
[1154,0,998,1031,961,1186,1174,1216],
[1027,1003,0,935,676,957,935,964],
[1152,970,1066,0,1083,1049,1074,1193],
[1095,1040,1325,918,0,1034,1222,1049],
[1071,815,1044,952,967,0,1041,1152],
[1021,827,1066,927,779,960,0,1050],
[987,785,1037,808,952,849,951,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 56, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,1019,994,980,992,980,1021],
[1003,0,985,1014,998,989,989,1009],
[982,1016,0,1030,1013,1014,1005,990],
[1007,987,971,0,982,1005,980,995],
[1021,1003,988,1019,0,1016,1009,1018],
[1009,1012,987,996,985,0,990,1014],
[1021,1012,996,1021,992,1011,0,1023],
[980,992,1011,1006,983,987,978,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 57, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,970,968,969,947,986,944,1032],
[1031,0,983,1004,963,1062,949,1004],
[1033,1018,0,1003,1000,1068,942,1006],
[1032,997,998,0,1014,1088,1004,1032],
[1054,1038,1001,987,0,1077,1017,1034],
[1015,939,933,913,924,0,956,952],
[1057,1052,1059,997,984,1045,0,1080],
[969,997,995,969,967,1049,921,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 58, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,984,964,1004,981,980,978],
[1011,0,1003,1020,1032,1030,992,1014],
[1017,998,0,1002,1049,1027,1014,1000],
[1037,981,999,0,1033,1018,958,970],
[997,969,952,968,0,1011,987,1007],
[1020,971,974,983,990,0,987,1001],
[1021,1009,987,1043,1014,1014,0,1004],
[1023,987,1001,1031,994,1000,997,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 59, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,936,961,904,979,900,988,985],
[1065,0,971,975,958,1001,1042,955],
[1040,1030,0,1015,1017,958,1037,1006],
[1097,1026,986,0,1034,991,1017,1008],
[1022,1043,984,967,0,948,1021,1016],
[1101,1000,1043,1010,1053,0,1041,1005],
[1013,959,964,984,980,960,0,1027],
[1016,1046,995,993,985,996,974,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 60, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,964,1087,1045,1077,992,1079,1062],
[1037,0,1018,960,1062,993,1040,1064],
[914,983,0,969,998,957,1021,1029],
[956,1041,1032,0,1008,1030,1034,1045],
[924,939,1003,993,0,981,1018,1001],
[1009,1008,1044,971,1020,0,1054,1027],
[922,961,980,967,983,947,0,988],
[939,937,972,956,1000,974,1013,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 61, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,983,985,993,962,961,1030,1028],
[1018,0,997,939,1004,1013,1047,1002],
[1016,1004,0,982,1031,987,1052,1058],
[1008,1062,1019,0,987,1016,1002,1022],
[1039,997,970,1014,0,921,1021,1050],
[1040,988,1014,985,1080,0,993,989],
[971,954,949,999,980,1008,0,986],
[973,999,943,979,951,1012,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 62, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1050,1041,1090,1025,1097,985,1098],
[951,0,993,1034,1011,1073,1042,1071],
[960,1008,0,1040,974,1030,987,1051],
[911,967,961,0,917,1025,953,994],
[976,990,1027,1084,0,1077,1010,1109],
[904,928,971,976,924,0,954,1019],
[1016,959,1014,1048,991,1047,0,1036],
[903,930,950,1007,892,982,965,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 63, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,973,926,944,973,902,926,902],
[1028,0,981,985,995,933,972,983],
[1075,1020,0,1009,1020,1006,984,933],
[1057,1016,992,0,974,943,994,958],
[1028,1006,981,1027,0,934,979,941],
[1099,1068,995,1058,1067,0,1039,1028],
[1075,1029,1017,1007,1022,962,0,970],
[1099,1018,1068,1043,1060,973,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 64, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1029,946,938,973,963,986,1183],
[972,0,915,1070,1041,924,996,1086],
[1055,1086,0,1061,1050,931,1052,1103],
[1063,931,940,0,1036,1027,1109,1151],
[1028,960,951,965,0,922,1087,1158],
[1038,1077,1070,974,1079,0,1005,1141],
[1015,1005,949,892,914,996,0,1146],
[818,915,898,850,843,860,855,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 65, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,969,1021,1037,1011,985,983],
[988,0,1067,1017,1056,1033,1033,1008],
[1032,934,0,1022,1086,965,1024,988],
[980,984,979,0,1052,1002,1022,1032],
[964,945,915,949,0,969,980,900],
[990,968,1036,999,1032,0,966,1007],
[1016,968,977,979,1021,1035,0,991],
[1018,993,1013,969,1101,994,1010,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 66, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1057,988,1048,1014,990,1032,1019],
[944,0,981,996,986,940,1078,971],
[1013,1020,0,1064,987,989,990,1005],
[953,1005,937,0,1051,1031,961,1029],
[987,1015,1014,950,0,991,989,1054],
[1011,1061,1012,970,1010,0,1033,1023],
[969,923,1011,1040,1012,968,0,1071],
[982,1030,996,972,947,978,930,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 67, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1018,993,959,1003,982,1009,1033],
[983,0,1022,999,1044,1064,1074,1014],
[1008,979,0,1005,923,998,981,1048],
[1042,1002,996,0,1011,1040,985,1054],
[998,957,1078,990,0,964,971,1025],
[1019,937,1003,961,1037,0,1041,1020],
[992,927,1020,1016,1030,960,0,985],
[968,987,953,947,976,981,1016,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 68, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,947,966,955,936,972,945,974],
[1054,0,985,972,1029,990,992,1005],
[1035,1016,0,972,972,962,1009,1023],
[1046,1029,1029,0,983,995,1032,997],
[1065,972,1029,1018,0,1006,1033,1022],
[1029,1011,1039,1006,995,0,1029,1023],
[1056,1009,992,969,968,972,0,1012],
[1027,996,978,1004,979,978,989,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 69, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,1002,984,985,1006,1007,999],
[990,0,1004,997,967,980,972,988],
[999,997,0,981,963,1024,997,986],
[1017,1004,1020,0,1011,1002,1004,972],
[1016,1034,1038,990,0,992,1012,991],
[995,1021,977,999,1009,0,1011,996],
[994,1029,1004,997,989,990,0,1002],
[1002,1013,1015,1029,1010,1005,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 70, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1008,954,1024,978,990,931,1001],
[993,0,947,995,976,974,964,994],
[1047,1054,0,1031,999,1011,977,1023],
[977,1006,970,0,952,989,985,1010],
[1023,1025,1002,1049,0,982,1002,1024],
[1011,1027,990,1012,1019,0,970,1026],
[1070,1037,1024,1016,999,1031,0,1019],
[1000,1007,978,991,977,975,982,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 71, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,964,936,986,987,1016,988,1015],
[1037,0,993,1018,1048,1025,1023,1046],
[1065,1008,0,1004,1023,1024,991,1042],
[1015,983,997,0,1026,1010,997,1041],
[1014,953,978,975,0,971,970,1023],
[985,976,977,991,1030,0,1010,994],
[1013,978,1010,1004,1031,991,0,977],
[986,955,959,960,978,1007,1024,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 72, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,972,972,919,971,922,962,1034],
[1029,0,1015,1046,1044,999,991,1048],
[1029,986,0,1059,1074,955,1047,1046],
[1082,955,942,0,1057,999,1012,1051],
[1030,957,927,944,0,959,1024,1050],
[1079,1002,1046,1002,1042,0,961,1007],
[1039,1010,954,989,977,1040,0,1051],
[967,953,955,950,951,994,950,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 73, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,1000,1037,1050,1073,970,1024],
[1002,0,935,972,967,1015,944,988],
[1001,1066,0,990,1022,1067,977,1014],
[964,1029,1011,0,984,1061,960,953],
[951,1034,979,1017,0,1030,959,967],
[928,986,934,940,971,0,907,942],
[1031,1057,1024,1041,1042,1094,0,972],
[977,1013,987,1048,1034,1059,1029,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 74, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,999,1027,1015,962,996,971],
[1009,0,1047,1002,976,947,1026,961],
[1002,954,0,1007,972,968,1034,1009],
[974,999,994,0,946,938,1017,997],
[986,1025,1029,1055,0,1016,1052,1028],
[1039,1054,1033,1063,985,0,1010,1016],
[1005,975,967,984,949,991,0,964],
[1030,1040,992,1004,973,985,1037,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 75, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,973,967,1015,958,945,983,930],
[1028,0,981,995,985,990,958,1006],
[1034,1020,0,1005,961,960,1005,972],
[986,1006,996,0,964,975,976,991],
[1043,1016,1040,1037,0,952,1011,974],
[1056,1011,1041,1026,1049,0,984,963],
[1018,1043,996,1025,990,1017,0,969],
[1071,995,1029,1010,1027,1038,1032,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 76, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,990,938,988,930,946,962],
[1000,0,997,1003,1020,1014,1010,1008],
[1011,1004,0,949,982,960,955,965],
[1063,998,1052,0,1024,1016,1028,1021],
[1013,981,1019,977,0,984,986,976],
[1071,987,1041,985,1017,0,964,1009],
[1055,991,1046,973,1015,1037,0,1006],
[1039,993,1036,980,1025,992,995,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 77, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1023,1041,989,1029,968,1032,1053],
[978,0,966,977,948,979,985,1012],
[960,1035,0,1001,1049,1035,1038,1048],
[1012,1024,1000,0,988,1030,997,1033],
[972,1053,952,1013,0,1008,1003,1035],
[1033,1022,966,971,993,0,1083,1047],
[969,1016,963,1004,998,918,0,1000],
[948,989,953,968,966,954,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 78, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,1014,1040,978,1032,985,1003],
[985,0,1001,1016,977,1009,962,978],
[987,1000,0,1011,961,979,959,979],
[961,985,990,0,917,985,1012,973],
[1023,1024,1040,1084,0,1053,994,1029],
[969,992,1022,1016,948,0,971,980],
[1016,1039,1042,989,1007,1030,0,996],
[998,1023,1022,1028,972,1021,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 79, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,1028,1067,1041,1015,993,1047],
[977,0,993,974,997,1009,1001,986],
[973,1008,0,1026,1023,976,1035,978],
[934,1027,975,0,1012,971,1021,973],
[960,1004,978,989,0,995,982,954],
[986,992,1025,1030,1006,0,986,933],
[1008,1000,966,980,1019,1015,0,971],
[954,1015,1023,1028,1047,1068,1030,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 80, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,971,984,970,960,999,985],
[1008,0,964,985,987,1008,1010,985],
[1030,1037,0,1020,985,1000,1061,1042],
[1017,1016,981,0,1009,1018,1023,1000],
[1031,1014,1016,992,0,996,1023,1028],
[1041,993,1001,983,1005,0,1005,984],
[1002,991,940,978,978,996,0,1018],
[1016,1016,959,1001,973,1017,983,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 81, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,997,981,955,957,981,971,984],
[1004,0,969,931,977,976,933,945],
[1020,1032,0,952,986,1025,994,988],
[1046,1070,1049,0,1013,1022,1029,986],
[1044,1024,1015,988,0,1022,1018,1007],
[1020,1025,976,979,979,0,1009,969],
[1030,1068,1007,972,983,992,0,1005],
[1017,1056,1013,1015,994,1032,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 82, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1025,1099,1050,1024,973,1042,1023],
[976,0,992,982,1077,975,1050,1023],
[902,1009,0,1028,911,1052,1004,967],
[951,1019,973,0,927,1067,1003,925],
[977,924,1090,1074,0,1077,1073,1006],
[1028,1026,949,934,924,0,1023,979],
[959,951,997,998,928,978,0,943],
[978,978,1034,1076,995,1022,1058,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 83, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1303,1267,958,1000,1252,817,1056],
[698,0,1040,954,1171,738,899,816],
[734,961,0,775,1088,819,1047,794],
[1043,1047,1226,0,1036,862,999,922],
[1001,830,913,965,0,981,894,824],
[749,1263,1182,1139,1020,0,1179,1350],
[1184,1102,954,1002,1107,822,0,1136],
[945,1185,1207,1079,1177,651,865,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 84, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1022,1025,990,1024,978,984,974],
[979,0,981,983,991,955,976,963],
[976,1020,0,992,995,960,1005,990],
[1011,1018,1009,0,1002,993,1003,1006],
[977,1010,1006,999,0,978,1005,967],
[1023,1046,1041,1008,1023,0,1026,998],
[1017,1025,996,998,996,975,0,991],
[1027,1038,1011,995,1034,1003,1010,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 85, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,998,993,1024,1048,981,1036],
[999,0,1005,965,1017,1001,998,1001],
[1003,996,0,1001,1037,1013,1039,972],
[1008,1036,1000,0,1055,1032,1036,1039],
[977,984,964,946,0,992,1040,968],
[953,1000,988,969,1009,0,1008,1014],
[1020,1003,962,965,961,993,0,992],
[965,1000,1029,962,1033,987,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 86, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,903,895,890,870,976,964,965],
[1098,0,1032,995,1083,1062,1070,1012],
[1106,969,0,970,1023,982,1019,1103],
[1111,1006,1031,0,976,1056,987,1041],
[1131,918,978,1025,0,1003,998,1055],
[1025,939,1019,945,998,0,1078,1061],
[1037,931,982,1014,1003,923,0,1082],
[1036,989,898,960,946,940,919,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 87, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,978,1008,965,1012,921,942,1028],
[1023,0,1007,985,956,962,1004,1040],
[993,994,0,1012,965,970,932,1005],
[1036,1016,989,0,947,947,983,974],
[989,1045,1036,1054,0,1030,1010,1049],
[1080,1039,1031,1054,971,0,1012,1030],
[1059,997,1069,1018,991,989,0,1061],
[973,961,996,1027,952,971,940,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 88, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1030,944,935,1024,1004,1020,995],
[971,0,942,925,933,959,1006,950],
[1057,1059,0,1026,1005,971,1098,976],
[1066,1076,975,0,1020,1034,1060,1009],
[977,1068,996,981,0,1001,1019,1035],
[997,1042,1030,967,1000,0,1041,1033],
[981,995,903,941,982,960,0,1040],
[1006,1051,1025,992,966,968,961,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 89, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,964,1005,980,1009,977,1019,970],
[1037,0,1011,1001,1025,1036,963,1092],
[996,990,0,935,1017,949,977,985],
[1021,1000,1066,0,1090,1052,1083,1054],
[992,976,984,911,0,942,985,1009],
[1024,965,1052,949,1059,0,1038,983],
[982,1038,1024,918,1016,963,0,1047],
[1031,909,1016,947,992,1018,954,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 90, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1021,1014,998,994,1011,1013,1017],
[980,0,991,988,984,975,994,1008],
[987,1010,0,978,989,976,1006,996],
[1003,1013,1023,0,962,976,989,971],
[1007,1017,1012,1039,0,996,1023,1009],
[990,1026,1025,1025,1005,0,1010,993],
[988,1007,995,1012,978,991,0,963],
[984,993,1005,1030,992,1008,1038,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 91, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,995,985,1003,1001,981,993,1002],
[1006,0,1038,1004,1018,995,1041,1026],
[1016,963,0,999,999,976,991,993],
[998,997,1002,0,1024,987,1006,981],
[1000,983,1002,977,0,976,1010,994],
[1020,1006,1025,1014,1025,0,1039,999],
[1008,960,1010,995,991,962,0,995],
[999,975,1008,1020,1007,1002,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 92, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1032,1028,1007,995,1059,1000,1050],
[969,0,1000,954,999,1026,961,1026],
[973,1001,0,973,981,1034,994,1016],
[994,1047,1028,0,1017,1094,968,1018],
[1006,1002,1020,984,0,1018,1008,991],
[942,975,967,907,983,0,925,978],
[1001,1040,1007,1033,993,1076,0,1039],
[951,975,985,983,1010,1023,962,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 93, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,868,886,1024,869,783,900,915],
[1133,0,996,1057,1061,1169,966,1090],
[1115,1005,0,1077,1048,869,998,1004],
[977,944,924,0,986,940,787,892],
[1132,940,953,1015,0,920,940,986],
[1218,832,1132,1061,1081,0,1020,1042],
[1101,1035,1003,1214,1061,981,0,1090],
[1086,911,997,1109,1015,959,911,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 94, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,1010,971,1020,998,993,997],
[996,0,1024,1029,1035,1034,1044,998],
[991,977,0,963,1015,937,1019,1009],
[1030,972,1038,0,1048,998,1003,1039],
[981,966,986,953,0,974,1001,985],
[1003,967,1064,1003,1027,0,1016,1008],
[1008,957,982,998,1000,985,0,1005],
[1004,1003,992,962,1016,993,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 95, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,984,984,1064,1024,1028,1011],
[985,0,958,1033,991,1020,979,938],
[1017,1043,0,994,1029,1012,1060,1030],
[1017,968,1007,0,1063,985,1018,970],
[937,1010,972,938,0,922,972,915],
[977,981,989,1016,1079,0,1023,978],
[973,1022,941,983,1029,978,0,962],
[990,1063,971,1031,1086,1023,1039,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 96, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,985,915,917,977,1037,955,980],
[1016,0,1000,989,993,1073,980,1022],
[1086,1001,0,1034,1011,1090,993,1059],
[1084,1012,967,0,966,1100,1029,1036],
[1024,1008,990,1035,0,1082,1007,1018],
[964,928,911,901,919,0,961,929],
[1046,1021,1008,972,994,1040,0,1019],
[1021,979,942,965,983,1072,982,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 97, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1032,1007,987,968,1038,1066,1033],
[969,0,1022,978,987,1005,1048,1012],
[994,979,0,1011,1026,1047,1068,1029],
[1014,1023,990,0,1011,1022,1051,1018],
[1033,1014,975,990,0,1012,1054,1005],
[963,996,954,979,989,0,1024,987],
[935,953,933,950,947,977,0,962],
[968,989,972,983,996,1014,1039,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 98, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1019,962,989,982,1021,1090,1030],
[982,0,1044,1066,1047,995,1044,1048],
[1039,957,0,1024,955,1046,1048,1022],
[1012,935,977,0,966,996,1049,1044],
[1019,954,1046,1035,0,939,1027,1049],
[980,1006,955,1005,1062,0,978,1021],
[911,957,953,952,974,1023,0,994],
[971,953,979,957,952,980,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 99, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,983,1004,1006,990,1026,989],
[988,0,968,1019,1034,980,972,1001],
[1018,1033,0,992,1020,958,1071,974],
[997,982,1009,0,1071,967,970,1021],
[995,967,981,930,0,943,1013,973],
[1011,1021,1043,1034,1058,0,998,1012],
[975,1029,930,1031,988,1003,0,959],
[1012,1000,1027,980,1028,989,1042,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 100, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,1016,1040,1007,1049,1053,1033],
[1014,0,968,988,998,1012,1037,1021],
[985,1033,0,1020,1036,1034,1037,1027],
[961,1013,981,0,1014,1024,1009,1028],
[994,1003,965,987,0,983,996,1035],
[952,989,967,977,1018,0,1027,1039],
[948,964,964,992,1005,974,0,1023],
[968,980,974,973,966,962,978,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 101, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1060,1099,1076,993,1011,981,1100],
[941,0,957,1010,1094,1026,914,1063],
[902,1044,0,968,930,974,961,974],
[925,991,1033,0,1003,1111,1092,1019],
[1008,907,1071,998,0,983,908,1058],
[990,975,1027,890,1018,0,1006,863],
[1020,1087,1040,909,1093,995,0,1028],
[901,938,1027,982,943,1138,973,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 102, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,1035,986,997,1011,1002,1016],
[998,0,1019,985,979,983,976,988],
[966,982,0,951,951,977,959,996],
[1015,1016,1050,0,1008,998,1012,999],
[1004,1022,1050,993,0,1010,1010,1006],
[990,1018,1024,1003,991,0,1010,1010],
[999,1025,1042,989,991,991,0,984],
[985,1013,1005,1002,995,991,1017,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 103, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1060,954,996,1177,1010,1128,1090],
[941,0,1054,999,1160,938,963,1045],
[1047,947,0,1031,1143,1058,1085,1071],
[1005,1002,970,0,1070,961,1045,1078],
[824,841,858,931,0,902,1019,970],
[991,1063,943,1040,1099,0,1140,1061],
[873,1038,916,956,982,861,0,978],
[911,956,930,923,1031,940,1023,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 104, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,1037,998,1030,1014,1001,1024],
[990,0,1004,967,1009,958,993,981],
[964,997,0,976,1017,981,998,980],
[1003,1034,1025,0,1000,982,1002,962],
[971,992,984,1001,0,940,977,994],
[987,1043,1020,1019,1061,0,1048,991],
[1000,1008,1003,999,1024,953,0,985],
[977,1020,1021,1039,1007,1010,1016,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 105, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,920,922,929,979,977,988],
[1002,0,993,1005,990,1035,986,1026],
[1081,1008,0,981,1057,1060,1013,1099],
[1079,996,1020,0,1007,1024,1096,1058],
[1072,1011,944,994,0,1060,1047,1057],
[1022,966,941,977,941,0,991,1006],
[1024,1015,988,905,954,1010,0,967],
[1013,975,902,943,944,995,1034,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 106, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1010,992,994,967,980,1005,984],
[991,0,963,988,973,978,978,1011],
[1009,1038,0,1006,990,1004,996,1004],
[1007,1013,995,0,1008,1000,1021,1009],
[1034,1028,1011,993,0,987,1026,1004],
[1021,1023,997,1001,1014,0,1011,1018],
[996,1023,1005,980,975,990,0,970],
[1017,990,997,992,997,983,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 107, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,971,983,1030,982,946,993,997],
[1030,0,1007,1054,999,1019,1024,1014],
[1018,994,0,1035,1013,990,962,1038],
[971,947,966,0,988,957,951,931],
[1019,1002,988,1013,0,982,996,1022],
[1055,982,1011,1044,1019,0,986,1028],
[1008,977,1039,1050,1005,1015,0,1018],
[1004,987,963,1070,979,973,983,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 108, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,956,987,978,998,950,977],
[985,0,1013,1016,1002,956,962,999],
[1045,988,0,1000,995,959,963,989],
[1014,985,1001,0,981,1004,936,949],
[1023,999,1006,1020,0,995,981,1021],
[1003,1045,1042,997,1006,0,939,1016],
[1051,1039,1038,1065,1020,1062,0,999],
[1024,1002,1012,1052,980,985,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 109, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,962,1013,974,1017,974,978,1005],
[1039,0,1005,1027,1033,1010,994,1014],
[988,996,0,1033,1029,1033,1019,1030],
[1027,974,968,0,1027,1011,993,1033],
[984,968,972,974,0,952,989,1011],
[1027,991,968,990,1049,0,1016,1073],
[1023,1007,982,1008,1012,985,0,1030],
[996,987,971,968,990,928,971,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 110, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,1000,1025,1040,1089,1023,1020],
[1000,0,994,1054,1014,1056,977,1004],
[1001,1007,0,1004,982,1048,987,1017],
[976,947,997,0,966,1010,993,947],
[961,987,1019,1035,0,1053,992,1031],
[912,945,953,991,948,0,975,964],
[978,1024,1014,1008,1009,1026,0,1029],
[981,997,984,1054,970,1037,972,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 111, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1023,997,1048,1020,960,1020,988],
[978,0,1037,1028,1018,1003,990,975],
[1004,964,0,1033,999,1015,1002,1013],
[953,973,968,0,991,955,963,953],
[981,983,1002,1010,0,1004,1002,1011],
[1041,998,986,1046,997,0,1021,989],
[981,1011,999,1038,999,980,0,999],
[1013,1026,988,1048,990,1012,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 112, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,1013,992,997,966,982,980],
[1000,0,1003,1020,1003,992,995,989],
[988,998,0,1008,989,982,987,988],
[1009,981,993,0,975,990,999,973],
[1004,998,1012,1026,0,1020,1007,1007],
[1035,1009,1019,1011,981,0,997,1018],
[1019,1006,1014,1002,994,1004,0,977],
[1021,1012,1013,1028,994,983,1024,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 113, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,937,991,997,928,920,946],
[1009,0,1026,1001,1014,980,966,1017],
[1064,975,0,1017,1037,978,1010,997],
[1010,1000,984,0,1037,997,929,957],
[1004,987,964,964,0,975,930,939],
[1073,1021,1023,1004,1026,0,965,1031],
[1081,1035,991,1072,1071,1036,0,979],
[1055,984,1004,1044,1062,970,1022,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 114, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,982,1004,988,983,1045,936,956],
[1019,0,1016,1025,999,1050,968,997],
[997,985,0,988,964,1028,1019,1025],
[1013,976,1013,0,1012,1059,932,932],
[1018,1002,1037,989,0,1090,992,997],
[956,951,973,942,911,0,883,954],
[1065,1033,982,1069,1009,1118,0,1039],
[1045,1004,976,1069,1004,1047,962,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 115, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,1044,985,997,979,991,1002],
[996,0,1018,976,1022,983,1027,1010],
[957,983,0,978,990,997,988,965],
[1016,1025,1023,0,1016,1006,1025,942],
[1004,979,1011,985,0,956,1010,925],
[1022,1018,1004,995,1045,0,1048,973],
[1010,974,1013,976,991,953,0,936],
[999,991,1036,1059,1076,1028,1065,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 116, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,1013,981,978,1012,1006,984],
[986,0,1005,1013,999,1027,995,1001],
[988,996,0,982,993,999,996,986],
[1020,988,1019,0,1019,1011,1015,1014],
[1023,1002,1008,982,0,992,1007,1002],
[989,974,1002,990,1009,0,1012,951],
[995,1006,1005,986,994,989,0,941],
[1017,1000,1015,987,999,1050,1060,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 117, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1027,1022,948,1076,956,967,991],
[974,0,1013,938,1015,954,1021,934],
[979,988,0,970,1030,955,998,950],
[1053,1063,1031,0,1078,1041,1006,998],
[925,986,971,923,0,989,968,903],
[1045,1047,1046,960,1012,0,1004,1042],
[1034,980,1003,995,1033,997,0,955],
[1010,1067,1051,1003,1098,959,1046,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 118, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1181,944,1061,899,1103,1004,931],
[820,0,1095,926,773,1011,1100,1205],
[1057,906,0,833,753,1094,970,958],
[940,1075,1168,0,1037,1312,1135,1282],
[1102,1228,1248,964,0,1281,1259,972],
[898,990,907,689,720,0,964,1076],
[997,901,1031,866,742,1037,0,935],
[1070,796,1043,719,1029,925,1066,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 119, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1030,1058,1058,1054,981,1059,1026],
[971,0,1071,1040,1037,968,994,984],
[943,930,0,992,1035,946,987,960],
[943,961,1009,0,1021,938,957,946],
[947,964,966,980,0,947,972,953],
[1020,1033,1055,1063,1054,0,1038,993],
[942,1007,1014,1044,1029,963,0,968],
[975,1017,1041,1055,1048,1008,1033,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 120, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1025,1020,985,1053,1060,1017,1044],
[976,0,1008,950,1010,963,938,1011],
[981,993,0,1004,1009,1024,1008,1033],
[1016,1051,997,0,1036,1007,995,1045],
[948,991,992,965,0,1000,961,994],
[941,1038,977,994,1001,0,954,996],
[984,1063,993,1006,1040,1047,0,1042],
[957,990,968,956,1007,1005,959,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 121, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,963,985,974,960,1045,976,960],
[1038,0,988,970,987,989,964,1013],
[1016,1013,0,963,953,1043,961,978],
[1027,1031,1038,0,999,1024,1045,1015],
[1041,1014,1048,1002,0,994,1099,1065],
[956,1012,958,977,1007,0,979,984],
[1025,1037,1040,956,902,1022,0,1045],
[1041,988,1023,986,936,1017,956,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 122, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1023,1016,1005,975,997,1011,1009],
[978,0,963,986,955,962,994,939],
[985,1038,0,1042,1018,1000,1032,982],
[996,1015,959,0,996,988,1013,969],
[1026,1046,983,1005,0,1020,990,1017],
[1004,1039,1001,1013,981,0,1034,978],
[990,1007,969,988,1011,967,0,954],
[992,1062,1019,1032,984,1023,1047,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 123, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,1020,1056,1002,903,973,984],
[1011,0,1070,1067,1037,1003,997,1018],
[981,931,0,997,951,913,911,894],
[945,934,1004,0,981,938,961,967],
[999,964,1050,1020,0,908,918,965],
[1098,998,1088,1063,1093,0,1010,1076],
[1028,1004,1090,1040,1083,991,0,1037],
[1017,983,1107,1034,1036,925,964,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 124, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,943,980,1224,943,850,1004,957],
[1058,0,1095,1080,812,972,1136,953],
[1021,906,0,1142,1064,987,898,1035],
[777,921,859,0,801,903,833,880],
[1058,1189,937,1200,0,1117,1047,1101],
[1151,1029,1014,1098,884,0,1110,995],
[997,865,1103,1168,954,891,0,972],
[1044,1048,966,1121,900,1006,1029,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 125, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1066,934,943,987,1039,1074,930],
[935,0,838,816,840,958,829,898],
[1067,1163,0,974,1032,1109,1065,1109],
[1058,1185,1027,0,1003,1017,959,1016],
[1014,1161,969,998,0,1025,1031,989],
[962,1043,892,984,976,0,1061,965],
[927,1172,936,1042,970,940,0,962],
[1071,1103,892,985,1012,1036,1039,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 126, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1038,1004,991,1048,1012,1053,1047],
[963,0,959,968,1021,971,949,923],
[997,1042,0,971,1061,899,1041,975],
[1010,1033,1030,0,1040,956,982,955],
[953,980,940,961,0,953,937,942],
[989,1030,1102,1045,1048,0,1038,985],
[948,1052,960,1019,1064,963,0,975],
[954,1078,1026,1046,1059,1016,1026,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 127, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,978,1004,1023,1035,968,977,978],
[1023,0,1045,1050,1031,985,1020,1009],
[997,956,0,1008,1023,1003,969,994],
[978,951,993,0,991,973,952,990],
[966,970,978,1010,0,963,980,1005],
[1033,1016,998,1028,1038,0,1008,1020],
[1024,981,1032,1049,1021,993,0,997],
[1023,992,1007,1011,996,981,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 128, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1063,1024,992,995,971,987,991],
[938,0,988,1018,974,985,992,973],
[977,1013,0,1016,975,1015,1046,977],
[1009,983,985,0,1010,1000,1026,1009],
[1006,1027,1026,991,0,1040,1039,1014],
[1030,1016,986,1001,961,0,1044,993],
[1014,1009,955,975,962,957,0,973],
[1010,1028,1024,992,987,1008,1028,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 129, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,974,999,996,929,975,979,957],
[1027,0,999,1028,1008,999,1026,1014],
[1002,1002,0,1020,1020,996,1006,1013],
[1005,973,981,0,987,968,1043,968],
[1072,993,981,1014,0,1039,1006,1004],
[1026,1002,1005,1033,962,0,1033,998],
[1022,975,995,958,995,968,0,989],
[1044,987,988,1033,997,1003,1012,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 130, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,1062,1011,1036,1045,1021,1019],
[1011,0,1035,976,1036,985,986,1047],
[939,966,0,935,1001,1013,1028,982],
[990,1025,1066,0,1055,1036,984,1090],
[965,965,1000,946,0,988,972,1015],
[956,1016,988,965,1013,0,991,1061],
[980,1015,973,1017,1029,1010,0,1017],
[982,954,1019,911,986,940,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 131, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,967,1020,1002,1031,1022,1003],
[981,0,996,1033,973,989,977,967],
[1034,1005,0,1030,997,1040,1029,988],
[981,968,971,0,977,974,993,1011],
[999,1028,1004,1024,0,1012,1018,1030],
[970,1012,961,1027,989,0,982,981],
[979,1024,972,1008,983,1019,0,982],
[998,1034,1013,990,971,1020,1019,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 132, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,1055,958,941,974,935,884],
[1022,0,1023,943,889,923,987,926],
[946,978,0,920,891,912,966,949],
[1043,1058,1081,0,995,1030,1051,1006],
[1060,1112,1110,1006,0,982,1019,1111],
[1027,1078,1089,971,1019,0,1045,988],
[1066,1014,1035,950,982,956,0,956],
[1117,1075,1052,995,890,1013,1045,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 133, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1104,999,1032,1005,1002,937,1063],
[897,0,987,1008,951,945,919,916],
[1002,1014,0,1036,959,1009,1061,1045],
[969,993,965,0,956,940,920,1045],
[996,1050,1042,1045,0,998,1074,1006],
[999,1056,992,1061,1003,0,936,1020],
[1064,1082,940,1081,927,1065,0,1051],
[938,1085,956,956,995,981,950,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 134, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,1035,1049,1013,1012,1070,991],
[988,0,971,1023,1020,1010,1036,936],
[966,1030,0,1027,1032,980,1041,949],
[952,978,974,0,998,951,1032,966],
[988,981,969,1003,0,991,1062,978],
[989,991,1021,1050,1010,0,1050,1015],
[931,965,960,969,939,951,0,912],
[1010,1065,1052,1035,1023,986,1089,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 135, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1021,1025,1012,991,1011,1010,1018],
[980,0,1011,987,988,968,968,998],
[976,990,0,1000,998,983,981,982],
[989,1014,1001,0,973,974,1001,1028],
[1010,1013,1003,1028,0,979,1007,996],
[990,1033,1018,1027,1022,0,1025,1006],
[991,1033,1020,1000,994,976,0,991],
[983,1003,1019,973,1005,995,1010,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 136, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,978,996,1039,1030,982,1016,1017],
[1023,0,1053,1009,1037,1029,1028,985],
[1005,948,0,1016,982,982,974,993],
[962,992,985,0,1019,978,1010,994],
[971,964,1019,982,0,1017,1050,1000],
[1019,972,1019,1023,984,0,1066,1002],
[985,973,1027,991,951,935,0,980],
[984,1016,1008,1007,1001,999,1021,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 137, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1030,994,962,971,999,984,1045],
[971,0,963,1018,975,994,983,967],
[1007,1038,0,961,1043,1086,1028,1062],
[1039,983,1040,0,1041,1002,1032,1016],
[1030,1026,958,960,0,1014,1006,1037],
[1002,1007,915,999,987,0,1072,1020],
[1017,1018,973,969,995,929,0,1025],
[956,1034,939,985,964,981,976,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 138, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,882,1019,985,971,1027,977,998],
[1119,0,1073,1047,1005,1012,984,966],
[982,928,0,939,981,1004,916,926],
[1016,954,1062,0,1000,1072,1001,1042],
[1030,996,1020,1001,0,1137,1050,957],
[974,989,997,929,864,0,1029,921],
[1024,1017,1085,1000,951,972,0,952],
[1003,1035,1075,959,1044,1080,1049,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 139, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,991,1042,1000,938,960,938,994],
[1010,0,1016,986,961,972,977,1015],
[959,985,0,974,954,982,923,961],
[1001,1015,1027,0,1008,1001,981,1020],
[1063,1040,1047,993,0,983,1038,1005],
[1041,1029,1019,1000,1018,0,962,996],
[1063,1024,1078,1020,963,1039,0,1021],
[1007,986,1040,981,996,1005,980,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 140, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,1000,1043,1044,1022,976,975],
[1024,0,1025,1020,994,1001,989,1069],
[1001,976,0,974,1017,994,983,1015],
[958,981,1027,0,1027,1028,1004,1013],
[957,1007,984,974,0,1051,999,1007],
[979,1000,1007,973,950,0,993,1033],
[1025,1012,1018,997,1002,1008,0,1081],
[1026,932,986,988,994,968,920,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 141, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,976,982,987,950,982,987,1010],
[1025,0,962,993,962,962,956,984],
[1019,1039,0,1048,974,996,975,976],
[1014,1008,953,0,933,932,941,986],
[1051,1039,1027,1068,0,955,1047,1003],
[1019,1039,1005,1069,1046,0,999,1031],
[1014,1045,1026,1060,954,1002,0,1003],
[991,1017,1025,1015,998,970,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 142, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1111,1044,866,1102,952,1006,947],
[890,0,819,1007,879,1002,887,842],
[957,1182,0,983,959,1057,922,1019],
[1135,994,1018,0,937,1079,930,1037],
[899,1122,1042,1064,0,976,992,1054],
[1049,999,944,922,1025,0,996,1001],
[995,1114,1079,1071,1009,1005,0,1109],
[1054,1159,982,964,947,1000,892,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 143, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,990,983,1014,1001,975,973,1017],
[1011,0,1013,969,972,992,993,972],
[1018,988,0,1001,974,977,945,965],
[987,1032,1000,0,979,1004,979,974],
[1000,1029,1027,1022,0,1006,995,988],
[1026,1009,1024,997,995,0,1005,992],
[1028,1008,1056,1022,1006,996,0,1005],
[984,1029,1036,1027,1013,1009,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 144, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,971,1011,1019,1001,1022,1028],
[995,0,975,955,935,955,987,972],
[1030,1026,0,1034,1047,1012,1026,983],
[990,1046,967,0,1032,1021,1024,1034],
[982,1066,954,969,0,1036,997,976],
[1000,1046,989,980,965,0,1034,1051],
[979,1014,975,977,1004,967,0,1023],
[973,1029,1018,967,1025,950,978,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 145, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1039,1011,1031,977,1022,1029,1040],
[962,0,969,965,981,1065,1004,1009],
[990,1032,0,1018,975,1053,1006,1077],
[970,1036,983,0,990,1018,984,1012],
[1024,1020,1026,1011,0,996,1002,1030],
[979,936,948,983,1005,0,991,968],
[972,997,995,1017,999,1010,0,1035],
[961,992,924,989,971,1033,966,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 146, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1023,1052,1001,1009,1019,1029,994],
[978,0,1025,971,978,983,1021,978],
[949,976,0,966,975,968,989,961],
[1000,1030,1035,0,1028,1026,1056,1010],
[992,1023,1026,973,0,1031,1006,1007],
[982,1018,1033,975,970,0,993,982],
[972,980,1012,945,995,1008,0,996],
[1007,1023,1040,991,994,1019,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 147, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,1012,821,1026,958,944,1104],
[977,0,1048,970,1042,1036,1091,1119],
[989,953,0,939,1005,937,910,1006],
[1180,1031,1062,0,1016,1064,943,1108],
[975,959,996,985,0,1015,962,1075],
[1043,965,1064,937,986,0,1042,1186],
[1057,910,1091,1058,1039,959,0,1142],
[897,882,995,893,926,815,859,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 148, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1031,1006,980,1031,1052,1006,994],
[970,0,982,977,981,1004,949,998],
[995,1019,0,991,1012,1059,1019,998],
[1021,1024,1010,0,1021,1053,990,997],
[970,1020,989,980,0,1003,987,987],
[949,997,942,948,998,0,963,1007],
[995,1052,982,1011,1014,1038,0,1022],
[1007,1003,1003,1004,1014,994,979,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 149, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1037,982,1038,1003,1044,1038,1041],
[964,0,985,986,970,976,994,986],
[1019,1016,0,1039,971,1013,1038,998],
[963,1015,962,0,974,943,969,988],
[998,1031,1030,1027,0,973,1025,1007],
[957,1025,988,1058,1028,0,995,995],
[963,1007,963,1032,976,1006,0,980],
[960,1015,1003,1013,994,1006,1021,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 150, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1022,1000,996,999,985,1031,1003],
[979,0,1004,988,999,971,979,1020],
[1001,997,0,1024,959,1022,1033,963],
[1005,1013,977,0,986,982,1026,964],
[1002,1002,1042,1015,0,1005,1031,998],
[1016,1030,979,1019,996,0,1045,968],
[970,1022,968,975,970,956,0,947],
[998,981,1038,1037,1003,1033,1054,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 151, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,966,987,985,999,964,1008,996],
[1035,0,992,1011,1013,1039,1023,1008],
[1014,1009,0,1007,1018,997,997,989],
[1016,990,994,0,1015,975,1012,985],
[1002,988,983,986,0,969,1030,970],
[1037,962,1004,1026,1032,0,1041,1011],
[993,978,1004,989,971,960,0,995],
[1005,993,1012,1016,1031,990,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 152, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,1058,1013,1049,1002,957,989],
[999,0,1122,986,1043,993,1012,1028],
[943,879,0,920,966,942,906,952],
[988,1015,1081,0,1055,964,988,1010],
[952,958,1035,946,0,934,942,975],
[999,1008,1059,1037,1067,0,1061,1046],
[1044,989,1095,1013,1059,940,0,1018],
[1012,973,1049,991,1026,955,983,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 153, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,1011,1051,994,1002,1007,1008],
[999,0,975,1015,967,1003,970,986],
[990,1026,0,1008,973,990,1020,990],
[950,986,993,0,1000,991,963,981],
[1007,1034,1028,1001,0,1001,997,1001],
[999,998,1011,1010,1000,0,988,995],
[994,1031,981,1038,1004,1013,0,998],
[993,1015,1011,1020,1000,1006,1003,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 154, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1186,1051,1065,1023,1129,998,1152],
[815,0,878,913,883,915,951,1020],
[950,1123,0,1062,1020,1006,914,1016],
[936,1088,939,0,901,936,984,964],
[978,1118,981,1100,0,958,972,1084],
[872,1086,995,1065,1043,0,943,1132],
[1003,1050,1087,1017,1029,1058,0,975],
[849,981,985,1037,917,869,1026,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 155, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1068,963,976,973,1019,1043,990],
[933,0,941,956,1011,975,988,1010],
[1038,1060,0,990,1019,990,1038,1029],
[1025,1045,1011,0,988,1017,1014,1035],
[1028,990,982,1013,0,1055,1033,1002],
[982,1026,1011,984,946,0,993,1011],
[958,1013,963,987,968,1008,0,981],
[1011,991,972,966,999,990,1020,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 156, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,961,961,982,975,1004,1007,977],
[1040,0,1002,1028,985,1031,1033,1026],
[1040,999,0,995,1018,1002,1017,1006],
[1019,973,1006,0,1042,1003,1050,1027],
[1026,1016,983,959,0,1015,986,993],
[997,970,999,998,986,0,995,973],
[994,968,984,951,1015,1006,0,984],
[1024,975,995,974,1008,1028,1017,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 157, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,995,993,995,967,958,1012],
[992,0,1010,982,1032,978,975,993],
[1006,991,0,977,990,994,963,1018],
[1008,1019,1024,0,1011,975,973,1015],
[1006,969,1011,990,0,960,949,968],
[1034,1023,1007,1026,1041,0,945,1022],
[1043,1026,1038,1028,1052,1056,0,995],
[989,1008,983,986,1033,979,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 158, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,933,1049,924,962,966,974,1028],
[1068,0,1053,1055,1062,994,1062,1038],
[952,948,0,1013,861,924,937,958],
[1077,946,988,0,936,910,1015,1038],
[1039,939,1140,1065,0,1030,1012,1107],
[1035,1007,1077,1091,971,0,945,1046],
[1027,939,1064,986,989,1056,0,1021],
[973,963,1043,963,894,955,980,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 159, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,968,1033,1006,1071,1049,1064,1035],
[1033,0,1006,974,1061,1009,1048,1037],
[968,995,0,995,1002,1038,1015,1002],
[995,1027,1006,0,1019,1028,994,992],
[930,940,999,982,0,990,982,983],
[952,992,963,973,1011,0,997,997],
[937,953,986,1007,1019,1004,0,983],
[966,964,999,1009,1018,1004,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 160, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1173,1322,899,883,1100,1084,1079],
[828,0,1001,990,898,941,887,1249],
[679,1000,0,896,897,959,765,938],
[1102,1011,1105,0,1002,875,1109,1071],
[1118,1103,1104,999,0,993,1072,1199],
[901,1060,1042,1126,1008,0,988,1007],
[917,1114,1236,892,929,1013,0,1198],
[922,752,1063,930,802,994,803,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 161, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1022,989,1052,990,1038,964,1005],
[979,0,945,1011,966,967,977,970],
[1012,1056,0,1087,1011,1045,1010,998],
[949,990,914,0,956,984,951,958],
[1011,1035,990,1045,0,1024,1022,989],
[963,1034,956,1017,977,0,972,986],
[1037,1024,991,1050,979,1029,0,1007],
[996,1031,1003,1043,1012,1015,994,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 162, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1126,1126,1056,1063,926,1127,1044],
[875,0,962,901,973,920,1198,1001],
[875,1039,0,1028,994,866,1167,892],
[945,1100,973,0,974,859,1045,967],
[938,1028,1007,1027,0,1066,962,1033],
[1075,1081,1135,1142,935,0,1151,1036],
[874,803,834,956,1039,850,0,971],
[957,1000,1109,1034,968,965,1030,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 163, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1018,1005,981,1040,1023,1003,1044],
[983,0,1024,1020,1042,971,896,1067],
[996,977,0,1007,1066,981,894,1019],
[1020,981,994,0,987,1012,926,941],
[961,959,935,1014,0,964,954,1082],
[978,1030,1020,989,1037,0,964,1059],
[998,1105,1107,1075,1047,1037,0,1103],
[957,934,982,1060,919,942,898,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 164, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,986,996,1005,1071,1046,1020],
[985,0,959,999,999,1051,1081,1012],
[1015,1042,0,1045,991,1016,1032,993],
[1005,1002,956,0,998,1002,1007,1005],
[996,1002,1010,1003,0,1041,1050,959],
[930,950,985,999,960,0,985,984],
[955,920,969,994,951,1016,0,949],
[981,989,1008,996,1042,1017,1052,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 165, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1052,959,961,1008,1003,892,1006],
[949,0,1069,947,1016,931,893,879],
[1042,932,0,883,1011,899,911,892],
[1040,1054,1118,0,1085,1080,1000,1083],
[993,985,990,916,0,1012,974,978],
[998,1070,1102,921,989,0,997,937],
[1109,1108,1090,1001,1027,1004,0,997],
[995,1122,1109,918,1023,1064,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 166, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,997,927,966,891,987,975],
[995,0,984,907,960,977,954,974],
[1004,1017,0,939,985,955,993,1051],
[1074,1094,1062,0,1048,1002,999,1036],
[1035,1041,1016,953,0,965,1006,1046],
[1110,1024,1046,999,1036,0,1030,1027],
[1014,1047,1008,1002,995,971,0,1020],
[1026,1027,950,965,955,974,981,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 167, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,975,996,1002,1026,1014,996,1000],
[1026,0,1015,1007,994,1017,999,986],
[1005,986,0,936,985,1006,954,970],
[999,994,1065,0,1017,1009,984,1025],
[975,1007,1016,984,0,997,1017,973],
[987,984,995,992,1004,0,1009,986],
[1005,1002,1047,1017,984,992,0,1015],
[1001,1015,1031,976,1028,1015,986,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 168, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,829,933,1124,1014,1135,944,1063],
[1172,0,1037,1285,1040,1280,1102,985],
[1068,964,0,1193,969,1190,1043,1036],
[877,716,808,0,771,1011,938,875],
[987,961,1032,1230,0,1164,1065,1109],
[866,721,811,990,837,0,769,928],
[1057,899,958,1063,936,1232,0,955],
[938,1016,965,1126,892,1073,1046,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 169, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,1011,1005,993,1017,1023,998],
[1000,0,997,997,985,1020,987,981],
[990,1004,0,991,1023,1030,987,1056],
[996,1004,1010,0,973,1001,1001,1041],
[1008,1016,978,1028,0,1009,979,1019],
[984,981,971,1000,992,0,966,981],
[978,1014,1014,1000,1022,1035,0,1054],
[1003,1020,945,960,982,1020,947,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 170, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1005,966,969,990,1012,990,1022],
[996,0,983,1013,1021,979,1003,1012],
[1035,1018,0,1009,1012,991,1011,1019],
[1032,988,992,0,1021,991,1018,1020],
[1011,980,989,980,0,974,990,1020],
[989,1022,1010,1010,1027,0,1003,1040],
[1011,998,990,983,1011,998,0,1024],
[979,989,982,981,981,961,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 171, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,1044,950,1014,985,1076,1088],
[986,0,1036,971,1057,1014,994,917],
[957,965,0,998,1115,1024,1109,1057],
[1051,1030,1003,0,1038,942,1074,1009],
[987,944,886,963,0,986,1045,1040],
[1016,987,977,1059,1015,0,1046,1037],
[925,1007,892,927,956,955,0,811],
[913,1084,944,992,961,964,1190,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 172, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1023,1043,1001,986,1043,1010,1062],
[978,0,971,981,1000,1010,978,1043],
[958,1030,0,971,966,990,988,1007],
[1000,1020,1030,0,1015,991,1009,1054],
[1015,1001,1035,986,0,1002,986,1048],
[958,991,1011,1010,999,0,992,1027],
[991,1023,1013,992,1015,1009,0,1022],
[939,958,994,947,953,974,979,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 173, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,1037,993,1020,966,983,1021],
[1013,0,1018,1012,1064,972,1053,1044],
[964,983,0,957,1026,979,1001,983],
[1008,989,1044,0,1048,1006,1032,1018],
[981,937,975,953,0,944,978,970],
[1035,1029,1022,995,1057,0,1025,1007],
[1018,948,1000,969,1023,976,0,998],
[980,957,1018,983,1031,994,1003,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 174, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,975,1014,962,1001,1011,1020,974],
[1026,0,982,993,1027,1000,1025,1010],
[987,1019,0,973,1036,1003,989,1017],
[1039,1008,1028,0,1030,987,1020,1027],
[1000,974,965,971,0,987,974,1004],
[990,1001,998,1014,1014,0,1023,1037],
[981,976,1012,981,1027,978,0,1001],
[1027,991,984,974,997,964,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 175, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,998,1005,1030,997,1019,990],
[987,0,1030,996,1000,1018,1013,992],
[1003,971,0,979,996,963,979,998],
[996,1005,1022,0,1042,1017,1020,1020],
[971,1001,1005,959,0,960,1005,972],
[1004,983,1038,984,1041,0,1019,1014],
[982,988,1022,981,996,982,0,1008],
[1011,1009,1003,981,1029,987,993,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 176, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,974,944,967,955,979,1022,1030],
[1027,0,979,985,984,1017,1036,1042],
[1057,1022,0,1052,940,986,1019,1065],
[1034,1016,949,0,1072,1048,1041,1032],
[1046,1017,1061,929,0,1033,1040,1083],
[1022,984,1015,953,968,0,993,1004],
[979,965,982,960,961,1008,0,1011],
[971,959,936,969,918,997,990,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 177, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,1011,969,1008,955,1000,981],
[1005,0,969,952,990,960,976,970],
[990,1032,0,994,993,1008,1003,1013],
[1032,1049,1007,0,1049,997,1019,1027],
[993,1011,1008,952,0,952,978,994],
[1046,1041,993,1004,1049,0,1034,1001],
[1001,1025,998,982,1023,967,0,991],
[1020,1031,988,974,1007,1000,1010,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 178, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1017,951,998,928,990,935,989],
[984,0,949,996,1019,1019,955,949],
[1050,1052,0,1039,1004,994,1043,984],
[1003,1005,962,0,979,993,985,968],
[1073,982,997,1022,0,980,967,989],
[1011,982,1007,1008,1021,0,981,1006],
[1066,1046,958,1016,1034,1020,0,1007],
[1012,1052,1017,1033,1012,995,994,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 179, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,968,970,957,951,969,923,966],
[1033,0,997,993,988,1022,989,1018],
[1031,1004,0,1020,1021,1009,991,1022],
[1044,1008,981,0,986,1004,985,991],
[1050,1013,980,1015,0,1002,982,1039],
[1032,979,992,997,999,0,1007,984],
[1078,1012,1010,1016,1019,994,0,997],
[1035,983,979,1010,962,1017,1004,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 180, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1049,1147,1104,1197,1116,1162,989],
[952,0,1045,1032,1024,974,1023,987],
[854,956,0,957,953,860,987,850],
[897,969,1044,0,975,913,1019,846],
[804,977,1048,1026,0,952,1071,888],
[885,1027,1141,1088,1049,0,1011,1007],
[839,978,1014,982,930,990,0,931],
[1012,1014,1151,1155,1113,994,1070,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 181, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1023,1014,1003,955,982,988,997],
[978,0,1007,948,983,977,938,987],
[987,994,0,964,979,984,968,993],
[998,1053,1037,0,1009,973,1011,1001],
[1046,1018,1022,992,0,1024,968,1007],
[1019,1024,1017,1028,977,0,975,983],
[1013,1063,1033,990,1033,1026,0,994],
[1004,1014,1008,1000,994,1018,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 182, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,990,979,1041,1043,1026,1022],
[995,0,1027,1006,1051,1009,995,1041],
[1011,974,0,1000,1018,1026,999,1019],
[1022,995,1001,0,1033,1046,991,1057],
[960,950,983,968,0,983,961,1017],
[958,992,975,955,1018,0,950,985],
[975,1006,1002,1010,1040,1051,0,1037],
[979,960,982,944,984,1016,964,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 183, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1039,981,1004,1011,1011,1050,995],
[962,0,967,977,980,979,1006,932],
[1020,1034,0,1006,999,1012,1043,1005],
[997,1024,995,0,960,985,993,959],
[990,1021,1002,1041,0,1004,1018,959],
[990,1022,989,1016,997,0,1020,965],
[951,995,958,1008,983,981,0,945],
[1006,1069,996,1042,1042,1036,1056,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 184, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,1003,1021,982,999,1047,1003],
[1008,0,1017,975,990,1033,1015,976],
[998,984,0,999,988,1012,1031,1003],
[980,1026,1002,0,981,1024,1020,976],
[1019,1011,1013,1020,0,1031,1013,982],
[1002,968,989,977,970,0,1036,989],
[954,986,970,981,988,965,0,962],
[998,1025,998,1025,1019,1012,1039,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 185, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1230,894,1065,933,920,747,813],
[771,0,1034,887,1037,1077,799,988],
[1107,967,0,1041,1289,1382,1170,1070],
[936,1114,960,0,1110,1347,1310,1079],
[1068,964,712,891,0,1225,1197,1068],
[1081,924,619,654,776,0,1027,624],
[1254,1202,831,691,804,974,0,873],
[1188,1013,931,922,933,1377,1128,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 186, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1059,1014,983,961,853,1031,1053],
[942,0,950,853,872,1013,1022,991],
[987,1051,0,1000,859,971,1092,931],
[1018,1148,1001,0,1020,986,1060,957],
[1040,1129,1142,981,0,1056,1085,1021],
[1148,988,1030,1015,945,0,1067,1012],
[970,979,909,941,916,934,0,899],
[948,1010,1070,1044,980,989,1102,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 187, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,940,942,944,1007,976,961,984],
[1061,0,1033,999,1045,1024,1021,1016],
[1059,968,0,1032,1051,1032,995,1015],
[1057,1002,969,0,1038,1005,1028,995],
[994,956,950,963,0,964,963,972],
[1025,977,969,996,1037,0,992,978],
[1040,980,1006,973,1038,1009,0,994],
[1017,985,986,1006,1029,1023,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 188, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,1090,990,1078,1085,1006,1043],
[988,0,1106,1008,1009,1051,995,1061],
[911,895,0,959,890,976,951,931],
[1011,993,1042,0,1031,1019,1074,1010],
[923,992,1111,970,0,999,987,1025],
[916,950,1025,982,1002,0,1037,989],
[995,1006,1050,927,1014,964,0,1040],
[958,940,1070,991,976,1012,961,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 189, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1090,1030,943,951,921,1040,1074],
[911,0,968,953,929,918,1032,971],
[971,1033,0,897,1001,979,981,947],
[1058,1048,1104,0,988,1028,1032,1023],
[1050,1072,1000,1013,0,1001,1029,1060],
[1080,1083,1022,973,1000,0,1108,1059],
[961,969,1020,969,972,893,0,969],
[927,1030,1054,978,941,942,1032,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 190, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,928,994,953,947,978,996,945],
[1073,0,1051,989,1027,980,1004,1010],
[1007,950,0,918,954,978,992,985],
[1048,1012,1083,0,997,1050,994,1039],
[1054,974,1047,1004,0,1021,1010,1041],
[1023,1021,1023,951,980,0,1042,1030],
[1005,997,1009,1007,991,959,0,976],
[1056,991,1016,962,960,971,1025,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 191, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,910,997,989,957,966,985],
[1008,0,1046,1000,1052,1060,1055,1074],
[1091,955,0,1002,1050,1030,997,996],
[1004,1001,999,0,1005,968,996,997],
[1012,949,951,996,0,963,998,969],
[1044,941,971,1033,1038,0,1031,1049],
[1035,946,1004,1005,1003,970,0,1015],
[1016,927,1005,1004,1032,952,986,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 192, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,971,1024,969,992,1019,983,964],
[1030,0,1016,986,999,1016,1005,992],
[977,985,0,952,990,1011,956,1001],
[1032,1015,1049,0,1031,1044,986,1014],
[1009,1002,1011,970,0,1027,1012,949],
[982,985,990,957,974,0,979,963],
[1018,996,1045,1015,989,1022,0,1013],
[1037,1009,1000,987,1052,1038,988,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 193, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1004,960,968,1021,1022,973,1028],
[997,0,966,973,1034,1028,1018,1032],
[1041,1035,0,985,1021,1025,1022,1041],
[1033,1028,1016,0,1024,999,1001,1019],
[980,967,980,977,0,953,935,973],
[979,973,976,1002,1048,0,967,1022],
[1028,983,979,1000,1066,1034,0,1018],
[973,969,960,982,1028,979,983,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 194, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1077,967,1052,1045,1067,1021,1033],
[924,0,942,961,1001,956,953,976],
[1034,1059,0,991,1075,981,1009,1020],
[949,1040,1010,0,1000,970,1010,1009],
[956,1000,926,1001,0,976,941,1000],
[934,1045,1020,1031,1025,0,1073,974],
[980,1048,992,991,1060,928,0,1042],
[968,1025,981,992,1001,1027,959,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 195, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,1019,1030,1019,989,1020,994],
[985,0,990,1004,970,999,983,981],
[982,1011,0,990,993,1026,986,993],
[971,997,1011,0,981,983,1007,957],
[982,1031,1008,1020,0,997,1014,989],
[1012,1002,975,1018,1004,0,1008,1012],
[981,1018,1015,994,987,993,0,985],
[1007,1020,1008,1044,1012,989,1016,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 196, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1080,917,1026,939,1032,952,1167],
[921,0,861,1047,863,981,866,924],
[1084,1140,0,983,983,1051,1071,1171],
[975,954,1018,0,939,992,927,1103],
[1062,1138,1018,1062,0,1121,984,1153],
[969,1020,950,1009,880,0,828,1083],
[1049,1135,930,1074,1017,1173,0,992],
[834,1077,830,898,848,918,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 197, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,1024,993,960,979,976,1006],
[1007,0,1037,988,1005,1023,1009,1004],
[977,964,0,955,942,947,982,997],
[1008,1013,1046,0,1022,997,1027,1032],
[1041,996,1059,979,0,1037,1042,1032],
[1022,978,1054,1004,964,0,1004,1013],
[1025,992,1019,974,959,997,0,991],
[995,997,1004,969,969,988,1010,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 198, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,917,995,1137,1043,1127,1143,1108],
[1084,0,1044,1031,977,1035,1119,1057],
[1006,957,0,1055,803,1038,1186,1127],
[864,970,946,0,1036,1067,1131,921],
[958,1024,1198,965,0,1129,1182,1127],
[874,966,963,934,872,0,985,1064],
[858,882,815,870,819,1016,0,945],
[893,944,874,1080,874,937,1056,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 199, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,955,948,891,955,824,966,911],
[1046,0,1138,1092,891,1269,1192,1032],
[1053,863,0,950,856,1216,1069,832],
[1110,909,1051,0,948,1109,1141,705],
[1046,1110,1145,1053,0,1288,1246,971],
[1177,732,785,892,713,0,998,917],
[1035,809,932,860,755,1003,0,736],
[1090,969,1169,1296,1030,1084,1265,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om, float("inf")) 
    start_time = time.time()
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([8, 2001, 200, "ME-BB", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebb/mebb_8_2001.csv", index=False, header=False)