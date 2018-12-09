"""
Created by Roman Polishchenko at 11/23/18
2 course, comp math
Taras Shevchenko National University of Kyiv
email: roma.vinn@gmail.com
"""
from time import clock


def lcs_numbers_recursion(seq_x: list, seq_y: list) -> list:
    """
    Основна функція рекурсивного пошуку найдовшої монотонно
    неспадної підпослідовності заданої послідовності чисел.
    :param seq_x:
    :param seq_y:
    :return: найбільша підпослідовність
    """
    return _lcs_numbers_recursion(seq_x, seq_y, float('-inf'))


def _lcs_numbers_recursion(seq_x: list, seq_y: list, prev: float):
    """
    Допоміжна рекурсивна функція пошуку найдовшої монотонно неспадної
    підпослідовності заданої послідовності чисел.

    Фактично ми розглядаємо пошук підпослідовності двох послідовностей,
    які спочатку є тотожними
    :param seq_x: перша послідовність
    :param seq_y: друга послідовність
    :param prev: попередній елемент
    :return:
    """
    # якщо дойшли до кінця одної із послідовностей
    if not seq_x or not seq_y:
        return []
    # відокремлюємо перші елементи
    x_first, new_seq_x, y_first, new_seq_y = seq_x[0], seq_x[1:], seq_y[0], seq_y[1:]
    # перевіряємо умову монотонності
    if x_first == y_first and x_first >= prev:
        # можливо, тактично краще буде не брати знайдений елемент
        # на цьому кроці, щоб взяти більше елементів пізніше
        # (наприклад, якщо x_first дуже великий), тому перевіряємо
        # два випадки із x_first та без нього
        return max([x_first] + _lcs_numbers_recursion(new_seq_x, new_seq_y, x_first),
                   _lcs_numbers_recursion(new_seq_x, new_seq_y, prev),
                   key=len)
    else:
        # інакше – продовжуємо пошук для двох випадків
        return max(_lcs_numbers_recursion(seq_x, new_seq_y, prev),
                   _lcs_numbers_recursion(new_seq_x, seq_y, prev),
                   key=len)


def lcs_numbers_dynamic(seq_1, seq_2):
    """
    Основна функція динамічного пошуку найдовшої монотонно
    неспадної підпослідовності заданих послідовностей чисел.
    :param seq_1: послідовність чисел
    :param seq_2: послідовність чисел
    :return: найбільша підпослідовність
    """

    lengths = [[0 for _ in range(len(seq_2)+1)] for _ in range(len(seq_1)+1)]

    for i, x in enumerate(seq_1):
        for j, y in enumerate(seq_2):
            if x == y:
                # рухаємось по діагоналі
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                # максимум із попередньо знайдених підпослідовностей
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])

    # відновлюємо підпослідовність за матрицею
    result = []
    x, y = len(seq_1), len(seq_2)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert seq_1[x-1] == seq_2[y-1]
            result = [seq_1[x-1]] + result
            x -= 1
            y -= 1
    return result


def get_successive(seq_x: list, seq_y: list, subseq: list) -> list:
    seq_x = ' ' + ' '.join(map(str, seq_x))
    seq_y = ' ' + ' '.join(map(str, seq_y))
    max_subseq = ''
    tmp = ''
    for elem in subseq:
        if tmp + ' ' + str(elem) in seq_x and tmp + ' ' + str(elem) in seq_y:
            tmp += ' ' + str(elem)
        else:
            max_subseq = max(max_subseq, tmp, key=len)
            tmp = ' ' + str(elem)
    max_subseq = max(max_subseq, tmp, key=len)
    return list(map(int, max_subseq.split()))


def test():
    sequence1 = [1, 2, 3, 4, 5]
    sequence2 = [1, 2, 0, 3, 4, 5]

    print('Послідовність 1:', *sequence1)
    print('Послідовність 2:', *sequence2)

    begin = clock()
    result = get_successive(sequence1, sequence2, lcs_numbers_recursion(sequence1, sequence2))
    print('Найбільша підпослідовність чисел ідучих підряд [rec]:',
          *result)
    print('Час рекурсивного алгоритму:', clock() - begin)
    print()
    begin = clock()
    result = get_successive(sequence1, sequence2, lcs_numbers_dynamic(sequence1, sequence2))
    print('Найбільша підпослідовність чисел ідучих підряд [rec]:',
          *result)
    print('Час рекурсивного алгоритму:', clock() - begin)
    print()


if __name__ == '__main__':
    test()
    pass
