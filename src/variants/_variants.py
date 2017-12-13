# -*- coding: utf-8 -*-
"""Provides the variant form decorator."""

import functools

__all__ = ['primary']


VARIANT_WRAPPED_ATTRIBUTES = (
    '__module__', '__name__', '__doc__', '__qualname__', '__annotations__'
)


def variant_wraps(vfunc, wrapped_attributes=VARIANT_WRAPPED_ATTRIBUTES):
    """Update the variant function wrapper a la ``functools.wraps``."""
    f = vfunc.__main_form__

    class SentinelObject:
        """A unique sentinel that is not None."""

    sentinel = SentinelObject()

    for attr in wrapped_attributes:
        attr_val = getattr(f, attr, sentinel)
        if attr is not sentinel:
            setattr(vfunc, attr, attr_val)

    return vfunc


class VariantFunction(object):
    """Wrapper class for functions with variant forms."""

    def __init__(self, primary_func):
        self._variants = set()
        self.__main_form__ = primary_func

    def __call__(self, *args, **kwargs):
        return self.__main_form__(*args, **kwargs)

    def __getattr__(self, key):
        return getattr(self.__main_form__, key)

    def _add_variant(self, var_name, vfunc):
        self._variants.add(var_name)
        setattr(self, var_name, vfunc)

    def variant(self, func_name):
        """Decorator to add a new variant form to the function."""
        def decorator(vfunc):
            self._add_variant(func_name, vfunc)

            return self

        return decorator

    def __get__(self, obj, objtype=None):
        # This is necessary to bind instance methods
        if obj is not None:
            rv = VariantMethod(self, obj)
            return variant_wraps(rv)

        return self

    def __repr__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.__name__)


class VariantMethod(VariantFunction):
    """Wrapper class for methods with variant forms."""

    def __init__(self, variant_func, instance):
        self.__instance = instance

        # Convert existing variants to methods
        for vname in variant_func._variants:
            vfunc = getattr(variant_func, vname)
            vmethod = self._as_bound_method(vfunc)

            setattr(self, vname, vmethod)

        self.__main_form__ = self._as_bound_method(variant_func.__main_form__)

    def _as_bound_method(self, vfunc):
        @functools.wraps(vfunc)
        def bound_method(*args, **kwargs):
            return vfunc(self.__instance, *args, **kwargs)

        return bound_method

    def _add_variant(self, var_name, vfunc):
        self._variants.add(var_name)
        setattr(self, var_name, self._as_bound_method(vfunc))


def primary(f):
    """
    Decorator to register a function that has variant forms.

    Decorate the main form of the function with this decorator, and then
    subsequent variants should be declared with the same name as the original
    function [#]_:

    .. code-block:: python

        import variants

        @variants.primary
        def myfunc(fpath):
            with open(fpath, 'r') as f:
                do_something(f.read())

        @myfunc.variant('from_url') as f:
        def myfunc(url):
            r = requests.get(url)
            do_something(r.text)

    The ``primary`` decorator returns an object that attempts to transparently
    proxy the original methods of the original callable, but variants added to
    the primary function will shadow the original methods and attributes. Other
    than this, any valid python identifier is a valid name for a variant.

    .. [#] Declaring subsequent variants with the same name as the original
        function is a stylistic convention, not a requirement. Decorating
        any function with the ``.variant`` decorator will mutate the primary
        function object, no matter the name of the variant function. However,
        whatever function you use for the variant function declaration will
        become an alias for the primary function.
    """
    f_out = variant_wraps(VariantFunction(f))

    return f_out
