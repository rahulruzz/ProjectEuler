# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fbSum = 0
for fb in fib():
    if fb > 4000000: break
    if fb % 2 == 0:
        fbSum += fb

print(fbSum)


