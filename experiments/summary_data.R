# Condorcet ranking
cr <- bind_rows(check_data_experiments_is_null(pors4cr),
  check_data_experiments_is_null(pors5cr),
  check_data_experiments_is_null(pors6cr),
  check_data_experiments_is_null(pors7cr),
  check_data_experiments_is_null(pors8cr),
  check_data_experiments_is_null(pors9cr),
  check_data_experiments_is_null(pors10cr),
  check_data_experiments_is_null(pors11cr),
  check_data_experiments_is_null(pors12cr),
  check_data_experiments_is_null(pors13cr))
rownames(cr) <- paste0("n",(1:nrow(cr))+4)
cr <- 5 - cr
# Condorcet winner
cw <- bind_rows(check_data_experiments_is_null(pors4cw),
                check_data_experiments_is_null(pors5cw),
                check_data_experiments_is_null(pors6cw),
                check_data_experiments_is_null(pors7cw),
                check_data_experiments_is_null(pors8cw),
                check_data_experiments_is_null(pors9cw),
                check_data_experiments_is_null(pors10cw),
                check_data_experiments_is_null(pors11cw),
                check_data_experiments_is_null(pors12cw),
                check_data_experiments_is_null(pors13cw))
rownames(cw) <- paste0("n",(1:nrow(cw))+4)
cw <- 5 - cw
# No Condorcet
nc <- bind_rows(check_data_experiments_is_null(pors4nc),
                check_data_experiments_is_null(pors5nc),
                check_data_experiments_is_null(pors6nc),
                check_data_experiments_is_null(pors7nc),
                check_data_experiments_is_null(pors8nc),
                check_data_experiments_is_null(pors9nc),
                check_data_experiments_is_null(pors10nc),
                check_data_experiments_is_null(pors11nc),
                check_data_experiments_is_null(pors12nc),
                check_data_experiments_is_null(pors13nc))
rownames(nc) <- paste0("n",(1:nrow(nc))+4)
nc <- 5 - nc

cw
cr
nc

check_data_experiments_margin(pors4nc)
check_data_experiments_margin(pors5nc)
check_data_experiments_margin(pors6nc)
check_data_experiments_margin(pors7nc)
check_data_experiments_margin(pors8nc)
check_data_experiments_margin(pors9nc)
check_data_experiments_margin(pors10nc)
check_data_experiments_margin(pors11nc)
check_data_experiments_margin(pors12nc)
check_data_experiments_margin(pors13nc)

check_data_experiments_margin(pors4cw)
check_data_experiments_margin(pors5cw)
check_data_experiments_margin(pors6cw)
check_data_experiments_margin(pors7cw)
check_data_experiments_margin(pors8cw)
check_data_experiments_margin(pors9cw)
check_data_experiments_margin(pors10cw)
check_data_experiments_margin(pors11cw)
check_data_experiments_margin(pors12cw)
check_data_experiments_margin(pors13cw)

check_data_experiments_margin(pors4cr)
check_data_experiments_margin(pors5cr)
check_data_experiments_margin(pors6cr)
check_data_experiments_margin(pors7cr)
check_data_experiments_margin(pors8cr)
check_data_experiments_margin(pors9cr)
check_data_experiments_margin(pors10cr)
check_data_experiments_margin(pors11cr)
check_data_experiments_margin(pors12cr)
check_data_experiments_margin(pors13cr)
