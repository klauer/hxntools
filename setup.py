from __future__ import (absolute_import, division, print_function)

import sys
import warnings


try:
    from setuptools import setup
except ImportError:
    try:
        from setuptools.core import setup
    except ImportError:
        from distutils.core import setup

from distutils.core import setup

setup(
    name='hxntools',
    version="0.0.1",
    author='Brookhaven National Laboratory',
    packages=['hxntools', 'hxntools.detectors'],
    install_requires=['numpy>=1.8',
                      'h5py>=2.5.0', 'filestore>=0.0.4'],

)
