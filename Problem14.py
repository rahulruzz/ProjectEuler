def chainCount(n):
    chain = 0
    while n > 1:
        chain += 1
        if n % 2 == 0:
            n = (n / 2)
        else:
            n = 3 * n + 1

    return chain + 1  # Adding the number 1 to the chain


maxCount = 0
maxNum = 0
for num in range(1000, 1000001):
    count = chainCount(num)
    if count > maxCount:
        maxCount = count
        maxNum = num

print(f"The number {maxNum} has the largest chain of {maxCount}")