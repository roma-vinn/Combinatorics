"""
by Roman Polishchenko
2 course, comp math
Taras Shevchenko National University of Kyiv
email: roma.vinn@gmail.com
"""
# A Dynamic Programming solution for Rod cutting problem
INT_MIN = float('-inf')


def cut_rod(price, n, cut_cost=0):
    """
    Returns the best obtainable price for a rod of length n and
    price[] as prices of different pieces if the cost of any cut is
    cut_cost
    :param price: array of prices
    :param n: length of rod
    :param cut_cost: cost of any cut (default = 0)
    :return: (best price, required pieces)
    """
    val = [0] * (n + 1)
    _cuts = [[0]] * (n + 1)

    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n + 1):
        max_val = INT_MIN
        for j in range(i):
            if max_val <= price[j] + val[i - j - 1] - cut_cost:
                _cuts[i] = _cuts[i - j - 1] + [j + 1]
                max_val = price[j] + val[i - j - 1] - cut_cost
        val[i] = max_val

    # if 0 cutting price is better, then return it
    if price[n-1] > val[n]:
        return price[n-1], [n]

    return val[n], _cuts[-1][1:]


def test(cut_cost):
    # test
    arr = [3, 5, 8, 9, 10, 17, 19, 20]
    size = len(arr)
    revenue, cuts = cut_rod(arr, size, cut_cost)
    print('Cut cost:', cut_cost)
    print("Maximum Obtainable Value is:", revenue)
    print('Optimal split is:', ' | '.join(map(str, cuts)))


if __name__ == '__main__':
    for c in [0, 1, 2]:
        test(c)
        print()
