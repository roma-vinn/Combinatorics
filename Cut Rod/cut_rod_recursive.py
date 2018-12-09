"""
Created by Roman Polishchenko at 12/5/18
2 course, comp math
Taras Shevchenko National University of Kyiv
email: roma.vinn@gmail.com
"""


def cut_rod(p, n, price):
    splitting = [[]] * (n + 1)
    return cut_rod_recursive(p, n, price, splitting)


def cut_rod_recursive(p, n, price, splitting):
    # перевіряємо всі можливі розрізи
    max_val, splitting = _cut_rod_recursive(p, n, price, splitting)
    # перевіряємо, а може краще не розрізати
    # max_val = max(max_val, p[n-1])
    if max_val <= p[n-1]:
        max_val = p[n-1]
        splitting[n] = n
    # if sum(splitting[n]) != n:
    #     splitting[n].append(n - sum(splitting[n]))
    return max_val, splitting


def _cut_rod_recursive(p, n, price, splitting):
    if n <= 0:
        return 0, splitting
    max_val = float('-inf')
    best_i = 0
    # best_splitting = splitting
    for i in range(n - 1):
        _cost, _splitting = cut_rod_recursive(p, n - i - 1, price, splitting)
        if max_val < p[i] + _cost - price:
            max_val = p[i] + _cost - price
            best_i = i
            # best_splitting = _splitting
    splitting[n] = best_i + 1
    return max_val, splitting


def build_cutting(splitting: list):
    """
    Функція побудови розбиття за заданим
    списком вказівників на індекси розбиття
    :param splitting: список індексів розбиття
    :return: список довжин елементів розбиття
    """
    cut_list = []
    pointer = len(splitting) - 1
    while pointer != 0:
        cut = splitting[pointer]
        cut_list.append(cut)
        pointer -= cut
    return cut_list


if __name__ == '__main__':
    arr = [3, 5, 8, 9, 10, 17, 19, 20]
    size = len(arr)
    for cut_cost in range(3):
        revenue, cuts = cut_rod(arr, size, cut_cost)
        cuts = build_cutting(cuts)
        print('Cut cost:', cut_cost)
        print("Maximum Obtainable Value is:", revenue)
        print('Optimal split is:', ' | '.join(map(str, cuts)))
        print()
