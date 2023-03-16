library(rlang)
profiles_ejor <- env()
files <- list.files(file.path(folder, "profiles_of_rankings"), full.names = T)
names <- list.files(file.path(folder, "profiles_of_rankings")) %>% str_remove(".RData")
for(i in 1:length(files)) {
  load(files[i], envir = profiles_ejor)
  assign(names[i], profiles_ejor$porsPredictTime, envir = profiles_ejor)
}
rm(porsPredictTime, envir = profiles_ejor)

