cdef extern from "algmoid.h" namespace "algmoid":
%for func in FUNCS:
    cdef T ${func}_tmpl[T, n, lim](T)
    cdef T ${func}[T](T, int, int)
%endfor
