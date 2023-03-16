# Los que propongo con el baseline

# me vs mebb
t.test(res_me_8$exec_time, res_mebb_8$exec_time)
t.test(res_me_9$exec_time, res_mebb_9$exec_time)
t.test(res_me_10$exec_time, res_mebb_10$exec_time)

# me vs mebbrcw
t.test(res_me_8$exec_time, res_mebbrcw_8$exec_time)
t.test(res_me_9$exec_time, res_mebbrcw_9$exec_time)
t.test(res_me_10$exec_time, res_mebbrcw_10$exec_time)

# El mejor con el otro
t.test(res_mebb_8$exec_time, res_mebbrcw_8$exec_time)
t.test(res_mebb_9$exec_time, res_mebbrcw_9$exec_time)
t.test(res_mebb_10$exec_time, res_mebbrcw_10$exec_time)

