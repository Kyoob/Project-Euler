from functools import reduce

def factDigitSum(num):
    return sum(int(d) for d in str(reduce((lambda x, y: x * y), range(1, num + 1))))

print(factDigitSum(100))