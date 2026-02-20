def factorial(n):
    result = 1
    while n > 1:
        result = n * result
        n -= 1
    return result


def factorial_recursion(n):
    if n==1:  # Base Case
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
print(factorial_recursion(5))
