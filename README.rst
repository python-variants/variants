========
variants
========


.. image:: https://img.shields.io/pypi/v/variants.svg
        :target: https://pypi.python.org/pypi/variants

.. image:: https://img.shields.io/travis/python-variants/variants.svg
        :target: https://travis-ci.org/python-variants/variants

.. image:: https://readthedocs.org/projects/variants/badge/?version=latest
        :target: https://variants.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

``variants`` is a library that provides syntactic sugar for creating alternate forms of functions and other callables, in the same way that alternate constructors are class methods that provide alternate forms of the constructor function.

To create a function with variants, simply decorate the primary form with ``@variants.primary``, which then adds the ``.variant`` decorator to the original function, which can be used to register new variants. Here is a simple example of a function that prints text, with variants that specify the source of the text to print:

.. code-block:: python

    import variants

    @variants.primary
    def print_text(txt):
        print(txt)

    @print_text.variant('from_file')
    def print_text(fobj):
        print_text(fobj.read())

    @print_text.variant('from_filepath')
    def print_text(fpath):
        with open(fpath, 'r') as f:
            print_text.from_file(f)

    @print_text.variant('from_url')
    def print_text(url):
        import requests
        r = requests.get(url)
        print_text(r.text)


``print_text`` and its variants can be used as such:

.. code-block:: python

    print_text('Hello, world!')                 # Hello, world!

    # Create a text file
    with open('hello_world.txt', 'w') as f:
        f.write('Hello, world (from file)')

    # Print from an open file object
    with open('hello_world.txt', 'r') as f:
        print_text.from_file(f)                 # Hello, world (from file)

    # Print from the path to a file object
    print_text.from_filepath('hello_world.txt') # Hello, world (from file)

    # Print from a URL
    hw_url = 'https://ganssle.io/files/hello_world.txt'
    print_text.from_url(hw_url)                 # Hello, world! (from url)


Differences from singledispatch
-------------------------------

While ``variants`` and |singledispatch|_ are both intended to provide alternative implementations
to a primary function, the overall aims are slightly different. ``singledispatch`` transparently
dispatches to variant functions based on the *type* of the argument, whereas ``variants`` provides
*explicit* alternative forms of the function. Note that in the above example, both
``print_text.from_filepath`` and ``print_text.from_url`` take a string, one representing a file
path and one representing a URL.

Additionally, the ``variants`` is compatible with ``singledispatch``, so you can have the best of
both worlds; an example that uses both:


.. code-block:: python

    @variants.primary
    @singledispatch
    def add(x, y):
        return x + y

    @add.variant('from_list')
    @add.register(list)
    def add(x, y):
        return x + [y]

Which then automatically dispatches between named variants based on type:

.. code-block:: python

    >>> add(1, 2)
    3
    >>> add([1], 2)
    [1, 2]

But also exposes the explicit variant functions:

.. code-block:: python

    >>> add.from_list([1], 2)
    [1, 2]
    >>> add.from_list()
          7 @add.register(list)
          8 def add(x, y):
    ----> 9     return x + [y]

    TypeError: unsupported operand type(s) for +: 'int' and 'list'

It is important to note that the ``variants`` decorators **must be the outer decorators**.


Installation
------------

To install variants, run this command in your terminal:

.. code-block:: console

    $ pip install variants


Requirements
------------

This is a library for Python, with support for versions 2.7 and 3.4+.

.. |singledispatch| replace:: ``singledispatch``
.. _singledispatch: https://docs.python.org/3/library/functools.html#functools.singledispatch

