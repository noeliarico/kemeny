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
# el de arriba está escrito pero hay que cambiarlo al de abajo que queda mejor
por <- parse_profile_of_rankings("5, C3 ≻ C2 ≻ C4 ≻ C1,
                                  1, C1 ≻ C4 ≻ C3 ≻ C2,
                                  3, C4 ≻ C3 ≻ C1 ≻ C2,
                                  1, C1 ≻ C2 ≻ C4 ≻ C3")

tikz <- kemeny_to_tikz(votrix(por)) 
sink("creation/step1.tex")
cat(tikz)
sink()

tikz <- kemeny_to_tikz(votrix(por)[-3,-3]) 
sink("creation/step2.tex")
cat(tikz)
sink()

tikz <- kemeny_to_tikz(votrix(por)[-c(3,2),-c(3,2)]) 
sink("creation/step3.tex")
cat(tikz)
sink()

tikz <- kemeny_to_tikz(votrix(por)[-c(3,4),-c(3,4)]) 
sink("creation/step4.tex")
cat(tikz)
sink()

tikz <- kemeny_to_tikz(votrix(por)[-4,-4])
sink("creation/step5.tex")
cat(tikz)
sink()


Ejemplo de condorcet recursivo con 6 candidatos:
  
  structure(list(profileOfRankings = structure(list(C1 = c(5L, 
                                                           5L, 2L, 2L), C2 = c(1L, 6L, 1L, 1L), C3 = c(6L, 4L, 4L, 4L), 
                                                    C4 = c(4L, 3L, 6L, 6L), C5 = c(2L, 2L, 5L, 3L), C6 = c(3L, 
                                                                                                           1L, 3L, 5L)), row.names = c(NA, -4L), class = "data.frame"), 
                 numberOfVoters = c(3, 3, 2, 2), candidates = c("C1", "C2", 
                                                                "C3", "C4", "C5", "C6"), votrix = structure(c(0, 7, 3, 6, 
                                                                                                              6, 6, 3, 0, 3, 3, 3, 3, 7, 7, 0, 6, 8, 8, 4, 7, 4, 0, 10, 
                                                                                                              10, 4, 7, 2, 0, 0, 5, 4, 7, 2, 0, 5, 0), .Dim = c(6L, 6L), .Dimnames = list(
                                                                                                                c("C1", "C2", "C3", "C4", "C5", "C6"), c("C1", "C2", 
                                                                                                                                                         "C3", "C4", "C5", "C6")))), class = c("por", "list"))

