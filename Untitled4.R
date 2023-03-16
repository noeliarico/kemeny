library(consensus)
por <- parse_profile_of_rankings("4, a_3>a_2>a_4>a_1,
                                  1, a_1>a_2>a_4>a_3,
                                  4, a_4>a_3>a_1>a_2,
                                  1, a_2>a_1>a_4>a_3")
k <- kemeny(por)
print(k, complete = TRUE)
k$distances$distance <- 60 - k$distances$distance
print(k, complete = TRUE)
