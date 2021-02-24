import numpy as np

def dRP(r, om): # distance from one ranking to a profile of rankings
  """Get two rankings and return the Kemeny distance between them

  Args:
    r (list): ranking
    om (matrix): matrix representing the profile of rankings

  Returns:
    int: a integer value representing the distance between r1 and r2
  """

  keep = np.ones(r.size, dtype=bool)
  total = 0
  for i in range(r.size):
    index = np.where(r == i)[0].astype(np.uint8)
    keep[index] = False
    total += np.sum(om[keep,:], axis = 0)[index]
    # print("index = {}, sum = {}, total: {}".format(index, np.sum(om[keep,:], axis = 0), total))

    # print("index of {} element is {}".format(i, index))
    # print(om)
    # print("The sum is: {} | Total = {}".format(np.sum(om[keep,:], axis = 0), total))
    
    
  return total
