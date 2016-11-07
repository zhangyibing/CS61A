def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    i = 1
    while 1 <= a * b:
        if i % a == 0 and i % b == 0:
            return i
        else:
            i += 1

def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """

    k = 0
    count = 0
    while k <= 9:
        if has_digit(n, k):
            count += 1
        k += 1
    return count

def has_digit(n, k):
    while n > 0:
        i = n % 10
        n = n // 10
        if i == k:
            return True
    return False

