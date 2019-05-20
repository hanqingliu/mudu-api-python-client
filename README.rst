========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |version| image:: https://img.shields.io/pypi/v/muduapiclient.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/muduapiclient

.. |commits-since| image:: https://img.shields.io/github/commits-since/hanqingliu/mudu-api-python-client/v0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/hanqingliu/mudu-api-python-client/compare/v0.1...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/muduapiclient.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/muduapiclient

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/muduapiclient.svg
    :alt: Supported versions
    :target: https://pypi.org/project/muduapiclient

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/muduapiclient.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/muduapiclient


.. end-badges

Python api client for mudu youke service.

* Free software: Apache Software License 2.0

Installation
============

::

    pip setup.py install

Documentation
=============


To use the project:

.. code-block:: python

    from muduapiclient.client import MuduApiClient
    api = MuduApiClient('access_key', 'secret_key')
    api.call('POST', 'live|audience|department', 'List|Info|...', kwargs)


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
