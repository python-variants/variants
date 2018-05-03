# -*- coding: utf-8 -*-

from variants import primary
from variants import inspect as vinsp

import pytest

###
# Setup functions
@primary
def prim_func():
    """Example primary function"""


@prim_func.variant('alt')
def prim_func():
    """Example alternate function"""


@prim_func.variant('prim_group')
@primary
def prim_func():
    """Nested variant functions"""


@prim_func.prim_group.variant('alt2')
def _():
    """Nested alternate function"""


def rfunc():
    """Arbitrary function"""


class SomeClass(object):
    @primary
    def prim_method(self):
        """Example of a primary method"""

    @prim_method.variant('alt')
    def prim_method(self):
        """Example of a method alternate"""


some_instance = SomeClass()


###
# Tests
@pytest.mark.parametrize('f,exp', [
    (prim_func, True),
    (rfunc, False),
    (prim_func.alt, False),
    (prim_func.prim_group, True),
    (prim_func.prim_group.alt2, False),
    (SomeClass.prim_method, True),
    (some_instance.prim_method, True),
    (SomeClass.prim_method.alt, False),
    (some_instance.prim_method.alt, False),
])
def test_is_primary(f, exp):
    assert vinsp.is_primary(f) == exp


@pytest.mark.parametrize('f,exp', [
    (SomeClass.prim_method, False),
    (some_instance.prim_method, True),
    (SomeClass.prim_method.alt, False),
    (some_instance.prim_method.alt, False),
    (prim_func, False),
    (rfunc, False),
    (prim_func.alt, False),
    (prim_func.prim_group, False),
    (prim_func.prim_group.alt2, False),
])
def test_is_primary_method(f, exp):
    assert vinsp.is_primary_method(f) == exp
