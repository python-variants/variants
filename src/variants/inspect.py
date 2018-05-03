# -*- coding: utf-8 -*-
"""
Provides inspection tools for extracting metadata from function groups.
"""
from ._variants import VariantFunction, VariantMethod

if False:   # pragma: nocover
    from typing import Any      # NOQA


def is_primary(f):
    # type: (Any) -> bool
    """
    Detect if a function is a primary function in a variant group
    """
    return isinstance(f, (VariantFunction, VariantMethod))


def is_primary_method(f):
    # type: (Any) -> bool
    """
    Detect if a function is a primary method in a variant group
    """
    return isinstance(f, VariantMethod)

