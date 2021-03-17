u11 <- function(profileOfRankings = NULL, om = NULL) {
  u <- u_abstract(profileOfRankings, om)
  om <- u$om
  half <- u$h
  
  # difference between the median and the mean of beta
  v <- rowSums(om)
  # mean of the rowsums
  return(mean(v)-median(v))
}
