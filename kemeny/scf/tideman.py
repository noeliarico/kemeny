import numpy as np

from creation import *

def tideman(om):

    n = om.shape[0]
    
    break_ties = np.arange(n)
    np.random.shuffle(break_ties)

    indices_pairs = np.triu_indices(n, 1)
    triu = om[indices_pairs]
    tril = om.T[indices_pairs]

    max_elem = np.maximum(triu, tril)

    it_is_from_upper = np.equal(max_elem, triu).tolist()
    for i in range(len(it_is_from_upper)):
        if not it_is_from_upper[i]:
            aux = indices_pairs[0][i]
            indices_pairs[0][i] = indices_pairs[1][i]
            indices_pairs[1][i] = aux


    # print("upper diagonal: {}, lower diagonal: {}, \n maximum element: {}, it is from the upper: {}".format(triu, tril, max_elem, it_is_from_upper))
    # print("indices pairs: {}".format(indices_pairs))

    # sort in descending order
    indices_sorted = ((-max_elem).argsort()[:max_elem.size]).tolist()
    # print("indices sorted: {}".format(indices_sorted))
    froms = indices_pairs[0]
    froms = froms[indices_sorted]
    tos = indices_pairs[1]
    tos = tos[indices_sorted]
    # print("froms: {}, tos: {}".format(froms, tos))

    # create the transitive matrix
    graph = np.zeros((n, n), dtype=bool)
    # print(graph)
    for i in range(froms.size):
        f = froms[i] # from
        t = tos[i] # to
        if not graph[t, f]:
            graph[f, t] = True  
            graph[f, :] = np.logical_or(graph[f, :], graph[t, :])    
        for j in range(n):
            if graph[j, f]:
                graph[j, :] = np.logical_or(graph[f, :], graph[j, :])  
    # print(indices_sorted)
    # print(graph)

    return graph.sum(axis = 1)

om = create_random_om(5, 10)
# print(om)
# print(tideman(om))

