#' Permute candidate
#' 
#' Takes an outranking matrix and two candidates and permute their positions
#' in the outranking matrix
#'
#' @param om  outranking matrix
#' @param c1  candidate to permute
#' @param c2  candidate to permute
#'
#' @return the outranking matrix with the two candidates permuted
#' @export
#'
#' @examples
permute_candidates <- function(om, c1, c2) {
  n <- ncol(om)
  # Store the corresponding rows and columns
  c1row <- om[c1, ]
  c1col <- om[ ,c1]
  c2row <- om[c2, ]
  c2col <- om[ ,c2]
  # Change the position of the 0 in the rows
  c1row <- c1row[-c1]
  c1row <- append(c1row, 0, after = c2-1)
  c2row <- c2row[-c2]
  c2row <- append(c2row, 0, after = c1-1)
  # Change the position of the 0 in the colums
  c1col <- c1col[-c1]
  c1col <- append(c1col, 0, after = c2-1)
  c2col <- c2col[-c2]
  c2col <- append(c2col, 0, after = c1-1)
  # Permute rows
  om[c1,] <- c2row
  om[c2,] <- c1row
  # Permute cols
  om[,c1] <- c2col
  om[,c2] <- c1col
  return(om)
}

