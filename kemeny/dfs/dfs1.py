import numpy as np
import logging

def kemeny2(om, d):

  # Candidates to explore, if there are n candidates, to_explore
  # contains the values [0, ..., n]
  to_explore = np.arange(om.shape[0], dtype=np.dtype('u1'))

  # At the beginning there isn't any solution to the problem
  solution = np.empty(0)

  # to store the best distance of all the rankings with candidate i as winner
  # initially the best distance is the one of the ranking given by parameter
  # current_best_dist = float('inf')
  #current_best_dist = dRP(r, om)
  current_best_dist = d

  # Call the recursive function that explore all the branches in the tree
  sol = kemeny_rec2(om, # outranking matrix
                          np.empty(0, dtype=np.int32), # candidates to explore
                          # remaining candidates to explore
                          to_explore, 
                          0, # current distance of the prefix being evaluated
                          current_best_dist, # the lowest distance up till now
                          # array to store the ranking(s) with the lowest dist
                          solution) 
  solution = sol[1]
  print("solution is {}".format(sol))
  ncol = om.shape[0] # the ranking is a vector of length n
  nrow = solution.size // ncol
  return np.reshape(solution, (nrow, ncol))

def kemeny_rec2(om, prefix, to_explore, dist, current_best_dist, solution):

  # Stop condition: the ranking gives a order for all the candidates
  if to_explore.size == 0:
    if dist < current_best_dist: # if it is best, overwritte
      # logging.info("{} NEW BEST! old distance = {}, best = {}".format(prefix, current_best_dist, dist))
      solution = prefix
      current_best_dist = dist
      # logging.info("Current solution: {}".format(solution))
    elif dist == current_best_dist: # if it is equal to the current, append
      solution = np.append(solution, prefix)
      # logging.info("{} BEST AGAIN! old distance = {}, best = {}".format(prefix, current_best_dist, dist))
      # logging.info("Current solution: {}".format(solution))

    # else, do nothing
    return (current_best_dist, solution)

  # Recursive call
  for i in range(to_explore.size):

    # Add the next element to the prefix
    prefix_rec = np.append(prefix, to_explore[i])
    # Remove the added element from the list of nodes to explore
    to_explore_rec = np.delete(to_explore, i)
    
    # Keep from the column of the element added in om only the rows that not
    # correspond to the elements that have been previously explroed
    keep = np.in1d(np.arange(om.shape[0]), prefix_rec, invert=True)
    dist_rec = dist + np.sum(om[keep,to_explore[i]])

    if dist < current_best_dist:
      # print("prefix = {}, to_explore = {}, dist {}+{}={})".format(prefix_rec, to_explore_rec, dist, np.sum(om[keep,to_explore[i]]), dist_rec))
      # logging.info("prefix = {}, to_explore = {}, dist {}+{}={})".format(prefix_rec, to_explore_rec, dist, np.sum(om[keep,to_explore[i]]), dist_rec))
      # logging.debug("{} ({}+{}={})".format(prefix_rec, dist, np.sum(om[keep,to_explore[i]]), dist_rec))

      # Recursive call
      sol = kemeny_rec2(om, # outranking matrix
                      prefix_rec, # beginning of the ranking
                      # remaining candidates to explore
                      to_explore_rec, 
                      dist_rec, # current distance of the prefix being evaluated
                      current_best_dist, # the lowest distance up till now
                      # array to store the ranking(s) with the lowest dist
                      solution) 
      if sol[0] <= current_best_dist:
        current_best_dist = sol[0]
        solution = sol[1]

  return current_best_dist, solution

om = np.array([0, 5, 8, 14, 9, 0, 8, 9, 6, 6, 0, 6, 0, 5, 8, 0]).reshape(4, 4)
print(om)

