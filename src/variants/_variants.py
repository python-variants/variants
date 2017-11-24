# -*- coding: utf-8 -*-
"""Provides the variant form decorator."""

import functools

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

        def __init__(self):
            self._variants = set()

        def __call__(self, *args, **kwargs):
            return f(*args, **kwargs)

        def _add_variant(self, var_name, vfunc):
            self._variants.add(var_name)
            setattr(self, var_name, vfunc)

        def variant(self, func_name):
            """Decorator to add a new variant form to the function."""
            def decorator(vfunc):
                self._add_variant(func_name, vfunc)

                return self

            return decorator

        def __get__(self, instance, owner):
            # This is necessary to bind instance methods
            if instance is not None:
                return VariantMethod(self, instance)

            return self

        def __repr__(self):
            return '<{} {}>'.format(self.__class__.__name__, self.__name__)

    class VariantMethod(VariantFunction):
        def __init__(self, variant_func, instance):
            self.__instance = instance
            self.__name__ = variant_func.__name__

            # Convert existing variants to methods
            for vname in variant_func._variants:
                vfunc = getattr(variant_func, vname)
                vmethod = self._as_bound_method(vfunc)

                setattr(self, vname, vmethod)

        def __call__(self, *args, **kwargs):
            return f(self.__instance, *args, **kwargs)

        def _as_bound_method(self, vfunc):
            @functools.wraps(vfunc)
            def bound_method(*args, **kwargs):
                return vfunc(self.__instance, *args, **kwargs)

            return bound_method

        def _add_variant(self, var_name, vfunc):
            self._variants.add(var_name)
            setattr(self, var_name, self._as_bound_method(vfunc))

    f_out = VariantFunction()
    f_out.__name__ = f.__name__

    return f_out
