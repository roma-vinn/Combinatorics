"""
Created by Roman Polishchenko at 11/23/18
2 course, comp math
Taras Shevchenko National University of Kyiv
email: roma.vinn@gmail.com
"""

import random
from math import gcd


def fermat_test(n: int, trial_count=8) -> bool:
    """ Fermat primality test.
    :param n: testing number
    :param trial_count: count of tests
    :return: True - probably prime, False - composite
    """
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    flag = True
    for i in range(trial_count):
        # get random number
        a = random.randrange(2, n - 1)
        while gcd(a, n) != 1:
            a = random.randrange(2, n - 1)
        # check Fermat theorem
        if pow(a, n-1, n) != 1:
            flag = False
            break

    return flag


if __name__ == '__main__':
    with open('output.txt', 'w') as file:
        for num in range(2, 580):
            if fermat_test(num):
                print('Number {} is prime by Fermat test.'.format(num, 1), file=file)
