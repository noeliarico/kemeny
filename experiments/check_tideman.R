check_tideman <- function(pors) {
  ts <- lapply(pors, function(x) lapply(x, function(y) tideman(y,break_ties=ranking(rowSums(votrix(y))))))
  ks <- lapply(pors, function(x) lapply(x, function(y) kemeny(y)))
  
  res <- c()
  for(i in 1:length(pors)) {
    for(j in 1:length(pors[[i]])) {
      k <- ks[[i]][[j]]$winningRanking
      t <- ts[[i]][[j]]
      # print(k)
      # print("####")
      # print(t)
      if(!is.null(nrow(k))) {
        if(any(rowSums(apply(k, 1, function(x) k == t)) > 0)) {
          res <- c(res, TRUE)
        } else {
          res <- c(res, FALSE)
        }
      }
      else {
        if(all(k == t)) {
          res <- c(res, TRUE)
        } else {
          res <- c(res, FALSE)
        }
      }
      
    }
  }
  return(table(res))
}

