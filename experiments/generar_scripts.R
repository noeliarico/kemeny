# Condorcet ranking -------------------------------------------------------

scripts_azzini(pors5cr, 5, "experiments/azzini5cr.py", rep = 3, type = "cr")
scripts_azzini(pors6cr, 6, "experiments/azzini6cr.py", rep = 3, type = "cr")
scripts_azzini(pors7cr, 7, "experiments/azzini7cr.py", rep = 3, type = "cr")
scripts_azzini(pors8cr, 8, "experiments/azzini8cr.py", rep = 3, type = "cr")
scripts_azzini(pors9cr, 9, "experiments/azzini9cr.py", rep = 3, type = "cr")
scripts_azzini(pors10cr, 10, "experiments/azzini10cr.py", rep = 3, type = "cr")
scripts_azzini(pors11cr, 11, "experiments/azzini11cr.py", rep = 3, type = "cr")
scripts_azzini(pors12cr, 12, "experiments/azzini12cr.py", rep = 3, type = "cr")
scripts_azzini(pors13cr, 13, "experiments/azzini13cr.py", rep = 3, type = "cr")

# Condorcet winner -------------------------------------------------------

scripts_azzini(pors5cw, 5, "experiments/azzini5cw.py", rep = 3, type = "cw")
scripts_azzini(pors6cw, 6, "experiments/azzini6cw.py", rep = 3, type = "cw")
scripts_azzini(pors7cw, 7, "experiments/azzini7cw.py", rep = 3, type = "cw")
scripts_azzini(pors8cw, 8, "experiments/azzini8cw.py", rep = 3, type = "cw")
scripts_azzini(pors9cw, 9, "experiments/azzini9cw.py", rep = 3, type = "cw")
scripts_azzini(pors10cw, 10, "experiments/azzini10cw.py", rep = 3, type = "cw")
scripts_azzini(pors11cw, 11, "experiments/azzini11cw.py", rep = 3, type = "cw")
scripts_azzini(pors12cw, 12, "experiments/azzini12cw.py", rep = 3, type = "cw")
scripts_azzini(pors13cw, 13, "experiments/azzini13cw.py", rep = 3, type = "cw")

# No Condorcet -----------------------------------------------------------

scripts_azzini(pors5nc, 5, "experiments/azzini5nc.py", rep = 3, type = "nc")
scripts_azzini(pors6nc, 6, "experiments/azzini6nc.py", rep = 3, type = "nc")
scripts_azzini(pors7nc, 7, "experiments/azzini7nc.py", rep = 3, type = "nc")
comparar_fuzzieee(pors8nc, 8, "azzini8nc.py", rep = 3, type = "nc")
comparar_fuzzieee(pors9nc, 9, "azzini9nc.py", rep = 3, type = "nc")
scripts_azzini(pors9nc, 9, "experiments/azzini9nc.py", rep = 3, type = "nc")
scripts_azzini(pors10nc, 10, "experiments/azzini10nc.py", rep = 3, type = "nc")
scripts_azzini(pors11nc, 11, "experiments/azzini11nc.py", rep = 3, type = "nc")
scripts_azzini(pors12nc, 12, "experiments/azzini12nc.py", rep = 3, type = "nc")
scripts_azzini(pors13nc, 13, "experiments/azzini13nc.py", rep = 3, type = "nc")

check_kemeny_condorcet_winner <- function(pors) {
  sapply(pors, function(x) {
    sapply(x, function(y) {
      k <- kemeny(y)
      print("###")
      print(condorcet_winner(y))
      print(k)
      if(is.null(nrow(k$winningRanking))) {
        return(which(k$winningRanking==1) == condorcet_winner(y))
      }
      else {
        w <- apply(sapply(k$winningRanking, function(z) z == 1), 1, which)
        return(all(w == condorcet_winner(y)))
      }
      
    })
  })
}
