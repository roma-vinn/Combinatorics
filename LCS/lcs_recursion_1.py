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
    Основна функція пошуку найдовшої монотонно неспадної
    підпослідовності заданої послідовності чисел.
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


if __name__ == '__main__':
    # Тест
    # вже для n = 14 час складає 5.641206
    for n in [5, 10]:
        sequence = list(np.random.randint(0, 100, n))
        print('Послідовність [n = {}]:'.format(n), *sequence)
        begin = clock()
        print('Найбільша монотонна підпослідовність:',
              *lcs_numbers_recursion(sequence))
        print('Час рекурсивного алгоритму:', clock() - begin)
        print()
