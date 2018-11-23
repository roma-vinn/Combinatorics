"""
Created by Roman Polishchenko at 11/23/18
2 course, comp math
Taras Shevchenko National University of Kyiv
email: roma.vinn@gmail.com
"""


def lcs_rec(_x, _y, _i, _j):
    if _i == 0 or _j == 0:
        if _x[_i] == _y[_j]:
            return 1
        else:
            return 0
    elif _x[_i] == _y[_j]:
        return lcs_rec(_x, _y, _i-1, _j-1) + 1
    else:
        return max(lcs_rec(_x, _y, _i-1, _j), lcs_rec(_x, _y, _i, _j-1))


if __name__ == '__main__':
    x = [1, 2, 3, 0, 4, -3, 5]
    y = [3, 0, 4, -3, 3, 0]
    c = []
    for i in range(len(x)):
        c.append([])
        for j in range(len(y)):
            c[i].append((lcs_rec(x, y, i, j), i, j, x[i], y[j]))
    # for i in c:
    #     print(i)

    print(lcs_rec(x, y, len(x) - 1, len(y) - 1))
