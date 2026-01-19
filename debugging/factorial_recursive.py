#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Recursively computes the factorial of a non-negative integer n.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of n. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Compute factorial using the first command-line argument
f = factorial(int(sys.argv[1]))
print(f)
