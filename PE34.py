def digitFact():
    total = 0
    for i in range(3, 100000):
        if i == fact(i):
            total += i
    return total

def fact(num):
    total = 0
    for d in str(num):
        total += factorial(int(d))
    return total

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

print(digitFact())