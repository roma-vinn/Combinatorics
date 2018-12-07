"""
Created by Roman Polishchenko at 11/24/18
2 course, comp math
Taras Shevchenko National University of Kyiv
email: roma.vinn@gmail.com
"""
from time import clock


def fibonacci_dynamic(n: int) -> list:
    """
    # Returns all Fibonacci numbers less than n.
    :param n: upper bound
    :return: numbers
    """
    nums = [0, 1]
    while nums[-1] <= n:
        nums.append(nums[-1] + nums[-2])
    return nums[:-1]


def fibonacci_recursion(n):
    numbers = [0, 1, 1, 2]
    return _fib_rec(n, numbers)


def _fib_rec(n, num):
    if len(num) > n:
        return num[n]
    else:
        return _fib_rec(n - 1, num) + _fib_rec(n - 2, num)


def test_time(func, time, file_path):
    i = 8
    while True:
        i = i ** 2
        begin = clock()
        func(i)
        begin = clock() - begin
        print('for {} time is {}'.format(i, begin), file=file_path)
        if begin > time:
            break
    return i


def task_1(n):
    """
    R
    :param n:
    :return:
    """
    fib = 1
    fib_arr = [1]
    i = 1
    while fib < n:
        fib = fibonacci_recursion(i)
        fib_arr.append(fib)
        i += 1
    return fib_arr


def task_2(n, k=100):
    return fibonacci_dynamic(n)[:k]


if __name__ == '__main__':
    with open('output.txt', 'w') as file:
        print('Task 1', file=file)
        print("При n >= {} час виконання більше 10 сек".format(test_time(task_1, 10, file)), file=file)

        # need a 10260-digit number, for running time > 1 sec
        print('Task 2', file=file)
        print("При n >= {} час виконання більше 0.5сек".format(test_time(task_2, 0.5, file)), file=file)
        print(task_2(10000), file=file)
