def sumEvenFib(upto):
    result = [1, 1]
    i = 1
    while result[i] < upto:
        i += 1
        term = result[i - 1] + result[i - 2]
        result.append(result[i - 1] + result[i - 2])
    return sum(list(filter(lambda k: not k % 2, result)))

print(sumEvenFib(4000000))