def powerSum(base, exp):
    return sum(int(d) for d in str(base ** exp))

print(powerSum(2, 1000))