cdef extern from "algmoid.h" namespace "algmoid":
%for func in FUNCS:
    cdef double ${func}[T, n, lim](double)
%endfor
