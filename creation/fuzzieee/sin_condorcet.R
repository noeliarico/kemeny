# n = 5 -------------------------------------------------------------------

pors <- create_profiles(5,10,5)
write <- lapply(pors, function(x) lapply(x, function(y) to_python_om(votrix(y))))
sink("n5.txt")
cat(paste(unlist(write), collapse = "\n"))
sink()
