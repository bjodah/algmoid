// -*- mode: c++-mode -*-
#ifndef _6RHPX737NVCOLB22EZI3GBEYCI
#define _6RHPX737NVCOLB22EZI3GBEYCI

// C++11 templated source code for algebraic sigmoids of type:
// s(x) := x*((x/lim)**n + 1)**(-1/n)

#include <cmath>

namespace algmoid{

using std::pow;
using std::log;

%for name, expr in [\
    ('sigmoid', 'x*pow(pow(x/static_cast<T>(lim), n) + 1, -1.0/n)'),\
    ('Dsigmoid', 'pow(pow(x/static_cast<T>(lim), n) + 1, -1 - 1.0/n)'),\
    ('D2sigmoid', '-pow(x/static_cast<T>(lim), n)*(n + 1)*pow(pow(x/static_cast<T>(lim), n) + 1, -(2*n + 1.0)/n)/x;'),\
    ('Dsigmoid_over_sigmoid', '1/(x*(pow(x/static_cast<T>(lim), n) + 1))'),\
    ('asigmoid', 'x*pow(-pow(x/static_cast<T>(lim), n) + 1, -1.0/n)'),\
    ('Dasigmoid', 'pow(-pow(x/static_cast<T>(lim), n) + 1, -1 - 1.0/n)'),\
    ('exps', 'exp(sigmoid<n, lim>(x))'),\
    ('logs', 'asigmoid<n, lim>(log(x))'),\
    ('Dexps', 'exps<n, lim>(x)*Dsigmoid<n, lim>(x)'),\
    ('Dlogs', 'Dasigmoid<n, lim>(log(x))/x'),\
    ]:
// ${name}:
template <typename T, int n, int lim>
T ${name}_tmpl(T x){
    return ${expr};
}
template <typename T>
T ${name}(T x, int n, int lim){
    return ${expr.replace('<n, lim>(x)', '(x, n, lim)')};
}

%endfor

}; //namespace algmoid
#endif
