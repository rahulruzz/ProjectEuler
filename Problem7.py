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


primeCount = 1
num = 1
while primeCount != 10001:
    num += 2
    if isPrime(num):
        primeCount += 1

print("Solution: " + str(num))
