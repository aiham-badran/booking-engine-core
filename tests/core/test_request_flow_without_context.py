import pytest

def test_request_flow_fails_without_context():
    """
    GIVEN an empty ContextRegistry
    WHEN executing a request with unknown context_id
    THEN an error should be raised
    """
    from src.context.context_registry import ContextRegistry
    from src.core.engine import CoreEngine

    registry = ContextRegistry()
    engine = CoreEngine(context_registry=registry)

    def dummy_operation(context):
        return True

    with pytest.raises(KeyError):
        engine.execute(
            context_id="unknown",
            operation=dummy_operation
        )
