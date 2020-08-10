largePalindrome = 0
for firstNum in range(100, 1000):
    for secondNum in range(100, 1000):
        multi = firstNum * secondNum
        if str(multi) == str(multi)[::-1] and multi > largePalindrome:
            largePalindrome = multi

print(largePalindrome)

# Could do it as a one liner
# max([x*y for x in range(100, 1000) for y in range(100, 1000) if str(x*y) == str(x*y)[::-1]])