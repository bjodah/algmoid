cdef extern from "algmoid_8_350.h" namespace "algmoid_8_350":
%for func in FUNCS:
    cdef double ${func}_8_350(double)
%endfor
