# -*- coding: utf-8 -*-
# distutils: language = c++

cimport numpy as cnp
import numpy as np
import cython

%for func in FUNCS:
%for n in range(*POWER_SPAN):
from algmoid cimport ${func} as _${func}

@cython.wraparound(False)
@cython.boundscheck(False)
cdef ${func}_arr_${n}(double[:] x):
    cdef int i
    cdef cnp.ndarray[cnp.float64_t, ndim=1] out = np.empty(x.size)
    for i in range(x.size):
        out[i] = _${func}[double, ${n}, 350](x)
    return out

def ${func}_${n}(x):
    try:
        return ${func}_arr_${n}(
            x.flatten()).reshape(x.shape)
    except:
        try:
            as_arr = np.asarray(x, dtype=np.float64)
            return ${func}_arr_${n}(
                as_arr.flatten()).reshape(as_arr.shape)
        except:
            return _${func}[double, ${n}, 350](x)
%endfor

def ${func}(x, n):
    return {
    %for n in range(*POWER_SPAN):
        ${n}: ${func}_${n},
    %endfor
    }[n](x)

%endfor
