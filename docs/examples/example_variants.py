import variants


@variants.primary
def primary_func(x, y):
    """
    This is the primary function. Its docstring should be shown under the
    primary function documentation.
    """


@primary_func.variant('variant_1')
def primary_func(x):
    """This is variant_1, it only takes one argument."""


@primary_func.variant('variant_2')
def primary_func(x, y, z):
    """This is variant_2, it takes three arguments."""


class VariantMethodsClass(object):
    @variants.primary
    def primary_method(self, x, y):
        """
        This is the primary method, its docstring should be shown under the
        primary method documentation.
        """

    @primary_method.variant('variant_1')
    def primary_method(self, x):
        """This is variant_1, it takes one argument."""
