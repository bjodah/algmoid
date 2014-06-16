=======
algmoid
=======
.. image:: https://travis-ci.org/bjodah/algmoid.png?branch=master
   :target: https://travis-ci.org/bjodah/algmoid

"algmoid" is a C++11 implementation (including native Python_ bindings) 
of algebraic sigmoidal_ functions of form:

```
    s(x) := x*((x/lim)**n + 1)**(-1/n)
```

Feel free to enhance modify and make pull request at github to the algmoid_ repository.

.. _Python: https://www.python.org
.. _Cython: http://cython.org
.. _algmoid: https://github.com/bjodah/algmoid
.. _sigmoidal: http://en.wikipedia.org/wiki/Sigmoid_function



Installation
============
See dependencies and make sure that manual dependencies are satisfied.

Example using pip (modify to your own needs):
    1. ``pip install --user --upgrade -r https://raw.github.com/bjodah/algmoid/v0.0.1/requirements.txt``
    2. ``pip install --user --upgrade https://github.com/bjodah/algmoid/archive/v0.0.1.tar.gz``

Manual installation:
    1. Clone repository ``git clone https://github.com/bjodah/algmoid.git``
    2. Install dependencies ``cd algmoid; pip install --user --upgrade -r requirements.txt``
    3. To install run ``python setup.py install --user`` or ``sudo python setup.py install``.

See distutils documentation_ for more options.

.. _documentation: http://docs.python.org/2/library/distutils.html

Note that the behaviour of ``setup(...)`` is modified slightly through the use of "CleverExtension" from pycompilation_.


Tests
=====
To run the full test suite, you need to build the python
bindings. (see Dependencies)
1. ``python setup.py build_ext --inplace``
2. ``py.test``


Dependencies
============
You need a C++ compiler supporting C++11 (-std=c++0x)
On a debian based linux system you can install it easily
by typing: ``sudo apt-get install g++``

Optional dependencies (for Python bindings):

- Python header files (sudo apt-get install python-dev)
- Python_ (tested with 2.7)
- NumPy_ 
- Cython_
- pycompilation_ (optional: enables use from python)
- pytest_ (sudo apt-get install python-pytest)

See requirements.txt for detailed information of versions tested for.

For all dependencies the following command may be issued on a debian
based system:
``sudo apt-get install g++ python2.7 libpython2.7-dev
python-numpy cython python-pip python-pytest; sudo
pip install --upgrade -r https://raw.github.com/bjodah/algmoid/v0.0.1/requirements.txt``

.. _NumPy: http://www.numpy.org/
.. _pycompilation: https://github.com/bjodah/pycompilation
.. _pytest: http://pytest.org/


License
=======
Open Source. Released under the very permissive "simplified
(2-clause) BSD license". See LICENSE.txt for further details.


Authors
=======
Björn Dahlgren. 

TODO
====
Write proper documentation.
