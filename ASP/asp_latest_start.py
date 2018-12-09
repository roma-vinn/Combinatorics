"""
Created by Roman Polishchenko at 12/10/18
2 course, comp math
Taras Shevchenko National University of Kyiv
email: roma.vinn@gmail.com
"""


def asp_iterative(s, f):
    n = len(f)
    print("The following activities are selected: ", end='')

    # The first activity is always selected
    i = n - 1
    print(i, end=' ')

    # Consider rest of the activities
    for j in range(n-1, -1, -1):

        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if f[j] <= s[i]:
            print(j, end=' ')
            i = j


def asp_recursive(s, f):
    """
    :param s: list of starts
    :param f: list of finishes
    :return: max activities
    """
    return [len(s)-1] + _asp_recursive(s, f, len(s) - 1, 0)


def _asp_recursive(s, f, k, n):
    """
    :param s: list of starts
    :param f: list of finishes
    :param k: curr inx
    :param n: len
    :return:
    """
    m = k - 1
    # look up first appropriate activity
    while m >= n and f[m] > s[k]:
        m -= 1
    if m >= n:
        return [m] + _asp_recursive(s, f, m, n)
    else:
        return []


def test():
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    start, finish = zip(*sorted(zip(start, finish)))
    print('S:', start)
    print('F:', finish)
    print('\tIterative')
    asp_iterative(start, finish)
    print()
    print('\tRecursive')
    print('The following activities are selected:', *asp_recursive(start, finish))


if __name__ == '__main__':
    test()
    pass
