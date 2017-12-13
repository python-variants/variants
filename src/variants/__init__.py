# -*- coding: utf-8 -*-
from ._variants import primary

try:
    from ._version import version as __version__
except ImportError:
    __version__ = 'unknown'

__all__ = ['primary']
