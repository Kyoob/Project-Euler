def largestPalindrome():
    largest = 0
    numRange = range(100, 1000)[::-1]
    for x in numRange:
        for y in numRange:
            z = x * y
            if isPalindrome(z) and z > largest:
                largest = z
    return largest

def isPalindrome(num):
    return str(num) == str(num)[::-1]

print(largestPalindrome())