def fibonacci(n):
    """
    Recursively calculate the nth Fibonacci number.

    The Fibonacci sequence is defined as:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2) for n > 1

    Parameters:
        n (int): The position in the Fibonacci sequence (must be a non-negative integer).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    # Check for invalid (negative) input
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Base case: F(0) = 0
    if n == 0:
        return 0
    # Base case: F(1) = 1
    elif n == 1:
        return 1
    else:
        # Recursive case: F(n) = F(n-1) + F(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))
print(fibonacci(10))