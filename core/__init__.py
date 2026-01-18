# core/__init__.py
"""
Core Package Initialization

Purpose:
- Control what is exposed publicly
- Hide internal modules from direct external import

Enforcement:
- Only modules explicitly listed in __all__ can be imported externally
"""

__all__ = [
    'sdk',  # SDK is the only public entry point
]
