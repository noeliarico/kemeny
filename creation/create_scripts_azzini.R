scripts_azzini <- function(oms, file_name) {
  out1 <- ' 
import azzinimunda.azzinimunda0 as am
import scf.initialization as init
import numpy as np
import time\n\n' 
  
  out2 <- paste0(' 
algorithm = am.AzziniMunda1(om) 
start_time = time.time()
sol = algorithm.execute()
exec_time = time.time() - start_time
f = open("', file_name, '", "a")
f.write("{}\\n".format(exec_time))
f.close()
print(exec_time)
##############################################')
  return(paste(out1, paste(paste(oms, out2), collapse = "\n"), sep = "\n"))
}

n = 4
r <- initialize(n, 10)
omr <- unlist(lapply(r, function(x) lapply(x, votrix)), recursive = F)
pom <- sapply(1:length(omr), function(x) to_python_om(omr[[x]], "om"))
sink("kemeny/scriptn4.py")
cat(scripts_azzini(pom, "results4A1.txt"))
sink()
