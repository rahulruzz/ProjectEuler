import math

QUESTION_NUMBER = 600851475143

def isPrime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0 and n > 2:
        return False

    for i in range(3, math.floor((math.sqrt(n))) + 1, 2):
        if n % i == 0:
            return False

    return True

def allPrimeFactors(n):
    return [x for x in range(1, math.floor((math.sqrt(n)))) if n % x == 0 and isPrime(x)]


print(max(allPrimeFactors(QUESTION_NUMBER)))


