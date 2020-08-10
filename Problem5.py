num = 0
while True:
    isDivisible = True
    num += 20
    for y in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
        if num % y != 0:
            isDivisible = False
            break

    if isDivisible:
        print(str(num))
        break
