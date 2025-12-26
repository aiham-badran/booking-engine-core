import pytest

def test_register_and_resolve_context():
    """
    GIVEN a ContextRegistry
    WHEN a Context is registered
    THEN it should be resolvable by its id
    """
    from src.context.context import Context
    from src.context.context_registry import ContextRegistry

    registry = ContextRegistry()
    ctx = Context(context_id="company_1")

    registry.register(ctx)

    resolved = registry.get("company_1")

    assert resolved is ctx


def test_resolving_unknown_context_raises_error():
    """
    GIVEN an empty ContextRegistry
    WHEN resolving a non-existing context
    THEN an error should be raised
    """
    from src.context.context_registry import ContextRegistry

    registry = ContextRegistry()

    with pytest.raises(KeyError):
        registry.get("unknown")
