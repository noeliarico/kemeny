
import numpy as np
import pandas as pd
import time
from kemeny import algorithms as alg
from kemeny import sc

rep = 1
results = np.zeros(0).reshape(0,7+rep)

##############################################################
om = np.array([
[0,1053,1051,1024,1061,933,963,960,1000,1043,1000],
[948,0,957,965,961,900,1010,1010,980,952,960],
[950,1044,0,975,1000,931,962,903,973,1032,978],
[977,1036,1026,0,1102,1031,1023,1055,1088,1043,1078],
[940,1040,1001,899,0,846,989,1003,918,999,944],
[1068,1101,1070,970,1155,0,1043,1041,1055,1116,1019],
[1038,991,1039,978,1012,958,0,976,995,992,991],
[1041,991,1098,946,998,960,1025,0,1004,1022,1002],
[1001,1021,1028,913,1083,946,1006,997,0,1021,958],
[958,1049,969,958,1002,885,1009,979,980,0,1010],
[1001,1041,1023,923,1057,982,1010,999,1043,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 1, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,985,1040,1031,982,1011,997,1017,1012,1023,1007],
[1016,0,1020,979,1016,998,1018,1020,1041,1016,1026],
[961,981,0,1019,1016,998,1011,984,1005,990,1005],
[970,1022,982,0,1019,1005,978,1000,1021,977,1014],
[1019,985,985,982,0,1024,988,1037,1033,1018,1018],
[990,1003,1003,996,977,0,973,1020,981,983,999],
[1004,983,990,1023,1013,1028,0,1027,1044,990,1025],
[984,981,1017,1001,964,981,974,0,1007,983,1032],
[989,960,996,980,968,1020,957,994,0,945,1012],
[978,985,1011,1024,983,1018,1011,1018,1056,0,1030],
[994,975,996,987,983,1002,976,969,989,971,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 2, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,989,991,998,1006,988,1013,1030,1012,998,960],
[1012,0,1032,997,1056,1012,1031,1032,1017,1074,1011],
[1010,969,0,956,1003,960,992,1030,1005,1052,959],
[1003,1004,1045,0,1048,992,1068,1053,996,1056,1026],
[995,945,998,953,0,965,1007,1042,975,1011,951],
[1013,989,1041,1009,1036,0,1044,1055,1037,1052,1004],
[988,970,1009,933,994,957,0,1032,999,991,1005],
[971,969,971,948,959,946,969,0,995,1006,950],
[989,984,996,1005,1026,964,1002,1006,0,1059,953],
[1003,927,949,945,990,949,1010,995,942,0,960],
[1041,990,1042,975,1050,997,996,1051,1048,1041,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 3, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1008,971,974,992,1012,1059,1015,981,1045,1015],
[993,0,982,961,996,1006,1000,1022,979,1037,1022],
[1030,1019,0,1003,1008,1034,1050,1027,990,1069,1018],
[1027,1040,998,0,973,1023,1044,1039,1005,1022,1033],
[1009,1005,993,1028,0,1007,1049,1028,1023,1042,1045],
[989,995,967,978,994,0,1039,1015,978,1017,984],
[942,1001,951,957,952,962,0,955,976,1002,985],
[986,979,974,962,973,986,1046,0,969,1020,1009],
[1020,1022,1011,996,978,1023,1025,1032,0,1064,1013],
[956,964,932,979,959,984,999,981,937,0,963],
[986,979,983,968,956,1017,1016,992,988,1038,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 4, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,957,975,1000,969,968,982,973,970,952,976],
[1044,0,989,1020,1018,1002,1052,970,1040,1023,1021],
[1026,1012,0,1041,969,987,999,981,991,988,1037],
[1001,981,960,0,920,956,967,979,976,982,1018],
[1032,983,1032,1081,0,1003,1035,994,1004,993,1058],
[1033,999,1014,1045,998,0,995,972,1023,1038,1016],
[1019,949,1002,1034,966,1006,0,997,1012,995,985],
[1028,1031,1020,1022,1007,1029,1004,0,1005,982,1006],
[1031,961,1010,1025,997,978,989,996,0,1019,1042],
[1049,978,1013,1019,1008,963,1006,1019,982,0,1044],
[1025,980,964,983,943,985,1016,995,959,957,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 5, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1008,974,1052,1008,1011,1007,1012,1002,975,988],
[993,0,1001,1015,1039,1022,1015,958,1004,946,962],
[1027,1000,0,971,1004,1017,989,968,981,946,954],
[949,986,1030,0,996,990,1017,1004,958,941,949],
[993,962,997,1005,0,997,1000,1013,989,955,938],
[990,979,984,1011,1004,0,973,999,998,994,948],
[994,986,1012,984,1001,1028,0,990,994,976,944],
[989,1043,1033,997,988,1002,1011,0,1041,989,939],
[999,997,1020,1043,1012,1003,1007,960,0,1002,941],
[1026,1055,1055,1060,1046,1007,1025,1012,999,0,1012],
[1013,1039,1047,1052,1063,1053,1057,1062,1060,989,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 6, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1028,1101,1072,1072,1030,1076,1108,992,1102,1045],
[973,0,1013,996,1029,991,1049,1121,1066,1044,1100],
[900,988,0,975,942,1025,930,958,915,950,1000],
[929,1005,1026,0,1002,973,978,961,915,1031,1037],
[929,972,1059,999,0,1037,1026,993,1069,990,1095],
[971,1010,976,1028,964,0,1062,1089,1010,976,978],
[925,952,1071,1023,975,939,0,1010,1015,1049,1042],
[893,880,1043,1040,1008,912,991,0,983,957,1007],
[1009,935,1086,1086,932,991,986,1018,0,1034,1118],
[899,957,1051,970,1011,1025,952,1044,967,0,1002],
[956,901,1001,964,906,1023,959,994,883,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 7, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,961,1006,1032,1047,990,981,967,1035,1002,1002],
[1040,0,1009,1055,1039,958,972,1018,1028,1038,1055],
[995,992,0,1060,1016,1003,1032,1005,1014,1031,1006],
[969,946,941,0,1002,935,926,992,969,990,996],
[954,962,985,999,0,966,954,982,939,991,985],
[1011,1043,998,1066,1035,0,986,943,1008,1026,1040],
[1020,1029,969,1075,1047,1015,0,1035,1041,1058,1033],
[1034,983,996,1009,1019,1058,966,0,1047,1016,1035],
[966,973,987,1032,1062,993,960,954,0,1010,1029],
[999,963,970,1011,1010,975,943,985,991,0,987],
[999,946,995,1005,1016,961,968,966,972,1014,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 8, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,996,1023,987,1013,1039,1023,1039,1020,1031,1023],
[1005,0,1021,1012,984,1019,986,993,1009,1045,1038],
[978,980,0,953,992,980,994,997,980,1023,977],
[1014,989,1048,0,960,1010,1000,1017,1025,1042,1007],
[988,1017,1009,1041,0,1032,1025,1027,1020,1062,1035],
[962,982,1021,991,969,0,1003,989,1006,1026,1011],
[978,1015,1007,1001,976,998,0,1004,996,1029,1006],
[962,1008,1004,984,974,1012,997,0,953,1023,983],
[981,992,1021,976,981,995,1005,1048,0,1017,987],
[970,956,978,959,939,975,972,978,984,0,958],
[978,963,1024,994,966,990,995,1018,1014,1043,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 9, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1020,1008,1019,1007,1046,1010,1056,999,1043,1036],
[981,0,940,938,960,976,1013,1010,1001,975,965],
[993,1061,0,992,1037,1041,1030,1057,1018,1003,1035],
[982,1063,1009,0,1020,1057,1050,1037,1022,1034,1037],
[994,1041,964,981,0,1018,1013,997,1028,1022,1020],
[955,1025,960,944,983,0,1008,1006,973,1005,1011],
[991,988,971,951,988,993,0,1031,995,959,1013],
[945,991,944,964,1004,995,970,0,997,965,951],
[1002,1000,983,979,973,1028,1006,1004,0,1032,1004],
[958,1026,998,967,979,996,1042,1036,969,0,993],
[965,1036,966,964,981,990,988,1050,997,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 10, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1028,980,1016,981,1052,1009,1032,1023,1056,1001],
[973,0,970,1005,959,1027,966,997,990,1000,978],
[1021,1031,0,1036,992,1046,1016,1035,1016,1051,998],
[985,996,965,0,984,990,968,997,1023,1024,996],
[1020,1042,1009,1017,0,1044,987,1043,1012,1069,1005],
[949,974,955,1011,957,0,961,987,960,1016,981],
[992,1035,985,1033,1014,1040,0,1032,1020,1051,1033],
[969,1004,966,1004,958,1014,969,0,984,1002,962],
[978,1011,985,978,989,1041,981,1017,0,1013,1006],
[945,1001,950,977,932,985,950,999,988,0,962],
[1000,1023,1003,1005,996,1020,968,1039,995,1039,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 11, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1058,1054,1089,1072,990,939,1001,1033,992,1004],
[943,0,1083,1045,1062,968,994,972,1079,977,981],
[947,918,0,1049,1036,951,950,943,1013,974,987],
[912,956,952,0,1039,938,925,954,951,938,916],
[929,939,965,962,0,881,908,920,987,893,931],
[1011,1033,1050,1063,1120,0,986,980,1025,1014,930],
[1062,1007,1051,1076,1093,1015,0,998,1112,1012,981],
[1000,1029,1058,1047,1081,1021,1003,0,1058,984,944],
[968,922,988,1050,1014,976,889,943,0,929,991],
[1009,1024,1027,1063,1108,987,989,1017,1072,0,993],
[997,1020,1014,1085,1070,1071,1020,1057,1010,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 12, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,893,989,973,1026,934,1021,1039,1133,976,1015],
[1108,0,1041,1078,1093,1014,1032,1034,1130,1093,964],
[1012,960,0,1070,987,1076,1104,1073,1015,1033,1001],
[1028,923,931,0,1066,913,954,900,974,914,951],
[975,908,1014,935,0,902,1013,994,1047,916,957],
[1067,987,925,1088,1099,0,975,1013,1006,933,932],
[980,969,897,1047,988,1026,0,979,1011,964,943],
[962,967,928,1101,1007,988,1022,0,1031,917,862],
[868,871,986,1027,954,995,990,970,0,951,920],
[1025,908,968,1087,1085,1068,1037,1084,1050,0,959],
[986,1037,1000,1050,1044,1069,1058,1139,1081,1042,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 13, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1015,1093,1061,1019,1023,997,1006,1038,1017,1062],
[986,0,1044,1005,1001,1015,988,1016,999,1016,1022],
[908,957,0,957,1004,977,951,934,946,964,1030],
[940,996,1044,0,1000,967,970,988,971,984,1043],
[982,1000,997,1001,0,1007,953,978,991,1007,1008],
[978,986,1024,1034,994,0,922,999,998,935,968],
[1004,1013,1050,1031,1048,1079,0,977,1037,989,1041],
[995,985,1067,1013,1023,1002,1024,0,993,997,998],
[963,1002,1055,1030,1010,1003,964,1008,0,985,1009],
[984,985,1037,1017,994,1066,1012,1004,1016,0,1040],
[939,979,971,958,993,1033,960,1003,992,961,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 14, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,964,1022,1001,973,951,1001,956,977,986],
[1017,0,977,1025,1015,999,966,1010,960,987,966],
[1037,1024,0,1016,1010,1000,1014,1039,990,1008,1011],
[979,976,985,0,991,965,979,1020,996,962,956],
[1000,986,991,1010,0,987,987,1013,951,985,991],
[1028,1002,1001,1036,1014,0,987,1019,997,992,963],
[1050,1035,987,1022,1014,1014,0,1029,994,997,965],
[1000,991,962,981,988,982,972,0,987,967,982],
[1045,1041,1011,1005,1050,1004,1007,1014,0,1020,987],
[1024,1014,993,1039,1016,1009,1004,1034,981,0,1010],
[1015,1035,990,1045,1010,1038,1036,1019,1014,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 15, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,978,964,1048,964,1091,1112,1138,1079,1024,1122],
[1023,0,1114,1093,995,1097,1064,1116,994,1081,1050],
[1037,887,0,1092,1019,1070,1053,1132,1008,1111,1125],
[953,908,909,0,954,1041,1005,994,948,973,1063],
[1037,1006,982,1047,0,1166,1018,1068,995,1042,1087],
[910,904,931,960,835,0,887,1018,992,950,1012],
[889,937,948,996,983,1114,0,1039,985,993,1030],
[863,885,869,1007,933,983,962,0,987,1045,1032],
[922,1007,993,1053,1006,1009,1016,1014,0,1052,1060],
[977,920,890,1028,959,1051,1008,956,949,0,998],
[879,951,876,938,914,989,971,969,941,1003,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 16, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,1024,1053,1033,999,1031,1024,1018,990,1033],
[999,0,1017,1016,1019,1000,1001,998,999,1014,1047],
[977,984,0,1009,1008,1008,976,1002,983,999,1014],
[948,985,992,0,998,972,984,973,961,962,1007],
[968,982,993,1003,0,984,998,981,982,986,1024],
[1002,1001,993,1029,1017,0,1003,1035,1031,1011,1008],
[970,1000,1025,1017,1003,998,0,998,1011,994,1004],
[977,1003,999,1028,1020,966,1003,0,1007,982,1035],
[983,1002,1018,1040,1019,970,990,994,0,1003,1007],
[1011,987,1002,1039,1015,990,1007,1019,998,0,1019],
[968,954,987,994,977,993,997,966,994,982,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 17, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,976,1013,978,979,983,976,958,1018,972,996],
[1025,0,1024,1018,986,969,989,976,1011,966,1006],
[988,977,0,1018,957,958,979,961,978,963,1001],
[1023,983,983,0,947,961,934,986,993,972,979],
[1022,1015,1044,1054,0,991,987,1010,1016,971,993],
[1018,1032,1043,1040,1010,0,988,1001,1031,987,1039],
[1025,1012,1022,1067,1014,1013,0,1000,1007,1008,1023],
[1043,1025,1040,1015,991,1000,1001,0,1019,1009,1022],
[983,990,1023,1008,985,970,994,982,0,964,996],
[1029,1035,1038,1029,1030,1014,993,992,1037,0,1011],
[1005,995,1000,1022,1008,962,978,979,1005,990,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 18, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1069,1043,967,1135,1139,1032,1045,1056,1134,1044],
[932,0,987,975,999,1052,979,980,932,1040,978],
[958,1014,0,985,1024,1123,997,1063,964,1082,1060],
[1034,1026,1016,0,1017,1080,936,1024,993,1020,1060],
[866,1002,977,984,0,1036,973,976,965,1050,1037],
[862,949,878,921,965,0,882,997,938,1024,940],
[969,1022,1004,1065,1028,1119,0,1049,1009,1069,1071],
[956,1021,938,977,1025,1004,952,0,989,1022,1042],
[945,1069,1037,1008,1036,1063,992,1012,0,1030,1055],
[867,961,919,981,951,977,932,979,971,0,1029],
[957,1023,941,941,964,1061,930,959,946,972,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 19, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,1079,1002,995,1060,1016,1047,1067,1033,1083],
[988,0,1012,975,993,1020,990,1043,1092,1028,1051],
[922,989,0,972,1019,1013,1014,1034,1045,1006,1031],
[999,1026,1029,0,1022,1015,1003,1033,1034,1044,1048],
[1006,1008,982,979,0,1018,1035,1017,1087,1029,1052],
[941,981,988,986,983,0,988,963,1029,961,1004],
[985,1011,987,998,966,1013,0,1059,1063,1059,1065],
[954,958,967,968,984,1038,942,0,1036,936,1031],
[934,909,956,967,914,972,938,965,0,976,1005],
[968,973,995,957,972,1040,942,1065,1025,0,1059],
[918,950,970,953,949,997,936,970,996,942,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 20, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,951,940,933,1015,973,991,974,969,1046,1020],
[1050,0,994,1022,1049,1047,1047,1019,1020,1138,990],
[1061,1007,0,975,1079,1057,1014,1070,1021,1120,1044],
[1068,979,1026,0,1020,1103,1066,1038,1038,1069,1049],
[986,952,922,981,0,1038,960,969,963,1133,1025],
[1028,954,944,898,963,0,1029,1022,1003,1021,1002],
[1010,954,987,935,1041,972,0,966,973,1032,1033],
[1027,982,931,963,1032,979,1035,0,961,1038,1056],
[1032,981,980,963,1038,998,1028,1040,0,1046,1030],
[955,863,881,932,868,980,969,963,955,0,968],
[981,1011,957,952,976,999,968,945,971,1033,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 21, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1072,1003,1009,981,1007,957,1013,1022,1042,1021],
[929,0,950,981,986,929,928,966,952,991,965],
[998,1051,0,980,1050,993,985,1016,1029,1003,996],
[992,1020,1021,0,1011,1003,941,953,1005,1023,971],
[1020,1015,951,990,0,992,982,1031,990,1042,997],
[994,1072,1008,998,1009,0,965,991,1016,1044,990],
[1044,1073,1016,1060,1019,1036,0,998,1031,1065,1018],
[988,1035,985,1048,970,1010,1003,0,995,1052,996],
[979,1049,972,996,1011,985,970,1006,0,1017,997],
[959,1010,998,978,959,957,936,949,984,0,916],
[980,1036,1005,1030,1004,1011,983,1005,1004,1085,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 22, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1063,1007,973,1051,973,955,1020,1030,901,1002],
[938,0,977,970,1013,996,971,1001,994,852,945],
[994,1024,0,1047,1004,1044,989,1041,915,958,952],
[1028,1031,954,0,1091,1007,1021,1039,1011,930,941],
[950,988,997,910,0,970,973,962,990,917,915],
[1028,1005,957,994,1031,0,1042,1034,971,1029,1032],
[1046,1030,1012,980,1028,959,0,1005,1076,902,948],
[981,1000,960,962,1039,967,996,0,988,924,952],
[971,1007,1086,990,1011,1030,925,1013,0,911,959],
[1100,1149,1043,1071,1084,972,1099,1077,1090,0,1017],
[999,1056,1049,1060,1086,969,1053,1049,1042,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 23, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,994,910,987,1057,1036,984,1029,1019,1005],
[1024,0,1035,982,1095,1131,986,1049,1020,1118,945],
[1007,966,0,919,974,1027,977,938,939,1025,936],
[1091,1019,1082,0,1007,1143,1066,985,987,1103,1029],
[1014,906,1027,994,0,1036,1005,1013,1008,1094,986],
[944,870,974,858,965,0,947,889,824,1023,907],
[965,1015,1024,935,996,1054,0,945,939,1097,949],
[1017,952,1063,1016,988,1112,1056,0,1025,1094,973],
[972,981,1062,1014,993,1177,1062,976,0,1062,1033],
[982,883,976,898,907,978,904,907,939,0,947],
[996,1056,1065,972,1015,1094,1052,1028,968,1054,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 24, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,973,1007,1017,997,959,1035,1000,1000,1025,978],
[1028,0,1020,1046,999,1013,1016,1028,990,1046,997],
[994,981,0,1055,1010,1004,1004,981,1020,1047,1007],
[984,955,946,0,939,951,958,968,918,995,946],
[1004,1002,991,1062,0,974,1058,993,976,1028,1008],
[1042,988,997,1050,1027,0,1082,1022,1054,1053,1041],
[966,985,997,1043,943,919,0,981,951,1035,981],
[1001,973,1020,1033,1008,979,1020,0,1002,1075,959],
[1001,1011,981,1083,1025,947,1050,999,0,1070,1003],
[976,955,954,1006,973,948,966,926,931,0,970],
[1023,1004,994,1055,993,960,1020,1042,998,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 25, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,972,991,1005,997,985,991,960,1012,993],
[992,0,987,1008,1028,988,990,1022,995,996,1001],
[1029,1014,0,1026,1025,992,1034,1035,1007,1007,1035],
[1010,993,975,0,1017,991,1023,1032,998,990,1036],
[996,973,976,984,0,990,986,1016,972,994,995],
[1004,1013,1009,1010,1011,0,1007,1017,988,1012,1037],
[1016,1011,967,978,1015,994,0,992,986,1001,1023],
[1010,979,966,969,985,984,1009,0,968,978,1005],
[1041,1006,994,1003,1029,1013,1015,1033,0,1011,1021],
[989,1005,994,1011,1007,989,1000,1023,990,0,983],
[1008,1000,966,965,1006,964,978,996,980,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 26, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1120,1082,1023,1061,1038,1068,1102,975,1123,1037],
[881,0,1003,968,1005,942,963,1061,879,1050,1027],
[919,998,0,980,1010,954,962,1032,891,1043,1005],
[978,1033,1021,0,1029,1022,1023,1097,1023,1100,1053],
[940,996,991,972,0,1020,989,1037,874,1070,1042],
[963,1059,1047,979,981,0,983,1028,950,1076,1051],
[933,1038,1039,978,1012,1018,0,1067,922,1070,1076],
[899,940,969,904,964,973,934,0,883,982,942],
[1026,1122,1110,978,1127,1051,1079,1118,0,1177,1074],
[878,951,958,901,931,925,931,1019,824,0,941],
[964,974,996,948,959,950,925,1059,927,1060,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 27, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,972,1010,1080,1029,1017,1031,967,1060,996,970],
[1029,0,994,1013,1017,969,1008,982,988,985,1002],
[991,1007,0,1055,1005,979,1049,976,1005,959,957],
[921,988,946,0,969,926,961,903,957,943,924],
[972,984,996,1032,0,947,989,954,1019,976,953],
[984,1032,1022,1075,1054,0,1020,971,1007,974,955],
[970,993,952,1040,1012,981,0,961,999,986,976],
[1034,1019,1025,1098,1047,1030,1040,0,998,1028,984],
[941,1013,996,1044,982,994,1002,1003,0,1019,987],
[1005,1016,1042,1058,1025,1027,1015,973,982,0,991],
[1031,999,1044,1077,1048,1046,1025,1017,1014,1010,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 28, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1053,966,991,952,990,1042,1009,1146,1071,1003],
[948,0,903,886,846,940,948,992,1059,1029,954],
[1035,1098,0,1054,958,1005,1078,1111,1148,1036,1001],
[1010,1115,947,0,1050,1024,1032,1063,1222,1119,1064],
[1049,1155,1043,951,0,1078,1011,1043,1159,1033,913],
[1011,1061,996,977,923,0,974,957,1056,1044,972],
[959,1053,923,969,990,1027,0,997,1035,1014,993],
[992,1009,890,938,958,1044,1004,0,1047,994,910],
[855,942,853,779,842,945,966,954,0,970,912],
[930,972,965,882,968,957,987,1007,1031,0,912],
[998,1047,1000,937,1088,1029,1008,1091,1089,1089,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 29, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1043,1016,1018,1032,1040,996,987,1038,1024,1025],
[958,0,1003,965,998,1022,1007,973,1018,983,981],
[985,998,0,1009,993,981,931,971,987,986,963],
[983,1036,992,0,1036,1011,974,1022,1044,977,1014],
[969,1003,1008,965,0,1022,891,981,1035,1004,1000],
[961,979,1020,990,979,0,988,958,984,979,980],
[1005,994,1070,1027,1110,1013,0,1032,1074,1030,1006],
[1014,1028,1030,979,1020,1043,969,0,1015,1034,1030],
[963,983,1014,957,966,1017,927,986,0,943,1008],
[977,1018,1015,1024,997,1022,971,967,1058,0,1005],
[976,1020,1038,987,1001,1021,995,971,993,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 30, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,964,963,1014,1004,1003,991,974,1012,1010,986],
[1037,0,967,1015,1007,980,986,1023,1049,1025,1010],
[1038,1034,0,1071,995,1018,1026,1045,1058,1010,1019],
[987,986,930,0,977,973,979,980,1004,1009,989],
[997,994,1006,1024,0,989,986,1007,1034,1000,1009],
[998,1021,983,1028,1012,0,1020,1031,1033,1012,1002],
[1010,1015,975,1022,1015,981,0,1027,1016,981,1016],
[1027,978,956,1021,994,970,974,0,985,970,990],
[989,952,943,997,967,968,985,1016,0,971,986],
[991,976,991,992,1001,989,1020,1031,1030,0,1008],
[1015,991,982,1012,992,999,985,1011,1015,993,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 31, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,980,1012,1046,1015,973,988,1006,982,1009,1005],
[1021,0,997,992,1005,991,984,1010,991,1012,985],
[989,1004,0,1010,992,959,990,991,955,1014,959],
[955,1009,991,0,969,1006,999,1017,1040,970,1006],
[986,996,1009,1032,0,984,988,979,968,1016,983],
[1028,1010,1042,995,1017,0,1028,1016,1035,1050,1017],
[1013,1017,1011,1002,1013,973,0,962,1001,1016,1012],
[995,991,1010,984,1022,985,1039,0,1015,1002,989],
[1019,1010,1046,961,1033,966,1000,986,0,1042,999],
[992,989,987,1031,985,951,985,999,959,0,988],
[996,1016,1042,995,1018,984,989,1012,1002,1013,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 32, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,761,601,697,907,945,797,593,847,738,1229],
[1240,0,1143,1196,1040,1230,885,814,1248,767,1323],
[1400,858,0,1463,1121,1388,1339,1429,956,1264,1690],
[1304,805,538,0,1011,1031,658,841,802,842,1156],
[1094,961,880,990,0,897,745,699,886,901,1196],
[1056,771,613,970,1104,0,919,947,622,669,1197],
[1204,1116,662,1343,1256,1082,0,1057,1119,1032,1005],
[1408,1187,572,1160,1302,1054,944,0,1184,1066,1524],
[1154,753,1045,1199,1115,1379,882,817,0,1024,1641],
[1263,1234,737,1159,1100,1332,969,935,977,0,1241],
[772,678,311,845,805,804,996,477,360,760,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 33, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,962,1015,1059,1039,1101,1062,1051,1062,979],
[985,0,1020,1041,1049,1008,1053,1021,1027,993,959],
[1039,981,0,1003,1009,983,1049,1005,1025,1028,982],
[986,960,998,0,1052,1021,1075,1053,1023,1026,1038],
[942,952,992,949,0,1017,1056,1019,971,984,990],
[962,993,1018,980,984,0,1053,1010,1016,1023,1011],
[900,948,952,926,945,948,0,953,944,969,924],
[939,980,996,948,982,991,1048,0,942,999,993],
[950,974,976,978,1030,985,1057,1059,0,991,971],
[939,1008,973,975,1017,978,1032,1002,1010,0,975],
[1022,1042,1019,963,1011,990,1077,1008,1030,1026,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 34, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1029,952,999,1050,965,975,969,987,963,1019],
[972,0,961,992,1002,956,1020,989,930,1059,1078],
[1049,1040,0,1004,987,1037,1005,1015,1008,962,1079],
[1002,1009,997,0,1021,1047,1014,961,984,1025,1019],
[951,999,1014,980,0,968,964,1018,959,1041,1053],
[1036,1045,964,954,1033,0,1012,1037,960,1020,1037],
[1026,981,996,987,1037,989,0,988,989,978,1051],
[1032,1012,986,1040,983,964,1013,0,984,981,1051],
[1014,1071,993,1017,1042,1041,1012,1017,0,1082,1111],
[1038,942,1039,976,960,981,1023,1020,919,0,1030],
[982,923,922,982,948,964,950,950,890,971,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 35, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1018,994,1024,992,986,988,973,980,1012,995],
[983,0,967,1025,1005,949,979,996,997,999,1040],
[1007,1034,0,989,994,981,970,980,1046,976,1006],
[977,976,1012,0,945,995,1009,1005,1036,1013,1031],
[1009,996,1007,1056,0,994,972,1018,1039,1003,1044],
[1015,1052,1020,1006,1007,0,995,1014,1040,1016,1013],
[1013,1022,1031,992,1029,1006,0,999,1038,1016,1005],
[1028,1005,1021,996,983,987,1002,0,1031,999,1042],
[1021,1004,955,965,962,961,963,970,0,990,1005],
[989,1002,1025,988,998,985,985,1002,1011,0,1020],
[1006,961,995,970,957,988,996,959,996,981,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 36, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1106,1047,1023,964,1026,1001,912,1077,1145,1065],
[895,0,815,956,883,1025,945,931,998,983,978],
[954,1186,0,1072,975,1095,1000,1053,1111,1060,1169],
[978,1045,929,0,954,976,811,951,986,917,925],
[1037,1118,1026,1047,0,1027,1081,895,1082,1142,1115],
[975,976,906,1025,974,0,933,956,1011,989,996],
[1000,1056,1001,1190,920,1068,0,1008,1115,1106,996],
[1089,1070,948,1050,1106,1045,993,0,1101,1005,1068],
[924,1003,890,1015,919,990,886,900,0,847,988],
[856,1018,941,1084,859,1012,895,996,1154,0,931],
[936,1023,832,1076,886,1005,1005,933,1013,1070,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 37, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,1002,1037,1044,1010,999,1020,1029,1013,993],
[1017,0,1018,1055,1037,1012,998,993,1069,1011,1037],
[999,983,0,1022,1031,977,985,1019,1031,1036,1004],
[964,946,979,0,986,935,958,987,1009,999,969],
[957,964,970,1015,0,949,971,984,1001,987,1028],
[991,989,1024,1066,1052,0,1015,1000,1039,1061,1023],
[1002,1003,1016,1043,1030,986,0,1028,1054,1042,1031],
[981,1008,982,1014,1017,1001,973,0,1050,1012,1035],
[972,932,970,992,1000,962,947,951,0,998,1000],
[988,990,965,1002,1014,940,959,989,1003,0,977],
[1008,964,997,1032,973,978,970,966,1001,1024,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 38, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1192,1002,975,889,1007,1046,969,937,1016,1000],
[809,0,891,955,726,892,846,843,801,890,825],
[999,1110,0,934,908,967,1002,1016,987,1079,981],
[1026,1046,1067,0,875,979,950,923,946,971,955],
[1112,1275,1093,1126,0,1096,1114,975,1172,1068,1065],
[994,1109,1034,1022,905,0,965,1087,998,995,920],
[955,1155,999,1051,887,1036,0,981,985,988,999],
[1032,1158,985,1078,1026,914,1020,0,1095,1093,972],
[1064,1200,1014,1055,829,1003,1016,906,0,1062,1011],
[985,1111,922,1030,933,1006,1013,908,939,0,980],
[1001,1176,1020,1046,936,1081,1002,1029,990,1021,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 39, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,994,984,1006,968,988,955,993,969,1024],
[998,0,1015,981,1017,1029,1020,1002,997,988,984],
[1007,986,0,984,1010,964,974,980,1000,982,977],
[1017,1020,1017,0,1010,999,1007,1000,1019,1003,997],
[995,984,991,991,0,997,997,975,976,971,990],
[1033,972,1037,1002,1004,0,1009,1009,1000,1028,1017],
[1013,981,1027,994,1004,992,0,1005,975,1007,1014],
[1046,999,1021,1001,1026,992,996,0,1032,1000,1015],
[1008,1004,1001,982,1025,1001,1026,969,0,962,994],
[1032,1013,1019,998,1030,973,994,1001,1039,0,1012],
[977,1017,1024,1004,1011,984,987,986,1007,989,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 40, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1022,1013,1027,1021,996,1039,1002,1046,978,992],
[979,0,961,983,992,984,1026,981,959,944,997],
[988,1040,0,1020,990,989,1034,994,1011,984,990],
[974,1018,981,0,1021,999,1011,1007,1014,980,997],
[980,1009,1011,980,0,1027,1021,1031,1022,997,1024],
[1005,1017,1012,1002,974,0,1020,984,1025,969,999],
[962,975,967,990,980,981,0,978,975,939,942],
[999,1020,1007,994,970,1017,1023,0,1029,1006,979],
[955,1042,990,987,979,976,1026,972,0,985,955],
[1023,1057,1017,1021,1004,1032,1062,995,1016,0,1010],
[1009,1004,1011,1004,977,1002,1059,1022,1046,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 41, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,1036,1006,990,995,1019,1002,1024,1004,988],
[977,0,1032,989,1031,996,1022,991,1041,1004,1010],
[965,969,0,951,994,943,990,978,986,966,951],
[995,1012,1050,0,1060,1031,1066,1035,1047,1030,1004],
[1011,970,1007,941,0,976,1011,1012,1031,981,989],
[1006,1005,1058,970,1025,0,1030,1007,1012,1017,1013],
[982,979,1011,935,990,971,0,983,1015,997,985],
[999,1010,1023,966,989,994,1018,0,1016,995,989],
[977,960,1015,954,970,989,986,985,0,962,952],
[997,997,1035,971,1020,984,1004,1006,1039,0,1001],
[1013,991,1050,997,1012,988,1016,1012,1049,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 42, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,878,851,927,1013,907,975,953,962,851,961],
[1123,0,913,1034,1172,955,1000,1098,1077,938,1090],
[1150,1088,0,988,1167,1033,1171,1111,1089,1068,1148],
[1074,967,1013,0,1102,922,1053,1038,1095,1054,1041],
[988,829,834,899,0,876,906,985,950,899,835],
[1094,1046,968,1079,1125,0,1032,1069,1130,1035,1150],
[1026,1001,830,948,1095,969,0,981,1046,951,971],
[1048,903,890,963,1016,932,1020,0,1057,990,924],
[1039,924,912,906,1051,871,955,944,0,985,970],
[1150,1063,933,947,1102,966,1050,1011,1016,0,949],
[1040,911,853,960,1166,851,1030,1077,1031,1052,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 43, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,975,833,1016,1066,969,926,949,776,1043,962],
[1026,0,962,1011,993,1038,1022,944,944,995,994],
[1168,1039,0,956,1137,904,1155,966,864,1090,1013],
[985,990,1045,0,1080,1035,1182,1031,1059,1057,1032],
[935,1008,864,921,0,936,945,862,845,1023,970],
[1032,963,1097,966,1065,0,1211,1072,912,1166,1075],
[1075,979,846,819,1056,790,0,1029,841,1038,1105],
[1052,1057,1035,970,1139,929,972,0,935,1148,986],
[1225,1057,1137,942,1156,1089,1160,1066,0,1144,1169],
[958,1006,911,944,978,835,963,853,857,0,865],
[1039,1007,988,969,1031,926,896,1015,832,1136,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 44, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,943,994,975,968,970,971,985,971,923,945],
[1058,0,1025,989,1033,987,1007,1005,1001,963,972],
[1007,976,0,978,959,946,991,976,996,970,960],
[1026,1012,1023,0,1013,989,1048,1010,1013,995,1020],
[1033,968,1042,988,0,1009,1018,999,1026,977,1010],
[1031,1014,1055,1012,992,0,1006,1004,1017,1038,1030],
[1030,994,1010,953,983,995,0,1009,1019,970,1003],
[1016,996,1025,991,1002,997,992,0,993,951,980],
[1030,1000,1005,988,975,984,982,1008,0,977,1000],
[1078,1038,1031,1006,1024,963,1031,1050,1024,0,1033],
[1056,1029,1041,981,991,971,998,1021,1001,968,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 45, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,947,968,948,986,1045,1034,976,954,1042,984],
[1054,0,987,1002,1020,1018,996,1015,955,1036,962],
[1033,1014,0,1017,1008,980,1025,1043,1000,1031,980],
[1053,999,984,0,1013,1034,1041,1039,1008,1016,1004],
[1015,981,993,988,0,1012,1013,981,985,1022,933],
[956,983,1021,967,989,0,1047,1066,1033,1058,986],
[967,1005,976,960,988,954,0,969,996,1070,967],
[1025,986,958,962,1020,935,1032,0,990,1050,941],
[1047,1046,1001,993,1016,968,1005,1011,0,1007,970],
[959,965,970,985,979,943,931,951,994,0,937],
[1017,1039,1021,997,1068,1015,1034,1060,1031,1064,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 46, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,963,1030,1022,934,1103,921,1008,1067,1002],
[990,0,969,894,975,967,1058,984,968,1033,931],
[1038,1032,0,1009,1055,959,1111,1060,1022,1036,1067],
[971,1107,992,0,1025,986,1082,991,955,1036,951],
[979,1026,946,976,0,878,1024,953,981,1082,986],
[1067,1034,1042,1015,1123,0,1130,997,1021,1106,987],
[898,943,890,919,977,871,0,935,868,906,910],
[1080,1017,941,1010,1048,1004,1066,0,1010,995,1031],
[993,1033,979,1046,1020,980,1133,991,0,1021,992],
[934,968,965,965,919,895,1095,1006,980,0,1009],
[999,1070,934,1050,1015,1014,1091,970,1009,992,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 47, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,952,927,947,1075,1030,958,996,972,1048,1022],
[1049,0,1000,1005,1097,998,984,1040,1010,1051,1042],
[1074,1001,0,995,1074,1016,1002,1037,977,1069,999],
[1054,996,1006,0,1034,1013,938,989,990,1044,1039],
[926,904,927,967,0,970,904,962,965,991,959],
[971,1003,985,988,1031,0,945,1026,990,1051,1004],
[1043,1017,999,1063,1097,1056,0,1037,1079,1022,1048],
[1005,961,964,1012,1039,975,964,0,1013,1024,982],
[1029,991,1024,1011,1036,1011,922,988,0,1048,994],
[953,950,932,957,1010,950,979,977,953,0,966],
[979,959,1002,962,1042,997,953,1019,1007,1035,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 48, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,969,979,955,1016,1004,994,955,975,972,1003],
[1032,0,1043,1056,1053,1027,1118,1058,1031,994,1087],
[1022,958,0,1024,1067,1025,1012,978,1010,1007,1013],
[1046,945,977,0,1002,1029,1032,1001,1014,978,992],
[985,948,934,999,0,986,1017,1007,993,959,1013],
[997,974,976,972,1015,0,1032,1031,982,981,998],
[1007,883,989,969,984,969,0,972,1001,963,1005],
[1046,943,1023,1000,994,970,1029,0,1018,938,1022],
[1026,970,991,987,1008,1019,1000,983,0,988,994],
[1029,1007,994,1023,1042,1020,1038,1063,1013,0,1010],
[998,914,988,1009,988,1003,996,979,1007,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 49, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,948,994,995,988,982,1028,1033,977,934,1031],
[1053,0,1070,1086,974,992,1036,1105,1001,985,1001],
[1007,931,0,1007,997,948,1018,1035,964,1006,1002],
[1006,915,994,0,944,939,988,1005,955,944,977],
[1013,1027,1004,1057,0,1025,942,1071,1043,1057,1012],
[1019,1009,1053,1062,976,0,1011,1045,1033,1022,1059],
[973,965,983,1013,1059,990,0,1059,1032,1048,1020],
[968,896,966,996,930,956,942,0,952,927,994],
[1024,1000,1037,1046,958,968,969,1049,0,973,1004],
[1067,1016,995,1057,944,979,953,1074,1028,0,1038],
[970,1000,999,1024,989,942,981,1007,997,963,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 50, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,1017,991,984,987,1038,1026,1057,1001,997],
[985,0,946,979,916,985,1034,1011,1018,959,982],
[984,1055,0,1015,1018,1010,1044,1021,1066,981,990],
[1010,1022,986,0,980,1043,1057,1035,1033,978,993],
[1017,1085,983,1021,0,1061,1065,1069,1064,1006,1032],
[1014,1016,991,958,940,0,1044,1024,1007,978,988],
[963,967,957,944,936,957,0,990,992,954,956],
[975,990,980,966,932,977,1011,0,1011,993,969],
[944,983,935,968,937,994,1009,990,0,961,966],
[1000,1042,1020,1023,995,1023,1047,1008,1040,0,969],
[1004,1019,1011,1008,969,1013,1045,1032,1035,1032,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 51, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1060,1035,1070,991,1040,982,1059,1025,1052,1008],
[941,0,1045,1043,1020,1028,1027,1096,1033,1087,998],
[966,956,0,1033,982,1016,984,1007,908,1049,1012],
[931,958,968,0,996,990,989,1045,913,1012,977],
[1010,981,1019,1005,0,1019,982,1054,999,1050,961],
[961,973,985,1011,982,0,1005,1015,931,1000,970],
[1019,974,1017,1012,1019,996,0,1067,976,1037,979],
[942,905,994,956,947,986,934,0,909,1008,965],
[976,968,1093,1088,1002,1070,1025,1092,0,1073,1045],
[949,914,952,989,951,1001,964,993,928,0,961],
[993,1003,989,1024,1040,1031,1022,1036,956,1040,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 52, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1037,987,1018,1004,1014,1008,1017,975,999,1034],
[964,0,993,947,970,950,964,988,955,972,1004],
[1014,1008,0,990,999,961,962,977,971,964,985],
[983,1054,1011,0,949,991,1010,1024,967,997,974],
[997,1031,1002,1052,0,991,990,979,990,1046,1026],
[987,1051,1040,1010,1010,0,988,1013,1020,1028,1062],
[993,1037,1039,991,1011,1013,0,998,991,988,978],
[984,1013,1024,977,1022,988,1003,0,1005,987,1031],
[1026,1046,1030,1034,1011,981,1010,996,0,1040,1054],
[1002,1029,1037,1004,955,973,1013,1014,961,0,1030],
[967,997,1016,1027,975,939,1023,970,947,971,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 53, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,998,987,1019,1042,1047,1022,1013,998,1075],
[1002,0,996,1014,1075,1031,1017,1003,1069,1007,1023],
[1003,1005,0,969,1046,1022,1038,983,1046,974,954],
[1014,987,1032,0,1041,1010,1032,1046,1041,1034,1027],
[982,926,955,960,0,973,972,979,1001,954,937],
[959,970,979,991,1028,0,990,1043,949,999,977],
[954,984,963,969,1029,1011,0,1039,1031,993,990],
[979,998,1018,955,1022,958,962,0,1009,971,1018],
[988,932,955,960,1000,1052,970,992,0,1024,957],
[1003,994,1027,967,1047,1002,1008,1030,977,0,1034],
[926,978,1047,974,1064,1024,1011,983,1044,967,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 54, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,1005,1008,990,1007,964,1022,986,963,982],
[1013,0,1040,1033,998,1031,1004,1054,1047,995,1029],
[996,961,0,986,995,990,958,1050,1032,968,987],
[993,968,1015,0,984,1006,951,1016,1002,969,1000],
[1011,1003,1006,1017,0,1029,990,1035,1019,984,995],
[994,970,1011,995,972,0,974,1022,989,983,978],
[1037,997,1043,1050,1011,1027,0,1054,1034,1001,1032],
[979,947,951,985,966,979,947,0,994,984,990],
[1015,954,969,999,982,1012,967,1007,0,956,991],
[1038,1006,1033,1032,1017,1018,1000,1017,1045,0,1023],
[1019,972,1014,1001,1006,1023,969,1011,1010,978,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 55, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1156,1094,1085,1085,1110,900,1149,1267,1105,1091],
[845,0,773,856,812,905,838,935,1020,1010,800],
[907,1228,0,906,978,1063,906,1123,1108,1025,917],
[916,1145,1095,0,1004,1052,861,1064,1154,1003,963],
[916,1189,1023,997,0,1007,967,1035,1013,1046,940],
[891,1096,938,949,994,0,839,987,1081,1011,936],
[1101,1163,1095,1140,1034,1162,0,1145,1225,973,1135],
[852,1066,878,937,966,1014,856,0,974,920,822],
[734,981,893,847,988,920,776,1027,0,947,784],
[896,991,976,998,955,990,1028,1081,1054,0,971],
[910,1201,1084,1038,1061,1065,866,1179,1217,1030,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 56, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,969,1029,1026,1054,1030,982,1050,970,1053,1016],
[1032,0,998,1044,1029,1071,961,1052,1024,1049,1047],
[972,1003,0,1015,1000,1027,982,1024,1005,1019,1015],
[975,957,986,0,987,1022,949,994,1007,990,994],
[947,972,1001,1014,0,1015,978,973,966,1009,988],
[971,930,974,979,986,0,943,997,980,993,998],
[1019,1040,1019,1052,1023,1058,0,991,998,1031,1020],
[951,949,977,1007,1028,1004,1010,0,1033,1028,1021],
[1031,977,996,994,1035,1021,1003,968,0,1055,1018],
[948,952,982,1011,992,1008,970,973,946,0,974],
[985,954,986,1007,1013,1003,981,980,983,1027,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 57, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1000,1005,984,1012,1012,1001,966,1036,999,1013],
[1001,0,1007,1034,1034,998,1006,1027,1024,1027,986],
[996,994,0,1038,997,1018,1034,1045,1084,987,1000],
[1017,967,963,0,1007,1016,976,943,1036,1012,974],
[989,967,1004,994,0,1029,1004,978,1048,985,958],
[989,1003,983,985,972,0,983,984,1041,1008,986],
[1000,995,967,1025,997,1018,0,1006,1033,1021,962],
[1035,974,956,1058,1023,1017,995,0,1048,1043,984],
[965,977,917,965,953,960,968,953,0,976,953],
[1002,974,1014,989,1016,993,980,958,1025,0,958],
[988,1015,1001,1027,1043,1015,1039,1017,1048,1043,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 58, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,1001,1040,1034,1002,996,1032,1020,1040,984],
[990,0,989,1048,1012,981,1008,1000,966,990,1008],
[1000,1012,0,1039,1028,1034,1022,1018,1030,991,982],
[961,953,962,0,1015,1028,986,996,988,997,989],
[967,989,973,986,0,992,967,972,1012,984,966],
[999,1020,967,973,1009,0,1017,1021,1014,1000,966],
[1005,993,979,1015,1034,984,0,966,992,991,967],
[969,1001,983,1005,1029,980,1035,0,987,1004,988],
[981,1035,971,1013,989,987,1009,1014,0,986,988],
[961,1011,1010,1004,1017,1001,1010,997,1015,0,987],
[1017,993,1019,1012,1035,1035,1034,1013,1013,1014,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 59, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,1014,983,1014,1021,997,1042,1000,986,981],
[988,0,1004,991,967,991,956,964,994,969,986],
[987,997,0,1000,994,1044,1010,1031,1065,994,1033],
[1018,1010,1001,0,1008,1023,986,1006,1002,966,1011],
[987,1034,1007,993,0,1035,1024,999,1001,950,1000],
[980,1010,957,978,966,0,1002,980,1011,967,984],
[1004,1045,991,1015,977,999,0,1005,1037,999,982],
[959,1037,970,995,1002,1021,996,0,1001,1053,1010],
[1001,1007,936,999,1000,990,964,1000,0,998,1002],
[1015,1032,1007,1035,1051,1034,1002,948,1003,0,1011],
[1020,1015,968,990,1001,1017,1019,991,999,990,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 60, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,991,984,978,969,961,977,923,1000,1018,982],
[1010,0,974,972,972,978,971,965,977,1010,1009],
[1017,1027,0,1023,1003,1017,996,1020,1021,1045,1046],
[1023,1029,978,0,997,992,993,981,999,1023,1034],
[1032,1029,998,1004,0,1005,997,978,1022,1063,1037],
[1040,1023,984,1009,996,0,1006,952,1029,1001,1023],
[1024,1030,1005,1008,1004,995,0,1016,1023,1024,1026],
[1078,1036,981,1020,1023,1049,985,0,1033,1021,1076],
[1001,1024,980,1002,979,972,978,968,0,1043,1030],
[983,991,956,978,938,1000,977,980,958,0,983],
[1019,992,955,967,964,978,975,925,971,1018,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 61, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,934,969,937,1049,962,999,983,928,1018,948],
[1067,0,979,968,1075,979,1010,1001,989,1000,996],
[1032,1022,0,978,1125,1035,1001,1035,1047,997,1028],
[1064,1033,1023,0,1067,1069,1070,985,1060,1038,1029],
[952,926,876,934,0,925,942,920,909,937,916],
[1039,1022,966,932,1076,0,1008,1016,981,959,947],
[1002,991,1000,931,1059,993,0,961,1004,982,989],
[1018,1000,966,1016,1081,985,1040,0,963,1049,1027],
[1073,1012,954,941,1092,1020,997,1038,0,992,984],
[983,1001,1004,963,1064,1042,1019,952,1009,0,988],
[1053,1005,973,972,1085,1054,1012,974,1017,1013,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 62, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,983,1011,1035,953,989,1018,981,987,1009,984],
[1018,0,1013,1049,1005,948,1027,1021,1005,995,982],
[990,988,0,1020,956,967,1042,1005,981,1014,1007],
[966,952,981,0,896,973,977,988,989,990,970],
[1048,996,1045,1105,0,1034,1088,1024,1034,1008,1030],
[1012,1053,1034,1028,967,0,1046,1023,1029,1002,1036],
[983,974,959,1024,913,955,0,1002,995,986,986],
[1020,980,996,1013,977,978,999,0,989,1000,1029],
[1014,996,1020,1012,967,972,1006,1012,0,1006,1008],
[992,1006,987,1011,993,999,1015,1001,995,0,1003],
[1017,1019,994,1031,971,965,1015,972,993,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 63, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,998,996,968,997,1017,996,1025,993,1002,996],
[1003,0,1034,1004,998,1018,1004,1023,1016,1011,1048],
[1005,967,0,1007,936,1004,978,1005,1005,1018,998],
[1033,997,994,0,979,1000,994,1018,976,1015,994],
[1004,1003,1065,1022,0,1031,999,1035,1018,1002,1020],
[984,983,997,1001,970,0,1014,989,998,990,994],
[1005,997,1023,1007,1002,987,0,1022,1006,1012,1011],
[976,978,996,983,966,1012,979,0,982,987,993],
[1008,985,996,1025,983,1003,995,1019,0,1027,994],
[999,990,983,986,999,1011,989,1014,974,0,996],
[1005,953,1003,1007,981,1007,990,1008,1007,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 64, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1089,1013,1035,1030,1036,1001,1045,1015,1018,988],
[912,0,983,1004,1027,1036,932,976,981,934,960],
[988,1018,0,1026,1066,1084,1024,1035,1017,1028,1063],
[966,997,975,0,1019,1029,985,1044,1004,1031,978],
[971,974,935,982,0,1023,957,993,973,999,995],
[965,965,917,972,978,0,982,992,939,973,982],
[1000,1069,977,1016,1044,1019,0,1026,1002,1042,1031],
[956,1025,966,957,1008,1009,975,0,952,978,974],
[986,1020,984,997,1028,1062,999,1049,0,1024,998],
[983,1067,973,970,1002,1028,959,1023,977,0,1008],
[1013,1041,938,1023,1006,1019,970,1027,1003,993,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 65, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,949,980,1008,968,950,931,974,1010,1025,1068],
[1052,0,967,1004,1058,981,964,1000,1015,1024,1110],
[1021,1034,0,1039,1073,1016,999,1020,1011,1017,1066],
[993,997,962,0,1001,1005,960,1004,952,977,1082],
[1033,943,928,1000,0,965,969,985,988,971,1027],
[1051,1020,985,996,1036,0,1022,968,1018,1025,1067],
[1070,1037,1002,1041,1032,979,0,968,995,1039,1082],
[1027,1001,981,997,1016,1033,1033,0,1011,1029,1072],
[991,986,990,1049,1013,983,1006,990,0,1037,1074],
[976,977,984,1024,1030,976,962,972,964,0,1024],
[933,891,935,919,974,934,919,929,927,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 66, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1037,1022,987,1024,1000,1028,1008,1056,982,1032],
[964,0,991,967,1041,983,968,946,1026,978,951],
[979,1010,0,1002,1006,957,990,974,1018,958,997],
[1014,1034,999,0,1037,1029,989,1003,1043,1012,1012],
[977,960,995,964,0,973,990,956,998,1011,917],
[1001,1018,1044,972,1028,0,1008,1004,1026,1019,997],
[973,1033,1011,1012,1011,993,0,969,991,969,949],
[993,1055,1027,998,1045,997,1032,0,1043,998,1012],
[945,975,983,958,1003,975,1010,958,0,962,1000],
[1019,1023,1043,989,990,982,1032,1003,1039,0,963],
[969,1050,1004,989,1084,1004,1052,989,1001,1038,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 67, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,958,943,1025,973,1008,972,981,956,945],
[988,0,1044,1016,1008,1015,992,1034,998,993,986],
[1043,957,0,979,976,1011,992,1004,987,996,959],
[1058,985,1022,0,1018,1037,1040,1041,998,1010,1023],
[976,993,1025,983,0,1008,1027,997,956,1009,989],
[1028,986,990,964,993,0,1024,1047,1007,1014,958],
[993,1009,1009,961,974,977,0,1013,989,988,964],
[1029,967,997,960,1004,954,988,0,992,960,979],
[1020,1003,1014,1003,1045,994,1012,1009,0,963,992],
[1045,1008,1005,991,992,987,1013,1041,1038,0,979],
[1056,1015,1042,978,1012,1043,1037,1022,1009,1022,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 68, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1017,1001,1040,1002,998,1006,990,996,989,1023],
[984,0,988,1025,1010,1024,1002,988,983,993,1012],
[1000,1013,0,1041,990,967,1012,1007,997,1004,1020],
[961,976,960,0,986,963,940,972,945,999,970],
[999,991,1011,1015,0,1011,984,1007,997,1010,1025],
[1003,977,1034,1038,990,0,1002,1000,992,1027,1043],
[995,999,989,1061,1017,999,0,1030,967,1003,986],
[1011,1013,994,1029,994,1001,971,0,1003,1050,1023],
[1005,1018,1004,1056,1004,1009,1034,998,0,1071,1032],
[1012,1008,997,1002,991,974,998,951,930,0,1005],
[978,989,981,1031,976,958,1015,978,969,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 69, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,1031,1076,1059,1024,1001,998,1028,1029,986],
[987,0,958,1023,990,993,1012,985,1009,969,987],
[970,1043,0,1042,1071,1014,995,1035,1048,1016,989],
[925,978,959,0,993,988,949,973,983,979,931],
[942,1011,930,1008,0,975,949,937,982,964,950],
[977,1008,987,1013,1026,0,1021,1000,1070,1012,1012],
[1000,989,1006,1052,1052,980,0,1035,1008,998,995],
[1003,1016,966,1028,1064,1001,966,0,1024,956,967],
[973,992,953,1018,1019,931,993,977,0,968,939],
[972,1032,985,1022,1037,989,1003,1045,1033,0,1002],
[1015,1014,1012,1070,1051,989,1006,1034,1062,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 70, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1012,1049,987,1032,1000,980,1040,1064,1035,964],
[989,0,1021,950,1011,1001,993,1032,1015,983,984],
[952,980,0,968,999,993,944,1009,977,989,964],
[1014,1051,1033,0,1019,1037,986,1032,1023,1042,1008],
[969,990,1002,982,0,1015,973,1034,1005,984,969],
[1001,1000,1008,964,986,0,989,1015,993,1022,972],
[1021,1008,1057,1015,1028,1012,0,1053,1039,1024,1000],
[961,969,992,969,967,986,948,0,960,993,931],
[937,986,1024,978,996,1008,962,1041,0,991,970],
[966,1018,1012,959,1017,979,977,1008,1010,0,968],
[1037,1017,1037,993,1032,1029,1001,1070,1031,1033,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 71, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,1050,1015,1053,982,1067,1030,1063,1013,1036],
[988,0,1020,1012,1005,933,995,1002,980,979,1002],
[951,981,0,987,982,997,967,981,994,942,925],
[986,989,1014,0,1006,947,924,1030,979,998,940],
[948,996,1019,995,0,952,991,1033,970,976,980],
[1019,1068,1004,1054,1049,0,984,1024,1030,1020,999],
[934,1006,1034,1077,1010,1017,0,993,1000,1007,984],
[971,999,1020,971,968,977,1008,0,993,985,1005],
[938,1021,1007,1022,1031,971,1001,1008,0,982,1005],
[988,1022,1059,1003,1025,981,994,1016,1019,0,1014],
[965,999,1076,1061,1021,1002,1017,996,996,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 72, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1057,975,899,986,1023,875,968,923,996,935],
[944,0,923,823,966,1038,940,927,969,989,960],
[1026,1078,0,967,965,1158,996,1117,964,1007,992],
[1102,1178,1034,0,968,1178,1068,1181,1020,996,1034],
[1015,1035,1036,1033,0,1158,1098,1086,1044,1075,996],
[978,963,843,823,843,0,855,932,950,949,927],
[1126,1061,1005,933,903,1146,0,1003,990,1118,992],
[1033,1074,884,820,915,1069,998,0,1046,995,920],
[1078,1032,1037,981,957,1051,1011,955,0,1054,963],
[1005,1012,994,1005,926,1052,883,1006,947,0,867],
[1066,1041,1009,967,1005,1074,1009,1081,1038,1134,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 73, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1233,801,930,763,851,1049,971,898,891,897],
[768,0,908,813,653,1138,1037,1011,780,1011,854],
[1200,1093,0,981,711,1178,1300,1269,850,678,976],
[1071,1188,1020,0,411,1183,1343,1298,922,869,923],
[1238,1348,1290,1590,0,1137,1501,1226,949,1158,1081],
[1150,863,823,818,864,0,1154,992,1046,791,922],
[952,964,701,658,500,847,0,1134,304,474,798],
[1030,990,732,703,775,1009,867,0,747,675,904],
[1103,1221,1151,1079,1052,955,1697,1254,0,1137,1200],
[1110,990,1323,1132,843,1210,1527,1326,864,0,883],
[1104,1147,1025,1078,920,1079,1203,1097,801,1118,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 74, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1048,969,997,1048,1002,1014,1073,1026,1027,999],
[953,0,947,963,1009,974,924,1001,985,928,954],
[1032,1054,0,1016,1061,1013,1030,1030,994,1066,1032],
[1004,1038,985,0,1017,1013,959,1053,977,985,998],
[953,992,940,984,0,959,905,986,964,948,978],
[999,1027,988,988,1042,0,935,1018,948,1033,1005],
[987,1077,971,1042,1096,1066,0,1019,1036,1052,1039],
[928,1000,971,948,1015,983,982,0,946,995,968],
[975,1016,1007,1024,1037,1053,965,1055,0,1033,1025],
[974,1073,935,1016,1053,968,949,1006,968,0,990],
[1002,1047,969,1003,1023,996,962,1033,976,1011,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 75, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1093,1020,1038,1022,970,1019,1070,996,871,892],
[908,0,949,841,951,934,985,1083,1033,880,1008],
[981,1052,0,1074,1142,1070,1246,1341,1080,914,1098],
[963,1160,927,0,1191,967,1086,1128,1025,911,1267],
[979,1050,859,810,0,969,1062,1057,1022,1002,1014],
[1031,1067,931,1034,1032,0,1129,1074,988,845,1040],
[982,1016,755,915,939,872,0,1147,898,844,956],
[931,918,660,873,944,927,854,0,994,842,863],
[1005,968,921,976,979,1013,1103,1007,0,804,915],
[1130,1121,1087,1090,999,1156,1157,1159,1197,0,1192],
[1109,993,903,734,987,961,1045,1138,1086,809,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 76, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,952,1020,996,1008,962,976,985,977,1001,998],
[1049,0,1043,1014,1029,1018,990,1022,1020,1018,1029],
[981,958,0,951,999,986,989,962,969,971,995],
[1005,987,1050,0,1002,986,970,970,1009,986,1000],
[993,972,1002,999,0,929,983,955,993,989,953],
[1039,983,1015,1015,1072,0,998,999,999,999,1009],
[1025,1011,1012,1031,1018,1003,0,993,1059,975,1003],
[1016,979,1039,1031,1046,1002,1008,0,997,1030,1009],
[1024,981,1032,992,1008,1002,942,1004,0,983,995],
[1000,983,1030,1015,1012,1002,1026,971,1018,0,978],
[1003,972,1006,1001,1048,992,998,992,1006,1023,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 77, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,975,1034,1021,989,992,1018,1007,1023,1034,1002],
[1026,0,1063,1023,1038,1025,995,1002,1020,1009,1032],
[967,938,0,966,982,948,993,959,992,974,971],
[980,978,1035,0,990,1008,992,1019,1011,1002,994],
[1012,963,1019,1011,0,993,976,994,981,963,1018],
[1009,976,1053,993,1008,0,1017,989,1022,1020,1041],
[983,1006,1008,1009,1025,984,0,1004,1021,982,993],
[994,999,1042,982,1007,1012,997,0,1040,1005,1013],
[978,981,1009,990,1020,979,980,961,0,991,996],
[967,992,1027,999,1038,981,1019,996,1010,0,1004],
[999,969,1030,1007,983,960,1008,988,1005,997,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 78, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,939,962,947,961,1010,955,924,963,927,970],
[1062,0,1006,975,1010,992,1023,942,1005,1010,1028],
[1039,995,0,1001,1033,1013,991,1011,1024,967,1015],
[1054,1026,1000,0,1049,1053,991,1007,1008,1011,1059],
[1040,991,968,952,0,961,966,946,967,919,963],
[991,1009,988,948,1040,0,996,978,979,950,1013],
[1046,978,1010,1010,1035,1005,0,1005,1050,972,1006],
[1077,1059,990,994,1055,1023,996,0,1028,961,1030],
[1038,996,977,993,1034,1022,951,973,0,951,995],
[1074,991,1034,990,1082,1051,1029,1040,1050,0,1063],
[1031,973,986,942,1038,988,995,971,1006,938,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 79, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,947,995,997,939,969,981,967,1000,966,949],
[1054,0,972,1028,992,1024,995,973,1025,971,975],
[1006,1029,0,1041,966,1004,966,987,1019,999,1000],
[1004,973,960,0,938,1028,998,993,1029,990,958],
[1062,1009,1035,1063,0,1052,1048,1000,1057,989,1054],
[1032,977,997,973,949,0,964,1009,1030,996,961],
[1020,1006,1035,1003,953,1037,0,1020,1060,967,1022],
[1034,1028,1014,1008,1001,992,981,0,1041,1029,1002],
[1001,976,982,972,944,971,941,960,0,976,952],
[1035,1030,1002,1011,1012,1005,1034,972,1025,0,1011],
[1052,1026,1001,1043,947,1040,979,999,1049,990,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 80, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,979,978,1022,1010,1002,992,1015,993,1004],
[995,0,980,953,1028,962,993,965,968,983,1002],
[1022,1021,0,1009,1023,1017,1011,986,984,1017,1008],
[1023,1048,992,0,1044,1012,991,1028,1003,1015,1030],
[979,973,978,957,0,993,968,983,974,984,982],
[991,1039,984,989,1008,0,977,982,990,1014,988],
[999,1008,990,1010,1033,1024,0,1005,1027,1017,1037],
[1009,1036,1015,973,1018,1019,996,0,980,980,1014],
[986,1033,1017,998,1027,1011,974,1021,0,995,1001],
[1008,1018,984,986,1017,987,984,1021,1006,0,1006],
[997,999,993,971,1019,1013,964,987,1000,995,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 81, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,964,1003,969,998,1040,1006,1018,957,1002,1013],
[1037,0,1025,1016,1019,1063,1000,1016,1015,988,1029],
[998,976,0,981,976,1024,948,991,970,963,1001],
[1032,985,1020,0,998,1057,960,993,984,996,1029],
[1003,982,1025,1003,0,1054,997,1020,998,1008,1038],
[961,938,977,944,947,0,964,974,959,971,990],
[995,1001,1053,1041,1004,1037,0,1018,1030,1026,1036],
[983,985,1010,1008,981,1027,983,0,991,1013,1029],
[1044,986,1031,1017,1003,1042,971,1010,0,989,1033],
[999,1013,1038,1005,993,1030,975,988,1012,0,1016],
[988,972,1000,972,963,1011,965,972,968,985,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 82, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1074,1030,1035,995,1014,1049,1044,1034,1020,1026],
[927,0,991,986,950,996,984,978,981,964,991],
[971,1010,0,1035,946,963,997,1010,1002,995,1019],
[966,1015,966,0,990,977,968,987,1015,995,1019],
[1006,1051,1055,1011,0,1010,1051,1020,1027,965,1014],
[987,1005,1038,1024,991,0,1019,1045,993,998,1007],
[952,1017,1004,1033,950,982,0,997,1040,986,1014],
[957,1023,991,1014,981,956,1004,0,981,970,1015],
[967,1020,999,986,974,1008,961,1020,0,996,986],
[981,1037,1006,1006,1036,1003,1015,1031,1005,0,1003],
[975,1010,982,982,987,994,987,986,1015,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 83, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1008,1020,1003,1010,1010,991,983,1013,978,1015],
[993,0,1015,1009,995,1020,980,991,1020,978,1000],
[981,986,0,967,964,985,958,953,958,950,978],
[998,992,1034,0,1024,988,954,1007,1004,948,1006],
[991,1006,1037,977,0,1021,979,1000,1035,968,997],
[991,981,1016,1013,980,0,966,992,996,994,1020],
[1010,1021,1043,1047,1022,1035,0,992,1032,1010,1022],
[1018,1010,1048,994,1001,1009,1009,0,1036,1013,1020],
[988,981,1043,997,966,1005,969,965,0,969,991],
[1023,1023,1051,1053,1033,1007,991,988,1032,0,1047],
[986,1001,1023,995,1004,981,979,981,1010,954,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 84, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,796,797,808,1045,1049,1013,734,617,660,1011],
[1205,0,1152,1320,1194,1080,1258,1370,1171,807,1280],
[1204,849,0,1298,1150,1303,1432,1238,1036,1041,1312],
[1193,681,703,0,722,704,1080,919,1072,776,1160],
[956,807,851,1279,0,865,1043,1025,937,960,1167],
[952,921,698,1297,1136,0,1097,1069,1050,735,1156],
[988,743,569,921,958,904,0,643,880,770,836],
[1267,631,763,1082,976,932,1358,0,732,983,948],
[1384,830,965,929,1064,951,1121,1269,0,927,1108],
[1341,1194,960,1225,1041,1266,1231,1018,1074,0,1056],
[990,721,689,841,834,845,1165,1053,893,945,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 85, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1088,1005,1024,1073,983,1040,924,1025,995,1079],
[913,0,1025,989,1089,984,1019,918,1016,1054,1023],
[996,976,0,941,954,920,1009,918,993,1031,1081],
[977,1012,1060,0,1041,991,995,1004,986,1072,969],
[928,912,1047,960,0,874,900,877,895,944,959],
[1018,1017,1081,1010,1127,0,1082,986,951,1050,1060],
[961,982,992,1006,1101,919,0,929,1009,1010,1026],
[1077,1083,1083,997,1124,1015,1072,0,1110,1103,1149],
[976,985,1008,1015,1106,1050,992,891,0,995,1087],
[1006,947,970,929,1057,951,991,898,1006,0,1071],
[922,978,920,1032,1042,941,975,852,914,930,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 86, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,915,949,948,976,994,991,901,954,995,944],
[1086,0,973,1004,1000,1001,1043,967,964,1049,955],
[1052,1028,0,987,1022,1022,999,999,1012,1076,977],
[1053,997,1014,0,972,1020,1036,1022,978,1004,986],
[1025,1001,979,1029,0,1096,1062,986,1006,1007,1002],
[1007,1000,979,981,905,0,927,919,957,970,1026],
[1010,958,1002,965,939,1074,0,951,1021,1002,1057],
[1100,1034,1002,979,1015,1082,1050,0,992,1046,1002],
[1047,1037,989,1023,995,1044,980,1009,0,1037,1012],
[1006,952,925,997,994,1031,999,955,964,0,995],
[1057,1046,1024,1015,999,975,944,999,989,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 87, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,964,1008,995,1038,1007,987,1045,987,1009,1034],
[1037,0,967,996,984,1049,967,1024,1016,1030,1045],
[993,1034,0,996,1020,1015,993,1017,1001,992,1022],
[1006,1005,1005,0,1018,1003,980,1011,1049,1008,1050],
[963,1017,981,983,0,1012,992,1002,971,991,1023],
[994,952,986,998,989,0,963,1022,985,980,1022],
[1014,1034,1008,1021,1009,1038,0,1036,997,1047,1056],
[956,977,984,990,999,979,965,0,972,1000,1018],
[1014,985,1000,952,1030,1016,1004,1029,0,990,1025],
[992,971,1009,993,1010,1021,954,1001,1011,0,1046],
[967,956,979,951,978,979,945,983,976,955,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 88, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,997,960,998,943,985,974,964,1001,960,1013],
[1004,0,1013,1048,953,1021,1023,949,995,999,1052],
[1041,988,0,1022,970,1004,970,1006,1013,986,1010],
[1003,953,979,0,946,992,978,961,986,970,1034],
[1058,1048,1031,1055,0,1034,1000,1019,1014,998,1038],
[1016,980,997,1009,967,0,981,975,1017,975,1031],
[1027,978,1031,1023,1001,1020,0,998,1016,971,1045],
[1037,1052,995,1040,982,1026,1003,0,1001,972,1028],
[1000,1006,988,1015,987,984,985,1000,0,980,1006],
[1041,1002,1015,1031,1003,1026,1030,1029,1021,0,994],
[988,949,991,967,963,970,956,973,995,1007,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 89, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1355,1154,1269,1007,1327,1168,1084,908,897,1092],
[646,0,757,894,709,676,730,1050,770,647,867],
[847,1244,0,1122,979,898,958,1132,854,948,1014],
[732,1107,879,0,810,847,847,1019,966,774,1114],
[994,1292,1022,1191,0,1062,1120,1145,1050,852,1092],
[674,1325,1103,1154,939,0,1276,1216,1020,1034,1281],
[833,1271,1043,1154,881,725,0,1013,951,1095,988],
[917,951,869,982,856,785,988,0,984,1107,887],
[1093,1231,1147,1035,951,981,1050,1017,0,1023,1002],
[1104,1354,1053,1227,1149,967,906,894,978,0,988],
[909,1134,987,887,909,720,1013,1114,999,1013,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 90, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,971,982,1027,1190,1064,962,1058,1010,1063,1066],
[1030,0,969,921,1074,1030,1116,963,971,956,953],
[1019,1032,0,1038,1186,1132,1122,893,1021,969,968],
[974,1080,963,0,1073,1200,1130,937,1004,1025,944],
[811,927,815,928,0,1034,973,975,890,979,821],
[937,971,869,801,967,0,975,932,990,878,946],
[1039,885,879,871,1028,1026,0,927,892,947,938],
[943,1038,1108,1064,1026,1069,1074,0,956,931,1049],
[991,1030,980,997,1111,1011,1109,1045,0,950,956],
[938,1045,1032,976,1022,1123,1054,1070,1051,0,1001],
[935,1048,1033,1057,1180,1055,1063,952,1045,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 91, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1004,991,1016,1037,984,1024,985,1008,1013,1032],
[997,0,1009,990,1028,991,997,976,977,1007,1032],
[1010,992,0,966,1007,930,980,974,983,1014,989],
[985,1011,1035,0,1040,1005,1006,990,987,1018,1038],
[964,973,994,961,0,918,1001,966,978,989,973],
[1017,1010,1071,996,1083,0,1047,1004,1008,1034,1065],
[977,1004,1021,995,1000,954,0,996,989,1030,992],
[1016,1025,1027,1011,1035,997,1005,0,995,1042,1020],
[993,1024,1018,1014,1023,993,1012,1006,0,1057,978],
[988,994,987,983,1012,967,971,959,944,0,1021],
[969,969,1012,963,1028,936,1009,981,1023,980,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 92, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1041,1007,960,950,995,1005,888,999,985,1006],
[960,0,942,984,931,959,987,938,983,972,975],
[994,1059,0,1017,1002,946,1086,983,1052,1019,1103],
[1041,1017,984,0,905,991,935,980,959,1009,989],
[1051,1070,999,1096,0,1019,1030,1044,1067,998,1038],
[1006,1042,1055,1010,982,0,1048,1015,1041,1060,1065],
[996,1014,915,1066,971,953,0,906,974,964,990],
[1113,1063,1018,1021,957,986,1095,0,983,1014,986],
[1002,1018,949,1042,934,960,1027,1018,0,990,1064],
[1016,1029,982,992,1003,941,1037,987,1011,0,1022],
[995,1026,898,1012,963,936,1011,1015,937,979,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 93, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1000,984,996,1012,1002,1009,970,962,983,1020],
[1001,0,1006,1016,1005,1011,1030,986,993,987,1023],
[1017,995,0,1000,1004,1012,1018,992,963,1000,1003],
[1005,985,1001,0,961,994,1013,971,1001,998,988],
[989,996,997,1040,0,1015,1016,993,975,992,992],
[999,990,989,1007,986,0,1021,1004,988,990,1005],
[992,971,983,988,985,980,0,963,990,957,987],
[1031,1015,1009,1030,1008,997,1038,0,1005,1004,1012],
[1039,1008,1038,1000,1026,1013,1011,996,0,1036,995],
[1018,1014,1001,1003,1009,1011,1044,997,965,0,1005],
[981,978,998,1013,1009,996,1014,989,1006,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 94, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,962,975,987,998,978,991,977,957,958,957],
[1039,0,976,995,987,988,986,949,975,964,975],
[1026,1025,0,1005,1002,1005,1031,959,986,994,1019],
[1014,1006,996,0,1005,1000,981,1003,980,1029,1008],
[1003,1014,999,996,0,1001,972,1010,975,994,1015],
[1023,1013,996,1001,1000,0,1006,972,967,1001,1029],
[1010,1015,970,1020,1029,995,0,981,953,1002,1008],
[1024,1052,1042,998,991,1029,1020,0,1001,1017,1022],
[1044,1026,1015,1021,1026,1034,1048,1000,0,1006,1012],
[1043,1037,1007,972,1007,1000,999,984,995,0,1027],
[1044,1026,982,993,986,972,993,979,989,974,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 95, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,1023,1024,1042,949,1032,995,987,1011,1025],
[987,0,1057,1104,1019,964,1014,1016,1027,951,1000],
[978,944,0,1043,1034,1006,1003,1054,1008,1003,959],
[977,897,958,0,942,905,951,952,962,954,930],
[959,982,967,1059,0,904,932,986,1007,950,993],
[1052,1037,995,1096,1097,0,1040,1049,1050,990,1056],
[969,987,998,1050,1069,961,0,1045,1002,973,940],
[1006,985,947,1049,1015,952,956,0,955,993,970],
[1014,974,993,1039,994,951,999,1046,0,1013,985],
[990,1050,998,1047,1051,1011,1028,1008,988,0,941],
[976,1001,1042,1071,1008,945,1061,1031,1016,1060,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 96, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,915,1018,987,813,883,997,1083,1010,944,989],
[1086,0,1010,1026,886,1030,1005,938,1022,1015,1022],
[983,991,0,993,1007,1009,1001,1031,993,997,1086],
[1014,975,1008,0,1024,1000,879,953,1067,1064,1050],
[1188,1115,994,977,0,1066,979,1079,998,1178,1048],
[1118,971,992,1001,935,0,1065,1031,1056,1063,1057],
[1004,996,1000,1122,1022,936,0,1096,1081,1073,1058],
[918,1063,970,1048,922,970,905,0,982,927,1043],
[991,979,1008,934,1003,945,920,1019,0,989,980],
[1057,986,1004,937,823,938,928,1074,1012,0,967],
[1012,979,915,951,953,944,943,958,1021,1034,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 97, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,966,985,1006,983,943,972,1011,1014,987,984],
[1035,0,1040,993,1020,1071,1015,1033,1072,1056,1009],
[1016,961,0,1070,1002,1000,1010,1047,1051,1004,1055],
[995,1008,931,0,978,1039,992,1033,1058,1025,981],
[1018,981,999,1023,0,1024,961,1027,1038,1020,1021],
[1058,930,1001,962,977,0,971,1020,1053,1013,1008],
[1029,986,991,1009,1040,1030,0,1012,1060,1055,1000],
[990,968,954,968,974,981,989,0,1043,1000,993],
[987,929,950,943,963,948,941,958,0,1009,975],
[1014,945,997,976,981,988,946,1001,992,0,981],
[1017,992,946,1020,980,993,1001,1008,1026,1020,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 98, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,962,984,1010,979,990,1052,1024,1002,998],
[1017,0,979,1004,1001,971,1000,1031,1040,989,1013],
[1039,1022,0,1037,1005,989,1024,1057,1040,1046,1029],
[1017,997,964,0,1018,994,1003,1030,1049,1022,1047],
[991,1000,996,983,0,984,1006,1036,1044,1056,1028],
[1022,1030,1012,1007,1017,0,1046,1010,1023,999,1085],
[1011,1001,977,998,995,955,0,1002,1009,983,1050],
[949,970,944,971,965,991,999,0,997,974,1007],
[977,961,961,952,957,978,992,1004,0,971,1009],
[999,1012,955,979,945,1002,1018,1027,1030,0,1036],
[1003,988,972,954,973,916,951,994,992,965,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 99, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,937,999,979,993,929,948,1025,981,974],
[998,0,947,969,987,972,947,990,977,966,975],
[1064,1054,0,1008,1056,1035,972,1030,1017,1029,1063],
[1002,1032,993,0,1015,1018,1005,1011,1017,988,1018],
[1022,1014,945,986,0,1010,975,1006,1011,988,1014],
[1008,1029,966,983,991,0,966,1007,1028,1028,989],
[1072,1054,1029,996,1026,1035,0,1014,1036,1023,1047],
[1053,1011,971,990,995,994,987,0,1006,1022,1020],
[976,1024,984,984,990,973,965,995,0,1015,1032],
[1020,1035,972,1013,1013,973,978,979,986,0,1036],
[1027,1026,938,983,987,1012,954,981,969,965,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 100, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,971,969,969,977,933,976,937,991,939,1031],
[1030,0,963,904,1030,926,964,891,951,1007,964],
[1032,1038,0,999,1040,1001,1039,962,998,1051,993],
[1032,1097,1002,0,1001,939,964,1003,961,960,997],
[1024,971,961,1000,0,880,995,951,997,959,997],
[1068,1075,1000,1062,1121,0,1052,1010,1021,1012,1046],
[1025,1037,962,1037,1006,949,0,965,1010,953,1025],
[1064,1110,1039,998,1050,991,1036,0,1022,1026,1064],
[1010,1050,1003,1040,1004,980,991,979,0,998,1028],
[1062,994,950,1041,1042,989,1048,975,1003,0,1037],
[970,1037,1008,1004,1004,955,976,937,973,964,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 101, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,968,1030,980,1081,969,967,945,1023,993,943],
[1033,0,1092,1031,1111,970,990,990,1035,1060,945],
[971,909,0,947,1015,924,967,995,1068,972,931],
[1021,970,1054,0,1022,992,975,1008,1033,997,986],
[920,890,986,979,0,950,988,984,989,905,903],
[1032,1031,1077,1009,1051,0,1044,995,1114,1044,995],
[1034,1011,1034,1026,1013,957,0,988,1029,1040,953],
[1056,1011,1006,993,1017,1006,1013,0,1059,1041,1049],
[978,966,933,968,1012,887,972,942,0,996,967],
[1008,941,1029,1004,1096,957,961,960,1005,0,1023],
[1058,1056,1070,1015,1098,1006,1048,952,1034,978,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 102, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,976,975,1006,980,987,1007,1002,983,977,949],
[1025,0,1017,1004,995,1006,1033,1016,1010,1005,1014],
[1026,984,0,1034,1002,1026,995,1044,1017,1011,997],
[995,997,967,0,979,993,992,1011,1009,1005,999],
[1021,1006,999,1022,0,1016,1031,1023,1015,1024,1016],
[1014,995,975,1008,985,0,968,1003,1004,982,976],
[994,968,1006,1009,970,1033,0,977,982,1006,1003],
[999,985,957,990,978,998,1024,0,995,978,990],
[1018,991,984,992,986,997,1019,1006,0,1015,966],
[1024,996,990,996,977,1019,995,1023,986,0,993],
[1052,987,1004,1002,985,1025,998,1011,1035,1008,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 103, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,1026,948,998,995,939,999,956,937,996],
[994,0,983,941,1003,991,959,1000,980,949,1004],
[975,1018,0,981,1021,988,950,1016,938,941,995],
[1053,1060,1020,0,1023,1003,995,1052,1002,989,1007],
[1003,998,980,978,0,1007,960,1002,957,943,1006],
[1006,1010,1013,998,994,0,961,993,980,961,983],
[1062,1042,1051,1006,1041,1040,0,1025,992,982,999],
[1002,1001,985,949,999,1008,976,0,935,946,999],
[1045,1021,1063,999,1044,1021,1009,1066,0,1012,1034],
[1064,1052,1060,1012,1058,1040,1019,1055,989,0,1027],
[1005,997,1006,994,995,1018,1002,1002,967,974,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 104, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1011,995,985,995,1004,1003,1005,962,1038,1021],
[990,0,968,991,1011,993,984,965,947,981,1000],
[1006,1033,0,1027,1033,986,1029,991,989,1032,1018],
[1016,1010,974,0,998,994,1022,1004,999,1038,986],
[1006,990,968,1003,0,1017,987,1017,1001,1026,1013],
[997,1008,1015,1007,984,0,1062,1010,969,1025,1015],
[998,1017,972,979,1014,939,0,989,957,1012,1024],
[996,1036,1010,997,984,991,1012,0,983,1023,1016],
[1039,1054,1012,1002,1000,1032,1044,1018,0,1042,1023],
[963,1020,969,963,975,976,989,978,959,0,979],
[980,1001,983,1015,988,986,977,985,978,1022,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 105, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,966,921,980,957,984,973,956,980,992],
[1014,0,968,929,993,1004,1023,1033,997,984,1033],
[1035,1033,0,954,1023,1008,1023,1036,1010,987,1003],
[1080,1072,1047,0,1011,1014,1069,1053,1044,999,1056],
[1021,1008,978,990,0,956,997,1070,1026,1013,1035],
[1044,997,993,987,1045,0,1024,1101,998,1022,1042],
[1017,978,978,932,1004,977,0,1037,1020,954,1015],
[1028,968,965,948,931,900,964,0,975,973,977],
[1045,1004,991,957,975,1003,981,1026,0,1016,1006],
[1021,1017,1014,1002,988,979,1047,1028,985,0,1057],
[1009,968,998,945,966,959,986,1024,995,944,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 106, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,970,1018,999,1012,997,948,1051,948,1020,1067],
[1031,0,996,1026,1014,1048,1038,881,1073,1038,1047],
[983,1005,0,972,993,977,942,1013,963,987,1027],
[1002,975,1029,0,1000,991,997,998,1004,1024,1049],
[989,987,1008,1001,0,1007,1033,993,1003,996,1050],
[1004,953,1024,1010,994,0,970,923,963,1070,1030],
[1053,963,1059,1004,968,1031,0,949,1025,1035,1041],
[950,1120,988,1003,1008,1078,1052,0,997,1034,1099],
[1053,928,1038,997,998,1038,976,1004,0,1137,1025],
[981,963,1014,977,1005,931,966,967,864,0,1002],
[934,954,974,952,951,971,960,902,976,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 107, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,960,1013,976,1014,1009,1034,995,1021,983],
[1024,0,1020,1044,987,1067,1039,1039,1015,1069,1055],
[1041,981,0,1082,1021,1035,1071,1042,1045,1013,1049],
[988,957,919,0,951,989,980,1002,1000,987,974],
[1025,1014,980,1050,0,1005,1037,1053,1036,1011,1022],
[987,934,966,1012,996,0,1025,994,984,982,1023],
[992,962,930,1021,964,976,0,984,991,975,999],
[967,962,959,999,948,1007,1017,0,981,979,1000],
[1006,986,956,1001,965,1017,1010,1020,0,1018,1047],
[980,932,988,1014,990,1019,1026,1022,983,0,1051],
[1018,946,952,1027,979,978,1002,1001,954,950,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 108, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1008,1040,1103,978,1074,1100,1022,1035,1078,1068],
[993,0,1025,1022,1028,1009,1064,1051,1001,1069,1068],
[961,976,0,986,995,968,1033,957,990,1026,1000],
[898,979,1015,0,994,1020,1030,940,907,995,972],
[1023,973,1006,1007,0,1052,1117,1000,971,1039,1077],
[927,992,1033,981,949,0,1041,983,986,1030,1018],
[901,937,968,971,884,960,0,882,935,974,983],
[979,950,1044,1061,1001,1018,1119,0,1039,1050,1089],
[966,1000,1011,1094,1030,1015,1066,962,0,1083,1044],
[923,932,975,1006,962,971,1027,951,918,0,992],
[933,933,1001,1029,924,983,1018,912,957,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 109, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,992,966,972,981,954,969,974,1005,999,1006],
[1009,0,988,1026,946,937,955,947,963,1026,996],
[1035,1013,0,1037,1003,986,1018,1003,1026,1028,1014],
[1029,975,964,0,967,947,931,950,978,978,994],
[1020,1055,998,1034,0,998,970,987,993,1034,1044],
[1047,1064,1015,1054,1003,0,988,997,1011,1035,1046],
[1032,1046,983,1070,1031,1013,0,986,1005,1014,1008],
[1027,1054,998,1051,1014,1004,1015,0,1026,1015,1066],
[996,1038,975,1023,1008,990,996,975,0,1023,1019],
[1002,975,973,1023,967,966,987,986,978,0,1002],
[995,1005,987,1007,957,955,993,935,982,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 110, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,962,989,1022,987,975,971,981,996,960],
[999,0,994,1000,1017,1020,993,978,1034,993,977],
[1039,1007,0,1003,1010,975,995,991,1000,1014,957],
[1012,1001,998,0,1016,992,1011,990,1017,1021,1000],
[979,984,991,985,0,965,998,986,1019,1009,981],
[1014,981,1026,1009,1036,0,1008,994,1012,1008,993],
[1026,1008,1006,990,1003,993,0,1016,1022,1000,1019],
[1030,1023,1010,1011,1015,1007,985,0,1005,1020,1023],
[1020,967,1001,984,982,989,979,996,0,1027,976],
[1005,1008,987,980,992,993,1001,981,974,0,998],
[1041,1024,1044,1001,1020,1008,982,978,1025,1003,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 111, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,977,975,998,1001,992,997,983,982,994,990],
[1024,0,1026,982,974,982,989,1027,999,1007,979],
[1026,975,0,1021,1021,985,1011,1031,972,1002,982],
[1003,1019,980,0,984,947,990,1001,969,961,972],
[1000,1027,980,1017,0,975,993,1002,982,994,1009],
[1009,1019,1016,1054,1026,0,998,1016,1010,994,1025],
[1004,1012,990,1011,1008,1003,0,1029,1008,1017,974],
[1018,974,970,1000,999,985,972,0,1025,964,955],
[1019,1002,1029,1032,1019,991,993,976,0,975,995],
[1007,994,999,1040,1007,1007,984,1037,1026,0,1014],
[1011,1022,1019,1029,992,976,1027,1046,1006,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 112, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1098,1013,1125,1009,1124,1094,1174,997,1189,1125],
[903,0,930,884,832,1142,962,833,938,1276,1117],
[988,1071,0,946,912,1131,1056,1022,959,1011,1184],
[876,1117,1055,0,956,1186,1072,1076,915,1131,1115],
[992,1169,1089,1045,0,1001,1055,1201,1170,1137,1227],
[877,859,870,815,1000,0,1033,1025,922,981,1092],
[907,1039,945,929,946,968,0,1084,1161,966,1114],
[827,1168,979,925,800,976,917,0,955,1035,1013],
[1004,1063,1042,1086,831,1079,840,1046,0,1099,1105],
[812,725,990,870,864,1020,1035,966,902,0,879],
[876,884,817,886,774,909,887,988,896,1122,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 113, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,950,1017,963,999,912,1077,951,962,995,949],
[1051,0,985,996,965,900,1031,985,971,1004,1033],
[984,1016,0,954,1002,868,1047,981,939,988,1021],
[1038,1005,1047,0,1025,935,1040,967,919,1033,1010],
[1002,1036,999,976,0,943,1016,993,985,978,970],
[1089,1101,1133,1066,1058,0,1077,1067,1000,1091,1086],
[924,970,954,961,985,924,0,974,947,1010,957],
[1050,1016,1020,1034,1008,934,1027,0,978,1004,965],
[1039,1030,1062,1082,1016,1001,1054,1023,0,1060,979],
[1006,997,1013,968,1023,910,991,997,941,0,931],
[1052,968,980,991,1031,915,1044,1036,1022,1070,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 114, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1050,979,965,1009,982,983,990,991,997,1028],
[951,0,985,939,981,932,1007,977,955,1000,1023],
[1022,1016,0,998,1034,991,1004,1007,986,1029,1050],
[1036,1062,1003,0,1048,1006,1021,986,1013,1057,1069],
[992,1020,967,953,0,976,975,997,978,1049,995],
[1019,1069,1010,995,1025,0,972,1004,994,1034,1034],
[1018,994,997,980,1026,1029,0,1011,991,1019,1038],
[1011,1024,994,1015,1004,997,990,0,973,1025,1022],
[1010,1046,1015,988,1023,1007,1010,1028,0,1027,1045],
[1004,1001,972,944,952,967,982,976,974,0,990],
[973,978,951,932,1006,967,963,979,956,1011,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 115, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,1013,1073,1075,1012,1030,997,974,1021,1003],
[992,0,1046,1063,1109,1008,1082,1060,1054,1094,1006],
[988,955,0,938,996,949,995,984,919,952,922],
[928,938,1063,0,1065,981,1014,979,994,982,959],
[926,892,1005,936,0,985,917,961,965,863,977],
[989,993,1052,1020,1016,0,983,991,1011,989,941],
[971,919,1006,987,1084,1018,0,945,1033,983,917],
[1004,941,1017,1022,1040,1010,1056,0,1008,1005,1010],
[1027,947,1082,1007,1036,990,968,993,0,1007,1011],
[980,907,1049,1019,1138,1012,1018,996,994,0,988],
[998,995,1079,1042,1024,1060,1084,991,990,1013,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 116, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,984,1043,983,1043,966,1042,964,1016,968,1021],
[1017,0,980,975,987,959,1016,1006,996,1010,979],
[958,1021,0,1016,938,994,999,924,1006,998,970],
[1018,1026,985,0,934,980,988,972,990,991,978],
[958,1014,1063,1067,0,962,982,996,995,1018,985],
[1035,1042,1007,1021,1039,0,996,997,1007,985,1010],
[959,985,1002,1013,1019,1005,0,964,961,968,1015],
[1037,995,1077,1029,1005,1004,1037,0,1020,984,1012],
[985,1005,995,1011,1006,994,1040,981,0,1007,954],
[1033,991,1003,1010,983,1016,1033,1017,994,0,988],
[980,1022,1031,1023,1016,991,986,989,1047,1013,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 117, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,1032,1017,1040,1039,975,1015,1022,1050,1075],
[994,0,1029,1059,1025,1059,998,1006,1001,993,1018],
[969,972,0,1042,1003,1029,1013,1006,998,1001,1022],
[984,942,959,0,991,979,952,1014,983,992,993],
[961,976,998,1010,0,1023,965,960,985,1043,993],
[962,942,972,1022,978,0,953,963,998,1059,1022],
[1026,1003,988,1049,1036,1048,0,1004,1046,1042,1034],
[986,995,995,987,1041,1038,997,0,1040,1042,982],
[979,1000,1003,1018,1016,1003,955,961,0,997,1046],
[951,1008,1000,1009,958,942,959,959,1004,0,1027],
[926,983,979,1008,1008,979,967,1019,955,974,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 118, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,914,980,921,893,930,931,987,1021,1052],
[1002,0,966,947,1039,918,998,982,1034,946,993],
[1087,1035,0,1036,1039,1033,1008,961,1043,1030,1074],
[1021,1054,965,0,973,961,993,932,906,1006,1033],
[1080,962,962,1028,0,952,963,937,971,963,1089],
[1108,1083,968,1040,1049,0,1052,1001,1055,1042,1055],
[1071,1003,993,1008,1038,949,0,956,1047,1053,1096],
[1070,1019,1040,1069,1064,1000,1045,0,1083,1034,1048],
[1014,967,958,1095,1030,946,954,918,0,963,1058],
[980,1055,971,995,1038,959,948,967,1038,0,1044],
[949,1008,927,968,912,946,905,953,943,957,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 119, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1023,1012,958,980,1012,1055,951,1060,1040,989],
[978,0,1041,922,993,956,1003,941,1027,992,987],
[989,960,0,978,936,983,995,890,1047,1040,1008],
[1043,1079,1023,0,1039,1047,1098,957,1107,1052,1059],
[1021,1008,1065,962,0,1023,1060,1039,1057,1033,1037],
[989,1045,1018,954,978,0,1023,917,1070,1017,990],
[946,998,1006,903,941,978,0,873,982,983,1030],
[1050,1060,1111,1044,962,1084,1128,0,1103,1129,1064],
[941,974,954,894,944,931,1019,898,0,1013,1000],
[961,1009,961,949,968,984,1018,872,988,0,966],
[1012,1014,993,942,964,1011,971,937,1001,1035,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 120, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1029,1042,1067,1069,1028,1005,1041,986,1037,1030],
[972,0,998,1006,1013,964,980,1052,1017,1024,977],
[959,1003,0,1007,1025,997,978,1011,988,1027,1016],
[934,995,994,0,1011,989,961,996,964,1010,971],
[932,988,976,990,0,969,964,979,963,997,974],
[973,1037,1004,1012,1032,0,996,1041,994,1036,1031],
[996,1021,1023,1040,1037,1005,0,1027,980,1044,1011],
[960,949,990,1005,1022,960,974,0,951,1024,969],
[1015,984,1013,1037,1038,1007,1021,1050,0,1044,1007],
[964,977,974,991,1004,965,957,977,957,0,959],
[971,1024,985,1030,1027,970,990,1032,994,1042,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 121, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1001,975,968,997,972,1006,982,1060,989,985],
[1000,0,1012,975,1000,982,1032,1026,1018,1019,1006],
[1026,989,0,997,994,971,972,971,1052,989,999],
[1033,1026,1004,0,1024,1007,1056,1046,1070,1043,994],
[1004,1001,1007,977,0,981,1005,1013,1052,1027,988],
[1029,1019,1030,994,1020,0,996,1028,1119,1024,992],
[995,969,1029,945,996,1005,0,961,1041,980,999],
[1019,975,1030,955,988,973,1040,0,1075,1016,998],
[941,983,949,931,949,882,960,926,0,932,918],
[1012,982,1012,958,974,977,1021,985,1069,0,990],
[1016,995,1002,1007,1013,1009,1002,1003,1083,1011,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 122, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,1025,1025,1022,1015,1009,1019,1045,1025,1049],
[1008,0,1020,1011,995,985,993,993,1009,998,1025],
[976,981,0,974,956,991,988,987,1022,990,1018],
[976,990,1027,0,967,1013,1000,997,1001,985,1001],
[979,1006,1045,1034,0,1036,1018,1010,1050,987,1064],
[986,1016,1010,988,965,0,1008,971,1025,983,999],
[992,1008,1013,1001,983,993,0,1016,1020,1006,1040],
[982,1008,1014,1004,991,1030,985,0,992,1005,1008],
[956,992,979,1000,951,976,981,1009,0,994,970],
[976,1003,1011,1016,1014,1018,995,996,1007,0,1026],
[952,976,983,1000,937,1002,961,993,1031,975,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 123, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1182,1162,1093,1043,1195,1272,1074,1003,1198,930],
[819,0,1065,1087,1183,891,877,830,1105,912,905],
[839,936,0,908,924,808,1002,726,1028,799,938],
[908,914,1093,0,773,1122,1036,740,880,1034,1097],
[958,818,1077,1228,0,967,915,848,853,941,896],
[806,1110,1193,879,1034,0,893,672,965,838,802],
[729,1124,999,965,1086,1108,0,974,1099,995,1227],
[927,1171,1275,1261,1153,1329,1027,0,1128,1041,1348],
[998,896,973,1121,1148,1036,902,873,0,894,1140],
[803,1089,1202,967,1060,1163,1006,960,1107,0,999],
[1071,1096,1063,904,1105,1199,774,653,861,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 124, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,990,967,1038,1002,1029,983,976,984,1003],
[1013,0,949,967,1038,1010,985,990,931,970,984],
[1011,1052,0,984,1058,1031,1029,1009,990,1011,1038],
[1034,1034,1017,0,1053,1018,1021,994,956,983,1039],
[963,963,943,948,0,988,972,945,950,941,970],
[999,991,970,983,1013,0,978,960,975,988,996],
[972,1016,972,980,1029,1023,0,980,982,1010,1021],
[1018,1011,992,1007,1056,1041,1021,0,1008,1015,1030],
[1025,1070,1011,1045,1051,1026,1019,993,0,1011,1016],
[1017,1031,990,1018,1060,1013,991,986,990,0,1032],
[998,1017,963,962,1031,1005,980,971,985,969,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 125, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,985,979,984,977,989,961,960,969,990,938],
[1016,0,1034,969,975,993,952,1015,946,1007,972],
[1022,967,0,975,994,1008,967,981,960,994,967],
[1017,1032,1026,0,1040,1026,1020,1003,971,1017,997],
[1024,1026,1007,961,0,1008,977,960,966,989,943],
[1012,1008,993,975,993,0,983,1002,950,997,951],
[1040,1049,1034,981,1024,1018,0,1008,958,1039,1005],
[1041,986,1020,998,1041,999,993,0,994,1035,1000],
[1032,1055,1041,1030,1035,1051,1043,1007,0,1035,999],
[1011,994,1007,984,1012,1004,962,966,966,0,938],
[1063,1029,1034,1004,1058,1050,996,1001,1002,1063,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 126, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,1020,1006,1011,1070,1011,1032,1076,1011,1023],
[1007,0,1046,965,1035,1002,1006,997,1061,1056,1032],
[981,955,0,981,1007,1017,995,981,1011,994,1038],
[995,1036,1020,0,1027,1057,998,1009,1032,1047,1001],
[990,966,994,974,0,1006,964,988,1017,1020,987],
[931,999,984,944,995,0,928,978,999,993,943],
[990,995,1006,1003,1037,1073,0,1010,1030,1056,1039],
[969,1004,1020,992,1013,1023,991,0,1016,1006,982],
[925,940,990,969,984,1002,971,985,0,991,969],
[990,945,1007,954,981,1008,945,995,1010,0,946],
[978,969,963,1000,1014,1058,962,1019,1032,1055,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 127, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1032,1024,1002,1001,1021,981,1000,1019,1006,1019],
[969,0,1044,985,1042,1020,1010,1008,1022,1009,1007],
[977,957,0,942,1023,996,988,1006,991,981,977],
[999,1016,1059,0,1024,1056,1054,1029,1024,1010,1010],
[1000,959,978,977,0,1002,995,983,979,1008,995],
[980,981,1005,945,999,0,982,992,984,975,999],
[1020,991,1013,947,1006,1019,0,963,1010,1020,987],
[1001,993,995,972,1018,1009,1038,0,1027,982,991],
[982,979,1010,977,1022,1017,991,974,0,982,986],
[995,992,1020,991,993,1026,981,1019,1019,0,996],
[982,994,1024,991,1006,1002,1014,1010,1015,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 128, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,942,966,982,997,1004,990,989,1008,958,1014],
[1059,0,1023,1024,1033,1021,1044,1064,1000,1019,1058],
[1035,978,0,1004,1039,1018,968,1011,982,996,1040],
[1019,977,997,0,1030,994,1017,1005,993,970,1055],
[1004,968,962,971,0,966,953,978,983,984,992],
[997,980,983,1007,1035,0,1006,1002,966,983,1034],
[1011,957,1033,984,1048,995,0,1014,1041,997,1035],
[1012,937,990,996,1023,999,987,0,990,971,994],
[993,1001,1019,1008,1018,1035,960,1011,0,985,1035],
[1043,982,1005,1031,1017,1018,1004,1030,1016,0,1057],
[987,943,961,946,1009,967,966,1007,966,944,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 129, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,956,1016,1008,999,979,982,973,1005,957,1005],
[1045,0,984,1031,1032,1007,1011,986,1037,1028,1013],
[985,1017,0,1001,1018,1022,972,995,1035,958,1008],
[993,970,1000,0,999,1001,1021,971,1031,974,1007],
[1002,969,983,1002,0,977,976,970,1002,979,975],
[1022,994,979,1000,1024,0,1021,985,999,977,1025],
[1019,990,1029,980,1025,980,0,971,1010,987,995],
[1028,1015,1006,1030,1031,1016,1030,0,1020,1000,997],
[996,964,966,970,999,1002,991,981,0,994,1005],
[1044,973,1043,1027,1022,1024,1014,1001,1007,0,1017],
[996,988,993,994,1026,976,1006,1004,996,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 130, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1040,1042,1089,1080,1080,979,1104,1046,1113,1067],
[961,0,1028,963,978,951,991,1084,933,1088,1011],
[959,973,0,924,1010,992,1031,1096,937,1016,990],
[912,1038,1077,0,1003,1008,1059,1048,1009,1014,1074],
[921,1023,991,998,0,930,1039,1162,1057,1073,1064],
[921,1050,1009,993,1071,0,1012,1080,1056,1056,1023],
[1022,1010,970,942,962,989,0,1087,1074,961,1020],
[897,917,905,953,839,921,914,0,1006,1000,887],
[955,1068,1064,992,944,945,927,995,0,1074,1087],
[888,913,985,987,928,945,1040,1001,927,0,932],
[934,990,1011,927,937,978,981,1114,914,1069,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 131, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1069,1037,1032,906,1045,923,936,957,939,925],
[932,0,1085,1062,980,994,972,1060,1082,1000,947],
[964,916,0,972,1003,1009,886,938,964,937,886],
[969,939,1029,0,944,1030,944,892,956,982,960],
[1095,1021,998,1057,0,983,953,928,939,928,938],
[956,1007,992,971,1018,0,893,987,930,941,929],
[1078,1029,1115,1057,1048,1108,0,984,998,1021,883],
[1065,941,1063,1109,1073,1014,1017,0,1041,991,1016],
[1044,919,1037,1045,1062,1071,1003,960,0,928,870],
[1062,1001,1064,1019,1073,1060,980,1010,1073,0,1024],
[1076,1054,1115,1041,1063,1072,1118,985,1131,977,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 132, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,1014,985,982,991,992,979,1003,994,988],
[1014,0,1016,1006,997,1012,1027,1001,1026,1015,1024],
[987,985,0,987,1011,988,986,985,967,957,972],
[1016,995,1014,0,1000,1002,1049,996,1022,1003,998],
[1019,1004,990,1001,0,989,1010,977,992,995,983],
[1010,989,1013,999,1012,0,1006,979,990,1025,1008],
[1009,974,1015,952,991,995,0,966,984,987,977],
[1022,1000,1016,1005,1024,1022,1035,0,1009,1003,994],
[998,975,1034,979,1009,1011,1017,992,0,978,978],
[1007,986,1044,998,1006,976,1014,998,1023,0,968],
[1013,977,1029,1003,1018,993,1024,1007,1023,1033,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 133, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1097,1062,1022,1041,990,1028,1037,1042,1077,1123],
[904,0,959,980,1000,965,943,982,982,1058,973],
[939,1042,0,1011,1032,1007,904,945,1029,1008,1058],
[979,1021,990,0,1031,975,912,990,1042,1000,994],
[960,1001,969,970,0,950,945,998,1039,1021,1042],
[1011,1036,994,1026,1051,0,933,996,1040,1039,1115],
[973,1058,1097,1089,1056,1068,0,1006,1004,1007,1076],
[964,1019,1056,1011,1003,1005,995,0,1048,1099,1048],
[959,1019,972,959,962,961,997,953,0,990,927],
[924,943,993,1001,980,962,994,902,1011,0,1023],
[878,1028,943,1007,959,886,925,953,1074,978,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 134, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,999,1015,983,1011,1009,995,958,1037,1021,999],
[1002,0,1011,994,999,1016,1010,978,1014,995,986],
[986,990,0,992,978,1014,979,981,1011,956,976],
[1018,1007,1009,0,1000,1006,994,971,1004,1001,983],
[990,1002,1023,1001,0,1039,1008,979,1019,1018,997],
[992,985,987,995,962,0,1008,1007,993,1012,1003],
[1006,991,1022,1007,993,993,0,956,1004,987,981],
[1043,1023,1020,1030,1022,994,1045,0,1063,1007,996],
[964,987,990,997,982,1008,997,938,0,1000,984],
[980,1006,1045,1000,983,989,1014,994,1001,0,1001],
[1002,1015,1025,1018,1004,998,1020,1005,1017,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 135, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,940,1035,942,882,1126,1036,1115,897,957,959],
[1061,0,1021,1051,1139,1109,1035,959,1182,981,939],
[966,980,0,946,1016,1096,983,1060,1024,936,826],
[1059,950,1055,0,992,1243,1114,1107,1142,1010,1015],
[1119,862,985,1009,0,1176,1028,1051,1081,1084,1079],
[875,892,905,758,825,0,1032,911,949,1006,891],
[965,966,1018,887,973,969,0,868,1117,844,810],
[886,1042,941,894,950,1090,1133,0,1047,977,1048],
[1104,819,977,859,920,1052,884,954,0,994,831],
[1044,1020,1065,991,917,995,1157,1024,1007,0,977],
[1042,1062,1175,986,922,1110,1191,953,1170,1024,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 136, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1008,1016,1025,994,993,990,954,1018,1001,967],
[993,0,998,1064,998,1020,989,997,1002,1014,949],
[985,1003,0,1051,1019,966,1041,1048,1003,1036,979],
[976,937,950,0,931,959,972,937,977,937,935],
[1007,1003,982,1070,0,992,1003,975,1015,955,1005],
[1008,981,1035,1042,1009,0,1033,988,1028,999,954],
[1011,1012,960,1029,998,968,0,1003,971,987,935],
[1047,1004,953,1064,1026,1013,998,0,1034,981,996],
[983,999,998,1024,986,973,1030,967,0,977,980],
[1000,987,965,1064,1046,1002,1014,1020,1024,0,1014],
[1034,1052,1022,1066,996,1047,1066,1005,1021,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 137, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1065,1097,1086,1114,999,1066,1128,1127,1080,1078],
[936,0,995,1041,1041,973,986,1035,1017,982,1037],
[904,1006,0,1024,1052,1029,992,1002,1002,972,975],
[915,960,977,0,1030,948,970,1047,968,978,989],
[887,960,949,971,0,928,970,973,984,957,972],
[1002,1028,972,1053,1073,0,998,1004,1016,1032,1031],
[935,1015,1009,1031,1031,1003,0,1054,1027,997,964],
[873,966,999,954,1028,997,947,0,999,996,1008],
[874,984,999,1033,1017,985,974,1002,0,927,952],
[921,1019,1029,1023,1044,969,1004,1005,1074,0,1002],
[923,964,1026,1012,1029,970,1037,993,1049,999,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 138, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1014,990,1015,1023,978,1002,1001,1011,988,991],
[987,0,1004,998,976,966,984,976,968,985,987],
[1011,997,0,1017,999,974,999,979,1007,1001,981],
[986,1003,984,0,996,1001,983,988,990,977,1021],
[978,1025,1002,1005,0,994,967,995,1015,971,1014],
[1023,1035,1027,1000,1007,0,1006,1003,1029,1012,1025],
[999,1017,1002,1018,1034,995,0,994,1003,1005,993],
[1000,1025,1022,1013,1006,998,1007,0,1021,1022,1022],
[990,1033,994,1011,986,972,998,980,0,1006,994],
[1013,1016,1000,1024,1030,989,996,979,995,0,1003],
[1010,1014,1020,980,987,976,1008,979,1007,998,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 139, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,994,1015,1034,979,996,993,1003,1015,1005],
[1007,0,977,1044,1051,1020,1013,996,994,976,1019],
[1007,1024,0,1014,999,1020,1035,1012,1031,1048,1041],
[986,957,987,0,983,969,956,933,960,961,1013],
[967,950,1002,1018,0,957,976,960,993,940,1019],
[1022,981,981,1032,1044,0,978,964,1010,996,1023],
[1005,988,966,1045,1025,1023,0,979,989,991,1028],
[1008,1005,989,1068,1041,1037,1022,0,1035,953,1048],
[998,1007,970,1041,1008,991,1012,966,0,1007,1066],
[986,1025,953,1040,1061,1005,1010,1048,994,0,1073],
[996,982,960,988,982,978,973,953,935,928,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 140, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,963,1008,1022,1032,994,989,969,1008,1003,981],
[1038,0,1004,1022,1040,989,1011,993,1015,1025,1037],
[993,997,0,990,1028,990,974,1014,987,986,1033],
[979,979,1011,0,1003,993,984,986,974,988,1006],
[969,961,973,998,0,984,969,970,984,939,994],
[1007,1012,1011,1008,1017,0,988,979,1019,995,1001],
[1012,990,1027,1017,1032,1013,0,999,1019,1001,1035],
[1032,1008,987,1015,1031,1022,1002,0,1022,975,1024],
[993,986,1014,1027,1017,982,982,979,0,1001,1006],
[998,976,1015,1013,1062,1006,1000,1026,1000,0,1013],
[1020,964,968,995,1007,1000,966,977,995,988,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 141, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,985,1032,960,1025,1016,989,990,1028,1022,1005],
[1016,0,1012,974,1036,1025,1010,1003,1027,1024,1015],
[969,989,0,973,1010,978,978,1002,1015,1021,996],
[1041,1027,1028,0,1021,1042,1024,1022,1020,998,1006],
[976,965,991,980,0,1001,1004,975,1030,1011,992],
[985,976,1023,959,1000,0,1006,962,1007,1020,998],
[1012,991,1023,977,997,995,0,994,1051,1015,979],
[1011,998,999,979,1026,1039,1007,0,1024,1014,1013],
[973,974,986,981,971,994,950,977,0,994,973],
[979,977,980,1003,990,981,986,987,1007,0,977],
[996,986,1005,995,1009,1003,1022,988,1028,1024,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 142, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,980,958,945,1021,981,953,970,939,992,992],
[1021,0,1015,995,1003,999,1023,963,959,984,1015],
[1043,986,0,993,1044,1039,989,975,961,920,970],
[1056,1006,1008,0,1040,1017,1048,1032,989,974,1022],
[980,998,957,961,0,989,994,937,952,932,954],
[1020,1002,962,984,1012,0,1002,972,968,930,959],
[1048,978,1012,953,1007,999,0,981,964,953,1033],
[1031,1038,1026,969,1064,1029,1020,0,1023,998,986],
[1062,1042,1040,1012,1049,1033,1037,978,0,1008,1041],
[1009,1017,1081,1027,1069,1071,1048,1003,993,0,1019],
[1009,986,1031,979,1047,1042,968,1015,960,982,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 143, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1057,1158,999,1132,1074,1069,1081,1300,1127,857],
[944,0,1174,1049,1260,1145,1192,1140,1211,1124,1077],
[843,827,0,850,962,776,827,856,1035,980,678],
[1002,952,1151,0,1248,965,1107,1160,1126,1247,993],
[869,741,1039,753,0,707,913,843,947,767,740],
[927,856,1225,1036,1294,0,1038,1075,1128,1113,963],
[932,809,1174,894,1088,963,0,1058,1099,1086,951],
[920,861,1145,841,1158,926,943,0,1089,1036,909],
[701,790,966,875,1054,873,902,912,0,977,648],
[874,877,1021,754,1234,888,915,965,1024,0,899],
[1144,924,1323,1008,1261,1038,1050,1092,1353,1102,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 144, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,961,921,1004,929,957,963,1004,1005,871,963],
[1040,0,1026,1094,979,995,969,1051,1069,1029,1025],
[1080,975,0,970,882,952,939,1017,941,975,956],
[997,907,1031,0,966,945,1011,1023,1017,963,937],
[1072,1022,1119,1035,0,1002,976,1101,1075,974,1033],
[1044,1006,1049,1056,999,0,892,1022,1047,977,946],
[1038,1032,1062,990,1025,1109,0,1025,987,1006,1040],
[997,950,984,978,900,979,976,0,951,935,913],
[996,932,1060,984,926,954,1014,1050,0,915,900],
[1130,972,1026,1038,1027,1024,995,1066,1086,0,969],
[1038,976,1045,1064,968,1055,961,1088,1101,1032,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 145, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1091,1030,1047,951,1059,1092,1064,1057,1019,1010],
[910,0,916,952,937,924,1001,995,977,842,873],
[971,1085,0,1125,1025,1139,1091,1122,1037,1012,1074],
[954,1049,876,0,899,980,983,1000,994,900,929],
[1050,1064,976,1102,0,1024,1017,1045,1025,981,984],
[942,1077,862,1021,977,0,1071,1060,960,998,1046],
[909,1000,910,1018,984,930,0,922,991,872,842],
[937,1006,879,1001,956,941,1079,0,948,916,907],
[944,1024,964,1007,976,1041,1010,1053,0,1032,987],
[982,1159,989,1101,1020,1003,1129,1085,969,0,1019],
[991,1128,927,1072,1017,955,1159,1094,1014,982,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 146, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1026,996,1027,1007,1003,998,1009,1017,1026,1042],
[975,0,1003,1010,1013,1001,971,989,977,1014,1001],
[1005,998,0,1022,1015,1015,991,993,1024,985,1021],
[974,991,979,0,991,986,962,961,978,976,982],
[994,988,986,1010,0,1018,984,992,975,986,1011],
[998,1000,986,1015,983,0,1002,982,996,999,1023],
[1003,1030,1010,1039,1017,999,0,974,1003,1002,1018],
[992,1012,1008,1040,1009,1019,1027,0,993,1017,1036],
[984,1024,977,1023,1026,1005,998,1008,0,999,1023],
[975,987,1016,1025,1015,1002,999,984,1002,0,1038],
[959,1000,980,1019,990,978,983,965,978,963,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 147, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1009,1026,1004,1001,1000,983,997,998,1055,963],
[992,0,992,975,1001,987,951,990,991,999,974],
[975,1009,0,974,960,964,960,963,991,1008,955],
[997,1026,1027,0,1026,991,936,991,1009,1011,964],
[1000,1000,1041,975,0,974,995,993,1003,1053,963],
[1001,1014,1037,1010,1027,0,1044,993,1030,1008,984],
[1018,1050,1041,1065,1006,957,0,982,1033,1039,1011],
[1004,1011,1038,1010,1008,1008,1019,0,1028,995,1011],
[1003,1010,1010,992,998,971,968,973,0,1027,967],
[946,1002,993,990,948,993,962,1006,974,0,933],
[1038,1027,1046,1037,1038,1017,990,990,1034,1068,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 148, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,966,1006,985,966,966,1018,956,975,993,1079],
[1035,0,1084,1044,1061,1032,992,924,943,977,1090],
[995,917,0,972,958,945,993,976,939,915,967],
[1016,957,1029,0,1043,1042,961,1011,1031,1078,1095],
[1035,940,1043,958,0,1039,1021,951,997,1015,1017],
[1035,969,1056,959,962,0,960,929,948,1030,1027],
[983,1009,1008,1040,980,1041,0,1060,1004,1017,1019],
[1045,1077,1025,990,1050,1072,941,0,1014,1087,1065],
[1026,1058,1062,970,1004,1053,997,987,0,993,1083],
[1008,1024,1086,923,986,971,984,914,1008,0,1017],
[922,911,1034,906,984,974,982,936,918,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 149, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,994,985,1000,965,1012,972,986,976,960],
[998,0,1009,1010,971,990,1014,1015,1060,1011,990],
[1007,992,0,1042,986,1012,983,1016,1035,984,979],
[1016,991,959,0,995,981,1004,990,999,939,1018],
[1001,1030,1015,1006,0,987,997,1035,1036,967,995],
[1036,1011,989,1020,1014,0,1026,1009,998,975,993],
[989,987,1018,997,1004,975,0,973,1028,969,948],
[1029,986,985,1011,966,992,1028,0,1011,978,968],
[1015,941,966,1002,965,1003,973,990,0,956,992],
[1025,990,1017,1062,1034,1026,1032,1023,1045,0,1007],
[1041,1011,1022,983,1006,1008,1053,1033,1009,994,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 150, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,976,997,1008,967,981,1014,1044,979,993,1013],
[1025,0,994,1045,994,990,1032,1046,962,974,1016],
[1004,1007,0,1001,976,1032,1024,1039,992,1004,990],
[993,956,1000,0,1019,983,1035,1005,994,965,979],
[1034,1007,1025,982,0,979,1040,1005,980,960,1043],
[1020,1011,969,1018,1022,0,1002,1092,1042,1005,1020],
[987,969,977,966,961,999,0,999,906,979,915],
[957,955,962,996,996,909,1002,0,1027,964,1000],
[1022,1039,1009,1007,1021,959,1095,974,0,967,995],
[1008,1027,997,1036,1041,996,1022,1037,1034,0,1022],
[988,985,1011,1022,958,981,1086,1001,1006,979,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 151, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,954,998,1024,951,1016,984,970,1013,1031,979],
[1047,0,1053,1041,1035,990,1065,986,1088,1075,1016],
[1003,948,0,978,1004,970,1011,965,1004,986,961],
[977,960,1023,0,992,953,992,986,1025,1015,957],
[1050,966,997,1009,0,1032,1051,1009,1052,1070,1018],
[985,1011,1031,1048,969,0,1055,1016,1084,1036,994],
[1017,936,990,1009,950,946,0,951,1007,1020,957],
[1031,1015,1036,1015,992,985,1050,0,1056,1042,1043],
[988,913,997,976,949,917,994,945,0,983,930],
[970,926,1015,986,931,965,981,959,1018,0,960],
[1022,985,1040,1044,983,1007,1044,958,1071,1041,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 152, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,995,993,980,947,1022,972,970,1008,977,997],
[1006,0,1015,1024,976,1052,1009,979,953,998,970],
[1008,986,0,995,973,1002,981,986,987,993,1000],
[1021,977,1006,0,999,976,1004,986,971,969,1026],
[1054,1025,1028,1002,0,989,972,955,980,1002,1015],
[979,949,999,1025,1012,0,996,988,971,1011,1024],
[1029,992,1020,997,1029,1005,0,989,997,1001,1043],
[1031,1022,1015,1015,1046,1013,1012,0,981,1011,1007],
[993,1048,1014,1030,1021,1030,1004,1020,0,996,997],
[1024,1003,1008,1032,999,990,1000,990,1005,0,1004],
[1004,1031,1001,975,986,977,958,994,1004,997,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 153, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1118,1056,1035,1038,1013,1030,1032,964,1000,994],
[883,0,907,961,894,881,986,966,944,930,867],
[945,1094,0,1082,1004,950,1043,1086,1018,1019,949],
[966,1040,919,0,959,926,1026,941,1031,975,947],
[963,1107,997,1042,0,999,1041,999,1014,1048,1046],
[988,1120,1051,1075,1002,0,1076,1045,982,1042,998],
[971,1015,958,975,960,925,0,962,896,925,961],
[969,1035,915,1060,1002,956,1039,0,989,996,925],
[1037,1057,983,970,987,1019,1105,1012,0,1050,993],
[1001,1071,982,1026,953,959,1076,1005,951,0,1001],
[1007,1134,1052,1054,955,1003,1040,1076,1008,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 154, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1043,986,1002,1009,999,1026,998,997,1032,1017],
[958,0,973,966,987,984,982,960,952,963,973],
[1015,1028,0,1021,1013,986,1023,997,989,1009,1014],
[999,1035,980,0,1032,997,1015,994,1004,1018,989],
[992,1014,988,969,0,968,993,976,956,1008,1005],
[1002,1017,1015,1004,1033,0,1005,981,989,1011,1008],
[975,1019,978,986,1008,996,0,987,970,975,994],
[1003,1041,1004,1007,1025,1020,1014,0,987,1017,989],
[1004,1049,1012,997,1045,1012,1031,1014,0,1026,983],
[969,1038,992,983,993,990,1026,984,975,0,1000],
[984,1028,987,1012,996,993,1007,1012,1018,1001,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 155, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1006,1034,997,1004,1013,1006,1007,984,997,997],
[995,0,1011,976,968,993,1006,991,1003,976,981],
[967,990,0,970,972,988,984,1013,971,988,963],
[1004,1025,1031,0,989,1001,1025,1028,1022,986,1005],
[997,1033,1029,1012,0,1041,1006,1028,1044,1007,1022],
[988,1008,1013,1000,960,0,989,1008,1010,992,983],
[995,995,1017,976,995,1012,0,978,1014,1019,961],
[994,1010,988,973,973,993,1023,0,1001,974,959],
[1017,998,1030,979,957,991,987,1000,0,1006,984],
[1004,1025,1013,1015,994,1009,982,1027,995,0,975],
[1004,1020,1038,996,979,1018,1040,1042,1017,1026,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 156, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1017,936,988,1014,1056,989,1016,1003,1053,962],
[984,0,993,1003,1023,1050,991,994,1022,1066,1038],
[1065,1008,0,1001,996,1072,1029,1035,1057,1121,1025],
[1013,998,1000,0,942,1065,1055,1038,1020,1013,983],
[987,978,1005,1059,0,1007,1006,993,963,1015,936],
[945,951,929,936,994,0,916,1001,938,957,968],
[1012,1010,972,946,995,1085,0,1005,965,1008,998],
[985,1007,966,963,1008,1000,996,0,985,997,959],
[998,979,944,981,1038,1063,1036,1016,0,1038,982],
[948,935,880,988,986,1044,993,1004,963,0,987],
[1039,963,976,1018,1065,1033,1003,1042,1019,1014,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 157, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,978,978,1019,967,1003,1051,984,978,1008,987],
[1023,0,1047,1033,1040,994,1078,1022,1028,1038,1031],
[1023,954,0,983,1035,1011,1059,991,1019,1028,998],
[982,968,1018,0,1008,974,1085,1019,1009,1006,985],
[1034,961,966,993,0,1037,1030,967,1042,1066,1002],
[998,1007,990,1027,964,0,1123,970,1023,1014,995],
[950,923,942,916,971,878,0,948,962,952,917],
[1017,979,1010,982,1034,1031,1053,0,1049,1006,981],
[1023,973,982,992,959,978,1039,952,0,1020,956],
[993,963,973,995,935,987,1049,995,981,0,959],
[1014,970,1003,1016,999,1006,1084,1020,1045,1042,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 158, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1025,1018,1036,989,1021,1053,994,1004,991,1011],
[976,0,988,1074,990,1034,1060,1024,1009,986,993],
[983,1013,0,1040,1005,1035,1023,1010,1026,1030,993],
[965,927,961,0,952,1031,1051,1015,1015,968,991],
[1012,1011,996,1049,0,1099,1037,1066,1029,995,1009],
[980,967,966,970,902,0,968,940,984,952,974],
[948,941,978,950,964,1033,0,965,972,942,1009],
[1007,977,991,986,935,1061,1036,0,987,1013,1000],
[997,992,975,986,972,1017,1029,1014,0,998,952],
[1010,1015,971,1033,1006,1049,1059,988,1003,0,995],
[990,1008,1008,1010,992,1027,992,1001,1049,1006,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 159, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,939,952,986,899,987,1024,900,1015,992,949],
[1062,0,1016,1052,950,1033,1040,1004,1022,1078,1027],
[1049,985,0,979,999,1036,1144,1042,958,1103,944],
[1015,949,1022,0,934,1042,1085,1008,991,1059,962],
[1102,1051,1002,1067,0,1074,1071,994,1027,1085,979],
[1014,968,965,959,927,0,992,916,1052,1088,967],
[977,961,857,916,930,1009,0,911,1032,1000,985],
[1101,997,959,993,1007,1085,1090,0,1048,1075,991],
[986,979,1043,1010,974,949,969,953,0,1072,946],
[1009,923,898,942,916,913,1001,926,929,0,928],
[1052,974,1057,1039,1022,1034,1016,1010,1055,1073,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 160, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,959,984,993,993,1021,980,971,949,973,1054],
[1042,0,1013,1041,936,966,1023,973,946,994,1017],
[1017,988,0,959,904,984,1019,963,989,938,987],
[1008,960,1042,0,957,998,988,1015,1035,1063,992],
[1008,1065,1097,1044,0,1067,1073,1044,969,994,1076],
[980,1035,1017,1003,934,0,1026,967,983,1023,987],
[1021,978,982,1013,928,975,0,1001,987,936,929],
[1030,1028,1038,986,957,1034,1000,0,1028,970,1018],
[1052,1055,1012,966,1032,1018,1014,973,0,1054,1011],
[1028,1007,1063,938,1007,978,1065,1031,947,0,1017],
[947,984,1014,1009,925,1014,1072,983,990,984,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 161, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,946,1015,984,998,1034,998,1006,1004,1011,960],
[1055,0,1021,976,1003,1039,1053,1012,1012,1026,1022],
[986,980,0,958,986,1007,1030,992,982,1025,978],
[1017,1025,1043,0,990,1018,1048,1027,1007,996,1021],
[1003,998,1015,1011,0,1039,1066,1016,974,1025,1020],
[967,962,994,983,962,0,995,1024,980,1021,982],
[1003,948,971,953,935,1006,0,974,999,1005,967],
[995,989,1009,974,985,977,1027,0,968,1009,975],
[997,989,1019,994,1027,1021,1002,1033,0,992,990],
[990,975,976,1005,976,980,996,992,1009,0,996],
[1041,979,1023,980,981,1019,1034,1026,1011,1005,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 162, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,1012,971,982,977,1016,990,1026,1004,1015],
[1013,0,998,953,999,1006,988,988,1036,994,1000],
[989,1003,0,973,1003,971,991,989,1029,1011,991],
[1030,1048,1028,0,995,1038,1027,1013,1020,1002,1025],
[1019,1002,998,1006,0,1010,1009,1015,1040,1016,1026],
[1024,995,1030,963,991,0,1005,999,1007,993,1008],
[985,1013,1010,974,992,996,0,988,1003,987,1004],
[1011,1013,1012,988,986,1002,1013,0,1019,1004,1012],
[975,965,972,981,961,994,998,982,0,983,1013],
[997,1007,990,999,985,1008,1014,997,1018,0,1015],
[986,1001,1010,976,975,993,997,989,988,986,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 163, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1003,991,1031,1007,1026,1004,1037,1034,1020,1032],
[998,0,990,1017,1000,1015,997,1032,1012,997,1052],
[1010,1011,0,992,995,1035,1017,1018,1011,1019,1006],
[970,984,1009,0,1003,1010,1021,1016,1013,1041,1025],
[994,1001,1006,998,0,1038,1013,979,1011,987,1050],
[975,986,966,991,963,0,993,1016,989,983,1015],
[997,1004,984,980,988,1008,0,1033,1028,1023,1035],
[964,969,983,985,1022,985,968,0,986,987,998],
[967,989,990,988,990,1012,973,1015,0,1001,1028],
[981,1004,982,960,1014,1018,978,1014,1000,0,1035],
[969,949,995,976,951,986,966,1003,973,966,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 164, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,987,1019,999,1024,1029,1001,1026,1021,1015,1023],
[1014,0,984,988,1026,1020,994,990,1016,992,1013],
[982,1017,0,990,997,1008,1011,1002,986,1002,999],
[1002,1013,1011,0,1005,1014,1009,1018,990,1022,1021],
[977,975,1004,996,0,1003,991,1008,999,1009,1011],
[972,981,993,987,998,0,945,984,986,983,1001],
[1000,1007,990,992,1010,1056,0,997,1008,1024,1015],
[975,1011,999,983,993,1017,1004,0,994,994,1006],
[980,985,1015,1011,1002,1015,993,1007,0,993,991],
[986,1009,999,979,992,1018,977,1007,1008,0,1001],
[978,988,1002,980,990,1000,986,995,1010,1000,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 165, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,994,1003,975,1047,988,1032,983,1010,1016,955],
[1007,0,1024,989,1019,1028,1015,1013,1017,1017,993],
[998,977,0,966,947,1019,985,940,1009,986,929],
[1026,1012,1035,0,1010,1001,1028,1014,1040,990,979],
[954,982,1054,991,0,998,1010,948,1001,978,989],
[1013,973,982,1000,1003,0,978,1005,1028,1015,977],
[969,986,1016,973,991,1023,0,961,1001,989,994],
[1018,988,1061,987,1053,996,1040,0,1047,998,1018],
[991,984,992,961,1000,973,1000,954,0,991,967],
[985,984,1015,1011,1023,986,1012,1003,1010,0,971],
[1046,1008,1072,1022,1012,1024,1007,983,1034,1030,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 166, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,991,979,982,975,976,1015,1013,1007,1007,997],
[1010,0,974,966,977,962,991,990,988,1002,972],
[1022,1027,0,1012,996,1015,1009,1048,1009,1035,1006],
[1019,1035,989,0,1031,1006,1015,991,994,995,983],
[1026,1024,1005,970,0,970,982,1010,1005,1039,1030],
[1025,1039,986,995,1031,0,1019,1001,1026,1009,1014],
[986,1010,992,986,1019,982,0,1008,1004,1001,962],
[988,1011,953,1010,991,1000,993,0,1014,998,1003],
[994,1013,992,1007,996,975,997,987,0,995,990],
[994,999,966,1006,962,992,1000,1003,1006,0,982],
[1004,1029,995,1018,971,987,1039,998,1011,1019,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 167, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,1019,975,976,1001,999,1023,1019,1022,981],
[988,0,1022,1015,983,1020,991,1001,1024,997,1012],
[982,979,0,970,967,971,958,997,988,986,987],
[1026,986,1031,0,986,1004,1012,1017,1015,1013,981],
[1025,1018,1034,1015,0,1010,1001,998,1048,1034,1017],
[1000,981,1030,997,991,0,992,1013,974,984,1003],
[1002,1010,1043,989,1000,1009,0,1039,1015,1001,1016],
[978,1000,1004,984,1003,988,962,0,1018,992,994],
[982,977,1013,986,953,1027,986,983,0,1002,1007],
[979,1004,1015,988,967,1017,1000,1009,999,0,1005],
[1020,989,1014,1020,984,998,985,1007,994,996,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 168, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1027,1011,920,1029,1082,959,1028,1053,958,1013],
[974,0,987,1056,1072,1035,1024,1130,1036,1017,1001],
[990,1014,0,998,967,1022,962,985,972,908,1084],
[1081,945,1003,0,946,1081,943,995,942,936,991],
[972,929,1034,1055,0,1052,960,1027,888,1017,950],
[919,966,979,920,949,0,918,971,979,1015,1012],
[1042,977,1039,1058,1041,1083,0,1076,1046,1082,983],
[973,871,1016,1006,974,1030,925,0,931,864,985],
[948,965,1029,1059,1113,1022,955,1070,0,1044,958],
[1043,984,1093,1065,984,986,919,1137,957,0,1044],
[988,1000,917,1010,1051,989,1018,1016,1043,957,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 169, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1016,1020,981,1031,988,1043,968,1006,1024,957],
[985,0,1048,993,1071,1035,1063,1006,998,1055,956],
[981,953,0,1032,1023,973,996,988,984,1007,993],
[1020,1008,969,0,1065,1017,997,952,929,998,995],
[970,930,978,936,0,1011,903,873,933,929,995],
[1013,966,1028,984,990,0,1046,1017,966,958,1023],
[958,938,1005,1004,1098,955,0,983,960,962,1003],
[1033,995,1013,1049,1128,984,1018,0,1004,995,1066],
[995,1003,1017,1072,1068,1035,1041,997,0,998,1060],
[977,946,994,1003,1072,1043,1039,1006,1003,0,1014],
[1044,1045,1008,1006,1006,978,998,935,941,987,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 170, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1033,1032,1023,1004,1048,1023,991,1010,1022,1012],
[968,0,1013,994,1001,1030,1008,985,994,1002,1005],
[969,988,0,1043,1004,1030,1028,1035,1006,989,1011],
[978,1007,958,0,992,1000,982,998,996,979,1001],
[997,1000,997,1009,0,1007,1004,993,979,991,990],
[953,971,971,1001,994,0,993,999,1018,952,999],
[978,993,973,1019,997,1008,0,1006,1025,980,1014],
[1010,1016,966,1003,1008,1002,995,0,1002,1009,1029],
[991,1007,995,1005,1022,983,976,999,0,1002,1024],
[979,999,1012,1022,1010,1049,1021,992,999,0,1049],
[989,996,990,1000,1011,1002,987,972,977,952,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 171, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,975,1001,997,989,978,1022,985,1008,993,987],
[1026,0,1001,1014,1008,980,1019,1014,1016,1013,1024],
[1000,1000,0,995,986,986,1017,1005,1000,1016,988],
[1004,987,1006,0,1016,960,1025,994,1043,968,1005],
[1012,993,1015,985,0,993,1022,1009,1033,981,1017],
[1023,1021,1015,1041,1008,0,1062,1014,1045,995,1024],
[979,982,984,976,979,939,0,991,994,943,966],
[1016,987,996,1007,992,987,1010,0,980,977,1001],
[993,985,1001,958,968,956,1007,1021,0,989,1011],
[1008,988,985,1033,1020,1006,1058,1024,1012,0,1015],
[1014,977,1013,996,984,977,1035,1000,990,986,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 172, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1030,1015,916,923,945,1033,1014,1051,1038,888],
[971,0,963,802,970,888,840,789,1032,917,847],
[986,1038,0,1002,1029,834,836,944,1000,975,993],
[1085,1199,999,0,1059,1000,971,952,1039,1069,1065],
[1078,1031,972,942,0,997,886,843,998,919,1133],
[1056,1113,1167,1001,1004,0,940,968,1017,1004,1065],
[968,1161,1165,1030,1115,1061,0,1096,1100,1136,1025],
[987,1212,1057,1049,1158,1033,905,0,1004,996,1065],
[950,969,1001,962,1003,984,901,997,0,917,958],
[963,1084,1026,932,1082,997,865,1005,1084,0,984],
[1113,1154,1008,936,868,936,976,936,1043,1017,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 173, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1031,1034,1035,1043,1067,1032,990,1050,1075,1078],
[970,0,1033,983,1007,1048,944,956,1050,1008,1044],
[967,968,0,1002,1028,1037,1022,1001,1035,1045,1059],
[966,1018,999,0,1013,1004,1004,942,1005,964,1022],
[958,994,973,988,0,1021,1000,977,1060,1000,1053],
[934,953,964,997,980,0,959,924,1016,1024,1007],
[969,1057,979,997,1001,1042,0,919,1038,997,1036],
[1011,1045,1000,1059,1024,1077,1082,0,1081,1056,1101],
[951,951,966,996,941,985,963,920,0,1026,959],
[926,993,956,1037,1001,977,1004,945,975,0,992],
[923,957,942,979,948,994,965,900,1042,1009,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 174, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,976,997,1004,984,1006,998,1006,1010,991],
[1013,0,1001,1002,997,999,999,1006,1007,1035,993],
[1025,1000,0,1024,1034,1003,1021,984,1017,1058,1024],
[1004,999,977,0,992,979,1014,1009,1019,1046,994],
[997,1004,967,1009,0,974,978,990,1005,1043,1020],
[1017,1002,998,1022,1027,0,1028,1008,1024,1018,1005],
[995,1002,980,987,1023,973,0,1000,1030,1027,1003],
[1003,995,1017,992,1011,993,1001,0,1010,1011,1021],
[995,994,984,982,996,977,971,991,0,1012,979],
[991,966,943,955,958,983,974,990,989,0,986],
[1010,1008,977,1007,981,996,998,980,1022,1015,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 175, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1080,936,929,999,982,898,972,944,945,987],
[921,0,968,882,991,956,962,959,969,819,919],
[1065,1033,0,984,1003,908,1007,1004,988,916,955],
[1072,1119,1017,0,1063,973,1022,1077,1042,1022,1063],
[1002,1010,998,938,0,903,935,912,958,852,896],
[1019,1045,1093,1028,1098,0,987,1005,1101,972,1094],
[1103,1039,994,979,1066,1014,0,957,922,959,897],
[1029,1042,997,924,1089,996,1044,0,1071,972,1040],
[1057,1032,1013,959,1043,900,1079,930,0,984,1061],
[1056,1182,1085,979,1149,1029,1042,1029,1017,0,1065],
[1014,1082,1046,938,1105,907,1104,961,940,936,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 176, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,936,998,839,986,979,960,971,1082,874,1121],
[1065,0,1069,955,1213,1062,1092,1179,1045,1096,1179],
[1003,932,0,1035,1040,1119,1090,1092,1037,959,1086],
[1162,1046,966,0,1135,1100,1135,1145,1160,1153,1174],
[1015,788,961,866,0,966,1042,1011,1029,841,1066],
[1022,939,882,901,1035,0,943,943,1066,1033,1011],
[1041,909,911,866,959,1058,0,1059,1047,981,953],
[1030,822,909,856,990,1058,942,0,1101,866,1004],
[919,956,964,841,972,935,954,900,0,835,1034],
[1127,905,1042,848,1160,968,1020,1135,1166,0,1052],
[880,822,915,827,935,990,1048,997,967,949,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 177, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,973,1001,1005,1022,1067,1032,958,1010,1072,1017],
[1028,0,1004,1024,1029,1069,1014,962,1011,1046,958],
[1000,997,0,999,1016,1087,998,1018,971,989,1002],
[996,977,1002,0,987,1019,1026,1010,967,1027,976],
[979,972,985,1014,0,1000,981,970,968,1009,988],
[934,932,914,982,1001,0,990,986,938,1019,965],
[969,987,1003,975,1020,1011,0,935,1010,1017,1000],
[1043,1039,983,991,1031,1015,1066,0,974,1043,1035],
[991,990,1030,1034,1033,1063,991,1027,0,1079,1032],
[929,955,1012,974,992,982,984,958,922,0,941],
[984,1043,999,1025,1013,1036,1001,966,969,1060,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 178, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1463,963,570,994,1104,740,885,757,620,1059],
[538,0,928,756,933,1116,916,894,557,555,1071],
[1038,1073,0,583,965,1530,1083,1139,1073,1055,1376],
[1431,1245,1418,0,1383,1724,1225,1530,1147,861,1505],
[1007,1068,1036,618,0,1210,945,939,630,812,822],
[897,885,471,277,791,0,963,682,538,657,876],
[1261,1085,918,776,1056,1038,0,802,868,1011,814],
[1116,1107,862,471,1062,1319,1199,0,778,885,1033],
[1244,1444,928,854,1371,1463,1133,1223,0,931,1360],
[1381,1446,946,1140,1189,1344,990,1116,1070,0,1231],
[942,930,625,496,1179,1125,1187,968,641,770,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 179, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,951,955,981,1053,985,988,982,946,953,991],
[1050,0,992,1040,1085,1024,1039,1031,993,1015,1013],
[1046,1009,0,1032,1066,1044,1016,1032,1000,1036,1031],
[1020,961,969,0,1031,981,995,1004,993,967,982],
[948,916,935,970,0,988,937,937,922,938,937],
[1016,977,957,1020,1013,0,997,1026,980,919,989],
[1013,962,985,1006,1064,1004,0,1020,954,1006,968],
[1019,970,969,997,1064,975,981,0,999,974,989],
[1055,1008,1001,1008,1079,1021,1047,1002,0,1034,991],
[1048,986,965,1034,1063,1082,995,1027,967,0,1004],
[1010,988,970,1019,1064,1012,1033,1012,1010,997,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 180, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,886,951,907,1033,862,1024,950,933,994,900],
[1115,0,1000,1098,1086,1026,1101,1037,968,1099,969],
[1050,1001,0,955,1107,941,1134,982,999,1032,963],
[1094,903,1046,0,1035,940,1085,1007,982,1086,1012],
[968,915,894,966,0,894,1033,977,898,976,976],
[1139,975,1060,1061,1107,0,1168,990,980,1115,1056],
[977,900,867,916,968,833,0,947,867,989,954],
[1051,964,1019,994,1024,1011,1054,0,1006,1088,978],
[1068,1033,1002,1019,1103,1021,1134,995,0,1089,1087],
[1007,902,969,915,1025,886,1012,913,912,0,932],
[1101,1032,1038,989,1025,945,1047,1023,914,1069,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 181, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1021,967,1016,978,1017,986,1042,995,991,1016],
[980,0,994,1021,960,1020,997,1042,986,981,1011],
[1034,1007,0,1020,995,1056,1044,1030,992,1001,1014],
[985,980,981,0,957,963,982,1033,985,974,1013],
[1023,1041,1006,1044,0,1022,1003,1051,994,983,1019],
[984,981,945,1038,979,0,1017,1011,974,938,968],
[1015,1004,957,1019,998,984,0,1052,948,947,971],
[959,959,971,968,950,990,949,0,968,928,977],
[1006,1015,1009,1016,1007,1027,1053,1033,0,973,1003],
[1010,1020,1000,1027,1018,1063,1054,1073,1028,0,1010],
[985,990,987,988,982,1033,1030,1024,998,991,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 182, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1002,987,1032,995,1008,978,990,995,978,1001],
[999,0,980,1013,1018,968,1008,994,978,992,966],
[1014,1021,0,1054,1038,1043,1004,982,1011,1026,1022],
[969,988,947,0,1020,964,961,1006,937,973,979],
[1006,983,963,981,0,996,1011,1018,989,986,1003],
[993,1033,958,1037,1005,0,1004,1018,1024,993,978],
[1023,993,997,1040,990,997,0,1007,1008,977,999],
[1011,1007,1019,995,983,983,994,0,1003,998,979],
[1006,1023,990,1064,1012,977,993,998,0,983,1001],
[1023,1009,975,1028,1015,1008,1024,1003,1018,0,1004],
[1000,1035,979,1022,998,1023,1002,1022,1000,997,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 183, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1039,957,1077,982,1017,1094,1094,1064,1152,1029],
[962,0,1065,927,972,1022,1057,1015,980,1071,992],
[1044,936,0,1056,1001,1002,1030,1003,1065,1052,1107],
[924,1074,945,0,1063,1060,1079,993,1072,1003,1008],
[1019,1029,1000,938,0,1079,1012,1056,954,1105,1023],
[984,979,999,941,922,0,962,1067,1054,1099,1093],
[907,944,971,922,989,1039,0,969,1013,1034,1103],
[907,986,998,1008,945,934,1032,0,1044,1079,1026],
[937,1021,936,929,1047,947,988,957,0,967,1034],
[849,930,949,998,896,902,967,922,1034,0,971],
[972,1009,894,993,978,908,898,975,967,1030,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 184, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,898,971,995,1004,890,970,946,992,951,1004],
[1103,0,984,943,969,954,1013,954,1063,1046,1007],
[1030,1017,0,1023,988,966,1066,1012,1084,1022,1071],
[1006,1058,978,0,1043,939,1049,1010,1149,1032,1015],
[997,1032,1013,958,0,1040,1074,1075,1030,1040,1049],
[1111,1047,1035,1062,961,0,1091,1018,1091,1071,1041],
[1031,988,935,952,927,910,0,928,1025,1001,972],
[1055,1047,989,991,926,983,1073,0,1054,1053,1025],
[1009,938,917,852,971,910,976,947,0,1021,928],
[1050,955,979,969,961,930,1000,948,980,0,966],
[997,994,930,986,952,960,1029,976,1073,1035,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 185, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,956,959,963,986,1009,961,953,964,972,961],
[1045,0,1044,992,1017,1021,1013,1025,1018,1018,984],
[1042,957,0,981,1005,1037,986,1005,998,1018,993],
[1038,1009,1020,0,1036,1050,1000,1036,1045,1028,998],
[1015,984,996,965,0,1008,996,1042,1025,1012,988],
[992,980,964,951,993,0,970,996,980,976,961],
[1040,988,1015,1001,1005,1031,0,1016,1010,1010,1032],
[1048,976,996,965,959,1005,985,0,1000,1003,967],
[1037,983,1003,956,976,1021,991,1001,0,1008,975],
[1029,983,983,973,989,1025,991,998,993,0,956],
[1040,1017,1008,1003,1013,1040,969,1034,1026,1045,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 186, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,946,967,999,982,1007,1017,992,951,928,956],
[1055,0,1073,1076,1022,1105,1088,1115,986,987,1049],
[1034,928,0,1038,986,1061,1072,1060,945,936,992],
[1002,925,963,0,978,1027,1022,1010,935,962,984],
[1019,979,1015,1023,0,1064,1024,1089,961,1030,1046],
[994,896,940,974,937,0,1029,1051,917,958,991],
[984,913,929,979,977,972,0,1059,908,927,997],
[1009,886,941,991,912,950,942,0,916,937,1008],
[1050,1015,1056,1066,1040,1084,1093,1085,0,987,1086],
[1073,1014,1065,1039,971,1043,1074,1064,1014,0,1036],
[1045,952,1009,1017,955,1010,1004,993,915,965,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 187, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,993,959,1034,981,981,995,1023,980,1019,1003],
[1008,0,926,1035,979,1032,1033,1047,1013,997,1019],
[1042,1075,0,1038,1007,1052,999,1086,1050,1070,1026],
[967,966,963,0,959,927,957,996,946,1005,1023],
[1020,1022,994,1042,0,1009,955,1058,1007,1000,1030],
[1020,969,949,1074,992,0,983,1029,999,1042,1018],
[1006,968,1002,1044,1046,1018,0,1051,1012,1032,1047],
[978,954,915,1005,943,972,950,0,973,1005,985],
[1021,988,951,1055,994,1002,989,1028,0,1040,1023],
[982,1004,931,996,1001,959,969,996,961,0,999],
[998,982,975,978,971,983,954,1016,978,1002,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 188, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,926,976,908,920,966,951,943,932,994,953],
[1075,0,1051,1025,1031,1025,1067,951,1023,1031,1026],
[1025,950,0,976,948,986,1014,908,961,997,924],
[1093,976,1025,0,1007,1043,1107,992,966,1076,998],
[1081,970,1053,994,0,992,1060,930,999,1014,975],
[1035,976,1015,958,1009,0,1057,1028,1002,1055,1002],
[1050,934,987,894,941,944,0,855,905,973,912],
[1058,1050,1093,1009,1071,973,1146,0,1022,1068,1039],
[1069,978,1040,1035,1002,999,1096,979,0,1053,1043],
[1007,970,1004,925,987,946,1028,933,948,0,964],
[1048,975,1077,1003,1026,999,1089,962,958,1037,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 189, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,1009,1025,1003,1014,1003,979,1010,1016,1022],
[988,0,978,988,979,968,948,969,1024,980,991],
[992,1023,0,1017,980,1027,994,982,997,1020,1013],
[976,1013,984,0,1006,980,968,946,970,1000,972],
[998,1022,1021,995,0,1008,1014,995,1023,1030,1037],
[987,1033,974,1021,993,0,979,976,991,986,980],
[998,1053,1007,1033,987,1022,0,981,1000,1022,1004],
[1022,1032,1019,1055,1006,1025,1020,0,1000,1044,1008],
[991,977,1004,1031,978,1010,1001,1001,0,986,990],
[985,1021,981,1001,971,1015,979,957,1015,0,978],
[979,1010,988,1029,964,1021,997,993,1011,1023,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 190, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1024,1021,1022,967,1055,998,965,975,998,928],
[977,0,1038,1068,1004,1014,1015,1008,1006,1022,960],
[980,963,0,1017,932,1043,1002,896,911,1005,952],
[979,933,984,0,943,956,964,872,937,986,937],
[1034,997,1069,1058,0,1035,1119,1011,991,1055,964],
[946,987,958,1045,966,0,989,996,979,951,965],
[1003,986,999,1037,882,1012,0,987,960,953,952],
[1036,993,1105,1129,990,1005,1014,0,1044,1039,1014],
[1026,995,1090,1064,1010,1022,1041,957,0,1003,1005],
[1003,979,996,1015,946,1050,1048,962,998,0,966],
[1073,1041,1049,1064,1037,1036,1049,987,996,1035,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 191, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1013,969,971,1031,1015,969,973,1012,956,1051],
[988,0,1007,1055,1001,1023,962,970,1002,954,1026],
[1032,994,0,1000,1010,1040,996,1022,1029,1005,1070],
[1030,946,1001,0,1027,1011,991,1024,1056,991,1061],
[970,1000,991,974,0,1003,979,1023,1020,996,1006],
[986,978,961,990,998,0,978,1007,1033,992,1042],
[1032,1039,1005,1010,1022,1023,0,1000,1013,1013,1058],
[1028,1031,979,977,978,994,1001,0,1013,980,1061],
[989,999,972,945,981,968,988,988,0,988,1019],
[1045,1047,996,1010,1005,1009,988,1021,1013,0,1042],
[950,975,931,940,995,959,943,940,982,959,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 192, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,988,983,1019,965,957,942,1054,966,974,1046],
[1013,0,986,1000,981,1035,957,1049,971,969,1049],
[1018,1015,0,1045,989,1018,982,1100,996,1001,1078],
[982,1001,956,0,965,1008,981,1073,946,999,1044],
[1036,1020,1012,1036,0,978,1015,1054,1006,986,1065],
[1044,966,983,993,1023,0,1005,1126,1006,980,1051],
[1059,1044,1019,1020,986,996,0,1111,1003,1061,1095],
[947,952,901,928,947,875,890,0,899,893,986],
[1035,1030,1005,1055,995,995,998,1102,0,989,1086],
[1027,1032,1000,1002,1015,1021,940,1108,1012,0,1078],
[955,952,923,957,936,950,906,1015,915,923,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 193, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,903,979,857,920,997,1051,975,843,959,1065],
[1098,0,998,1034,1019,1202,1125,1049,982,1161,1087],
[1022,1003,0,918,932,1084,1001,899,922,1086,1148],
[1144,967,1083,0,1001,1263,1154,1037,1123,1169,1313],
[1081,982,1069,1000,0,1149,1130,1007,1110,1181,1252],
[1004,799,917,738,852,0,917,916,872,944,839],
[950,876,1000,847,871,1084,0,827,940,1106,1052],
[1026,952,1102,964,994,1085,1174,0,979,1085,1195],
[1158,1019,1079,878,891,1129,1061,1022,0,1179,1076],
[1042,840,915,832,820,1057,895,916,822,0,1038],
[936,914,853,688,749,1162,949,806,925,963,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 194, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1032,1064,973,1035,1034,996,1043,1009,1049,1032],
[969,0,1028,1013,1016,1068,950,1030,1006,1007,1036],
[937,973,0,996,963,954,968,1016,1028,1007,984],
[1028,988,1005,0,1004,982,989,1047,1008,988,953],
[966,985,1038,997,0,956,951,1022,1046,975,977],
[967,933,1047,1019,1045,0,980,1035,1001,986,989],
[1005,1051,1033,1012,1050,1021,0,1058,1011,1037,974],
[958,971,985,954,979,966,943,0,973,962,967],
[992,995,973,993,955,1000,990,1028,0,1026,996],
[952,994,994,1013,1026,1015,964,1039,975,0,941],
[969,965,1017,1048,1024,1012,1027,1034,1005,1060,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 195, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,986,1032,1014,987,1005,1016,1034,1036,1026,1027],
[1015,0,1019,990,1011,986,1025,1054,1033,1017,989],
[969,982,0,1021,1003,987,991,1026,1029,1006,1001],
[987,1011,980,0,974,990,1005,1032,1024,1010,1007],
[1014,990,998,1027,0,1033,1002,1054,1020,1026,1013],
[996,1015,1014,1011,968,0,1007,1054,1011,1015,998],
[985,976,1010,996,999,994,0,1054,1023,1022,985],
[967,947,975,969,947,947,947,0,983,979,973],
[965,968,972,977,981,990,978,1018,0,1027,983],
[975,984,995,991,975,986,979,1022,974,0,970],
[974,1012,1000,994,988,1003,1016,1028,1018,1031,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 196, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,979,976,947,993,885,943,1035,999,1039,995],
[1022,0,989,973,979,1004,952,1039,1069,1043,1016],
[1025,1012,0,964,1004,971,1004,1034,1053,1051,1036],
[1054,1028,1037,0,1006,961,1002,1070,1072,1093,1019],
[1008,1022,997,995,0,977,969,1111,1032,1068,1083],
[1116,997,1030,1040,1024,0,1023,1068,1090,1079,1056],
[1058,1049,997,999,1032,978,0,1054,1025,1095,1005],
[966,962,967,931,890,933,947,0,978,1007,986],
[1002,932,948,929,969,911,976,1023,0,1028,966],
[962,958,950,908,933,922,906,994,973,0,959],
[1006,985,965,982,918,945,996,1015,1035,1042,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 197, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,958,988,993,953,998,955,972,968,979,981],
[1043,0,1018,1033,1011,1022,1019,1009,1000,980,1011],
[1013,983,0,1032,968,994,983,978,1001,1009,1007],
[1008,968,969,0,985,1000,985,976,978,961,994],
[1048,990,1033,1016,0,1019,986,992,977,977,1000],
[1003,979,1007,1001,982,0,983,995,1005,975,1007],
[1046,982,1018,1016,1015,1018,0,1006,976,978,1024],
[1029,992,1023,1025,1009,1006,995,0,975,987,1017],
[1033,1001,1000,1023,1024,996,1025,1026,0,1011,1040],
[1022,1021,992,1040,1024,1026,1023,1014,990,0,1037],
[1020,990,994,1007,1001,994,977,984,961,964,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 198, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,1007,995,1011,952,984,1051,967,932,1033,976],
[994,0,1008,1027,995,992,1078,1048,1013,1041,1001],
[1006,993,0,989,969,1030,1006,998,957,988,1023],
[990,974,1012,0,983,1020,974,943,903,967,948],
[1049,1006,1032,1018,0,999,1046,1010,962,1055,994],
[1017,1009,971,981,1002,0,977,1001,988,974,1018],
[950,923,995,1027,955,1024,0,982,961,973,973],
[1034,953,1003,1058,991,1000,1019,0,990,960,996],
[1069,988,1044,1098,1039,1013,1040,1011,0,1056,1026],
[968,960,1013,1034,946,1027,1028,1041,945,0,980],
[1025,1000,978,1053,1007,983,1028,1005,975,1021,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 199, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

##############################################################
om = np.array([
[0,896,1000,942,899,926,1033,1029,990,1001,976],
[1105,0,1025,1042,899,911,1032,936,1044,1099,1100],
[1001,976,0,992,991,884,1054,955,961,981,1035],
[1059,959,1009,0,833,914,996,934,986,953,1051],
[1102,1102,1010,1168,0,949,999,933,1005,1136,1039],
[1075,1090,1117,1087,1052,0,1066,967,1109,1019,993],
[968,969,947,1005,1002,935,0,1035,989,1013,977],
[972,1065,1046,1067,1068,1034,966,0,1027,1054,1231],
[1011,957,1040,1015,996,892,1012,974,0,1046,1011],
[1000,902,1020,1048,865,982,988,947,955,0,956],
[1025,901,966,950,962,1008,1024,770,990,1045,0]])



times = np.zeros(rep)
for i in range(rep):
    # Algorithm with Condorcet winner
    algorithm = alg.AzziniMunda5(om) 
    start_time = time.time()
    d = alg.dRP(sc.ranking_to_lineal(sc.borda(om)), om)
    algorithm.best_dist = d
    sol = algorithm.execute()
    t = (time.time() - start_time)
    times[i] = t
    #print(t)
exec_time = np.median(times)
result = np.append(np.array([11, 2001, 200, "ME-BBd", exec_time, sol.shape[0], algorithm.ntentative], dtype=np.dtype(object)), times)
print(result[:7])
results = np.vstack((results, result))

 
pd.DataFrame(results).to_csv("/Users/noeliarico/Desktop/folder-kemeny/2021EJOR/results/mebbd/mebbd_11_2001.csv", index=False, header=False)