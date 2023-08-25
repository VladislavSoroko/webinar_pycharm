from fibonacci import *
from duration import *
from fibonacci_simple_cach import fib_simple_cache
from fibonacci_lru_cache import fib_lru_cache


@duration
def main_simple(n: int) -> int:
    return fib(n)


@duration
def main_simple_cache(n: int) -> int:
    return fib_simple_cache(n)


@duration
def main_simple_lru_cache(n: int) -> int:
    return fib_lru_cache(n)


if __name__ == "__main__":
    n = 30
    print(main_simple(n))
    print(main_simple_cache(n))
    print(main_simple_lru_cache(n))
