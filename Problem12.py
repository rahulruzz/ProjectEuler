import math


def divisorCount(n):
    count = 0
    currentNum = 1
    while currentNum < math.sqrt(n):
        if n % currentNum == 0:
            if n / currentNum == currentNum:
                count += 1
            else:
                count += 2
        currentNum += 1
    return count


def calcTriangleNum(n):
    triSum = 0
    for num in range(1, n+1):
        triSum += num

    return triSum


triNumber, triCount, found = 0, 0, False
while True:
    triNumber = calcTriangleNum(triCount)
    count = divisorCount(triNumber)
    if count >= 500:
        print(f'The triangle number {triNumber} has {count} divisors')
        break
    triCount += 1
