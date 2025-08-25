def factorial(n):
    """
    Calculate the factorial of a number.
    Args:
        n (int): The number to calculate factorial for    
    Returns:
        int: The factorial of n, or error message for negative numbers    
    Examples:
        factorial(5) → 120
        factorial(0) → 1
        factorial(-1) → "Error: Factorial not defined for negative numbers"
    """
    # Check for negative numbers
    if n < 0:
        return "Error: Factorial not defined for negative numbers"
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Calculate factorial using iterative approach
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# Test cases
if __name__ == "__main__":
    test_cases = [5, 0, 1, 3, -1]
    print("Testing Factorial Function:")
    print("=" * 30)
    for n in test_cases:
        result = factorial(n)
        print(f"factorial({n}) → {result}")
    print(f"\nExample: factorial(5) = 5 × 4 × 3 × 2 × 1 = {factorial(5)}")
