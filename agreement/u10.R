u10 <- function(profileOfRankings = NULL, om = NULL) {
  if(is.null(profileOfRankings) && is.null(om)) {
    stop("Preferences are needed to compute the uncertainty.")
  }
  if(!is.null(profileOfRankings) && !is.null(om)) {
    warning("om will be ignored as a complete profile of rankings has been given.")
  }
  if(!is.null(profileOfRankings)) {
    om <- votrix(profileOfRankings)
    half <- sum(profileOfRankings$numberOfVoters)/2
  } else {
    half <- om[1,2]+om[2,1]
  }
  
  v <- rowSums(om)
  
  # sum of the absolute majorities
  return(mean(v))
}
