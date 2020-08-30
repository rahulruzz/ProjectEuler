def readMatrix():
    with open('Problem11Grid.txt.txt') as file:
        matrix = [[int(x) for x in line.split()] for line in file]
    return matrix


matrix = readMatrix()
largestProduct = 0
col = 20
row = 20

for i in range(row):
    for j in range(col):
        if i + 3 < 20:
            currentProduct = matrix[i][j] * matrix[i + 1][j] * matrix[i + 2][j] * matrix[i + 3][j]
            if largestProduct < currentProduct:
                largestProduct = currentProduct

        if j + 3 < 20:
            currentProduct = matrix[i][j] * matrix[i][j + 1] * matrix[i][j + 2] * matrix[i][j + 3]
            if largestProduct < currentProduct:
                largestProduct = currentProduct

        if i + 3 < 20 and j + 3 < 20:
            currentProduct = matrix[i][j] * matrix[i + 1][j + 1] * matrix[i + 2][j + 2] * matrix[i + 3][j + 3]
            if largestProduct < currentProduct:
                largestProduct = currentProduct

for i in range(20, -1, -1):
    for j in range(20):
        if i + 3 < 20 and j - 3 >= 0:
            currentProduct = matrix[i][j] * matrix[i + 1][j - 1] * matrix[i + 2][j - 2] * matrix[i + 3][j - 3]

            if largestProduct < currentProduct:
                largestProduct = currentProduct


print(largestProduct)
