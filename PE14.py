def calculate(num):
    if num == 1:
        return 1
    if num % 2 == 0:
        return calculate(num / 2) + 1
    return calculate(3*num + 1) + 1

def collatz(upto):
    longest = 1
    largestChainLength = 1
    currentChainLength = 1
    for i in range(1, upto):
        currentChainLength = calculate(i)
        if currentChainLength > largestChainLength:
            print(i)
            largestChainLength = currentChainLength
            longest = i
    return longest

print(collatz(1000000))