por <- structure(list(profileOfRankings = structure(
  list(C1 = c(4L,3L, 1L), 
       C2 = c(2L, 4L, 3L), 
       C3 = c(1L, 2L, 4L), 
       C4 = c(3L, 1L,2L)), 
  row.names = c(NA, -3L), 
  class = "data.frame"), 
  numberOfVoters = c(5, 3, 2), 
  candidates = c("C1", "C2", "C3", "C4")), 
  class = c("por","list"))

tikz <- kemeny_to_tikz(votrix(por)) 
sink("creation/step1.tex")
cat(tikz)
sink()

tikz <- kemeny_to_tikz(votrix(por)[-3,-3]) 
sink("creation/step2.tex")
cat(tikz)
sink()

tikz <- kemeny_to_tikz(votrix(por)[-4,-4])
sink("creation/step4.tex")
cat(tikz)
sink()


