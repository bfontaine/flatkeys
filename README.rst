========
flatkeys
========

.. image:: https://img.shields.io/travis/bfontaine/flatkeys.png
   :target: https://travis-ci.org/bfontaine/flatkeys
   :alt: Build status

.. image:: https://coveralls.io/repos/bfontaine/flatkeys/badge.png?branch=master
   :target: https://coveralls.io/r/bfontaine/flatkeys?branch=master
   :alt: Coverage status

.. image:: https://img.shields.io/pypi/v/flatkeys.png
   :target: https://pypi.python.org/pypi/flatkeys
   :alt: Pypi package

.. image:: https://img.shields.io/pypi/dm/flatkeys.png
   :target: https://pypi.python.org/pypi/flatkeys

``flatkeys`` is a dictionary flattening library for Python.

Install
-------

.. code-block::

    [sudo] pip install flatkeys

The library works with both Python 2.x and 3.x.

Usage
-----

.. code-block::

    >>> from flatkeys import flatkeys
    >>> flatkeys({})
    {}
    >> flatkeys({1: {2: {3: "yolo"}}})
    {"1.2.3": "yolo"}
