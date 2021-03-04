# Example used in the paper for fuzzieee 2021
# Recursive process with only one b=0
por <- parse_profile_of_rankings("5, C3 ≻ C2 ≻ C4 ≻ C1,
                                  1, C1 ≻ C4 ≻ C3 ≻ C2,
                                  3, C4 ≻ C3 ≻ C1 ≻ C2,
                                  1, C1 ≻ C2 ≻ C4 ≻ C3")
por <- set_candidates(por, paste0("a_",1:4))

# poner este en el paper que se nota que uno de los ganadores es el resultado
por <- parse_profile_of_rankings("4, C3 ≻ C2 ≻ C4 ≻ C1,
                                  1, C1 ≻ C2 ≻ C4 ≻ C3 ,
                                  4, C4 ≻ C3 ≻ C1 ≻ C2,
                                  1, C2 ≻ C1 ≻ C4 ≻ C3")
por <- set_candidates(por, paste0("a_",1:4))
votrix(por)
kemeny(por)
condorcet(por, seePoints = T)
rowSums(por$votrix)
por$votrix[-3,-3]
rowSums(por$votrix[-3,-3])
por$votrix[-c(3,2),-c(3,2)]
por$votrix[-c(3,4),-c(3,4)]
por$votrix[-4,-4]
rowSums(por$votrix[-4,-4])
k <- kemeny(por)
print(k, complete = T)
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

# sin condorcet winner y 2 beta=0

# special case all the candidates are also tied with one of the condorcet losers
# but c2 is a weak condorcet loser
por <- parse_profile_of_rankings("
2, C5 ≻ C1 ≻ C2 ≻ C4 ≻ C3,
5, C2 ≻ C4 ≻ C3 ≻ C5 ≻ C1,
3, C1 ≻ C2 ≻ C5 ≻ C4 ≻ C3")
condorcet(por, seePoints = T)
votrix(por)
kemeny(por)

# c3 is tied with all the candidates
por <- parse_profile_of_rankings("
3, C4 ≻ C5 ≻ C1 ≻ C3 ≻ C2,
3, C2 ≻ C3 ≻ C5 ≻ C4 ≻ C1,
2, C3 ≻ C5 ≻ C1 ≻ C4 ≻ C2,
2, C1 ≻ C5 ≻ C4 ≻ C2 ≻ C3")
condorcet(por, seePoints = T)
votrix(por)
kemeny(por)

# c3 and c5 have beta=0 and c1 and c4 are also tied
# all the solutions have permutations of c3 and c5 at the end but
# there are 4 solutions which is > than factorial(2)
por <- parse_profile_of_rankings("
3, C2 ≻ C4 ≻ C5 ≻ C3 ≻ C1,
2, C1 ≻ C2 ≻ C3 ≻ C5 ≻ C4,
1, C1 ≻ C3 ≻ C4 ≻ C2 ≻ C5,
2, C2 ≻ C4 ≻ C1 ≻ C3 ≻ C5,
2, C2 ≻ C1 ≻ C5 ≻ C4 ≻ C3")
condorcet(por, seePoints = T)
votrix(por)
kemeny(por)

# c2 and c3 have beta=0 and there are no more ties. All the solutions end with
# c2>c3 or c3>c2 and there are two solutions which is factorial(2)
por <- parse_profile_of_rankings("
1, C2 ≻ C1 ≻ C4 ≻ C3 ≻ C5,
1, C5 ≻ C2 ≻ C1 ≻ C4 ≻ C3,
3, C1 ≻ C4 ≻ C2 ≻ C5 ≻ C3,
3, C1 ≻ C4 ≻ C5 ≻ C3 ≻ C2,
2, C3 ≻ C5 ≻ C2 ≻ C4 ≻ C1")
condorcet(por, seePoints = T)
votrix(por)
kemeny(por)

# c2 and c4 have beta=0 and there are no more ties. All the solutions end with
# c2>c4 or c4>c1 and there are two solutions which is factorial(2)
por <- parse_profile_of_rankings("
2, C3 ≻ C5 ≻ C4 ≻ C2 ≻ C1,
2, C3 ≻ C1 ≻ C5 ≻ C4 ≻ C2,
2, C3 ≻ C5 ≻ C1 ≻ C2 ≻ C4,
3, C5 ≻ C1 ≻ C3 ≻ C2 ≻ C4,
1, C4 ≻ C5 ≻ C3 ≻ C1 ≻ C2")
condorcet(por, seePoints = T)
votrix(por)
kemeny(por)

# c1 and c3 have beta=0 and c2 and c4 are also tied.
# All the solutions end with a permutation of c1 and c3 but there are 4 solutions
# which is > than factorial(2)
por <- parse_profile_of_rankings("
1, C3 ≻ C1 ≻ C2 ≻ C4,
4, C2 ≻ C4 ≻ C3 ≻ C1,
2, C4 ≻ C1 ≻ C2 ≻ C3,
3, C4 ≻ C2 ≻ C1 ≻ C3")
condorcet(por, seePoints = T)
votrix(por)
kemeny(por)

# condorcet winner y 2 beta=0

numberOfVoters           ranking
1 C3 ≻ C1 ≻ C4 ≻ C2
4 C4 ≻ C2 ≻ C3 ≻ C1
2 C4 ≻ C1 ≻ C2 ≻ C3
3 C4 ≻ C2 ≻ C1 ≻ C3

numberOfVoters                ranking
1              3 C4 ≻ C1 ≻ C5 ≻ C3 ≻ C2
2              2 C1 ≻ C2 ≻ C4 ≻ C3 ≻ C5
3              3 C4 ≻ C1 ≻ C5 ≻ C2 ≻ C3
4              2 C5 ≻ C4 ≻ C3 ≻ C2 ≻ C1

numberOfVoters                ranking
1              3 C1 ≻ C4 ≻ C2 ≻ C5 ≻ C3
2              2 C3 ≻ C5 ≻ C1 ≻ C4 ≻ C2
3              2 C2 ≻ C3 ≻ C1 ≻ C4 ≻ C5
4              3 C1 ≻ C4 ≻ C5 ≻ C3 ≻ C2

# with three zeros and condorcet winner
numberOfVoters           ranking
1              3 C4 ≻ C3 ≻ C2 ≻ C1
2              2 C2 ≻ C4 ≻ C1 ≻ C3
3              2 C2 ≻ C3 ≻ C1 ≻ C4
4              3 C1 ≻ C2 ≻ C3 ≻ C4

1              2 C6 ≻ C4 ≻ C3 ≻ C1 ≻ C5 ≻ C2
2              3 C3 ≻ C4 ≻ C5 ≻ C6 ≻ C2 ≻ C1
3              3 C3 ≻ C1 ≻ C4 ≻ C2 ≻ C6 ≻ C5
4              2 C5 ≻ C4 ≻ C3 ≻ C2 ≻ C6 ≻ C1

1              3 C1 ≻ C4 ≻ C2 ≻ C3 ≻ C6 ≻ C5
2              2 C6 ≻ C1 ≻ C3 ≻ C2 ≻ C4 ≻ C5
3              3 C2 ≻ C1 ≻ C3 ≻ C5 ≻ C4 ≻ C6
4              2 C4 ≻ C2 ≻ C5 ≻ C6 ≻ C3 ≻ C1

1              2 C5 ≻ C3 ≻ C2 ≻ C6 ≻ C4 ≻ C1
2              2 C2 ≻ C5 ≻ C1 ≻ C6 ≻ C4 ≻ C3
3              3 C2 ≻ C6 ≻ C5 ≻ C1 ≻ C3 ≻ C4
4              3 C5 ≻ C3 ≻ C4 ≻ C2 ≻ C6 ≻ C1

1              2 C3 ≻ C6 ≻ C1 ≻ C2 ≻ C5 ≻ C4
2              3 C6 ≻ C5 ≻ C2 ≻ C3 ≻ C4 ≻ C1
3              2 C3 ≻ C5 ≻ C4 ≻ C2 ≻ C6 ≻ C1
4              3 C5 ≻ C1 ≻ C2 ≻ C3 ≻ C6 ≻ C4


# c3 and c6 have beta=0 and c2 and c3 are also tied.
# All the solutions end with a permutation of c2 and c3 but there are 2 solutions
# which is = to factorial(2). c4 is a Condorcet winner
por <- parse_profile_of_rankings("
3, C1 ≻ C4 ≻ C3 ≻ C6 ≻ C5 ≻ C2,
1, C4 ≻ C5 ≻ C1 ≻ C2 ≻ C6 ≻ C3,
4, C4 ≻ C2 ≻ C5 ≻ C1 ≻ C6 ≻ C3,
2, C4 ≻ C5 ≻ C3 ≻ C2 ≻ C6 ≻ C1")
condorcet(por, seePoints = T)
votrix(por)
kemeny(por)


# c3 and c6 have beta=0 
# c2 (wcw) and c4 (wcw) are also tied
# c1 and c6 (beta=0) are also tied
# All the solutions end with a permutation of c1, c3 and c6
# there are 6 solutions which is > than factorial(2)
por <- parse_profile_of_rankings("
2, C4 ≻ C2 ≻ C3 ≻ C5 ≻ C1 ≻ C6,
4, C2 ≻ C4 ≻ C5 ≻ C6 ≻ C1 ≻ C3,
3, C1 ≻ C5 ≻ C4 ≻ C3 ≻ C2 ≻ C6,
1, C6 ≻ C1 ≻ C2 ≻ C5 ≻ C3 ≻ C4")
condorcet(por, seePoints = T)
votrix(por)
kemeny(por)

# c1 and c6 have beta=0 
# c2 (wcw) and c3 are also tied
# c2 (wcw) and c6 (beta=0) are also tied
# All the solutions end with a permutation of c1 and c6
# there are 2 solutions which is = tO factorial(2)
por <- parse_profile_of_rankings("
2, C2 ≻ C3 ≻ C4 ≻ C1 ≻ C5 ≻ C6,
3, C5 ≻ C4 ≻ C3 ≻ C6 ≻ C2 ≻ C1,
3, C2 ≻ C5 ≻ C1 ≻ C3 ≻ C4 ≻ C6,
2, C3 ≻ C6 ≻ C2 ≻ C5 ≻ C4 ≻ C1")
condorcet(por, seePoints = T)
votrix(por)
kemeny(por)

# c1 and c3 have beta=0 
# c1 (beta=0) is also tied with c4 and c5
# c2 and c6 are also tied
# c3 (beta=0) is also tied with c5
# c4 is tied with c5 and c6
# All the solutions end with a permutation of c1 and c6
# there are 2 solutions which is = tO factorial(2)
por <- parse_profile_of_rankings("
3, C6 ≻ C5 ≻ C2 ≻ C1 ≻ C4 ≻ C3,
2, C6 ≻ C1 ≻ C3 ≻ C4 ≻ C5 ≻ C2,
3, C2 ≻ C4 ≻ C6 ≻ C3 ≻ C1 ≻ C5,
2, C5 ≻ C4 ≻ C3 ≻ C2 ≻ C6 ≻ C1")
condorcet(por, seePoints = T)
votrix(por)
kemeny(por)


# c2, c3, c4 have beta=0
# c1 is a condorcet winner
# c5 is also tied with c3
# c6 is also tied with c3
# 10 solutions
# c4 and c2 are always after c5 and c6
# c3 permutes with c5 and c6
por <- parse_profile_of_rankings("
2, C6 ≻ C5 ≻ C1 ≻ C2 ≻ C4 ≻ C3,
2, C3 ≻ C1 ≻ C6 ≻ C4 ≻ C5 ≻ C2,
3, C1 ≻ C2 ≻ C3 ≻ C6 ≻ C5 ≻ C4,
3, C1 ≻ C5 ≻ C6 ≻ C4 ≻ C3 ≻ C2")
condorcet(por, seePoints = T)
votrix(por)
kemeny(por)

por <- parse_profile_of_rankings("
2, C6 ≻ C5 ≻ C1 ≻ C2 ≻ C4 ≻ C3,
2, C3 ≻ C1 ≻ C6 ≻ C4 ≻ C5 ≻ C2,
3, C1 ≻ C2 ≻ C6 ≻ C5 ≻ C3 ≻ C4,
3, C1 ≻ C5 ≻ C6 ≻ C4 ≻ C3 ≻ C2")
condorcet(por, seePoints = T)
votrix(por)
kemeny(por)

# c4, c5, c6 have beta=0
# c1 is also tied with c2 and c6
# c2 is a weak condorcet winner (tied with c4 and c6)
# c3 is a weak condorcet winner (tied with c6)
por <- parse_profile_of_rankings("
3, C6 ≻ C3 ≻ C1 ≻ C4 ≻ C2 ≻ C5,
3, C3 ≻ C2 ≻ C1 ≻ C5 ≻ C4 ≻ C6,
2, C4 ≻ C2 ≻ C6 ≻ C3 ≻ C1 ≻ C5,
2, C1 ≻ C3 ≻ C5 ≻ C6 ≻ C2 ≻ C4")
condorcet(por, seePoints = T)
votrix(por)
kemeny(por)

por <- parse_profile_of_rankings("
2, C1 ≻ C3 ≻ C2 ≻ C4 ≻ C6 ≻ C5,
4, C1 ≻ C2 ≻ C6 ≻ C4 ≻ C5 ≻ C3,
1, C6 ≻ C4 ≻ C2 ≻ C5 ≻ C1 ≻ C3,
3, C3 ≻ C6 ≻ C5 ≻ C2 ≻ C1 ≻ C4")
condorcet(por, seePoints = T)
votrix(por)
kemeny(por)



por <- parse_profile_of_rankings("5, C3 ≻ C2 ≻ C4 ≻ C1,
                                  1, C1 ≻ C4 ≻ C3 ≻ C2,
                                  3, C4 ≻ C3 ≻ C1 ≻ C2,
                                  1, C1 ≻ C2 ≻ C4 ≻ C3")
por <- set_candidates(por, paste0("a_",1:4))

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

por <- parse_profile_of_rankings("
2, C1 ≻ C3 ≻ C4 ≻ C2,
1, C1 ≻ C2 ≻ C3 ≻ C4,
5, C2 ≻ C4 ≻ C3 ≻ C1,
2, C4 ≻ C1 ≻ C2 ≻ C3")
por <- set_candidates(por, paste0("a_",1:4))
get_alpha(por)
condorcet(por, seePoints = T)
kemeny(r)
