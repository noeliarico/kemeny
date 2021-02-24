import numpy as np

def borda(om):
  """Get the outranking matrix and returns the Borda Count

  Args:
    n (int): the number of candidates

  Returns:
    ndarray: a random ranking
  """
  noutranks = np.sum(om, axis=1)
  # print(noutranks)
  out = np.argsort(noutranks)
  sorted_noutranks = noutranks[out]
  sorted_index = np.searchsorted(sorted_noutranks, noutranks)
  return (out.size - 1) - sorted_index 

def ranking_to_lineal(r):
  for i in range(max(r)+1):
    # print(i)
    indexes = np.where(r == i)[0]
    # print(indexes)
    if indexes.size > 1: # there are tied candidates
      # Increment all the candidates that are later on the ranking
      # r[r > i] = r[r > i] + indexes.size-1
      # Untie
      values = i - np.arange(indexes.size) 
      values = values[::-1]
      # print("New values {}".format(values))
      r[indexes] = values
  return r
