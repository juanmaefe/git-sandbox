def classify(lag_seconds: float, max_duration: float,
             oldest_open_age: float | None = None) -> str:
    """Toy version of the watchdog verdict."""
    if lag_seconds < 0:
        raise ValueError("lag cannot be negative")
    if max_duration > 0 and lag_seconds < max_duration:
        return "healthy"
    if oldest_open_age is not None and oldest_open_age < max_duration:
        return "busy"
    return "down"