=====================
Documentation example
=====================

Using the `sphinx_autodoc_variants <https://github.com/python-variants/sphinx_autodoc_variants>`_ extension, primary and variant functions can be grouped together as a single function group.

Functions
---------

With the ``sphinx_autodoc_variants`` extension enabled in ``conf.py``, function groups at the module level will automatically be grouped together by the ``automodule`` directive. To explicitly document a function group, use the ``autoprimary_function`` directive:

.. code-block:: rst

    .. autoprimary_function:: examples.example_variants.primary_func
        :members:

Which generates:

.. autoprimary_function:: examples.example_variants.primary_func
    :members:
    :noindex:


Methods
-------
For a class containing function group methods, the ``autoclass`` directive works, so:

.. code-block:: rst

    .. autoclass:: examples.example_variants.VariantMethodsClass
        :members:

Resulting in:

.. autoclass:: examples.example_variants.VariantMethodsClass
    :members:
    :noindex:


As with functions, individual method groups can be documented using the ``autoprimary_method`` directive:

.. code-block:: rst

    .. autoprimary_method:: examples.example_variants.VariantMethodsClass.primary_method
        :members:

Which generates:

.. autoprimary_method:: examples.example_variants.VariantMethodsClass.primary_method
    :members:


.. .. automodule:: examples.example_variants
..    :members:
..    :undoc-members:
