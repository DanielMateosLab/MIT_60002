def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fast_fib(n, memo={}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except:
        result = fast_fib(n - 1, memo) + fast_fib(n - 2, memo)
        memo[n] = result
        return result
