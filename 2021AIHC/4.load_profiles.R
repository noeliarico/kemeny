library(rlang)
profiles_aihc <- env()
files <- list.files(file.path(folder, "profiles"), full.names = T)
names <- list.files(file.path(folder, "profiles")) %>% str_remove(".RData")
for(i in 1:length(files)) {
  load(files[i], envir = profiles_aihc)
  assign(names[i], profiles_aihc$porsPredictTime, envir = profiles_aihc)
}
rm(porsPredictTime, envir = profiles_aihc)

