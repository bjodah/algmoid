# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import numpy as np
import sympy

from algmoid import sigmoid, Dsigmoid, asigmoid, Dasigmoid
from algmoid._algmoid import sigmoid_8_350


def _get_sigm(x, n, lim):
    return x/((x/lim)**n+1)**(1/n)


def _get_asigm(x, n, lim):
    return x/(1-(x/lim)**n)**(1/n)


symbs = x, n, lim = sympy.symbols('x n lim')


assert (_get_asigm(_get_sigm(*symbs), n, lim).subs(
    dict(zip(symbs, map(sympy.S, [3, 5, 13]))))).simplify() == 3


ref = {
    'sigmoid': _get_sigm(x, n, lim),
    'Dsigmoid': _get_sigm(x, n, lim).diff(x).simplify(),
    'asigmoid': _get_asigm(x, n, lim),
    'Dasigmoid': _get_asigm(x, n, lim).diff(x).simplify(),
}


def check(cb, vals):
    return abs(cb(*vals) - ref[cb.__name__].subs(dict(zip(symbs, vals)))) < 1e-15


def test_sigmoid():
    assert abs(5 - sigmoid(5, n=2, lim=350)) < 1e-3
    assert abs(5 - sigmoid(5, n=4, lim=350)) < 1e-7
    assert abs(9 - sigmoid(9, n=6, lim=350)) < 1e-9
    assert abs(5 + sigmoid(-5, n=2, lim=350)) < 1e-3
    assert abs(5 + sigmoid(-5, n=4, lim=350)) < 1e-7
    assert abs(9 + sigmoid(-9, n=6, lim=350)) < 1e-9
    assert np.allclose(sigmoid(np.array(
        [-9, -5, 5, 9]), n=6, lim=350), [-9, -5, 5, 9], atol=1e-7)
    assert check(sigmoid, [13, 7, 11])


def test_Dsigmoid():
    assert check(Dsigmoid, [13, 7, 11])


def test_asigmoid():
    assert check(asigmoid, [5, 7, 11])
    assert abs(asigmoid(sigmoid(5, 7, 11), 7, 11) - 5) < 1e-15


def test_Dasigmoid():
    assert check(Dasigmoid, [5, 7, 11])



def test_sigmoid_8_350():
    assert abs(5 - sigmoid_8_350(5)) < 1e-3
    assert abs(5 - sigmoid_8_350(5)) < 1e-7
    assert abs(9 - sigmoid_8_350(9)) < 1e-9
    assert abs(5 + sigmoid_8_350(-5)) < 1e-3
    assert abs(5 + sigmoid_8_350(-5)) < 1e-7
    assert abs(9 + sigmoid_8_350(-9)) < 1e-9
    assert np.allclose(sigmoid_8_350(np.array(
        [-9, -5, 5, 9])), [-9, -5, 5, 9], atol=1e-7)


if __name__ == '__main__':
    print('\n'.join([k+': '+sympy.latex(v) for k,v in ref.items()]))
