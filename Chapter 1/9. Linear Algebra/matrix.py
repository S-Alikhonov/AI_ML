import numpy as np
from numpy.core.defchararray import add

def copy_of_matrix(s1,s2):
    return np.array([s1,s2])
a = [1,2]
b = [4,8]
copy_of_matrix(a,b)


def add_row(m):
    m = np.array(m)
    row = np.zeros(m.shape[1]).reshape((1,m.shape[1]))
    res = np.vstack((m,row))
    return(res)
add_row([[2,3,4],[5,5,5]])

def add_column(m):
    m = np.array(m)
    col = np.zeros(m.shape[0]).reshape((m.shape[0],1))
    res = np.hstack((m,col))
    return (res)
add_column([[3,4,4],[4,5,4],[3,3,4]])

def add_matrices(m1,m2):
    res = np.array(m1) + np.array(m2)
    return res
add_matrices([[1,2],[3,4]],[[2,2],[2,2]])

def scalar_mult(s,m):
    res = s*np.array(m)
    return res
scalar_mult(3,[[4,5],[5,6]])

def row_times_column(m1,row,m2,col):
    return(np.dot(np.array(m1)[row,:],np.array(m2)[:,col]))

row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 0)
   

def matrix_prod(m1,m2):
    res = np.dot(np.array(m1),np.array(m2))
    return res

matrix_prod([[1, 2], [3,  4]], [[5, 6], [7, 8]])


def transpose(m):
    return np.array(m).T
transpose([[3, 1], [4, 5], [6, 9]])

