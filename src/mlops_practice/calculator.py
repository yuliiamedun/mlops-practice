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


def divide(a: int, b: int) -> float:
    """Divide one number by another.

    Args:
        a: The dividend (number to be divided).
        b: The divisor (number to divide by).

    Returns:
        The division of a and b.

    Example:
        >>> divide(1, 2)
        0.5
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
