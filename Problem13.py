total = 0
for line in open('Problem13Nums.txt'):
    total += int(line)

print(str(total)[:10])