#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from distutils.core import setup

name_ = 'algmoid'
version_ = '0.0.1'

if '--help'in sys.argv[1:] or sys.argv[1] in (
        '--help-commands', 'egg_info', 'clean', '--version'):
    cmdclass_ = {}
    ext_modules_ = []
else:
    import numpy
    from pycompilation.dist import clever_build_ext
    from pycompilation.dist import CleverExtension
    subsd =  { # ('sigmoid',),
        'FUNCS': 'sigmoid Dsigmoid D2sigmoid asigmoid Dasigmoid exps Dexps logs Dlogs'.split(),
    }
    cmdclass_ = {'build_ext': clever_build_ext}
    def _render(build_temp, full_ext_path, ext, tmpl, out):
        print(build_temp)
        print(full_ext_path)
        from pycompilation.util import render_mako_template_to
        render_mako_template_to(tmpl, out, subsd)

    ext_modules_ = [
        CleverExtension(
            name_+"._algmoid"+mod,
            sources=[name_+'/_algmoid'+mod+'_template.pyx'],
            language='c++',
            include_dirs=['./include', numpy.get_include()],
            template_regexps=[
                (r'^(\w+)_template.(\w+)$', r'\1.\2', subsd),
            ],
            pycompilation_compile_kwargs={
                'std': 'c++0x',
            },
            pycompilation_link_kwargs={
                'libs': ['m']
            },
            build_callbacks=[
                (_render, ('./include/algmoid'+mod+'_template.h',
                           './include/algmoid'+mod+'.h'), {}),
                (_render, ('./include/algmoid'+mod+'_template.pxd',
                           './include/algmoid'+mod+'.pxd'), {}),
            ],
            logger=True,
        ) for mod in ('', '_8_350')
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
