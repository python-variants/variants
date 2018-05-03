import variants


@variants.primary
def primary_func(x, y):
    """
    This is the primary function. Its docstring should be shown under the
    primary function documentation.
    """


@primary_func.variant('onearg')
def primary_func(x):
    """This is the ``onearg`` variant, it only takes one argument."""


@primary_func.variant('threearg')
def primary_func(x, y, z):
    """This is the ``threearg`` variant, it takes three arguments."""


class VariantMethodsClass(object):
    @variants.primary
    def primary_method(self, x, y):
        """
        This is the primary method, its docstring should be shown under the
        primary method documentation.
        """

    @primary_method.variant('onearg')
    def primary_method(self, x):
        """This is the ``onearg`` variant, it takes one argument."""

    def normal_method(self, a, b):
        """This is a normal method, it has no variants"""
