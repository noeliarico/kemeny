u10 <- function(profileOfRankings = NULL, om = NULL) {
  u <- u_abstract(profileOfRankings, om)
  om <- u$om
  
  # get rowsum for each row
  v <- rowSums(om)
  # mean of the rowsums
  return(sd(v))
}
