#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from distutils.core import setup

name_ = 'algmoid'
version_ = '0.0.2'

if '--help'in sys.argv[1:] or sys.argv[1] in (
        '--help-commands', 'egg_info', 'clean', '--version'):
    cmdclass_ = {}
    ext_modules_ = []
else:
    import numpy
    from pycodeexport.dist import pce_build_ext, PCEExtension
    subsd =  {
        'FUNCS': 'sigmoid Dsigmoid D2sigmoid asigmoid Dasigmoid exps Dexps logs Dlogs'.split(),
    }
    cmdclass_ = {'build_ext': pce_build_ext}
    def _render(build_temp, full_ext_path, ext, tmpl, out):
        from pycodeexport.util import render_mako_template_to
        render_mako_template_to(tmpl, out, subsd)

    ext_modules_ = [
        PCEExtension(
            name_+"._algmoid",
            sources=[name_+'/_algmoid_template.pyx'],
            language='c++',
            include_dirs=['./include', numpy.get_include()],
            template_regexps=[
                (r'^(\w+)_template.(\w+)$', r'\1.\2', subsd),
            ],
            pycompilation_compile_kwargs={
                'std': 'c++0x',
                'options': ['pic', 'warn', 'fast']
            },
            pycompilation_link_kwargs={
                'libs': ['m']
            },
            build_callbacks=[
                (_render, ('./include/algmoid_template.h',
                           './include/algmoid.h'), {}),
                (_render, ('./include/algmoid_template.pxd',
                           './include/algmoid.pxd'), {}),
            ],
            logger=True,
        )
    ]


classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: C++",
    "Programming Language :: Cython",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Mathematics",
]

setup(
    name=name_,
    version=version_,
    author='Björn Dahlgren',
    author_email='bjodah@DELETEMEgmail.com',
    description="Algebraic sigmoidal functions and damped exp/log",
    license = "BSD",
    url='https://github.com/bjodah/'+name_.lower(),
    download_url='https://github.com/bjodah/'+name_.lower()+'/archive/v'+version_+'.tar.gz',
    packages = [name_],
    ext_modules=ext_modules_,
    cmdclass = cmdclass_,
)
