"""Cree una función lamba que compruebe si un número es par o impar."""

def factorial(n):
    if n > 1:
        fact = n * factorial(n-1)
    else:
        return 1
    return fact


n = 4
print(factorial(n))

