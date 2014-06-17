# -*- coding: utf-8 -*-
# distutils: language = c++

cimport numpy as cnp
import numpy as np
import cython

# Work-around for non-type tempalte arguments
cdef extern from *:
    ctypedef void * eight "8"
    ctypedef void * threehundredfifty "350"


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


# Specialized for n=8, lim=350:
from algmoid cimport ${func}_tmpl as c_${func}_tmpl

@cython.wraparound(False)
@cython.boundscheck(False)
cdef ${func}_arr_8_350(double[:] x):
    cdef int i
    cdef cnp.ndarray[cnp.float64_t, ndim=1] out = np.empty(x.size)
    for i in range(x.size):
        out[i] = c_${func}_tmpl[double, eight, threehundredfifty](x[i])
    return out

def ${func}_8_350(x):
    try:
        return ${func}_arr_8_350(
            x.flatten()).reshape(x.shape)
    except:
        try:
            as_arr = np.asarray(x, dtype=np.float64)
            return ${func}_arr_8_350(
                as_arr.flatten()).reshape(as_arr.shape)
        except:
            return c_${func}_tmpl[double, eight, threehundredfifty](x)

%endfor
