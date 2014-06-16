#ifndef _SE4B2QFUERFJVJCUDHB2NGK7DI
#define _SE4B2QFUERFJVJCUDHB2NGK7DI
// This is a workaround to:
// https://groups.google.com/forum/#!topic/cython-users/3iVlnQXNq2I
#include "algmoid.h"

namespace algmoid_8_350{
%for func in FUNCS:
double ${func}_8_350(double x){
    return algmoid::${func}<double, 8, 350>(x);
}
%endfor
}; // namespace algmoid_8_350
#endif
