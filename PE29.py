def distinctPowers(uptoA, uptoB):
    combinations = [a ** b for a in range(2, uptoA + 1) for b in range(2, uptoB + 1)]
    for item in combinations:
        temp = item
        combinations = list(filter(lambda x: x != item, combinations))
        combinations.append(temp)
    return len(combinations)

print(distinctPowers(100, 100))