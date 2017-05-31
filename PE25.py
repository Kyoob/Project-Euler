def fibFirst(num):
    fib = {"1": 1, "2": 1}
    i = 3
    digits = 0
    while True:
        fib[str(i)] = fib[str(i - 1)] + fib[str(i - 2)]
        for d in str(fib[str(i)]):
            digits += 1
            if digits == num:
                return i
        i += 1
        digits = 0

print(fibFirst(1000))