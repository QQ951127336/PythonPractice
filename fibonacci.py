# -*- coding : utf-8 -*-

def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}


def fibonacciCache(n: int) -> int:
    if n not in memo:
        memo[n] = fibonacciCache(n - 1) + fibonacciCache(n - 2)
    return memo[n]


if __name__ == '__main__':
    print(fibonacci(20))
    print(fibonacciCache(20))
