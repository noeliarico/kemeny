to_python_om <- function(matrix, name = "om") {
  out <- apply(t(matrix), 2, function(x) paste(x, collapse = ","))
  out <- paste0("[", out, "]")
  out <- paste0(out, collapse = ",\n")
  out <- paste0(name, " = np.array([\n", out, "])\n")
  out
}

to_python_ranking <- function(ranking, name = "r") {
  r <- as.numeric(ranking) - 1
  r <- paste0(r, collapse = ",")
  out <- paste0(name, " = np.array([", r, "])\n")
  out
}