from __future__ import division

import pytest

try:
    from functools import singledispatch
except ImportError:
    from singledispatch import singledispatch

import variants


###
# Example implementation - single dispatched function
@variants.primary
@singledispatch
def add_one(arg):
    return arg + 1


@add_one.variant('from_list')
@add_one.register(list)
def add_one(arg):
    return arg + [1]


@add_one.variant('from_tuple')
@add_one.register(tuple)
def add_one(arg):
    return arg + (1,)


### Tests
def test_single_dispatch_int():
    assert add_one(1) == 2


def test_single_dispatch_list():
    assert add_one([2]) == [2, 1]


def test_single_dispatch_tuple():
    assert add_one((2,)) == (2, 1)


def test_dispatch_list_variant_succeeds():
    assert add_one.from_list([4]) == [4, 1]


@pytest.mark.parametrize('arg', [3, (2,)])
def test_dispatch_list_variant_fails(arg):
    with pytest.raises(TypeError):
        add_one.from_list(arg)


def test_dispatch_tuple_variant_succeeds():
    assert add_one.from_tuple((2,)) == (2, 1)


@pytest.mark.parametrize('arg', [3, [2]])
def test_dispatch_tuple_variant_fails(arg):
    with pytest.raises(TypeError):
        add_one.from_tuple(arg)
