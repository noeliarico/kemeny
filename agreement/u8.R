u8 <- function(profileOfRankings = NULL, om = NULL) {
  u <- u_abstract(profileOfRankings, om)
  om <- u$om
  half <- u$h
  
  # check the absolute majorities
  v <- om > half
  # sum of the absolute majorities
  return(sum(v))
}
