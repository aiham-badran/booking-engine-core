# core/domain/__init__.py
"""
Domain Layer Initialization

Purpose:
- Mark domain modules as Internal Only
- Ensure Core business entities are not accessed externally

Enforcement:
- Raise RuntimeError if imported outside SDK
"""

import sys
caller = sys._getframe(1).f_globals.get('__name__')
if caller and not caller.startswith('core.sdk'):
    raise RuntimeError('Direct import of domain modules is prohibited. Use SDK only.')

__all__ = []  # Internal only
