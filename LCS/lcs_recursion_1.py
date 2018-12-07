"""
Created by Roman Polishchenko at 12/7/18
2 course, comp math
Taras Shevchenko National University of Kyiv
email: roma.vinn@gmail.com
"""
import numpy as np
from time import clock


def lcs_numbers_recursion(arr: list):
    """
    Основна функція рекурсивного пошуку найдовшої монотонно
    неспадної підпослідовності заданої послідовності чисел.
    :param arr: послідовність чисел
    :return: найбільша підпослідовність
    """
    return _lcs_numbers_recursion(arr, arr, float('-inf'))


def _lcs_numbers_recursion(seq_x: list, seq_y: list, prev: float):
    """
    Допоміжна рекурсивна функція пошуку найдовшої монотонно неспадної
    підпослідовності заданої послідовності чисел.

    Фактично ми розглядаємо пошук підпослідовності двох послідовностей,
    які спочатку є тотожними
    :param seq_x: перша послідовність
    :param seq_y: друга послідовність
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


def test_rec():
    for n in [5, 10]:
        sequence = list(np.random.randint(0, 100, n))
        print('Послідовність [n = {}]:'.format(n), *sequence)
        begin = clock()
        print('Найбільша монотонна підпослідовність [rec]:',
              *lcs_numbers_recursion(sequence))
        print('Час рекурсивного алгоритму:', clock() - begin)
        print()


def test_dyn():
    for n in [500, 1500]:
        sequence_1 = list(np.random.randint(0, 100, n))
        sequence_2 = list(np.random.randint(0, 100, n))
        print('Послідовність [n = {}]:'.format(n), *sequence_1)
        print('Послідовність [n = {}]:'.format(n), *sequence_2)
        begin = clock()
        print('Найбільша підпослідовність [dyn]:',
              *lcs_numbers_dynamic(sequence_1, sequence_2))
        print('Час динамічного алгоритму:', clock() - begin)
        print()


if __name__ == '__main__':
    # Тест
    # recursive: вже для n = 14 час складає 5.641206
    # dynamic: для n = 1500 час складає 1.529204
    test_rec()
    test_dyn()
