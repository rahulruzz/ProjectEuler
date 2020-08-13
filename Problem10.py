import math


def isPrime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, math.floor((math.sqrt(n))) + 1, 2):
        if n % i == 0:
            return False

    return True


sum = 2
for x in range(1, 2000001, 2):
    if isPrime(x):
        sum += x

print(f"{sum}")
# sum([x for x in range(1, 2000001) if isPrime(x)])
