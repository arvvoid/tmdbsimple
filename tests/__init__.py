# -*- coding: utf-8 -*-

"""
__init__.py
~~~~~~~~~~~

This test suite checks the methods of tmdbsimple.

Use the following command to run all the tests:
    python -W ignore:ResourceWarning -m unittest discover tests

:copyright: (c) 2013-2025 by Celia Oakley.
:license: GPLv3, see LICENSE for more details.
"""

"""
Either place your API_KEY in the following constant:
"""
API_KEY = ''

"""
or include it in a keys.py file.
"""
try:
    from .keys import API_KEY, USERNAME, PASSWORD, SESSION_ID
except ImportError:
    pass

__all__ = ['API_KEY', 'USERNAME', 'PASSWORD', 'SESSION_ID']
