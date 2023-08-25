def fib(n: int) -> int:
    """Return n-element of Fibonacci sequence"""

    if not isinstance(n, int):
        raise TypeError(f"argument of fib() must be integers, not {type(n)}")
    return n if n < 2 else fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    test_cases = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3)]
    for arg, result in test_cases:
        assert fib(arg) == result, f"ERROR! fib({arg}) != {result}"
