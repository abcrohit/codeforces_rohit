palindrome_n = [0] * 8
not_palindrome_n_rev = [0] * 8
not_palindrome_n_no_rev = [0] * 8

palindrome_n[1] = -1
not_palindrome_n_rev[1] = 1
not_palindrome_n_no_rev[1] = -1

for i in range(2, 8):
    ## Put 1. Palindrom, Not Palindrome
    if i%2 == 0:
        palindrome_n[i] = -1 + -1 * not_palindrome_n_rev[i-1]
        not_palindrome_n_no_rev[i] = -1 -not_palindrome_n_rev[i-1]
        not_palindrome_n_rev[i] = max(-not_palindrome_n_no_rev[i], not_palindrome_n_no_rev[i])
    if i%2 == 1:
        palindrome_n[i] = -1 + max(-not_palindrome_n_rev[i-1], -palindrome_n[i-1])
        not_palindrome_n_no_rev[i] = -1 - palindrome_n[i-1]
        not_palindrome_n_rev[i] = max(-not_palindrome_n_no_rev[i], not_palindrome_n_no_rev[i])

print(palindrome_n[1:])
print(not_palindrome_n_no_rev[1:])
print(not_palindrome_n_rev[1:])