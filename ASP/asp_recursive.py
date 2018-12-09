"""
Created by Roman Polishchenko at 12/9/18
2 course, comp math
Taras Shevchenko National University of Kyiv
email: roma.vinn@gmail.com
"""
from asp_iterative import asp_iterative
from time import clock


def asp_recursive(s, f):
    """
    :param s: list of starts
    :param f: list of finishes
    :return: max activities
    """
    return [0] + _asp_recursive(s, f, 0, len(s) - 1)


def _asp_recursive(s, f, k, n):
    """
    :param s: list of starts
    :param f: list of finishes
    :param k: curr inx
    :param n: len
    :return:
    """
    m = k
    # look up first appropriate activity
    while m <= n and s[m] < f[k]:
        m += 1
    if m <= n:
        return [m] + _asp_recursive(s, f, m, n)
    else:
        return []


def test():
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    b = clock()
    asp_iterative(start, finish)
    print()
    print('Time:', clock() - b)
    print()
    b = clock()
    print(asp_recursive(start, finish))
    print('Time:', clock() - b)


if __name__ == '__main__':
    test()
    pass
