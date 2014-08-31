#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

import argh
import numpy as np
import time
import algmoid

code_ = r"""
#include <algmoid>

void cb(int n, const double * const __restrict__ in, double * const __restrict__ out){
    for (int i=0; i<n; ++i)
        out[i] = algmoid::%(name)_tmpl<%(n), %(lim)>(in[i]);
}

#include <Python>
#include <arrayobject>

PyObject* %(name)(PyObject* a_){
    PyArrayObject* a=(PyArrayObject*) a_;
    int n = a->dimensions[0];
    int dims[1];
    dims[0] = n;
    PyArrayObject* ret;
    ret = (PyArrayObject*) PyArray_FromDims(1, dims, NPY_DOUBLE);
    cb(n, a->data, ret->data);
    return (PyObject *)ret;
}
"""


def compile_cb(name):
    return np.weave(code_ % {'name': name, 'n': 8, 'lim': 350})


def main(func='asigmoid', xlim=200, N=1024*1024):
    n = 8
    lim = 350
    x = np.linspace(2, xlim, N)

    # general
    t = time.time()
    y_g = getattr(algmoid, func)(x, n, lim)
    t_g = time.time() - t

    # special
    t = time.time()
    y_s = getattr(algmoid, func+'_8_350')(x)
    t_s = time.time() - t
    assert np.allclose(y_g, y_s)

    # Auto-vectorization from compiling C++ code
    cb = compile_cb(func)
    t = time.time()
    y_c = getattr(algmoid, func+'_8_350')(x)
    t_c = time.time() - t
    assert np.allclose(y_g, y_c)

    # numexpr
    try:
        import numexpr
        t = time.time()
        y_n = numexpr.evaluate({
            'Dsigmoid': '((x/lim)**n + 1)**(-1 - 1/n)',
            'logs': '(-(log(x)/lim)**n + 1)**(-1/n)*log(x)',
            'sigmoid': 'x*((x/lim)**n + 1)**(-1/n)',
            'exps': 'exp(x*((x/lim)**n + 1)**(-1/n))',
            'Dlogs': '(-(log(x)/lim)**n + 1)**(-1 - 1/n)/x',
            'asigmoid': 'x*(-(x/lim)**n + 1)**(-1/n)',
            'Dasigmoid': '(-(x/lim)**n + 1)**(-1 - 1/n)',
            'Dexps': '((x/lim)**n + 1)**(-1 - 1/n)*exp(x*((x/lim)**n + 1)**(-1/n))'
        }[func])
        t_n = time.time() - t
        assert np.allclose(y_g, y_n)
    except ImportError:
        t_n = -1


    print(t_g, t_s, t_n)


if __name__ == '__main__':
    argh.dispatch_command(main)
