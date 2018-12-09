"""
Created by Roman Polishchenko at 12/9/18
2 course, comp math
Taras Shevchenko National University of Kyiv
email: roma.vinn@gmail.com
"""

import time

MIN = -1


def matrix_chain_memo(dimensions):
    """ Recursive function with memoization to solve
    matrix chain problem
    :param dimensions: array of dimensions of matrix
    :return: array n x n of maximum amount of elementary operations for each pair i, j
             array n x n of right split of matrix chain
    """
    n = len(dimensions) - 1
    m = [[MIN for _ in range(0, n+1)] for _ in range(0, n+1)]
    s = [[0 for _ in range(0, n+1)] for _ in range(0, n+1)]
    _matrix_chain(m, s, dimensions, 1, n)
    return m, s


def _matrix_chain(m, s, p, i, j):
    """ Recursive solution of reversed matrix chain problem -
        find the sequence of brackets that gives the biggest number of
        elementary operations for multiplication the chain of matrix
    :param m: array n+1 x n+1 of results of subproblems (cache)
    :param s: array n+1 x n+1 of index of split the chain for rebuild the answer
    :param p: array 1 x n of matrix dimensions
    :param i: start of piece
    :param j: end of piece
    :return: solution of subproblem
    """
    if m[i][j] > MIN:    # if we have already calculated this subproblem
        return m[i][j]   # return the calculated result
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            q = _matrix_chain(m, s, p, i, k) + _matrix_chain(m, s, p, k + 1, j) + p[i - 1] * p[k] * p[j]
            if q > m[i][j]:
                m[i][j] = q
                s[i][j] = k        # in addition remember the index of splitting
    return m[i][j]


def get_answer(s, i, j, res: list):
    """ Get the sequence of brackets and matrices
        that gives the maximum number of operations
    :param s: array nxn of right split of matrix chain from matrix_chain_memo
    :param i: start of piece
    :param j: end of piece
    :param res: array of string from set {'(', ')', 'a[i]'}
    :return: None (array changes inside of function)
    """
    if i == j:
        res.append('A[{}]'.format(i-1))    # on the main diagonal length of piece == 0, so matrix only one
    else:
        res.append('(')                  # at the other places the internal block of matrix opens
        get_answer(s, i, s[i][j], res)
        get_answer(s, s[i][j]+1, j, res)
        res.append(')')


def test():
    dims = [1, 2, 3, 4, 5, 6]
    size = len(dims)
    res_m, s = matrix_chain_memo(dims)
    answer = []
    get_answer(s, 1, size-1, answer)

    print("Maximal number of operations: {}".format(res_m[1][size - 1]))

    print("Order: {}".format(''.join(answer)))


if __name__ == '__main__':
    begin = time.time()
    test()
    print('Time:', time.time() - begin)
