def recursive_factorial(n):
    if n == 1:
        return n
    else:
        temporary_var = recursive_factorial(n - 1)
        temporary_var = temporary_var * n

    return temporary_var


print(recursive_factorial(5))