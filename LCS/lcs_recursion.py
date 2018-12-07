"""
Created by Roman Polishchenko at 11/23/18
2 course, comp math
Taras Shevchenko National University of Kyiv
email: roma.vinn@gmail.com
"""


def lcs_rec(seq_1, seq_2):
    indexes = set()
    _i = len(seq_1) - 1
    _j = len(seq_2) - 1
    length = _lcs_rec(seq_1, seq_2, _i, _j, indexes)
    sub_sequence = [x[i] for i in indexes]
    return length, sub_sequence


def _lcs_rec(seq_1, seq_2, _i, _j, _ind):
    if _i == 0 or _j == 0:
        if seq_1[_i] == seq_2[_j]:
            return 1
        else:
            return 0
    elif seq_1[_i] == seq_2[_j]:
        if _i not in _ind:
            _ind.add(_i)
        return _lcs_rec(seq_1, seq_2, _i-1, _j-1, _ind) + 1
    else:
        return max(_lcs_rec(seq_1, seq_2, _i-1, _j, _ind), _lcs_rec(seq_1, seq_2, _i, _j-1, _ind))


if __name__ == '__main__':
    x = [1, 2, 3, 0, 4, -3, 5]
    y = [3, 0, 4, -3, 3, 0]

    print(lcs_rec(x, y))
