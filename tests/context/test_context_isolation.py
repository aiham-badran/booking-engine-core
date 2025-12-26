def test_multiple_contexts_are_isolated():
    """
    GIVEN multiple Contexts
    WHEN they are registered
    THEN each Context should be independent
    """
    from src.context.context import Context
    from src.context.context_registry import ContextRegistry

    registry = ContextRegistry()

    ctx1 = Context(context_id="company_1")
    ctx2 = Context(context_id="company_2")

    registry.register(ctx1)
    registry.register(ctx2)

    assert registry.get("company_1") is not registry.get("company_2")
