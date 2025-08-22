def factorial_febo(n):
    # Calculate factorial
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    # Generate Fibonacci series up to n terms
    fibo = []
    a, b = 0, 1
    for _ in range(n):
        fibo.append(a)
        a, b = b, a + b

    return factorial, fibo

# Demonstration
for test_n in [4]:
    fact, fibo_series = factorial_febo(test_n)
    print(f"n = {test_n}: Factorial = {fact}, Fibonacci series = {fibo_series}")