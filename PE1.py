def sumMult3or5(upto):
    return sum(list(filter(lambda k: not k % 5 or not k % 3, range(1, upto))))

print(sumMult3or5(1000))