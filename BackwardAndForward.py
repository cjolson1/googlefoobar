"""
The sign outside reads: Name no one man.

"Escape. We must escape." Staring at the locked door of his cage, Beta Rabbit, spy and brilliant mathematician, 
has a revelation. "Of course! Name no one man - it's a palindrome! Palindromes are the key to opening this lock!"

To help Beta Rabbit crack the lock, write a function answer(n) which returns the smallest positive integer base b, 
at least 2, in which the integer n is a palindrome. The input n will satisfy "0 <= n <= 1000."
"""
def conv2base(x, b):
#converts any number x into any base b
    r = ''
    while x > 0:
        r += str(x%b)
        x //= b
    return r

def answer(n):
    for i in range(2, 37):
        pali = conv2base(n, i)
        if ''.join(reversed(pali)) == pali:
            return i
