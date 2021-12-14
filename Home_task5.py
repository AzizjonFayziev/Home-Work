def calcSumBetweeb(x, y):
    acc = 0
    for i in range(x + 1, y):
        acc += 1
        return acc
print(calcSumBetweeb(10, 15))