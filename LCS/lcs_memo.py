"""
Created by Roman Polishchenko at 12/9/18
2 course, comp math
Taras Shevchenko National University of Kyiv
email: roma.vinn@gmail.com
"""


def lcs_dynamic(seq_x, seq_y):
    """ Динамічна функція пошуку LCS двох послідовностей елементів
    :param seq_x: послідовність елементів
    :param seq_y: послідовність елементів
    :return: динамічна таблиця
    """
    m = len(seq_x)
    n = len(seq_y)
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if seq_x[i] == seq_y[j]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    return matrix


def build_seq(matrix, seq_x, seq_y, i, j):
    """ Функція, що будує LCS за динамічною таблицею
    :param matrix: array 0..m-1, 0..n-1 where matrix[i][j] == length of LCS of a[:i] and b[..j]
    :param seq_x: sequence of any elements
    :param seq_y: sequence of any elements
    :param i: last index in a
    :param j: last index in b
    :return: LCS
    """
    if i == 0 or j == 0:
        return [seq_x[0]] if i == 0 else [seq_y[0]]

    elif matrix[i][j] == matrix[i-1][j-1] + 1:
        return build_seq(matrix, seq_x, seq_y, i-1, j-1) + [seq_x[i]]
    elif matrix[i][j] == matrix[i-1][j]:
        return build_seq(matrix, seq_x, seq_y, i-1, j)
    elif matrix[i][j] == matrix[i-1][j]:
        return build_seq(matrix, seq_x, seq_y, i, j-1)


if __name__ == '__main__':
    sequence_1 = '12345abcd6789'
    sequence_2 = '123ab45cde89'
    len_1 = len(sequence_1)
    len_2 = len(sequence_2)

    res = lcs_dynamic(sequence_1, sequence_2)
    lcs = build_seq(res, sequence_1, sequence_2, len_1-1, len_2-1)

    print('Sequence 1: [{}]'.format(', '.join(sequence_1)))
    print('Sequence 2: [{}]'.format(', '.join(sequence_2)))
    print()
    print('Length of maximal LCS:', res[len_1-1][len_2-1])
    print('LCS: [{}]'.format(', '.join(lcs)))
