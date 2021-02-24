check_data_experiments_is_null <- function(pors) {
  sapply(pors, function(x) sum(sapply(x, function(y) is.null(y))))
}

check_data_experiments_is_condorcet <- function(pors) {
  sapply(pors, function(x) sapply(x, function(y) as.logical(ifelse(!is.null(y), condorcet(y), NA))))
}

check_data_experiments_is_condorcet_winner <- function(pors) {
  sapply(pors, function(x) sapply(x, function(y) as.logical(ifelse(!is.null(y), condorcet_winner(y), NA))))
}

check_data_experiments_margin <- function(pors) {
  lapply(pors, function(x) sapply(x, function(y) ifelse(!is.null(y), agreement_margin(votrix(y)), NA)))
}

