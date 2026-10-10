import pytest
from engine.calc import classify

def test_healthy():
    assert classify(5, 600) == "healthy"

def test_down():
    assert classify(900, 600) == "down"

def test_negative_rejected():
    with pytest.raises(ValueError):
        classify(-1, 600)