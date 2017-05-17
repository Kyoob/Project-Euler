def smallestMultiple(upto):
    smallest = upto
    while True:
        for num in range(upto + 1)[:1:-1]:
            print(num)
            if smallest % num != 0:
                smallest += upto
                break
        else:
            return smallest

print(smallestMultiple(20))