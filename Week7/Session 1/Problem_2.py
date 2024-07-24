def factorial(n):
    result = 1
    if n == 1:
        return n
    else:
        result = n * factorial( n - 1 )
    return result

print(factorial(5))