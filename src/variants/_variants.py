# -*- coding: utf-8 -*-
"""Provides the variant form decorator."""

import six

import types

__all__ = ['variants']


class _StaticCallableMetaclass(type):
    """Metaclass for a static callable function."""

    def __call__(cls, *args, **kwargs):
        """Rather than calling the constructor, call a static function."""
        return cls.__main_form__(*args, **kwargs)

    def __repr__(cls):
        return cls.__func_repr__()


def variants(f):
    """
    Decorator to register a function that has variant forms.

    Decorate the main form of the function with this decorator, and then
    subsequent variants should be declared with the same name as the original
    function.

    .. example::

        @variants
        def myfunc(fpath):
            with open(fpath, 'r') as f:
                do_something(f.read())

        @myfunc.variant('from_url') as f:
        def myfunc(url):
            r = requests.get(url)
            do_something(r.text)
    """

    @six.add_metaclass(_StaticCallableMetaclass)
    class VariantFunction:
        __doc__ = f.__doc__

        @staticmethod
        def __main_form__(*args, **kwargs):
            return f(*args, **kwargs)

        @classmethod
        def variant(cls, func_name):
            def decorator(vfunc):
                setattr(cls, func_name, vfunc)
                return cls

            return decorator

        @classmethod
        def __func_repr__(cls):
            return '<VariantFunction {}>'.format(cls.__name__)

    VariantFunction.__name__ = f.__name__

    return VariantFunction
