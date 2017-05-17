def difference(upto):
    squareSum = sum(map(lambda k: k ** 2, range(upto + 1)))
    return sum(range(upto + 1)) ** 2 - squareSum

print(difference(100))