def is_palindrome(n):
    a, b = n, 0
    while a != 0:
        b *= 10
        b += a % 10
        a //= 10
    return b == n

output = filter(is_palindrome, range(1, 1000))
print(list(output))
