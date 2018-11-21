"""
Created by Roman Polishchenko at 11/21/18
2 course, comp math
Taras Shevchenko National University of Kyiv
email: roma.vinn@gmail.com
"""

import random


def is_prime(n: int, k=8) -> bool:
    """
    Miller-Rabin primality test.

    :param n: testing number
    :param k: parameter, determines the accuracy of test
    :return: True, if n is prime, otherwise - False
    """
    # check if the number is integer
    if n != int(n):
        return False
    n = int(n)

    # checking trivial numbers n < 10
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False

    if n == 2 or n == 3 or n == 5 or n == 7:
        return True

    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    # number of trials
    for trial in range(k):
        ran = random.randrange(2, n)
        if trial_composite(ran):
            return False

    return True


if __name__ == '__main__':
    for num in range(1, 1000):
        if is_prime(num):
            print('Number {} is prime by Miller-Rabin test.'.format(num))
