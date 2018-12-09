"""
Created by Roman Polishchenko at 12/9/18
2 course, comp math
Taras Shevchenko National University of Kyiv
email: roma.vinn@gmail.com
"""
from asp_recursive import asp_recursive
from asp_iterative import asp_iterative
from time import clock


def latest_non_conflict(s, f, i):
    for j in range(i - 1, -1, -1):
        if f[j] <= s[i-1]:
            return j
    return -1


def asp_profit(s, f, p, n, choice):
    """

    :param s: starts
    :param f: finishes
    :param p: profits
    :param n: index of current process
    :param choice:
    :return: maximal profit
    """
    if n == 1:
        choice += [0]
        return p[n-1], choice
    include_profit = p[n-1]
    include_choice = choice + [n-1]
    i = latest_non_conflict(s, f, n)
    if i != -1:
        pr, include_choice = asp_profit(s, f, p, i + 1, include_choice)
        include_profit += pr
    exclude_profit, exclude_choice = asp_profit(s, f, p, n - 1, choice)
    if include_profit > exclude_profit:
        return include_profit, include_choice
    else:
        return exclude_profit, exclude_choice


def test():
    start = [1, 3, 6, 2]
    finish = [2, 5, 19, 100]
    profits = [50, 20, 100, 200]

    b = clock()
    profit, choice = asp_profit(start, finish, profits, len(start), [])
    print('Max profit:', profit)
    print('The following activities are selected:', *list(reversed(choice)))
    print('Time:', clock() - b)
    print()

    b = clock()
    asp_iterative(start, finish)
    print()
    print('Time:', clock() - b)
    print()

    b = clock()
    print('The following activities are selected:', *asp_recursive(start, finish))
    print('Time:', clock() - b)


if __name__ == '__main__':
    test()
    pass
