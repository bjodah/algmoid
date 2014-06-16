# -*- coding: utf-8 -*-

import numpy as np

# from algmoid import sigmoid
from algmoid._algmoid_8_350 import sigmoid

# def test_sigmoid():
#     assert abs(5 - sigmoid(5, n=2)) < 1e-3
#     assert abs(5 - sigmoid(5, n=4)) < 1e-7
#     assert abs(9 - sigmoid(9, n=6)) < 1e-9
#     assert abs(5 + sigmoid(-5, n=2)) < 1e-3
#     assert abs(5 + sigmoid(-5, n=4)) < 1e-7
#     assert abs(9 + sigmoid(-9, n=6)) < 1e-9
#     assert np.allclose(sigmoid(np.array(
#         [-9, -5, 5, 9]), n=6), [-9, -5, 5, 9], atol=1e-7)

def test_sigmoid():
    assert abs(5 - sigmoid(5)) < 1e-3
    assert abs(5 - sigmoid(5)) < 1e-7
    assert abs(9 - sigmoid(9)) < 1e-9
    assert abs(5 + sigmoid(-5)) < 1e-3
    assert abs(5 + sigmoid(-5)) < 1e-7
    assert abs(9 + sigmoid(-9)) < 1e-9
    assert np.allclose(sigmoid(np.array(
        [-9, -5, 5, 9])), [-9, -5, 5, 9], atol=1e-7)
