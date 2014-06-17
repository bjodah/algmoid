#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import

import argh
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

import algmoid

def main(xlim=1, ylim=1, output='', show=False, semilogy=False):
    x = np.linspace(-xlim, xlim)
    plt.figure(figsize=(20, 8))
    ns = np.array(range(2,10+1, 2))
    y, e = {}, {}
    for i, n in enumerate(ns):
        y[n] = algmoid.sigmoid(x, n, ylim)
        e[n] = (x-y[n])/x
        plt.subplot(1, 3, 1)
        plt.plot(x, y[n], label=(
            r'$\frac{x}{\sqrt[%d]{\left( \frac{x}{%d} \right) ^{%d}+1}}$'
            ) % (n, ylim, n))
        plt.subplot(1, 3, 2)
        {True: plt.semilogy, False: plt.plot}[semilogy](x, e[n], label=(
            r'$\frac{x}{\sqrt[%d]{\left( \frac{x}{%d} \right) ^{%d}+1}}$'
        ) % (n, ylim, n))

    for i in range(2):
        plt.subplot(1, 3, i+1)
        plt.xlabel('x')
        plt.ylabel(('y', '(x-y)/y')[i])
        plt.legend(loc='best', prop={'size': 22})

    plt.subplot(1, 3, 3)
    e_n = [interp1d(x, e[n])(-xlim/2) for n in ns]
    p = np.polyfit(ns, np.log(e_n), 1)
    plt.semilogy(ns, e_n, 'd')
    rele = (((xlim/2)/ylim)**ns+1)**(1/ns)-1
    plt.semilogy(ns, rele, ':',
                 label=r'$^{n}\sqrt{\left(\frac{%3.1f}{%d}\right)^n+1} - 1$' % (xlim/2, ylim))
    plt.semilogy(ns, np.exp(np.polyval(p, ns)),
                 '--', label='$dE/dn = E_0 10 ^{%4.2f n}$' % (p[0]/np.log(10)))
    plt.ylabel(r'$(x-y)/y|_{x=%f}$' % (-xlim/2))
    plt.xlabel('n')
    plt.legend(loc='best', prop={'size': 18})
    plt.tight_layout()

    if output:
        plt.savefig(output)
    if show:
        plt.show()

if __name__ == '__main__':
    argh.dispatch_command(main)
