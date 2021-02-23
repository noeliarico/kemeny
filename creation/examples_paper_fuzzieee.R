# Example used in the paper for fuzzieee 2021
por <- parse_profile_of_rankings("5, C3 ≻ C2 ≻ C4 ≻ C1,
                                  1, C1 ≻ C4 ≻ C3 ≻ C2,
                                  3, C4 ≻ C3 ≻ C1 ≻ C2,
                                  1, C1 ≻ C2 ≻ C4 ≻ C3")
por <- set_candidates(por, paste0("a_",1:4))

# for the figure of the paper (this scripts were changed later a little bit
# directly in the latex document to fit the two column version)
# tikz <- kemeny_to_tikz(votrix(por)) 
# sink("creation/step1.tex")
# cat(tikz)
# sink()
# tikz <- kemeny_to_tikz(votrix(por)[-3,-3]) 
# sink("creation/step2.tex")
# cat(tikz)
# sink()
# tikz <- kemeny_to_tikz(votrix(por)[-c(3,2),-c(3,2)]) 
# sink("creation/step3.tex")
# cat(tikz)
# sink()
# tikz <- kemeny_to_tikz(votrix(por)[-c(3,4),-c(3,4)]) 
# sink("creation/step4.tex")
# cat(tikz)
# sink()
# tikz <- kemeny_to_tikz(votrix(por)[-4,-4])
# sink("creation/step5.tex")
# cat(tikz)
# sink()


# Ejemplo de condorcet recursivo con 6 candidatos:
por <- structure(list(profileOfRankings = structure(list(
  C1 = c(5L,5L,2L,2L), 
  C2 = c(1L,6L,1L,1L), 
  C3 = c(6L,4L,4L,4L), 
  C4 = c(4L,3L,6L,6L), 
  C5 = c(2L,2L,5L,3L), 
  C6 = c(3L,1L,3L,5L)), 
  row.names = c(NA, -4L), 
  class = "data.frame"), 
  numberOfVoters = c(3, 3, 2, 2), 
  candidates = c("C1", "C2", "C3", "C4", "C5", "C6"), 
  votrix = structure(c(0, 7, 3, 6, 6, 6, 3, 0, 3, 3, 3, 3, 7, 7, 0, 6, 8, 8,
                       4, 7, 4, 0, 10, 10, 4, 7, 2, 0, 0, 5, 4, 7, 2, 0, 5, 0), 
                     .Dim = c(6L, 6L), .Dimnames = list(c("C1", "C2", "C3", "C4", "C5", "C6"), 
                                                        c("C1", "C2","C3", "C4", "C5", "C6")))), 
  class = c("por", "list"))
condorcet(por, seePoints = T) # no condorcet ranking
v <- votrix(por)
print(v)
rowSums(v) >= colSums(v) # three candidates to explore
# but there was a Condorcet winner because 
# the the second alternative had row score = 5
# all the winning rankings must start with alternative C2
rowSums(v[-2,-2] > 5) # no condert ranking (neither winner) with the remaining alternatives
rowSums(v[-2,-2]) >= colSums(v[-2,-2]) # check the next alternatives to explore
rowSums(v[-c(2,5),-c(2,5)] > 5) # now there is a Condorcet ranking so the... 
# ...recursive process can stop for alternative C5: C2 > C5 > C6 > C4 > C1 > C3
# now explore C6
rowSums(v[-c(2,6),-c(2,6)] > 5) # again there is a Condorcet ranking
# C2 > C6 > C5 > C4 > C1 > C3
# tentative solutions (those are filtered to keep the closest ones)
# C2 > C5 > C6 > C4 > C1 > C3
# C2 > C6 > C5 > C4 > C1 > C3
kemeny(por)
