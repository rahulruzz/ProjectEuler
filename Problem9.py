total = 1000
found = False
for a in range(1, int((total/3)+1)):
    for b in range(a+1, int(total/2)+1):
        c = total - a - b
        if a*a + b*b == c*c:
            print(f"a = {a}, b = {b}, c = {c}")
            print(f"Solution: {a*b*c}")
            found = True
            break
    if found:
        break