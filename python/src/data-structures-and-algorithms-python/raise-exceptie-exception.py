def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError('x must be numeric')
    elif x < 0:
        raise ValueError('x cannot be negative')
    else:
        return x**0.5

print(sqrt(25))
print(sqrt(9))
print(sqrt(6))
print(sqrt(24))
print(sqrt(8))
