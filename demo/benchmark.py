#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

import argh
import numpy as np
import time
import algmoid

def main(func='asigmoid', xlim=200, N=1024*1024):
    n = 8
    ylim = 350
    x = np.linspace(2, xlim, N)

    # general
    t = time.time()
    y_g = getattr(algmoid, func)(x, n, ylim)
    t_g = time.time() - t

    # special
    t = time.time()
    y_s = getattr(algmoid, func+'_8_350')(x)
    t_s = time.time() - t

    assert np.allclose(y_g, y_s)

    print(t_g, t_s)


if __name__ == '__main__':
    argh.dispatch_command(main)
