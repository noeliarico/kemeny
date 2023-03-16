check_data_experiments_is_null <- function(pors) {
  sapply(pors, function(x) sum(sapply(x, function(y) is.null(y))))
}

check_data_experiments_is_condorcet <- function(pors) {
  sapply(pors, function(x) sapply(x, function(y) as.logical(ifelse(!is.null(y), condorcet(y), NA))))
}

check_data_experiments_is_condorcet_winner <- function(pors) {
  sapply(pors, function(x) sapply(x, function(y) as.logical(ifelse(!is.null(y), condorcet_winner(y), NA))))
}

check_data_experiments_n <- function(pors, v = 10) {
  lapply(pors, function(x) lapply(x, function(y) ifelse(!is.null(y), length(y$candidates), NA)))
}

check_data_experiments_alphas <- function(pors) {
  lapply(pors, function(x) lapply(x, function(y) get_alpha(y)))
}

check_data_experiments_betas <- function(pors, v = 10) {
  lapply(pors, function(x) lapply(x, function(y) sort(rowSums(votrix(y) > (v/2)))))
}

check_data_experiments_margin <- function(pors) {
  lapply(pors, function(x) sapply(x, function(y) ifelse(!is.null(y), agreement_margin(votrix(y)), NA)))
}

check_data_experiments_d <- function(pors, d) {
  lapply(pors, function(x) sapply(x, function(y) ifelse(!is.null(y), d(y), NA)))
}

check_data_experiments_omega <- function(pors) {
  sapply(pors, function(x) sapply(x, function(y) ifelse(!is.null(y), get_omega(y), NA)))
}

check_data_experiments_distinct <- function(pors) {
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

