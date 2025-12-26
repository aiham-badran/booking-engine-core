def test_request_flow_executes_with_valid_context():
    """
    GIVEN a registered Context
    WHEN a request is executed with a valid context_id
    THEN the operation should execute successfully
    """
    from src.context.context import Context
    from src.context.context_registry import ContextRegistry
    from src.core.engine import CoreEngine

    registry = ContextRegistry()
    ctx = Context(context_id="company_1")
    registry.register(ctx)

    engine = CoreEngine(context_registry=registry)

    def dummy_operation(context):
        return context.context_id

    result = engine.execute(
        context_id="company_1",
        operation=dummy_operation
    )

    assert result == "company_1"
