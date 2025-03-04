import pytest
from a import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_add_type_error():
    with pytest.raises(TypeError):
        add(2, "3")  # Mixing int and str should raise an error
