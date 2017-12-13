"""
Example module with function variants
"""

from variants import primary

@primary
def func():
    """This is the primary variant"""

@func.variant('alternate')
def func():
    """This is an alternate function"""


def non_variant_func():
    """This is a function that is NOT a variant"""
