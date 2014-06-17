# -*- coding: utf-8 -*-
# distutils: language = c++

cimport numpy as cnp
import numpy as np
import cython

%for func in FUNCS:
from algmoid cimport ${func} as c_${func}

@cython.wraparound(False)
@cython.boundscheck(False)
cdef ${func}_arr(double[:] x, int n, int lim):
    cdef int i
    cdef cnp.ndarray[cnp.float64_t, ndim=1] out = np.empty(x.size, dtype=np.float64)
    for i in range(x.size):
        out[i] = c_${func}[double](x[i], n, lim)
    return out

def ${func}(x, int n, int lim):
    try:
        return ${func}_arr(x.flatten(), n, lim).reshape(x.shape)
    except:
        try:
            as_arr = np.asarray(x, dtype=np.float64)
            return ${func}_arr(as_arr.flatten(), n, lim).reshape(as_arr.shape)
        except:
            return c_${func}[double](x, n, lim)
%endfor
