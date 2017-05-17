def nthPrime(n):
    count = 1
    answer = 2
    while count < n:
        answer += 1
        for divisor in range(2, answer):
            if answer % divisor == 0:
                break
        else:
            count += 1
            print(count)
    return answer

print(nthPrime(10001))