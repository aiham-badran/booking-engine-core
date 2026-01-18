# core/application/__init__.py
"""
Application Layer Initialization

Purpose:
- Mark application modules as Internal Only
- Provide clear guidance for developers

Enforcement:
- Raise RuntimeError if imported directly outside SDK
"""

import sys

caller = sys._getframe(1).f_globals.get('__name__')
if caller and not caller.startswith('core.sdk'):
    raise RuntimeError('Direct import of application modules is prohibited. Use SDK only.')

__all__ = []  # Internal only, no public exports
