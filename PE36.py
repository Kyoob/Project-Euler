def doublePalindrome(upto):
    total = 0
    for i in range(1, upto):
        if isPalindrome(i) and isPalindrome(bin(i)[2:]):
            total += i
    return total

def isPalindrome(num):
    return str(num) == str(num)[::-1]

print(doublePalindrome(1000000))