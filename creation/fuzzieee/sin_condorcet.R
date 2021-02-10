path <- file.path("creation","scripts")
# n = 5 -------------------------------------------------------------------

pors5 <- create_profiles(5,10,5)
pors6 <- create_profiles(6,10,5)
pors7 <- create_profiles(7,10,5,max_iter = 1000)
pors8 <- create_profiles(8,10,5,max_iter = 10000)
pors9 <- create_profiles(9,10,5,max_iter = 100000)
pors10 <- create_profiles(10,10,5,max_iter = 100000)
pors11 <- create_profiles(11,10,5,max_iter = 100000)
pors12 <- create_profiles(12,10,5,max_iter = 100000)
pors13 <- create_profiles(13,10,5,max_iter = 100000)
pors14 <- create_profiles(14,10,5,max_iter = 100000)

write <- lapply(pors, function(x) lapply(x, function(y) to_python_om(votrix(y))))
sink(file.path(path, "n5.py"))
cat(paste(unlist(write), collapse = "\n"))
sink()
