cdef extern from "algmoid.h" namespace "algmoid":
%for func in FUNCS:
    #cdef double ${func}_tmpl[T, n, lim](T)
    cdef double ${func}[T](T, int, int)
%endfor
