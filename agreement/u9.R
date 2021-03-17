u9 <- function(profileOfRankings = NULL, om = NULL) {
  u <- u_abstract(profileOfRankings, om)
  om <- u$om
  half <- u$h
  
  # get beta for each alternative
  v <- om > half
  v <- rowSums(v)
  # mean value of beta
  return(mean(v))
}
