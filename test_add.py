# tests using pytest

from add import add_numbers


def test_add_integers():
    assert add_numbers(2, 3) == 5  # nosec B101


def test_add_strings_raises_error():
    try:
        add_numbers("a", "b")
    except ValueError:
        pass  # Expected error
    else:
        raise AssertionError("Should raise ValueError")
