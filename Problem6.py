sumOfSquare = 0
squareOfSum = 0
for i in range(1, 101):
    sumOfSquare += i*i
    squareOfSum += i

squareOfSum = squareOfSum * squareOfSum

print(squareOfSum - sumOfSquare)

#Better solution
#sumOfSquares = sum(map(lambda x: x**2, range(1, 101)))

#squareOfSums = sum(range(1, 101))**2