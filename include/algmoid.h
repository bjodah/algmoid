// -*- mode: c++-mode -*-
#ifndef _6RHPX737NVCOLB22EZI3GBEYCI
#define _6RHPX737NVCOLB22EZI3GBEYCI

// C++11 templated source code for algebraic sigmoids of type:
// s(x) := x*((x/lim)**n + 1)**(-1/n)

#include <cmath>

namespace algmoid{

using std::pow;
using std::log;

template <typename T, int n, int lim>
T sigmoid(T x){
    return x*pow(pow(x/static_cast<T>(lim), n) + 1, -1.0/n);
}

template <typename T, int n, int lim>
T Dsigmoid(T x){
    return pow(pow(x/static_cast<T>(lim), n) + 1, -1 - 1.0/n);
}

template <typename T, int n, int lim>
T D2sigmoid(T x){
    return -pow(x/static_cast<T>(lim), n)*(n + 1)*\
        pow(pow(x/static_cast<T>(lim), n) + 1, -(2*n + 1.0)/n)/x;
}

template <typename T, int n, int lim>
T Dsigmoid_over_sigmoid(T x){
    1/(x*(pow(x/static_cast<T>(lim), n) + 1));
}

template <typename T, int n, int lim>
T asigmoid(T x){
    return x*pow(-pow(x/static_cast<T>(lim), n) + 1, -1.0/n);
}

template <typename T, int n, int lim>
T Dasigmoid(T x){
    return pow(-pow(x/static_cast<T>(lim), n) + 1, -1 - 1.0/n);
}

template <typename T, int n, int lim>
T exps(T x){
    return exp(sigmoid<n, lim>(x)); // exp of sigmoid
}

template <typename T, int n, int lim>
T logs(T x){
    return asigmoid<n, lim>(log(x)); // anti function to exps
}

template <typename T, int n, int lim>
T Dexps(T x){
    return exps<n, lim>(x)*Dsigmoid<n, lim>(x);
}

template <typename T, int n, int lim>
T Dlogs(T x){
    return Dasigmoid<n, lim>(log(x))/x;
}


}; // namespace algmoid
#endif
