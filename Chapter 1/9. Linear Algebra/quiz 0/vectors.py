import numpy as np

def add_vectors(u,v):
    res = np.array(u) + np.array(v)
    return res
add_vectors([2,2,2],[4,3,5])


def scalar_mult(s,v):
    res = s*np.array(v)
    return res
scalar_mult(3,[4,5,6])

def dot_prod(u,v):
    res = np.dot(np.array(u),np.array(v))
    return res
dot_prod([3,4,5],[1,1,1])

