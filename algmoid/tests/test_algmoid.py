# -*- coding: utf-8 -*-

import numpy as np

from algmoid import sigmoid

def test_sigmoid():
    assert abs(5 - sigmoid(5, n=2, lim=350)) < 1e-3
    assert abs(5 - sigmoid(5, n=4, lim=350)) < 1e-7
    assert abs(9 - sigmoid(9, n=6, lim=350)) < 1e-9
    assert abs(5 + sigmoid(-5, n=2, lim=350)) < 1e-3
    assert abs(5 + sigmoid(-5, n=4, lim=350)) < 1e-7
    assert abs(9 + sigmoid(-9, n=6, lim=350)) < 1e-9
    assert np.allclose(sigmoid(np.array(
        [-9, -5, 5, 9]), n=6, lim=350), [-9, -5, 5, 9], atol=1e-7)

from algmoid._algmoid_8_350 import sigmoid as sigmoid_8_350

def test_sigmoid_8_350():
    assert abs(5 - sigmoid_8_350(5)) < 1e-3
    assert abs(5 - sigmoid_8_350(5)) < 1e-7
    assert abs(9 - sigmoid_8_350(9)) < 1e-9
    assert abs(5 + sigmoid_8_350(-5)) < 1e-3
    assert abs(5 + sigmoid_8_350(-5)) < 1e-7
    assert abs(9 + sigmoid_8_350(-9)) < 1e-9
    assert np.allclose(sigmoid_8_350(np.array(
        [-9, -5, 5, 9])), [-9, -5, 5, 9], atol=1e-7)
