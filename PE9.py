def pythagTriplet(upto):
    for i in range(1, upto + 1):
        print(i)
        for j in range(i, upto + 1):
            if i + j > 1000:
                break
            for k in range(j, upto + 1):
                if i + j + k > 1000:
                    break
                if i ** 2 + j ** 2 == k ** 2 and i + j + k == upto:
                    return ((i, j, k), i * j * k)

print(pythagTriplet(1000))