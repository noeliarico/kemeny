sink("pors9.txt")
for(i in 1:20) {
  r <- random_profile_of_rankings(9,10)
  cat(paste0("\nprint('## ",i,"#########################')\n"))
  cat(to_python_om(votrix(r)))
  cat("results9 = np.vstack((results9, measure(9,0,rep=1,om=om)))")
}
sink()


sink("pors10.txt")
for(i in 1:10) {
  r <- random_profile_of_rankings(10,10)
  cat(paste0("\nprint('## ",i,"#########################')\n"))
  cat(to_python_om(votrix(r)))
  cat("results10 = np.vstack((results10, measure(10,0,rep=1,om=om)))")
}
sink()



sink("pors11.txt")
for(i in 1:10) {
  r <- random_profile_of_rankings(11,10,distinct=10)
  cat(paste0("\nprint('## ",i," ########################')\n"))
  cat(to_python_om(votrix(r)))
  cat("results11 = np.vstack((results11, measure(11,0,rep=1,om=om)))")
}
sink()

sink("pors12.txt")
for(i in 1:10) {
  r <- random_profile_of_rankings(12,10,distinct=10)
  cat(paste0("\nprint('## ",i," ########################')\n"))
  cat(to_python_om(votrix(r)))
  cat("results11 = np.vstack((results11, measure(11,0,rep=1,om=om)))")
}
sink()


sink("pors8.txt")
for(i in 1:30) {
  r <- random_profile_of_rankings(8,10,distinct=10)
  cat(paste0("\nprint('## ",i," ########################')\n"))
  cat(to_python_om(votrix(r)))
  cat("print(measure(8,0,rep=3,om=om))")
}
sink()
