
def classify(lag_seconds: float, max_duration: float) -> str:
    """Toy version of the watchdog verdict."""
    if lag_seconds < 0:
        raise ValueError("lag cannot be negative")
    if lag_seconds < max_duration:
        return "healthy"
    return "down"