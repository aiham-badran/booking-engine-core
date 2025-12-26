import pytest

def test_context_can_be_created_with_valid_id():
    """
    GIVEN a valid context identifier
    WHEN a Context is created
    THEN the Context should store the identifier
    """
    from src.context.context import Context

    ctx = Context(context_id="company_1")

    assert ctx.context_id == "company_1"


def test_context_id_cannot_be_empty():
    """
    GIVEN an empty context identifier
    WHEN a Context is created
    THEN an error should be raised
    """
    from src.context.context import Context

    with pytest.raises(ValueError):
        Context(context_id="")
