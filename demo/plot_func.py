#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

import argh
import numpy as np
import matplotlib.pyplot as plt

import algmoid

def main(func='asigmoid', n=2, xlim=0.9, ylim=1, output='', show=False, semilogy=False):
    x = np.linspace(-xlim, xlim, 1024)
    y = getattr(algmoid, func)(x, n, ylim)
    plt.plot(x, y)
    if output:
        plt.savefig(output)
    if show:
        plt.show()


if __name__ == '__main__':
    argh.dispatch_command(main)
