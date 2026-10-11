import pytest
from engine.calc import classify

def test_healthy():
    assert classify(5, 600) == "healthy"

def test_down():
    assert classify(900, 600) == "down"

def test_negative_rejected():
    with pytest.raises(ValueError):
        classify(-1, 600)
        
def test_busy_when_inflight_work_is_young():
    assert classify(900, 600, oldest_open_age=120) == "busy"

def test_zero_max_duration_never_healthy_on_zero_lag():
    assert classify(0, 0) == "down"