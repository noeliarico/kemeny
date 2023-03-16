create_profiles_nc <- function(n, nvotes, total = 100, 
                               seed = NULL, 
                               max_distinct = NULL,
                               distribution = "norm")  {
  
  profiles <- vector(mode = "list", length = total)
  names(profiles) <- paste0("pr",1:total)
  
  created <- 1
  if(!is.null(seed)) set.seed(seed)
  if(is.null(max_distinct)) max_distinct <- nvotes
  if(max_distinct > nvotes) stop("max_distinct must be < than nvotes")
  
  while(created <= total) {
    
    d <- sample(1:max_distinct, 1)
    r <- random_profile_of_rankings(n, nvotes, seed = seed, distinct = d, distribution = distribution)
    
    if(!condorcet(r) && !condorcet_winner(r)) { 
      profiles[[created]] <- r
      created <- created + 1
    }
    
  }
  return(profiles)
}



#ncandidates <- 8:10
ncandidates <- 4
nvoters <- seq(10,500,10)
for(i in ncandidates) {
  for(j in nvoters) {
    cat(paste0("Candidatos ", i, ", votantes ", j, "\n"))
    name <- paste("profiles", i, j, sep = "_")
    p <- create_profiles_nc(n = i, nvotes = j, total = 100)
    assign(name, p)
    save(list = name, file = paste0(name, ".RData"))
  }
}

to_python_om <- function(matrix, name = "om") {
  out <- apply(t(matrix), 2, function(x) paste(x, collapse = ","))
  out <- paste0("[", out, "]")
  out <- paste0(out, collapse = ",\n")
  out <- paste0(name, " = np.array([\n", out, "])\n")
  out
}

scripts_tfg <- function(pors,n,m,
                       file_name,
                       path_out_py = ".") {
  out <- c(paste0('
import numpy as np
profiles = []
'))
  
  for(i in 1:length(pors)) {
    
    out0 <- "##############################################################\n\n"
    # out1 <- to_python_om(votrix(pors[[i]]), name = names(pors)[i])
    # out2 <- paste0('profiles["', names(pors)[i], '"] = ', names(pors)[i], "\n\n")
    out1 <- to_python_om(votrix(pors[[i]]))
    out2 <- "profiles.append(om)\n\n"
    out <- paste0(out, out0, out1, out2)
    
    
  } # end for
  
  file_name <- paste(file_name, n, m, sep="_")
  #out <- c(out, paste0(' 
#pd.DataFrame(results).to_csv("',file.path(path_out_csv,file_name),'.csv", index=False, header=False)'))
  #out <- paste(out, collapse = "\n")
  
  out <- c(out, paste0("
with open('", file_name, ".npy', 'wb') as f:
  np.save(f, profiles)
                       "))
  sink(paste0(file.path(path_out_py,file_name), ".py"))
  cat(out)
  sink()
}

for(i in ncandidates) {
  for(j in nvoters) {
    cat(paste0("Candidatos ", i, ", votantes ", j, "\n"))
    name <- paste("profiles", i, j, sep = "_")
    scripts_tfg(get(name), i, j, "profiles_tfg")
  }
}

