# plugins/__init__.py
"""
Plugins Initialization

Purpose:
- Ensure plugins import only the SDK
- Prevent direct access to Core modules

Enforcement:
- Raise RuntimeError if a plugin imports Core modules directly
"""

import sys
caller = sys._getframe(1).f_globals.get('__name__')
if caller and caller.startswith('core.'):
    raise RuntimeError('Plugins must not import Core modules directly. Use SDK only.')
