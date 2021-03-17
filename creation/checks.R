check_data_experiments_is_null <- function(pors) {
  sapply(pors, function(x) sum(sapply(x, function(y) is.null(y))))
}

check_data_experiments_is_condorcet <- function(pors) {
  sapply(pors, function(x) sapply(x, function(y) as.logical(ifelse(!is.null(y), condorcet(y), NA))))
}

check_data_experiments_is_condorcet_winner <- function(pors) {
  sapply(pors, function(x) sapply(x, function(y) as.logical(ifelse(!is.null(y), condorcet_winner(y), NA))))
}

check_data_experiments_condorcet_dist <- function(pors, v = 10) {
  lapply(pors, function(x) lapply(x, function(y) ifelse(!is.null(y), rowSums(votrix(y) > (v/2)), NA)))
}

check_data_experiments_margin <- function(pors) {
  lapply(pors, function(x) sapply(x, function(y) ifelse(!is.null(y), agreement_margin(votrix(y)), NA)))
}

check_data_experiments_u <- function(pors, u) {
  lapply(pors, function(x) sapply(x, function(y) ifelse(!is.null(y), u(y), NA)))
}

check_data_experiments_omega <- function(pors) {
  sapply(pors, function(x) sapply(x, function(y) ifelse(!is.null(y), get_omega(y), NA)))
}

check_data_experiments_nrp <- function(pors) {
  lapply(pors, function(x) sapply(x, function(y) ifelse(!is.null(y), nrow(y$profileOfRankings), NA)))
}

check_data_votrix <- function(pors, votes = 10) {
  is_votrix_ok <- function(v) {
    for(i in 1:ncol(v)) {
      for(j in 1:nrow(v)) {
        if(i!=j && v[i,j]+v[j,i] != votes) return(FALSE)
      }
    }
    return(TRUE)
  }
  return(all(sapply(pors, function(x) sapply(x, function(y) ifelse(!is.null(y), is_votrix_ok(votrix(y)), NA))), na.rm = TRUE))
} 

