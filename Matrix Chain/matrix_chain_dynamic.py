"""
Created by Roman Polishchenko at 12/9/18
2 course, comp math
Taras Shevchenko National University of Kyiv
email: roma.vinn@gmail.com
"""
import time


def matrix_chain_dynamic(dimensions, n):
    """ Dynamic Programming Python implementation of Matrix
        Chain Multiplication - build the worst sequence of brackets
        (it means that this sequence have the biggest number of elementary operations).
    :param dimensions: array of dimensions
    :param n: length of matrix sequence
    :return: array n x n of maximum amount of elementary operations for each pair i, j
             array n x n of right split of matrix chain
    """

    m = [[-1 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]

    # multiplying matrix by itself
    for i in range(1, n):
        m[i][i] = 0

    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dimensions[i - 1] * dimensions[k] * dimensions[j]
                if cost > m[i][j]:
                    m[i][j] = cost
                    # index if splitting
                    s[i][j] = k
    return m, s


def get_answer(s, i, j, res: list):
    """ Reconstruct the sequence of brackets and matrix
        that give the maximum number of operations
    :param s: array n x n of right split of matrix chain from matrix_chain_dynamic
    :param i: start of piece
    :param j: end of piece
    :param res: array of string from set {'(', ')', 'a[i]'}
    :return: None (array changes inside of function)
    """
    if i == j:
        res.append('a[{}]'.format(i-1))
    else:
        res.append('(')
        get_answer(s, i, s[i][j], res)
        get_answer(s, s[i][j]+1, j, res)
        res.append(')')


def test():

    arr = [1, 2, 3, 4, 5, 6]
    size = len(arr)
    res_m, res_s = matrix_chain_dynamic(arr, size)
    answer = []
    get_answer(res_s, 1, size-1, answer)
    print("Maximal number of operations: {}".format(res_m[1][size-1]))

    print("Order: {}".format(''.join(answer)))


if __name__ == '__main__':
    begin = time.time()
    test()
    print('Time:', time.time() - begin)
