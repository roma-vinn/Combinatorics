"""
Created by Roman Polishchenko at 12/9/18
2 course, comp math
Taras Shevchenko National University of Kyiv
email: roma.vinn@gmail.com
"""

# n --> Total number of activities
# s[]--> An array that contains start time of all activities
# f[] --> An array that contains finish time of all activities


def asp_iterative(s, f):
    n = len(f)
    print("The following activities are selected: ", end='')

    # The first activity is always selected
    i = 0
    print(i, end=' ')

    # Consider rest of the activities
    for j in range(n):

        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if s[j] >= f[i]:
            print(j, end=' ')
            i = j



def test():
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    asp_iterative(start, finish)


if __name__ == '__main__':
    test()
