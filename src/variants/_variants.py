# -*- coding: utf-8 -*-
"""Provides the variant form decorator."""

import types

__all__ = ['variants']


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

    class VariantFunction:
        __doc__ = f.__doc__

        def __call__(self, *args, **kwargs):
            return f(*args, **kwargs)

        def variant(self, func_name):
            """Decorator to add a new variant form to the function."""
            def decorator(vfunc):
                setattr(self.__class__, func_name, staticmethod(vfunc))
                return self

            return decorator

        def __get__(self, instance, owner):
            # This is necessary to bind instance methods
            if instance is None:
                return self

            return types.MethodType(self, instance)

        def __repr__(self):
            return '<VariantFunction {}>'.format(self.__name__)

    f_out = VariantFunction()
    f_out.__name__ = f.__name__

    return f_out
