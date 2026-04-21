def add(a: int, b: int) -> int:
    """Add two numbers together.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The sum of a and b.

    Example:
        >>> add(1, 2)
        3
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Expected numbers, got {type(a)} and {type(b)}")
    return a + b
