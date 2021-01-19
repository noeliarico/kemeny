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
