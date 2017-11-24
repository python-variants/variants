from __future__ import division

import math

from variants import variants

from ._division_data import DivisionData

import pytest


###
# Example implementation - division function
@variants
def divide(x, y):
    """A function that divides x by y."""
    return x / y


@divide.variant('round')
def divide(x, y):
    """A version of divide that also rounds."""
    return round(x / y)


@divide.variant('round_callmain')
def divide(x, y):
    return round(divide(x, y))


@divide.variant('floor')
def divide(x, y):
    return math.floor(divide(x, y))


@divide.variant('ceil')
def divide(x, y):
    return math.ceil(divide(x, y))


@divide.variant('mode')
def divide(x, y, mode=None):
    funcs = {
        None: divide,
        'round': divide.round,
        'floor': divide.floor,
        'ceil': divide.ceil
    }

    return funcs[mode](x, y)

###
# Division Function Tests
@pytest.mark.parametrize('x, y, expected', DivisionData.DIV_VALS)
def test_main(x, y, expected):
    assert divide(x, y) == expected


@pytest.mark.parametrize('x,y,expected', DivisionData.ROUND_VALS)
def test_round(x, y, expected):
    assert divide.round(x, y) == expected


@pytest.mark.parametrize('x,y,expected', DivisionData.ROUND_VALS)
def test_round_callmain(x, y, expected):
    assert divide.round_callmain(x, y) == expected


@pytest.mark.parametrize('x,y,expected', DivisionData.FLOOR_VALS)
def test_floor(x, y, expected):
    assert divide.floor(x, y) == expected


@pytest.mark.parametrize('x,y,expected', DivisionData.CEIL_VALS)
def test_ceil(x, y, expected):
    assert divide.ceil(x, y) == expected


@pytest.mark.parametrize('x,y,expected,mode', DivisionData.MODE_VALS)
def test_mode(x, y, expected, mode):
    assert divide.mode(x, y, mode) == expected


###
# Division function metadata tests
def test_name():
    assert divide.__name__ == 'divide'


def test_docstring():
    assert divide.__doc__ == """A function that divides x by y."""


def test_repr():
    assert repr(divide) == '<VariantFunction divide>'
